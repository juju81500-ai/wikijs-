---
title: "Fiche Simple - VM Proxmox pfSense CE Deploiement Installer pfSense CE"
description: "Installer pfSense CE sur le disque virtuel et affecter correctement WAN et LAN."
published: true
date: 2026-10-29T20:22:42Z
tags: ["pfsense", "ce", "proxmox", "firewall", "lab"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Fiche_Simple_-_VM_Proxmox_pfSense_CE_Deploiement_Installer_pfSense_CE.md

- **Environnement** : VM pfSense CE en laboratoire sur Proxmox VE, deux interfaces (WAN et LAN isolés)
- **OS / Version** : pfSense Community Edition 2.9.0 (VM x86-64 sur Proxmox VE)
- **Catégorie** : pare-feu et routage
- **Tags** : `pfsense`, `ce`, `proxmox`, `firewall`, `lab`

---

## Problème précis à résoudre

Installer pfSense CE sur le disque virtuel et affecter correctement WAN et LAN.

## 1. Hors-Production (Lab / Test / POC)

1. Démarrer la VM sur le Netgate Installer : **VM > Démarrer** puis **Console**.
   👉 Explication : lance l'assistant officiel.

2. Sélectionner **Install CE** si le matériel est éligible à pfSense Plus.
   👉 Explication : le scénario du guide est CE; choisir la version marquée courante/stable.

3. Choisir le disque cible, vérifier son identité, puis accepter le partitionnement.
   👉 Explication : l'installation efface le disque sélectionné; il doit être le disque virtuel vide de la VM.

4. Terminer puis redémarrer en retirant l'ISO : **Matériel > CD/DVD > Ne pas utiliser de média**.
   👉 Explication : évite de relancer l'installateur.

5. Dans Proxmox, relever les MAC de chaque carte :
   ```bash
   sudo qm config 9100 | grep net
   ```
   👉 Explication : les MAC affichées servent à vérifier l'affectation (9100 = identifiant d'exemple à remplacer).

6. À l'assignation des interfaces dans la console pfSense, affecter `vtnet0` au WAN et `vtnet1` au LAN en confirmant par les MAC.
   👉 Explication : ne pas se fier à l'ordre supposé si les MAC ne correspondent pas.

## 2. Production — Contrôles

Conserver la capture de la version installée et de l'affectation des interfaces.

## 3. Production — Sécurité

- La politique sortante par défaut du LAN (tout autorisé) n'est pas une politique finale.

## Validation et retour arrière

- **Validation** : la console affiche WAN sur `vtnet0` et LAN sur `vtnet1` avec l'IP LAN `192.168.1.1`.
- **Retour arrière** : recréer la VM de test si l'installation est incorrecte; rien d'autre n'est touché.

## Si le problème n'est pas résolu

- [Netgate — assistant d'installation](https://docs.netgate.com/pfsense/en/latest/install/install-walkthrough.html)
- [Netgate — pfSense CE 2.9.0](https://docs.netgate.com/pfsense/en/latest/releases/2-9-0.html)
- [Guide complet](/02-fiches-completes/pfsense/toutes-versions/installation-deploiement/70-deploiement-pfsense-ce-2-9-0-proxmox-lab#4-installer-pfsense-ce)