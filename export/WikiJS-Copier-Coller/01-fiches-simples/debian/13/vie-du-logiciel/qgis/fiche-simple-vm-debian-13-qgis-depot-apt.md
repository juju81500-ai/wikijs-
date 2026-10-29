# Fiche_Simple_-_VM_Debian_13_QGIS_Depot_APT.md

- **Environnement** : QGIS Desktop sur Debian 13 amd64
- **OS / Version** : Debian 13; QGIS 3.44 LTR
- **Catégorie** : SIG / dépôt APT

---

## Problème précis à résoudre

Ajouter le dépôt QGIS LTR signé pour Trixie.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les outils :
   ```bash
   sudo apt update
   sudo apt install -y ca-certificates curl gnupg
   ```
   👉 Explication : Fournit le téléchargement HTTPS et gpg.

2. Télécharger la clé et afficher son empreinte :
   ```bash
   curl --fail --location --proto '=https' --tlsv1.2 -o qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg
   gpg --show-keys --with-fingerprint qgis-archive-keyring.gpg
   ```
   👉 Explication : L'empreinte doit être `2D7E 3441 A707 FDB3 E705 9441 D155 B8E6 A419 C5BE` (clé 2022-2027); sinon interrompre.

3. Installer la clé :
   ```bash
   sudo install -d -m 0755 /etc/apt/keyrings
   sudo install -m 0644 qgis-archive-keyring.gpg /etc/apt/keyrings/qgis-archive-keyring.gpg
   rm qgis-archive-keyring.gpg
   ```
   👉 Explication : Le fichier téléchargé est supprimé après installation.

4. Créer la source dédiée :
   ```bash
   sudoedit /etc/apt/sources.list.d/qgis.sources
   ```
   👉 Explication : Y coller le contenu ci-dessous.

5. Contenu du fichier `qgis.sources` :
   ```text
   Types: deb
   URIs: https://qgis.org/debian-ltr
   Suites: trixie
   Architectures: amd64
   Components: main
   Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg
   ```
   👉 Explication : `Signed-By` limite la clé à ce dépôt.

## 2. Production — Contrôles

Prévoir un dépôt miroir ou une stratégie de validation avant mise à jour des postes.

## 3. Production — Sécurité

- Ne pas ajouter de dépôt nightly ou testing sur un poste de production.
- Interrompre si l'empreinte diffère ou si la clé est expirée.

## Validation et retour arrière

- **Validation** : `apt update` lit le dépôt qgis.org/debian-ltr sans erreur de signature.
- **Retour arrière** : supprimer `/etc/apt/sources.list.d/qgis.sources` et la clé, puis `sudo apt update`.

## Si le problème n'est pas résolu

- [QGIS — installation Linux](https://qgis.org/resources/installation-guide/)
- [QGIS — guide utilisateur 3.44](https://docs.qgis.org/3.44/en/docs/user_manual/)
- [Guide complet QGIS Debian 13](/02-fiches-completes/debian/13/installation-deploiement/75-deploiement-qgis-3-44-ltr-debian-13#2-ajouter-la-cle-et-le-depot-officiels)