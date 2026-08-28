# Nextendo App — iOS

L'application compagnon de [Nextendo Network](https://nextendo.network) : ton compte, tes amis et
tes parties dans la poche.

<sub>iPhone · iOS 16 et plus · français, anglais, espagnol, portugais, allemand, italien, russe,
chinois, japonais, arabe</sub>

---

## Ce qu'elle fait

**Tes amis.** La liste complète avec la photo de chacun, qui est en ligne, à quoi il joue et
depuis quel appareil — l'émulateur ou une vraie console. Recherche par pseudo, par nom de compte
ou par code ami. Les meilleurs amis restent en tête, toujours au même endroit. Demandes d'amitié,
blocages, et le code ami de ton compte pour te faire ajouter.

**Ce qui se passe maintenant.** L'accueil dit qui joue, à quoi, et depuis combien de temps. Le fil
d'activité remonte les parties récentes de tout le monde, jeu par jeu.

**Les jeux.** N'importe quel jeu Switch se cherche par son nom — la base couvre tout le catalogue,
pas seulement les jeux dont on héberge l'en ligne. Chaque fiche donne les visuels, la description
dans ta langue, l'éditeur, la date de sortie, et lesquels de tes amis y jouent.

**Les mods.** Le catalogue GameBanana du jeu, avec ses captures, ses fichiers et ce que l'auteur
autorise. Mets un mod de côté et tu le retrouves dans le magasin de l'émulateur — c'est la même
liste, attachée à ton compte.

**Tes sauvegardes.** Celles que l'émulateur a envoyées dans le nuage, avec leur poids et leur
date. Et ton historique de jeu : le temps passé sur chaque titre.

**Ta console.** Scanne le QR affiché par une Switch pour la rattacher à ton compte.

---

## Installation

L'application n'est pas sur l'App Store. Trois chemins, selon ton appareil.

### iPhone jailbreaké — le paquet `.deb` (recommandé)

C'est la voie la plus sûre : le paquet copie les fichiers et ne passe jamais par le service
d'installation d'iOS, qui refuse parfois une application non signée par Apple.

1. Télécharge `NextendoApp.deb` depuis la [dernière version](../../releases/latest).
2. Transfère-le sur le téléphone (Filza lit un partage réseau, AirDrop et les nuages).
3. Dans **Filza**, appuie sur le fichier → **Installer**.

L'icône apparaît sur l'écran d'accueil sans redémarrer.

### iPhone jailbreaké — l'archive `.ipa` signée

Prends `NextendoApp-fakesigned.ipa`, transfère-la, puis **Filza → Installer**.

⚠️ **AppSync Unified doit être installé**, sinon iOS refuse l'archive malgré la signature.

### Sans jailbreak — sideload

`NextendoApp.ipa` s'installe avec AltStore, SideStore ou Sideloadly, avec un compte Apple
gratuit. L'application est alors à resigner tous les sept jours, ce dont AltStore et SideStore
se chargent seuls tant qu'ils tournent.

---

## Il faut un compte Nextendo

L'application ne crée pas de compte : elle en utilise un. Si tu n'en as pas, ouvre-le sur
[nextendo.network](https://nextendo.network), puis connecte-toi ici.

La connexion passe par le site : l'application ne voit jamais ton mot de passe. Tu accordes des
droits nommés — voir ton identité, tes amis, ton profil, tes sauvegardes, lier une console — et
tu peux les retirer à tout moment depuis ton compte.

---

## Ce qu'elle ne fait pas

**Elle n'installe pas de mods.** Un mod est un dossier que l'émulateur pose à côté du jeu, sur
l'ordinateur. Le téléphone sert à les trouver et à les mettre de côté ; l'installation se fait
là-bas.

**Elle ne joue pas.** C'est une application compagnon, pas un émulateur.

---

## Signaler un problème

Par les [tickets](../../issues) de ce dépôt, ou sur le Discord de Nextendo Network. Dis quelle
version tu utilises — elle est en bas de l'onglet **Compte**.
