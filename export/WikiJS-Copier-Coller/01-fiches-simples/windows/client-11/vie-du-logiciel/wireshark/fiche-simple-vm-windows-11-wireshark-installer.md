# Fiche_Simple_-_VM_Windows_11_Wireshark_Installer.md

- **Environnement** : Poste Windows 11 x64 d'administration réseau (compte administrateur local disponible)
- **OS / Version** : Windows 11 x64; Wireshark stable (vérifier la version publiée) + Npcap
- **Catégorie** : analyse réseau

---

## Problème précis à résoudre

Installer Wireshark et Npcap depuis les sources officielles.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'installeur depuis https://www.wireshark.org/download.html (GUI : navigateur).
   👉 Explication : Source officielle uniquement; pas de site tiers.

2. Vérifier le hash SHA256 publié sur la page de téléchargement.
```powershell
Get-FileHash "$env:USERPROFILE\Downloads\FICHIER_INSTALLEUR.exe" -Algorithm SHA256
```
   👉 Explication : Remplacer FICHIER_INSTALLEUR par le nom téléchargé; comparer au hash officiel.

3. GUI : double-cliquer l'installeur (UAC > Oui), accepter la licence, garder Wireshark et TShark, puis à l'écran Npcap laisser l'installation de Npcap.
   👉 Explication : Npcap est le pilote de capture; l'installeur Wireshark le propose ou le lance.

4. Npcap : si proposé séparément, télécharger sur https://npcap.com/#download. Options : cocher « Support raw 802.11 traffic (monitor mode) » seulement si nécessaire; ne pas cocher « Restrict Npcap driver's access to Administrators only » si des utilisateurs standard doivent capturer (voir fiche Sécuriser).
   👉 Explication : Les cases dépendent de l'écran proposé par l'installeur; vérifier la version publiée.

5. USBPcap (si proposé) : ne l'installer que pour capturer des périphériques USB.
   👉 Explication : Composant optionnel supplémentaire avec son propre pilote; à éviter sinon.

6. PowerShell (administrateur) pour Wireshark seul via winget, si winget est disponible :
```powershell
winget install --id WiresharkFoundation.Wireshark --source winget
```
   👉 Explication : Installation depuis le dépôt winget; Npcap peut nécessiter une étape GUI. L'installation silencieuse de Npcap relève de la licence OEM.

7. Vérifier l'installation.
```powershell
& "$env:ProgramFiles\Wireshark\tshark.exe" -v | Select-Object -First 1
Get-Service npcap -ErrorAction SilentlyContinue
```
   👉 Explication : Affiche la version de TShark et l'état du service Npcap.

## 2. Production — Contrôles

Un redémarrage peut être demandé après installation du pilote.

## 3. Production — Sécurité

- Aucun secret n'est écrit dans la fiche; capturer uniquement dans le périmètre autorisé.
- Les placeholders en MAJUSCULES sont à remplacer.

## Validation et retour arrière

- **Validation** : `tshark -v` répond et `tshark -D` liste les interfaces.
- **Retour arrière** : Désinstaller via **Paramètres > Applications > Applications installées** : Wireshark, puis Npcap (voir fiche MAJ/retour arrière).

## Si le problème n'est pas résolu

- [Wireshark — téléchargement officiel](https://www.wireshark.org/download.html)
- [Wireshark — guide utilisateur Windows](https://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallWinInstall.html)
- [Npcap — site officiel](https://npcap.com/)
- [Npcap — guide utilisateur et licence](https://npcap.com/guide/)
- [Série Debian 13 — Wireshark](/01-fiches-simples/debian/13/vie-du-logiciel/wireshark/fiche-simple-vm-debian-13-wireshark-analyse-installer)