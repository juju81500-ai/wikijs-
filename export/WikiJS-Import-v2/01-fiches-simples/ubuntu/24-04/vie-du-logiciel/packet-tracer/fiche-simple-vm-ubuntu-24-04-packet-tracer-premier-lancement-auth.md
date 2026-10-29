---
title: "Fiche Simple - VM Ubuntu 24.04 Packet Tracer Premier Lancement Auth"
description: "Se connecter avec le compte propriétaire et ranger les fichiers correctement."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu24.04", "cisco", "packet-tracer", "netacad", "authentification"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Packet_Tracer_Premier_Lancement_Auth.md

- **Environnement** : Poste Ubuntu Desktop 24.04 (VM) pour la simulation réseau pédagogique
- **OS / Version** : Ubuntu Desktop 24.04 LTS amd64; Cisco Packet Tracer 9.0.1
- **Catégorie** : simulation réseau / authentification
- **Tags** : `ubuntu24.04`, `cisco`, `packet-tracer`, `netacad`, `authentification`

---

## Problème précis à résoudre

Se connecter avec le compte propriétaire et ranger les fichiers correctement.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer l'application : **Activités > Cisco Packet Tracer**
   👉 Explication : ouvre l'application depuis le menu.

2. Cliquer le bouton de connexion **Skills for All / NetAcad** puis se connecter avec son compte.
   👉 Explication : ne pas partager le compte de cours entre opérateurs.

3. Créer un dossier de travail personnel :
   ```bash
   mkdir -p ~/PacketTracer
   ```
   👉 Explication : les diagrammes restent dans le répertoire utilisateur ou l'espace de cours approuvé.

## 2. Production — Contrôles

Poste de cours: un compte par utilisateur.

## 3. Production — Sécurité

- Ne pas y copier de configurations réelles, mots de passe ou données client.

## Validation et retour arrière

- **Validation** : connexion réussie.
- **Retour arrière** : **Packet Tracer > Fichier > Se déconnecter**.

## Si le problème n'est pas résolu

- [Cisco Networking Academy — téléchargements Packet Tracer](https://www.netacad.com/resources/lab-downloads)
- [Cisco — instructions de téléchargement et d'installation](https://www.netacad.com/skillsforall/files/Cisco_Packet_Tracer_Download_and_Installation_Instructions.pdf)
- [Guide complet Packet Tracer Ubuntu 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/78-deploiement-cisco-packet-tracer-9-0-1-ubuntu-24-04#4-premier-lancement-et-authentification)