---
title: "Fiche Simple - VM Debian 13 Postman Mise A Jour Retour Arriere"
description: "Mettre à jour Postman et Newman sur Debian 13 de manière contrôlée, avec sauvegarde de l'archive en place et retour arrière possible."
published: true
date: 2026-10-29T20:56:02Z
tags: ["debian13", "postman", "api", "newman", "vie-du-logiciel"]
editor: markdown
dateCreated: 2026-10-29T20:56:02Z
dateModified: 2026-10-29T20:56:02Z
---

# Fiche_Simple_-_VM_Debian_13_Postman_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13 Trixie avec bureau graphique, Postman Desktop et Newman
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : API / mise à jour et retour arrière
- **Tags** : `debian13`, `postman`, `api`, `newman`, `vie-du-logiciel`

---

## Problème précis à résoudre

Mettre à jour Postman et Newman sur Debian 13 de manière contrôlée, avec sauvegarde de l'archive en place et retour arrière possible.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder collections et environnements :
   ```text
   Postman > COLLECTION_LAB > ⋯ > Export > enregistrer dans SAUVEGARDE_DIR
   ```
   👉 Explication : Remplacer `SAUVEGARDE_DIR` par le dossier de sauvegarde ; exporter l'environnement sans secret.

2. Conserver l'installation actuelle :
   ```bash
   sudo cp -a /opt/Postman /opt/Postman.OLD
   ```
   👉 Explication : Copie de retour arrière complète de l'ancienne version.

3. Installer la nouvelle archive :
   ```bash
   curl -fL -o /tmp/postman-linux-x64.tar.gz https://dl.pstmn.io/download/latest/linux64
   sudo rm -rf /opt/Postman
   sudo tar -xzf /tmp/postman-linux-x64.tar.gz -C /opt
   sudo chown -R root:root /opt/Postman
   ```
   👉 Explication : Remplace le répertoire par la version publiée. Avec snap : `sudo snap refresh postman`.

4. Mettre à jour Newman :
   ```bash
   npm outdated -g newman
   sudo npm install -g newman@VERSION_NEWMAN
   newman --version
   ```
   👉 Explication : Remplacer `VERSION_NEWMAN` par la version validée sur le pilote.

5. Retour arrière de Postman :
   ```bash
   sudo rm -rf /opt/Postman
   sudo mv /opt/Postman.OLD /opt/Postman
   ```
   👉 Explication : Restaure l'ancienne version ; réimporter les collections au besoin.

6. Retour arrière de Newman :
   ```bash
   sudo npm install -g newman@VERSION_PRECEDENTE
   ```
   👉 Explication : Remplacer `VERSION_PRECEDENTE` par la version précédente.

## 2. Production — Contrôles

Lire les notes de version Postman avant diffusion ; mettre à jour d'abord un poste pilote ; exporter les collections et environnements (sans secrets) avant la mise à jour.

## 3. Production — Sécurité

- Télécharger les mises à jour uniquement depuis le canal officiel.
- Désactiver la mise à jour automatique sur les postes figés si la politique l'impose (à vérifier dans les paramètres).
- Sauvegarder les exports hors du poste avant de désinstaller.

## Validation et retour arrière

- **Validation** : Nouvelle version affichée, collections accessibles, recette Newman réussie.
- **Retour arrière** : Réinstaller la version précédente validée ou restaurer la copie `/opt/Postman.OLD` ; réimporter les collections exportées.

## Si le problème n'est pas résolu

- [Postman — documentation officielle](https://learning.postman.com/docs/)
- [Postman — téléchargement](https://www.postman.com/downloads/)
- [Newman — documentation](https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/)
- [Fiche d'entrée Postman](/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-postman)
- [Fiche connexe Prerequis_Limites](</01-fiches-simples/debian/13/vie-du-logiciel/postman/fiche-simple-vm-debian-13-postman-prerequis-limites>)
- [Fiche connexe Installer](</01-fiches-simples/debian/13/vie-du-logiciel/postman/fiche-simple-vm-debian-13-postman-installer>)