---
title: "Fiche Simple - VM Windows 11 Wireshark Sauvegarder Restaurer"
description: "Sauvegarder la configuration Wireshark (profils) et les captures utiles, puis les restaurer."
published: true
date: 2026-10-29T20:55:32Z
tags: ["wireshark", "npcap", "windows11", "capture", "pcap"]
editor: markdown
dateCreated: 2026-10-29T20:55:32Z
dateModified: 2026-10-29T20:55:32Z
---

# Fiche_Simple_-_VM_Windows_11_Wireshark_Sauvegarder_Restaurer.md

- **Environnement** : Poste Windows 11 x64 d'administration réseau (compte administrateur local disponible)
- **OS / Version** : Windows 11 x64; Wireshark stable (vérifier la version publiée) + Npcap
- **Catégorie** : analyse réseau
- **Tags** : `wireshark`, `npcap`, `windows11`, `capture`, `pcap`

---

## Problème précis à résoudre

Sauvegarder la configuration Wireshark (profils) et les captures utiles, puis les restaurer.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : **Aide > À propos de Wireshark > Dossiers** pour repérer le dossier de configuration personnel.
   👉 Explication : En général `%APPDATA%\Wireshark`; vérifier dans l'interface.

2. Sauvegarder les profils.
```powershell
Compress-Archive -Path "$env:APPDATA\Wireshark" -DestinationPath C:\Sauvegardes\wireshark-profils.zip -Force
```
   👉 Explication : Archive profils, colonnes et filtres; C:\Sauvegardes doit exister et être protégé.

3. Sauvegarder les captures utiles.
```powershell
Compress-Archive -Path C:\Captures -DestinationPath C:\Sauvegardes\captures.zip -Force
```
   👉 Explication : À stocker chiffré, car les pcap peuvent contenir des données sensibles.

4. Restaurer les profils après fermeture de Wireshark.
```powershell
Expand-Archive C:\Sauvegardes\wireshark-profils.zip -DestinationPath "$env:APPDATA" -Force
```
   👉 Explication : Remet les profils en place.

5. GUI : relancer Wireshark et vérifier **Édition > Configuration Profiles**.
   👉 Explication : Confirme la restauration.

## 2. Production — Contrôles

Secrets : aucun; ne pas inclure de clés TLS/pre-master secrets dans la sauvegarde sans chiffrement.

## 3. Production — Sécurité

- Aucun secret n'est écrit dans la fiche; capturer uniquement dans le périmètre autorisé.
- Les placeholders en MAJUSCULES sont à remplacer.

## Validation et retour arrière

- **Validation** : Les profils sont visibles et un pcap restauré s'ouvre.
- **Retour arrière** : Supprimer le dossier restauré et réimporter l'ancienne archive.

## Si le problème n'est pas résolu

- [Wireshark — téléchargement officiel](https://www.wireshark.org/download.html)
- [Wireshark — guide utilisateur Windows](https://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallWinInstall.html)
- [Npcap — site officiel](https://npcap.com/)
- [Npcap — guide utilisateur et licence](https://npcap.com/guide/)
- [Série Debian 13 — Wireshark](/01-fiches-simples/debian/13/vie-du-logiciel/wireshark/fiche-simple-vm-debian-13-wireshark-analyse-installer)