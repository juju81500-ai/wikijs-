# Fiche_Simple_-_VM_Windows_11_Wireshark_Configurer_Capture_Locale.md

- **Environnement** : Poste Windows 11 x64 d'administration réseau (compte administrateur local disponible)
- **OS / Version** : Windows 11 x64; Wireshark stable (vérifier la version publiée) + Npcap
- **Catégorie** : analyse réseau

---

## Problème précis à résoudre

Réaliser une première capture locale limitée à une interface et un filtre.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les interfaces.
```powershell
& "$env:ProgramFiles\Wireshark\tshark.exe" -D
```
   👉 Explication : Repère le numéro de l'interface à capturer.

2. GUI : ouvrir Wireshark en administrateur si nécessaire, **Capture > Options**, cocher l'interface, saisir le filtre de capture `host ADRESSE_IP` (à remplacer).
   👉 Explication : Le filtre de capture limite le volume et les données collectées.

3. Ligne de commande : capture 30 s dans un fichier.
```powershell
New-Item -ItemType Directory -Force C:\Captures | Out-Null
& "$env:ProgramFiles\Wireshark\tshark.exe" -i NUMERO_INTERFACE -a duration:30 -f "host ADRESSE_IP" -w C:\Captures\test.pcapng
```
   👉 Explication : NUMERO_INTERFACE et ADRESSE_IP sont à remplacer; sans Npcap, la commande échoue.

4. Générer du trafic : `ping ADRESSE_IP` dans un autre terminal.
   👉 Explication : Produit des paquets ICMP à observer.

5. GUI : **Fichier > Ouvrir**, `C:\Captures\test.pcapng`, filtre d'affichage `icmp`.
   👉 Explication : Le filtre d'affichage ne modifie pas le fichier.

6. Profils : **Édition > Configuration Profiles** pour créer un profil `LAB`.
   👉 Explication : Isole colonnes et filtres par usage.

## 2. Production — Contrôles

Capture limitée : boucle locale non capturable sans l'adaptateur Npcap Loopback; mode monitor non garanti.

## 3. Production — Sécurité

- Aucun secret n'est écrit dans la fiche; capturer uniquement dans le périmètre autorisé.
- Les placeholders en MAJUSCULES sont à remplacer.

## Validation et retour arrière

- **Validation** : Des paquets ICMP apparaissent dans le fichier.
- **Retour arrière** : Supprimer `C:\Captures\test.pcapng` et le profil de test.

## Si le problème n'est pas résolu

- [Wireshark — téléchargement officiel](https://www.wireshark.org/download.html)
- [Wireshark — guide utilisateur Windows](https://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallWinInstall.html)
- [Npcap — site officiel](https://npcap.com/)
- [Npcap — guide utilisateur et licence](https://npcap.com/guide/)
- [Série Debian 13 — Wireshark](/01-fiches-simples/debian/13/vie-du-logiciel/wireshark/fiche-simple-vm-debian-13-wireshark-analyse-installer)