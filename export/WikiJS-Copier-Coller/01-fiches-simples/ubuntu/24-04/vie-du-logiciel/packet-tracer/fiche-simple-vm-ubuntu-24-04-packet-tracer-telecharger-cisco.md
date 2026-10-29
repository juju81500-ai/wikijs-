# Fiche_Simple_-_VM_Ubuntu_24.04_Packet_Tracer_Telecharger_Cisco.md

- **Environnement** : Poste Ubuntu Desktop 24.04 (VM) pour la simulation réseau pédagogique
- **OS / Version** : Ubuntu Desktop 24.04 LTS amd64; Cisco Packet Tracer 9.0.1
- **Catégorie** : simulation réseau / téléchargement

---

## Problème précis à résoudre

Obtenir le paquet officiel Packet Tracer pour Ubuntu.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir le Resource Hub et se connecter avec son compte : **https://www.netacad.com/resources/lab-downloads > Connexion**
   👉 Explication : accès réservé aux comptes Cisco/NetAcad.

2. Si nécessaire, s'inscrire au cours gratuit : **Getting Started with Cisco Packet Tracer > Enroll**
   👉 Explication : ce cours donne accès aux ressources.

3. Sélectionner **Packet Tracer 9.0.1 Ubuntu 64bit** et conserver le nom d'origine du fichier.
   👉 Explication : seul le paquet Linux officiel est à télécharger; noter la version obtenue.

4. Lister le fichier téléchargé :
   ```bash
   ls -l ~/Téléchargements/
   ```
   👉 Explication : confirme nom et taille (aucun hash n'est publié par l'éditeur).

## 2. Production — Contrôles

Si le portail propose une autre version, vérifier ses prérequis et son manuel d'abord.

## 3. Production — Sécurité

- Ne pas télécharger depuis un miroir tiers.
- Ne pas fabriquer ni réutiliser une empreinte provenant d'un site tiers.

## Validation et retour arrière

- **Validation** : paquet `.deb` Ubuntu officiel obtenu.
- **Retour arrière** : supprimer le fichier téléchargé.

## Si le problème n'est pas résolu

- [Cisco Networking Academy — téléchargements Packet Tracer](https://www.netacad.com/resources/lab-downloads)
- [Cisco — instructions de téléchargement et d'installation](https://www.netacad.com/skillsforall/files/Cisco_Packet_Tracer_Download_and_Installation_Instructions.pdf)
- [Guide complet Packet Tracer Ubuntu 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/78-deploiement-cisco-packet-tracer-9-0-1-ubuntu-24-04#2-telecharger-depuis-cisco)