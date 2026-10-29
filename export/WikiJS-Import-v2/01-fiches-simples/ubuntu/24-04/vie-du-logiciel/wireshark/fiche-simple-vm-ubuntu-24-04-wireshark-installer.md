---
title: "Fiche Simple - VM Ubuntu 24.04 Wireshark Installer"
description: "Installer Wireshark (GUI) et TShark (CLI) depuis les dépôts Ubuntu."
published: true
date: 2026-10-29T20:58:07Z
tags: ["wireshark", "ubuntu24.04", "vie-du-logiciel", "installer"]
editor: markdown
dateCreated: 2026-10-29T20:58:07Z
dateModified: 2026-10-29T20:58:07Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Wireshark_Installer

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Wireshark
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Wireshark / installation
- **Tags** : `wireshark`, `ubuntu24.04`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer Wireshark (GUI) et TShark (CLI) depuis les dépôts Ubuntu.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les paquets candidats :
   ```bash
   sudo apt update
   apt-cache policy wireshark tshark wireshark-common
   ```
   👉 Explication : Confirme noms, versions et origine avant installation; noms de paquets à vérifier si la distribution les a modifiés.

2. Installer :
   ```bash
   sudo apt install wireshark tshark
   ```
   👉 Explication : Installe l’analyseur et les outils en ligne de commande. Pendant l’installation, répondre « Non » à la question sur la capture par les non-superutilisateurs si la capture ne doit pas être déléguée; pour la changer plus tard : `sudo dpkg-reconfigure wireshark-common`.

3. Contrôler les versions :
   ```bash
   wireshark --version | head -n 1
   tshark --version | head -n 1
   dumpcap --version | head -n 1
   ```
   👉 Explication : Consigne la version; en session sans écran, `wireshark` peut échouer, ce qui est normal : tshark suffit.

## 2. Production — Contrôles

Consigner version et origine; décider qui reçoit le droit de capture.

## 3. Production — Sécurité

- Ne jamais lancer l’interface graphique en root.
- Préférer les dépôts de la distribution.

## Validation et retour arrière

- **Validation** : Les trois commandes affichent une version.
- **Retour arrière** : Désinstaller : `sudo apt remove wireshark tshark wireshark-common`.

## Si le problème n’est pas résolu

- [Wireshark — documentation officielle](https://www.wireshark.org/docs/)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireshark)
- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireshark/fiche-simple-vm-ubuntu-24-04-wireshark-configurer)
- [Étape précédente du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/wireshark/fiche-simple-vm-ubuntu-24-04-wireshark-prerequis-limites)