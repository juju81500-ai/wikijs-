---
title: "Fiche Simple - VM Debian 13 Postman Installer"
description: "Installer Postman Desktop sur Debian 13 depuis l'archive officielle Postman, sans paquet non officiel, puis créer un lanceur."
published: true
date: 2026-10-29T20:56:02Z
tags: ["debian13", "postman", "api", "newman", "vie-du-logiciel"]
editor: markdown
dateCreated: 2026-10-29T20:56:02Z
dateModified: 2026-10-29T20:56:02Z
---

# Fiche_Simple_-_VM_Debian_13_Postman_Installer

- **Environnement** : VM Debian 13 Trixie avec bureau graphique, Postman Desktop et Newman
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : API / installation
- **Tags** : `debian13`, `postman`, `api`, `newman`, `vie-du-logiciel`

---

## Problème précis à résoudre

Installer Postman Desktop sur Debian 13 depuis l'archive officielle Postman, sans paquet non officiel, puis créer un lanceur.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'archive officielle Linux 64 bits :
   ```bash
   curl -fL -o /tmp/postman-linux-x64.tar.gz https://dl.pstmn.io/download/latest/linux64
   file /tmp/postman-linux-x64.tar.gz
   ```
   👉 Explication : Télécharge l'archive depuis le domaine officiel ; `file` doit indiquer `gzip compressed data`. Postman ne publie pas de somme SHA-256 officielle simple : vérifier la page de téléchargement.

2. Extraire dans /opt :
   ```bash
   sudo tar -xzf /tmp/postman-linux-x64.tar.gz -C /opt
   sudo chown -R root:root /opt/Postman
   ls /opt/Postman
   ```
   👉 Explication : Installe l'application sous `/opt/Postman`, propriétaire root pour éviter qu'un utilisateur modifie les binaires.

3. Créer le lien et le lanceur de bureau :
   ```bash
   sudo ln -sf /opt/Postman/Postman /usr/local/bin/postman
   sudo tee /usr/share/applications/postman.desktop >/dev/null <<'EOF'
   [Desktop Entry]
   Type=Application
   Name=Postman
   Exec=/opt/Postman/Postman %U
   Terminal=false
   Categories=Development;
   EOF
   ```
   👉 Explication : Rend `postman` accessible dans le PATH et dans le menu. Le chemin de l'icône est optionnel et à vérifier dans `/opt/Postman/app/resources/app/assets`.

4. Alternative documentée : snap (si snapd est autorisé) :
   ```bash
   sudo apt install -y snapd
   sudo snap install postman
   ```
   👉 Explication : Méthode alternative officielle Postman ; compatibilité de snapd avec Debian 13 à vérifier avant usage en production.

5. Lancer l'application :
   ```bash
   postman &
   ```
   👉 Explication : Démarre l'interface ; l'écran de connexion apparaît au premier lancement.

## 2. Production — Contrôles

Installer d'abord sur un poste pilote ; conserver l'installeur validé et la version dans l'inventaire logiciel ; vérifier le canal officiel et la licence/équipe.

## 3. Production — Sécurité

- Ne pas exécuter un installeur dont la signature est invalide.
- Utiliser un compte standard pour le quotidien ; l'élévation n'est requise que pour l'installation.
- Ne pas ouvrir de collections reçues par mail sans relecture de leurs scripts.

## Validation et retour arrière

- **Validation** : Postman démarre, la version est relevée et la source est officielle.
- **Retour arrière** : `sudo rm -rf /opt/Postman /usr/local/bin/postman /usr/share/applications/postman.desktop` (ou `sudo snap remove postman`).

## Si le problème n'est pas résolu

- [Postman — documentation officielle](https://learning.postman.com/docs/)
- [Postman — téléchargement](https://www.postman.com/downloads/)
- [Newman — documentation](https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/)
- [Fiche d'entrée Postman](/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-postman)
- [Fiche connexe Prerequis_Limites](</01-fiches-simples/debian/13/vie-du-logiciel/postman/fiche-simple-vm-debian-13-postman-prerequis-limites>)