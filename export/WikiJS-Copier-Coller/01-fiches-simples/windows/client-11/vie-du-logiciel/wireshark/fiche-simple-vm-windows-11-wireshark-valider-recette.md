# Fiche_Simple_-_VM_Windows_11_Wireshark_Valider_Recette.md

- **Environnement** : Poste Windows 11 x64 d'administration réseau (compte administrateur local disponible)
- **OS / Version** : Windows 11 x64; Wireshark stable (vérifier la version publiée) + Npcap
- **Catégorie** : analyse réseau

---

## Problème précis à résoudre

Prouver que Wireshark capture et analyse correctement.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier la version.
```powershell
& "$env:ProgramFiles\Wireshark\tshark.exe" -v | Select-Object -First 1
```
   👉 Explication : Confirme l'installation.

2. Capturer 10 paquets ICMP.
```powershell
& "$env:ProgramFiles\Wireshark\tshark.exe" -i NUMERO_INTERFACE -c 10 -f icmp -w C:\Captures\recette.pcapng
```
   👉 Explication : NUMERO_INTERFACE est à remplacer; ping en parallèle.

3. Relire le fichier.
```powershell
& "$env:ProgramFiles\Wireshark\tshark.exe" -r C:\Captures\recette.pcapng -c 5
```
   👉 Explication : Prouve l'écriture et la lecture.

4. GUI : ouvrir le fichier avec Wireshark, **Statistiques > Résumé**.
   👉 Explication : Contrôle l'affichage graphique.

## 2. Production — Contrôles

Conserver le résultat dans le ticket sans joindre le pcap s'il contient des données sensibles.

## 3. Production — Sécurité

- Aucun secret n'est écrit dans la fiche; capturer uniquement dans le périmètre autorisé.
- Les placeholders en MAJUSCULES sont à remplacer.

## Validation et retour arrière

- **Validation** : 10 paquets lus, aucune erreur de pilote.
- **Retour arrière** : Supprimer `recette.pcapng`; revenir à l'étape Installer en cas d'échec.

## Si le problème n'est pas résolu

- [Wireshark — téléchargement officiel](https://www.wireshark.org/download.html)
- [Wireshark — guide utilisateur Windows](https://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallWinInstall.html)
- [Npcap — site officiel](https://npcap.com/)
- [Npcap — guide utilisateur et licence](https://npcap.com/guide/)
- [Série Debian 13 — Wireshark](/01-fiches-simples/debian/13/vie-du-logiciel/wireshark/fiche-simple-vm-debian-13-wireshark-analyse-installer)