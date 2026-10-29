---
title: "Fiche Simple - VM Windows 11 Wireshark Mise A Jour Retour Arriere"
description: "Mettre à jour Wireshark/Npcap et savoir revenir en arrière."
published: true
date: 2026-10-29T20:55:32Z
tags: ["wireshark", "npcap", "windows11", "capture", "pcap"]
editor: markdown
dateCreated: 2026-10-29T20:55:32Z
dateModified: 2026-10-29T20:55:32Z
---

# Fiche_Simple_-_VM_Windows_11_Wireshark_Mise_A_Jour_Retour_Arriere.md

- **Environnement** : Poste Windows 11 x64 d'administration réseau (compte administrateur local disponible)
- **OS / Version** : Windows 11 x64; Wireshark stable (vérifier la version publiée) + Npcap
- **Catégorie** : analyse réseau
- **Tags** : `wireshark`, `npcap`, `windows11`, `capture`, `pcap`

---

## Problème précis à résoudre

Mettre à jour Wireshark/Npcap et savoir revenir en arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder les profils (voir fiche Sauvegarder/restaurer) et noter la version.
```powershell
& "$env:ProgramFiles\Wireshark\tshark.exe" -v | Select-Object -First 1
```
   👉 Explication : Permet de revenir à l'état connu.

2. Conserver l'installeur actuel et télécharger la nouvelle version sur https://www.wireshark.org/download.html; vérifier le SHA256.
   👉 Explication : Un installeur ancien sert de retour arrière.

3. PowerShell (administrateur) :
```powershell
winget upgrade --id WiresharkFoundation.Wireshark
```
GUI : lancer le nouvel installeur par-dessus.
   👉 Explication : Met à jour Wireshark; la mise à jour de Npcap peut être proposée séparément.

4. Revalider avec la fiche Valider la recette.
   👉 Explication : Confirme la capture après mise à jour.

5. Retour arrière : **Paramètres > Applications > Applications installées**, désinstaller Wireshark, puis réinstaller l'ancien installeur et restaurer les profils.
```powershell
winget uninstall --id WiresharkFoundation.Wireshark
```
   👉 Explication : Npcap est un composant distinct à désinstaller ou rétrograder si le pilote pose problème; un redémarrage peut être nécessaire.

## 2. Production — Contrôles

Planifier sur un poste pilote avant généralisation.

## 3. Production — Sécurité

- Aucun secret n'est écrit dans la fiche; capturer uniquement dans le périmètre autorisé.
- Les placeholders en MAJUSCULES sont à remplacer.

## Validation et retour arrière

- **Validation** : La version attendue est installée et la recette passe.
- **Retour arrière** : Réinstaller l'installeur précédent conservé.

## Si le problème n'est pas résolu

- [Wireshark — téléchargement officiel](https://www.wireshark.org/download.html)
- [Wireshark — guide utilisateur Windows](https://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallWinInstall.html)
- [Npcap — site officiel](https://npcap.com/)
- [Npcap — guide utilisateur et licence](https://npcap.com/guide/)
- [Série Debian 13 — Wireshark](/01-fiches-simples/debian/13/vie-du-logiciel/wireshark/fiche-simple-vm-debian-13-wireshark-analyse-installer)