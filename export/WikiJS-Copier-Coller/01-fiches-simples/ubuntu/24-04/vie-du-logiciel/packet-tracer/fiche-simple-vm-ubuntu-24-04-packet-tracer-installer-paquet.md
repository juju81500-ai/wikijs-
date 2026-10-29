# Fiche_Simple_-_VM_Ubuntu_24.04_Packet_Tracer_Installer_Paquet.md

- **Environnement** : Poste Ubuntu Desktop 24.04 (VM) pour la simulation réseau pédagogique
- **OS / Version** : Ubuntu Desktop 24.04 LTS amd64; Cisco Packet Tracer 9.0.1
- **Catégorie** : simulation réseau / installation

---

## Problème précis à résoudre

Installer Packet Tracer sans contourner les dépendances.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le système :
   ```bash
   cat /etc/os-release
   dpkg --print-architecture
   free -h
   df -h "$HOME"
   ```
   👉 Explication : confirme l'OS avant d'installer.

2. Ouvrir le dossier de téléchargement : **Fichiers > Téléchargements**, puis ouvrir le `.deb` avec **Installation de logiciels** et confirmer avec l'authentification système.
   👉 Explication : méthode graphique décrite par le guide.

3. Si une dépendance manque, annuler et vérifier les dépôts officiels :
   ```bash
   sudo apt update
   ```
   👉 Explication : ne pas ajouter de dépôt tiers.

## 2. Production — Contrôles

Redémarrer la session graphique si l'application n'apparaît pas dans le menu.

## 3. Production — Sécurité

- Ne pas lancer de script de forum pour contourner une dépendance.
- Ne pas ajouter de dépôt Debian ou Ubuntu tiers.

## Validation et retour arrière

- **Validation** : Packet Tracer apparaît dans le menu des applications.
- **Retour arrière** : **Installation de logiciels > Packet Tracer > Désinstaller**.

## Si le problème n'est pas résolu

- [Cisco Networking Academy — téléchargements Packet Tracer](https://www.netacad.com/resources/lab-downloads)
- [Cisco — instructions de téléchargement et d'installation](https://www.netacad.com/skillsforall/files/Cisco_Packet_Tracer_Download_and_Installation_Instructions.pdf)
- [Guide complet Packet Tracer Ubuntu 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/78-deploiement-cisco-packet-tracer-9-0-1-ubuntu-24-04#3-installer-le-paquet)