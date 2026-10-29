# Fiche_Simple_-_VM_Ubuntu_24.04_Packet_Tracer_Sauvegarder_Maintenir.md

- **Environnement** : Poste Ubuntu Desktop 24.04 (VM) pour la simulation réseau pédagogique
- **OS / Version** : Ubuntu Desktop 24.04 LTS amd64; Cisco Packet Tracer 9.0.1
- **Catégorie** : simulation réseau / maintenance

---

## Problème précis à résoudre

Conserver les fichiers sources et mettre à jour proprement.

## 1. Hors-Production (Lab / Test / POC)

1. Copier les fichiers source de simulation vers l'espace sauvegardé (destination d'exemple à remplacer) :
   ```bash
   cp -a ~/PacketTracer/*.pkt /chemin/sauvegarde/
   ```
   👉 Explication : le fichier modifiable prime sur une capture ou un PDF.

2. Contrôler la version installée :
   ```bash
   dpkg -l | grep -i packettracer
   ```
   👉 Explication : comparer avec la dernière version du Resource Hub.

3. Pour mettre à jour, retourner au Resource Hub Cisco, noter version et systèmes supportés, et installer uniquement le paquet Ubuntu : **https://www.netacad.com/resources/lab-downloads**
   👉 Explication : tester ensuite une copie du projet.

## 2. Production — Contrôles

Garder une copie de la version précédente selon la politique de poste.

## 3. Production — Sécurité

- Ne pas installer de paquet hors Resource Hub.

## Validation et retour arrière

- **Validation** : projets ouverts sans perte après mise à jour.
- **Retour arrière** : réinstaller la version précédente conservée et rouvrir la copie du projet.

## Si le problème n'est pas résolu

- [Cisco Networking Academy — téléchargements Packet Tracer](https://www.netacad.com/resources/lab-downloads)
- [Cisco — instructions de téléchargement et d'installation](https://www.netacad.com/skillsforall/files/Cisco_Packet_Tracer_Download_and_Installation_Instructions.pdf)
- [Guide complet Packet Tracer Ubuntu 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/78-deploiement-cisco-packet-tracer-9-0-1-ubuntu-24-04#6-sauvegarder-et-maintenir)