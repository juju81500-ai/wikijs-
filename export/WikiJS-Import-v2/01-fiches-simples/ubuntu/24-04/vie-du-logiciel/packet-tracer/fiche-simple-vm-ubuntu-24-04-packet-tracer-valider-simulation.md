---
title: "Fiche Simple - VM Ubuntu 24.04 Packet Tracer Valider Simulation"
description: "Vérifier qu'une topologie pédagogique locale se crée, se sauvegarde et fonctionne dans le simulateur sans être reliée à un réseau réel."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu2404", "cisco", "packettracer", "simulation", "validation", "formation"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Packet_Tracer_Valider_Simulation.md

- **Environnement** : Cisco Packet Tracer 9.0.1 sur Ubuntu Desktop 24.04 LTS
- **OS / Version** : Ubuntu 24.04 LTS amd64
- **Catégorie** : simulation réseau / formation
- **Tags** : `ubuntu2404`, `cisco`, `packettracer`, `simulation`, `validation`, `formation`

---

## Problème précis à résoudre

Vérifier qu'une topologie pédagogique locale se crée, se sauvegarde et fonctionne dans le simulateur sans être reliée à un réseau réel.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer Ubuntu 24.04 amd64 et les ressources :
   ```bash
   lsb_release -d
   dpkg --print-architecture
   nproc; free -h; df -h ~
   ```
   👉 Explication : comparer aux minimums du portail Cisco.

2. Installer le paquet 9.0.1 téléchargé depuis le Resource Hub Cisco/NetAcad :
   ```bash
   sudo apt install ./CiscoPacketTracer_901_Ubuntu_64bit.deb
   ```
   👉 Explication : le nom de fichier dépend du téléchargement; lancer ensuite **Cisco Packet Tracer** depuis le menu des applications.

3. Se connecter avec son propre compte Cisco/NetAcad quand le client le demande.
   👉 Explication : ne jamais partager de compte.

4. Créer la topologie : en bas à gauche, **End Devices** > glisser deux PC, **Network Devices > Switches** > un commutateur, puis **Connections** (câble droit) pour relier les PC au commutateur.
   👉 Explication : aucun nœud connecté au réseau physique.

5. Configurer des IP (clic sur PC > **Desktop > IP Configuration**, ex. 192.0.2.1 et 192.0.2.2 /24), tester avec **Desktop > Command Prompt** : `ping 192.0.2.2`. Enregistrer : **File > Save**, puis **File > Open**.
   👉 Explication : vérifier liens, adresses et résultat du ping après réouverture.

## 2. Production — Contrôles

Packet Tracer est un outil d'apprentissage et non une validation de configuration de production. Documenter le fichier, le cours, la version du client et les hypothèses du scénario.

## 3. Production — Sécurité

- Utiliser exclusivement le téléchargement Cisco officiel; accès du compte nominatif.
- Ne pas copier des secrets, données client ou configurations de production dans la maquette.
- Garder les simulations déconnectées des interfaces et réseaux réels.
- Vérifier les conditions Cisco avant de distribuer les fichiers de cours ou supports.

## Validation et retour arrière

- **Validation** : fichier rouvert, topologie intacte, résultat observable dans le simulateur, aucune liaison réelle.
- **Retour arrière** : conserver une copie du projet précédent et supprimer uniquement le projet temporaire.

## Si le problème n'est pas résolu

- [Cisco — ressources Packet Tracer](https://www.netacad.com/resources/lab-downloads)
- [Cisco — cours de démarrage Packet Tracer](https://www.netacad.com/courses/getting-started-cisco-packet-tracer)
- [Guide complet Packet Tracer 9.0.1 Ubuntu 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/78-deploiement-cisco-packet-tracer-9-0-1-ubuntu-24-04)