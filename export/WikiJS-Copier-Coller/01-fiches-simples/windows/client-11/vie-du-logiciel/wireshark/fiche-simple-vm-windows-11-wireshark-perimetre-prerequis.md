# Fiche_Simple_-_VM_Windows_11_Wireshark_Perimetre_Prerequis.md

- **Environnement** : Poste Windows 11 x64 d'administration réseau (compte administrateur local disponible)
- **OS / Version** : Windows 11 x64; Wireshark stable (vérifier la version publiée) + Npcap
- **Catégorie** : analyse réseau

---

## Problème précis à résoudre

Cadrer le périmètre légal et technique avant d'installer Wireshark et Npcap sur un poste Windows 11.

## 1. Hors-Production (Lab / Test / POC)

1. Obtenir l'autorisation écrite de capturer (réseau, interfaces, durée) auprès du responsable du réseau.
   👉 Explication : Une capture peut contenir des données personnelles et des identifiants en clair.

2. Vérifier l'architecture et la version de Windows.
```powershell
(Get-CimInstance Win32_OperatingSystem).Version; $env:PROCESSOR_ARCHITECTURE
```
   👉 Explication : Windows 11 et x64/ARM64 déterminent le bon installeur (vérifier la version publiée).

3. Vérifier les droits : ouvrir **Démarrer > Windows PowerShell > Exécuter en tant qu'administrateur**.
```powershell
([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
```
   👉 Explication : `True` : l'installation du pilote Npcap exige l'administrateur.

4. Lire la licence Npcap sur https://npcap.com/ (édition gratuite limitée à un usage restreint; usage en entreprise, redistribution ou installation silencieuse : licence OEM/Pro).
   👉 Explication : Le pilote Npcap est obligatoire pour capturer; sans lui Wireshark ne peut qu'ouvrir des fichiers existants.

5. Lister les besoins : capture Ethernet/Wi-Fi seulement, mode monitor Wi-Fi, ou USB.
   👉 Explication : Les options de l'installeur (mode monitor 802.11, USBPcap) ne se cochent que si nécessaires.

## 2. Production — Contrôles

Limites : mode monitor Wi-Fi dépendant de la carte et du pilote, souvent indisponible sous Windows; capture du trafic d'autres postes impossible sans miroir de port.

## 3. Production — Sécurité

- Aucun secret n'est écrit dans la fiche; capturer uniquement dans le périmètre autorisé.
- Les placeholders en MAJUSCULES sont à remplacer.

## Validation et retour arrière

- **Validation** : Décision écrite : périmètre, version, options et licence Npcap validés.
- **Retour arrière** : Aucune modification n'a été faite; rien à annuler.

## Si le problème n'est pas résolu

- [Wireshark — téléchargement officiel](https://www.wireshark.org/download.html)
- [Wireshark — guide utilisateur Windows](https://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallWinInstall.html)
- [Npcap — site officiel](https://npcap.com/)
- [Npcap — guide utilisateur et licence](https://npcap.com/guide/)
- [Série Debian 13 — Wireshark](/01-fiches-simples/debian/13/vie-du-logiciel/wireshark/fiche-simple-vm-debian-13-wireshark-analyse-installer)