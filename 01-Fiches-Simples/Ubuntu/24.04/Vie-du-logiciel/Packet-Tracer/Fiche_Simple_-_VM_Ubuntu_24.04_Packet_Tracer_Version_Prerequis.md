# Fiche_Simple_-_VM_Ubuntu_24.04_Packet_Tracer_Version_Prerequis.md

- **Environnement** : Poste Ubuntu Desktop 24.04 (VM) pour la simulation réseau pédagogique
- **OS / Version** : Ubuntu Desktop 24.04 LTS amd64; Cisco Packet Tracer 9.0.1
- **Catégorie** : simulation réseau / prérequis
- **Tags** : `ubuntu24.04`, `cisco`, `packet-tracer`, `netacad`, `prerequis`

---

## Problème précis à résoudre

Vérifier que le poste est compatible avec Packet Tracer 9.0.1.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'OS, l'architecture, la mémoire et le disque :
   ```bash
   cat /etc/os-release | grep PRETTY_NAME
   dpkg --print-architecture
   free -h
   df -h "$HOME"
   ```
   👉 Explication : Ubuntu 22.04/24.04 amd64, 4 Go de RAM libre et 1,4 Go de disque sont indiqués.

## 2. Production — Contrôles

Un poste de cours reste un poste pédagogique; Packet Tracer ne valide pas un équipement réel.

## 3. Production — Sécurité

- Le téléchargement est réservé aux comptes Cisco/NetAcad; ne pas automatiser l'authentification.

## Validation et retour arrière

- **Validation** : Ubuntu 24.04 amd64 avec ressources suffisantes.
- **Retour arrière** : lecture seule: rien à annuler.

## Si le problème n'est pas résolu

- [Cisco Networking Academy — téléchargements Packet Tracer](https://www.netacad.com/resources/lab-downloads)
- [Cisco — instructions de téléchargement et d'installation](https://www.netacad.com/skillsforall/files/Cisco_Packet_Tracer_Download_and_Installation_Instructions.pdf)
- [Guide complet Packet Tracer Ubuntu 24.04](../../../../../02-Fiches-Completes/Ubuntu/24.04/Installation-Deploiement/78_Deploiement_Cisco_Packet_Tracer_9.0.1_Ubuntu_24.04.md#1-version-et-prerequis)
