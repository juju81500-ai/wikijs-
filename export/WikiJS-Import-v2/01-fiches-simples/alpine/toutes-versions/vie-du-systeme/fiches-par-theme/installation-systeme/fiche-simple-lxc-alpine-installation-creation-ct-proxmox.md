---
title: "Fiche Simple - LXC Alpine Installation Creation CT Proxmox"
description: "Créer un conteneur LXC Alpine sur Proxmox à partir d'un template maintenu, avec les ressources, le stockage et le réseau adaptés au rôle prévu."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[alpine]", "[proxmox]", "[lxc]", "[installation]", "[template]", "[unprivileged]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Fiche_Simple_-_LXC_Alpine_Installation_Creation_CT_Proxmox.md

- **Environnement** : Hôte Proxmox VE et nouveau conteneur LXC
- **OS / Version** : Alpine Linux depuis un template maintenu proposé par Proxmox
- **Catégorie** : Installation / Virtualisation
- **Tags** : `[alpine]`, `[proxmox]`, `[lxc]`, `[installation]`, `[template]`, `[unprivileged]`

## 🎯 Problème précis à résoudre
Créer un conteneur LXC Alpine sur Proxmox à partir d'un template maintenu, avec les ressources, le stockage et le réseau adaptés au rôle prévu.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Sur le nœud Proxmox, mettre à jour la liste des templates et repérer une branche Alpine maintenue :
   ```bash
   pveam update
   pveam available | grep -i alpine
   ```
2. Télécharger le template vers le stockage de templates du nœud :
   ```bash
   pveam download <STOCKAGE_TEMPLATE> <NOM_TEMPLATE_ALPINE>
   ```
3. Créer le CT dans l'interface Proxmox : **Créer CT > Général > Template > Disques > CPU > Mémoire > Réseau > DNS > Confirmer**.
   - Utiliser un identifiant unique, un hostname conforme et un mot de passe administrateur transmis de manière sécurisée.
   - Choisir un CT non privilégié; donner au disque, CPU et mémoire les valeurs nécessaires au lab.
   - Sélectionner le bridge/VLAN réellement configuré et une adresse DHCP ou statique réservée.
   👉 *Explication : noms de stockages, bridge, VLAN, adresse IP et template sont des exemples dépendants du cluster.*

## ⚡ 2. Production — Façon Simplifiée
1. Confirmer le template maintenu, les besoins de l'application, les quotas, les points de montage et la politique de sauvegarde.
2. Dans **Options**, conserver le démarrage automatique uniquement si requis; dans **Ressources**, éviter le nesting et les périphériques hôte sauf besoin validé.
3. Démarrer le CT et vérifier depuis sa console :
   ```sh
   cat /etc/alpine-release
   ip -br addr
   ip route
   rc-status
   ```
4. Appliquer les fiches distinctes de première configuration, réseau, compte d'administration et services.

## 🔒 3. Production — Façon Sécurisée
1. Préférer un CT non privilégié, limiter les capacités et ne pas monter des chemins sensibles de l'hôte.
2. Ne pas activer nesting, FUSE ou accès périphérique pour contourner un besoin sans évaluer l'isolation.
3. Ne pas choisir Alpine 3.19 pour un nouveau déploiement; utiliser une branche maintenue disponible et prévoir son cycle de mises à jour.

## ✅ Validation et retour arrière
- Vérifier l'ID/hostname, le template, les ressources, le bridge/VLAN, l'adresse, le démarrage et le statut non privilégié.
- Avant toute donnée de production, effectuer une sauvegarde test et confirmer que la restauration est possible.
- Supprimer un CT de test uniquement après avoir vérifié son ID et l'absence de données à conserver.