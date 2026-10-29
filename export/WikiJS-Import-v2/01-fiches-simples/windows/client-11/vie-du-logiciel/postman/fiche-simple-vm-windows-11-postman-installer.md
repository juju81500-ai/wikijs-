---
title: "Fiche Simple - VM Windows 11 Postman Installer"
description: "Installer Postman Desktop depuis la source officielle sur Windows 11 et vérifier l'éditeur avant le premier lancement."
published: true
date: 2026-10-29T20:56:02Z
tags: ["windows-11", "postman", "api", "newman", "vie-du-logiciel"]
editor: markdown
dateCreated: 2026-10-29T20:56:02Z
dateModified: 2026-10-29T20:56:02Z
---

# Fiche_Simple_-_VM_Windows_11_Postman_Installer

- **Environnement** : Poste Windows 11 géré, compte standard, Postman Desktop et Newman
- **OS / Version** : Windows 11 Client
- **Catégorie** : API / installation
- **Tags** : `windows-11`, `postman`, `api`, `newman`, `vie-du-logiciel`

---

## Problème précis à résoudre

Installer Postman Desktop depuis la source officielle sur Windows 11 et vérifier l'éditeur avant le premier lancement.

## 1. Hors-Production (Lab / Test / POC)

1. Installer par winget (source officielle de l'éditeur) :
   ```powershell
   winget search Postman
   winget install --id Postman.Postman -e
   ```
   👉 Explication : Recherche puis installe l'identifiant `Postman.Postman` (vérifier l'identifiant exact dans le résultat de la recherche).

2. Alternative GUI : télécharger l'installeur officiel :
   ```text
   Navigateur > https://www.postman.com/downloads/ > Windows 64-bit > télécharger l'installeur
   ```
   👉 Explication : Utiliser uniquement le site officiel postman.com ; ne pas passer par un miroir.

3. Vérifier la signature du fichier téléchargé :
   ```powershell
   Get-AuthenticodeSignature -FilePath "$HOME\Downloads\Postman-win64-Setup.exe" | Format-List Status,SignerCertificate
   ```
   👉 Explication : Le nom du fichier peut varier : à remplacer par le nom réel. Exiger `Status : Valid` et un éditeur Postman.

4. Lancer et relever la version :
   ```text
   Démarrer > Postman > icône du profil/Paramètres > About Postman (libellé à vérifier selon la version)
   ```
   👉 Explication : Noter la version installée dans le registre des logiciels avant de se connecter.

## 2. Production — Contrôles

Installer d'abord sur un poste pilote ; conserver l'installeur validé et la version dans l'inventaire logiciel ; vérifier le canal officiel et la licence/équipe.

## 3. Production — Sécurité

- Ne pas exécuter un installeur dont la signature est invalide.
- Utiliser un compte standard pour le quotidien ; l'élévation n'est requise que pour l'installation.
- Ne pas ouvrir de collections reçues par mail sans relecture de leurs scripts.

## Validation et retour arrière

- **Validation** : Postman démarre, la version est relevée et la source est officielle.
- **Retour arrière** : Désinstaller via `winget uninstall --id Postman.Postman -e` ou Paramètres > Applications > Applications installées > Postman > Désinstaller.

## Si le problème n'est pas résolu

- [Postman — documentation officielle](https://learning.postman.com/docs/)
- [Postman — téléchargement](https://www.postman.com/downloads/)
- [Newman — documentation](https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/)
- [Fiche d'entrée Postman](/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-postman)
- [Fiche connexe Prerequis_Limites](</01-fiches-simples/windows/client-11/vie-du-logiciel/postman/fiche-simple-vm-windows-11-postman-prerequis-limites>)