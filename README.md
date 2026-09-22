# Nextendo App for iOS

The companion app for [Nextendo Network](https://nextendo.network): your account, your friends
and your play sessions, in your pocket.

<sub>iPhone · iOS 16 and later · English, French, Spanish, Portuguese, German, Italian, Russian,
Chinese, Japanese, Arabic</sub>

---

## What it does

**Your friends.** The full list with everyone's picture, who is online, what they are playing and
from which device: the emulator or a real console. Search by nickname, account name or friend
code. Best friends stay at the top, always in the same place. Friend requests, blocking, and your
own friend code to get added.

**What's happening now.** The home screen shows who is playing, what, and for how long. The
activity feed brings up everyone's recent sessions, grouped by game.

**Games.** Any Switch game can be looked up by name: the database covers the whole catalogue,
not only the games whose online we host. Each page gives the artwork, the description in your
language, the publisher, the release date, and which of your friends play it.

**Mods.** The game's GameBanana catalogue, with its screenshots, its files and what the author
allows. Save a mod here and you'll find it in the emulator's store: it's the same list, attached
to your account.

**Your saves.** The ones the emulator uploaded to the cloud, with their size and date. And your
play history: the time spent on each title.

**Your console.** Scan the QR code shown by a Switch to link it to your account.

---

## Installing

The app is not on the App Store. Three routes, depending on your device.

### Jailbroken iPhone: the `.deb` package (recommended)

This is the safest route: the package copies the files and never goes through iOS's install
service, which sometimes refuses an app that Apple hasn't signed.

1. Download `NextendoApp.deb` from the [latest release](../../releases/latest).
2. Transfer it to the phone (Filza reads a network share, AirDrop and cloud storage).
3. In **Filza**, tap the file → **Install**.

The icon appears on the home screen without rebooting.

### Jailbroken iPhone: the signed `.ipa`

Take `NextendoApp-fakesigned.ipa`, transfer it, then **Filza → Install**.

⚠️ **AppSync Unified must be installed**, otherwise iOS refuses the archive despite the signature.

### No jailbreak: sideloading

`NextendoApp.ipa` installs with AltStore, SideStore or Sideloadly, using a free Apple account.
The app then has to be re-signed every seven days, which AltStore and SideStore handle on their
own as long as they are running.

---

## You need a Nextendo account

The app doesn't create an account: it uses one. If you don't have one, open it at
[nextendo.network](https://nextendo.network), then sign in here.

Signing in goes through the site: the app never sees your password. You grant named permissions
(see your identity, your friends, your profile, your saves, link a console), and you can revoke
them at any time from your account.

---

## What it doesn't do

**It doesn't install mods.** A mod is a folder the emulator places next to the game, on the
computer. The phone is there to find them and set them aside; installing happens over there.

**It doesn't play games.** This is a companion app, not an emulator.

---

## Reporting a problem

Through this repository's [issues](../../issues), or on the Nextendo Network Discord. Say which
version you are running: it's at the bottom of the **Account** tab.
