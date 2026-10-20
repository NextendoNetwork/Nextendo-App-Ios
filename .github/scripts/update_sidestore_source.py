#!/usr/bin/env python3
"""Rebuild sidestore/source.json from this repository's GitHub releases.

Every published, non-prerelease release that ships NextendoApp.ipa becomes a
version entry. Version, build and minimum iOS come from the IPA's Info.plist;
size and sha256 from the downloaded bytes; entitlements from the binary's
code signature. Entries whose asset is unchanged are reused without
downloading the IPA again.
"""

from __future__ import annotations

import hashlib
import io
import json
import os
import plistlib
import re
import struct
import sys
import urllib.request
import zipfile
from pathlib import Path

ASSET_NAME = "NextendoApp.ipa"
SOURCE_PATH = Path("sidestore/source.json")
API = "https://api.github.com"
# AltStore asks sources to leave these two out of appPermissions.entitlements.
OMITTED_ENTITLEMENTS = {"application-identifier", "com.apple.developer.team-identifier"}
ENTITLEMENTS_MAGIC = b"\xfa\xde\x71\x71"


def request(url: str, accept: str = "application/vnd.github+json") -> bytes:
    headers = {"Accept": accept, "User-Agent": "sidestore-source-updater"}
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith(API):
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=120) as response:
        return response.read()


def releases(repository: str) -> list[dict]:
    found, page = [], 1
    while True:
        batch = json.loads(request(f"{API}/repos/{repository}/releases?per_page=100&page={page}"))
        found.extend(batch)
        if len(batch) < 100:
            return found
        page += 1


def binary_entitlements(binary: bytes) -> dict:
    """Read the entitlements blob from the code signature, if there is one."""
    offset = binary.find(ENTITLEMENTS_MAGIC)
    while offset != -1:
        length = struct.unpack(">I", binary[offset + 4 : offset + 8])[0]
        blob = binary[offset + 8 : offset + length]
        if blob.lstrip().startswith(b"<?xml") or blob.lstrip().startswith(b"<plist"):
            return plistlib.loads(blob)
        offset = binary.find(ENTITLEMENTS_MAGIC, offset + 4)
    return {}


def inspect_ipa(data: bytes) -> dict:
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        names = archive.namelist()
        plists = [name for name in names if re.fullmatch(r"Payload/[^/]+\.app/Info\.plist", name)]
        if len(plists) != 1:
            raise SystemExit("The IPA must contain exactly one Payload/*.app/Info.plist.")
        info = plistlib.loads(archive.read(plists[0]))
        entitlements: set[str] = set()
        privacy: dict[str, str] = {}
        for name in names:
            if re.fullmatch(r"Payload/.+\.(app|appex)/Info\.plist", name):
                bundle_info = plistlib.loads(archive.read(name))
                privacy.update(
                    (key, value)
                    for key, value in bundle_info.items()
                    if key.endswith("UsageDescription") and isinstance(value, str)
                )
                executable = name.rsplit("/", 1)[0] + "/" + bundle_info.get("CFBundleExecutable", "")
                if executable in names:
                    entitlements.update(binary_entitlements(archive.read(executable)))
    return {
        "bundleIdentifier": info["CFBundleIdentifier"],
        "version": str(info["CFBundleShortVersionString"]),
        "buildVersion": str(info["CFBundleVersion"]),
        "minOSVersion": info.get("MinimumOSVersion"),
        "appPermissions": {
            "entitlements": sorted(entitlements - OMITTED_ENTITLEMENTS),
            "privacy": dict(sorted(privacy.items())),
        },
    }


def release_notes(release: dict, version: str) -> str:
    body = release.get("body") or ""
    match = re.search(r"## What changed\s*(.*?)(?:\n## |\Z)", body, re.S)
    notes = (match.group(1) if match else body).split("\n## ")[0]
    notes = re.sub(r"\*\*|`", "", notes)
    notes = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", notes).strip()
    return notes[:3000] or f"Nextendo App {version}"


def main() -> None:
    repository = os.environ.get("GITHUB_REPOSITORY", "NextendoNetwork/Nextendo-App-Ios")
    source = json.loads(SOURCE_PATH.read_text())
    app = source["apps"][0]
    known = {(entry["downloadURL"], entry["size"]): entry for entry in app["versions"]}

    versions, latest_permissions = [], None
    for release in releases(repository):
        if release["draft"] or release["prerelease"]:
            continue
        asset = next((a for a in release["assets"] if a["name"] == ASSET_NAME), None)
        if asset is None:
            continue
        entry = known.get((asset["browser_download_url"], asset["size"]))
        if entry is None or latest_permissions is None:
            data = request(asset["url"], accept="application/octet-stream")
            if len(data) != asset["size"]:
                raise SystemExit(f"{release['tag_name']}: downloaded size does not match the asset.")
            ipa = inspect_ipa(data)
            if ipa["bundleIdentifier"] != app["bundleIdentifier"]:
                raise SystemExit(f"{release['tag_name']}: unexpected bundle {ipa['bundleIdentifier']}.")
            if latest_permissions is None:
                latest_permissions = ipa["appPermissions"]
            if entry is None:
                entry = {
                    "version": ipa["version"],
                    "buildVersion": ipa["buildVersion"],
                    "date": release["published_at"],
                    "localizedDescription": release_notes(release, ipa["version"]),
                    "downloadURL": asset["browser_download_url"],
                    "size": len(data),
                    "sha256": hashlib.sha256(data).hexdigest(),
                }
                if ipa["minOSVersion"]:
                    entry["minOSVersion"] = ipa["minOSVersion"]
        versions.append(entry)

    if not versions:
        raise SystemExit(f"No release ships {ASSET_NAME}.")
    versions.sort(key=lambda entry: int(entry["buildVersion"]), reverse=True)
    builds = [int(entry["buildVersion"]) for entry in versions]
    if len(set(builds)) != len(builds):
        raise SystemExit("Two releases share a build number; CFBundleVersion must increase.")
    order = sorted(versions, key=lambda entry: entry["date"], reverse=True)
    if [entry["buildVersion"] for entry in order] != [entry["buildVersion"] for entry in versions]:
        print("Warning: a newer release has a lower build number than an older one.", file=sys.stderr)

    app["versions"] = versions
    app["appPermissions"] = latest_permissions
    SOURCE_PATH.write_text(json.dumps(source, ensure_ascii=False, indent=2) + "\n")
    print(f"{len(versions)} versions, latest {versions[0]['version']} ({versions[0]['buildVersion']}).")


if __name__ == "__main__":
    main()
