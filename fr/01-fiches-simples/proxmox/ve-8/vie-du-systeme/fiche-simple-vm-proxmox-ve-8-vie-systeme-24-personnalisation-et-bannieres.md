---
title: "Fiche Simple - VM Proxmox VE 8 Vie Systeme 24 Personnalisation Et Bannieres"
description: "Afficher un avertissement légal à la connexion."
published: true
date: 2026-11-03T09:36:13Z
tags: ["proxmoxve8", "vie-du-systeme", "cycle-de-vie", "etape-24"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_24_Personnalisation_Et_Bannieres

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 24 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-24`

---

## Problème précis à résoudre

Afficher un avertissement légal à la connexion.

## 1. Hors-Production (Lab / Test / POC)

1. Éditer la bannière [[Glossary:SSH]] :
   ```bash
   echo 'Accès réservé aux administrateurs autorisés. Toute connexion est journalisée.' > /etc/issue.net
   nano /etc/ssh/sshd_config
   ```
   👉 Explication : ajouter `Banner /etc/issue.net` puis `systemctl reload ssh`.

2. Ajouter des notes au nœud ([[Glossary:GUI]] : **Nœud > Summary > Notes**).
   👉 Explication : indique le rôle et le responsable de l'hôte.

3. Mettre à jour `/etc/motd` avec le nom et le rôle de l'hôte.
   ```bash
   nano /etc/motd
   ```
   👉 Explication : rappel visible à chaque connexion console.

## 2. Production — Contrôles

Texte validé par le service juridique.

## 3. Production — Sécurité

La bannière ne doit pas révéler de version ni d'information sensible.

## Validation et retour arrière

- **Validation** : La bannière s'affiche à la connexion SSH.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire Proxmox VE 8](/fr/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)