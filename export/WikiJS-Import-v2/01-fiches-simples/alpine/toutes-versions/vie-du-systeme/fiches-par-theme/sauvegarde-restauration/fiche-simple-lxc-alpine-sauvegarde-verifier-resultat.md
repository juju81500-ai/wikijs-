---
title: "Fiche Simple - LXC Alpine Sauvegarde Verifier Resultat"
description: "Confirmer que le job a protégé le CT et ses dépendances et que les éléments requis pour une récupération sont disponibles."
published: true
date: 2026-10-29T20:14:10Z
tags: ["alpine", "proxmox", "pbs", "backup", "verification"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_LXC_Alpine_Sauvegarde_Verifier_Resultat.md

- **Environnement** : job de sauvegarde CT sur PVE/PBS et accès aux journaux autorisés
- **OS / Version** : Proxmox VE et PBS selon versions déployées
- **Catégorie** : sauvegarde LXC / contrôle
- **Tags** : `alpine`, `proxmox`, `pbs`, `backup`, `verification`

---

## Problème précis à résoudre

Confirmer que le job a protégé le CT et ses dépendances et que les éléments requis pour une récupération sont disponibles.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le journal du job : **Datacenter > Backup** (dernier résultat) ou **Nœud > Tasks**, et côté PBS **Datastore > Content**.
   👉 Explication : vérifier date, durée, taille et statut `OK`.

2. Vérifier la liste des sauvegardes et l'espace :
   ```bash
   pvesm list STOCKAGE_PBS --vmid CTID
   pvesm status
   ```
   👉 Explication : la rétention et l'espace de la cible doivent être suffisants; lancer aussi une vérification d'intégrité côté PBS (**Verify**).

3. Conserver la configuration du CT et les clés hors du CT :
   ```bash
   pct config CTID > /root/ct-CTID.conf
   ```
   👉 Explication : sauvegarder clés de chiffrement et secrets dans le coffre prévu, avec la liste des montages.

## 2. Production — Contrôles

Documenter le JobID ou point de sauvegarde, durée, taille, résultat d'intégrité, rétention et anomalies avec l'équipe responsable.

## 3. Production — Sécurité

- Ne pas publier les secrets ni les clés de chiffrement dans les journaux ou la fiche.
- Ne pas considérer un job réussi comme une preuve de restaurabilité.
- Limiter l'accès aux journaux, inventaires et configurations de récupération.
- Ne pas effacer d'anciens points avant de vérifier la politique de rétention.

## Validation et retour arrière

- **Validation** : sauvegarde présente et vérifiée, configuration CT recensée, clés accessibles aux personnes autorisées.
- **Arrêt** : déclencher une investigation si données, volume ou statut ne correspond pas au périmètre approuvé.

## Si le problème n'est pas résolu

- [Proxmox Backup Server — vérification d'intégrité](https://pbs.proxmox.com/docs/maintenance.html)
- [Proxmox Backup Server — documentation](https://pbs.proxmox.com/docs/)
- [Guide complet sauvegarde/restauration LXC Alpine](/02-fiches-completes/alpine/toutes-versions/autres/18-alpine-lxc-sauvegarde-restauration-production#3-verifier-le-resultat-de-sauvegarde)