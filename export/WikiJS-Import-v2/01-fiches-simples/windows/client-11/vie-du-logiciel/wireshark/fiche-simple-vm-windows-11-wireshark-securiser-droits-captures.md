---
title: "Fiche Simple - VM Windows 11 Wireshark Securiser Droits Captures"
description: "Limiter qui peut capturer et protéger les fichiers de capture."
published: true
date: 2026-10-29T20:55:32Z
tags: ["wireshark", "npcap", "windows11", "capture", "pcap"]
editor: markdown
dateCreated: 2026-10-29T20:55:32Z
dateModified: 2026-10-29T20:55:32Z
---

# Fiche_Simple_-_VM_Windows_11_Wireshark_Securiser_Droits_Captures.md

- **Environnement** : Poste Windows 11 x64 d'administration réseau (compte administrateur local disponible)
- **OS / Version** : Windows 11 x64; Wireshark stable (vérifier la version publiée) + Npcap
- **Catégorie** : analyse réseau
- **Tags** : `wireshark`, `npcap`, `windows11`, `capture`, `pcap`

---

## Problème précis à résoudre

Limiter qui peut capturer et protéger les fichiers de capture.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installeur Npcap (ou en le réinstallant), choisir si la capture est réservée aux administrateurs (« Restrict Npcap driver's access to Administrators only »).
   👉 Explication : Réserver aux admins limite l'écoute du réseau par un compte standard; l'effet exact dépend de la version publiée.

2. Restreindre le dossier de captures.
```powershell
icacls C:\Captures /inheritance:r /grant:r "BUILTIN\Administrators:(OI)(CI)F" "NT AUTHORITY\SYSTEM:(OI)(CI)F"
```
   👉 Explication : Seuls administrateurs et SYSTEM accèdent aux fichiers.

3. Vérifier les droits.
```powershell
icacls C:\Captures
```
   👉 Explication : Contrôle le résultat.

4. Ne pas utiliser « Capture > Options > Save » vers un partage ou un dossier synchronisé (OneDrive).
   👉 Explication : Évite la fuite de données capturées.

5. Supprimer les captures après analyse ou les chiffrer (clic droit > Propriétés > Avancé > Chiffrer ou BitLocker).
   👉 Explication : Les pcap peuvent contenir des mots de passe en clair; BitLocker protège le volume.

## 2. Production — Contrôles

Ne pas lancer Wireshark GUI en administrateur en continu : privilégier la capture par TShark/dumpcap puis analyse en compte standard.

## 3. Production — Sécurité

- Aucun secret n'est écrit dans la fiche; capturer uniquement dans le périmètre autorisé.
- Les placeholders en MAJUSCULES sont à remplacer.

## Validation et retour arrière

- **Validation** : Un compte standard non autorisé ne lit pas `C:\Captures`.
- **Retour arrière** : Rétablir les droits : `icacls C:\Captures /reset /T`.

## Si le problème n'est pas résolu

- [Wireshark — téléchargement officiel](https://www.wireshark.org/download.html)
- [Wireshark — guide utilisateur Windows](https://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallWinInstall.html)
- [Npcap — site officiel](https://npcap.com/)
- [Npcap — guide utilisateur et licence](https://npcap.com/guide/)
- [Série Debian 13 — Wireshark](/01-fiches-simples/debian/13/vie-du-logiciel/wireshark/fiche-simple-vm-debian-13-wireshark-analyse-installer)