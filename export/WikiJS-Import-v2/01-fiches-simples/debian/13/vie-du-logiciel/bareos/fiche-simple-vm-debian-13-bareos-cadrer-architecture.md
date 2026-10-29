---
title: "Fiche Simple - VM Debian 13 Bareos Cadrer Architecture"
description: "Définir l'architecture et le plan de sauvegarde avant d'installer Bareos ou d'intégrer des données réelles."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "bareos", "backup", "architecture", "rpo", "rto"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Bareos_Cadrer_Architecture.md

- **Environnement** : lab Bareos 25 sur Debian 13, Director/Storage/File Daemon et catalogue PostgreSQL
- **OS / Version** : Debian 13 Trixie; Bareos Community 25
- **Catégorie** : sauvegarde réseau / cadrage
- **Tags** : `debian13`, `bareos`, `backup`, `architecture`, `rpo`, `rto`

---

## Problème précis à résoudre

Définir l'architecture et le plan de sauvegarde avant d'installer Bareos ou d'intégrer des données réelles.

## 1. Hors-Production (Lab / Test / POC)

1. Inventorier les rôles et le stockage :
   ```bash
   hostnamectl --static
   df -h /var/lib/bareos/storage 2>/dev/null || df -h /
   ```
   👉 Explication : Director, Storage Daemon (stockage dédié), File Daemon par client, catalogue PostgreSQL; séparer les rôles en production.

2. Relever les ports à ouvrir entre composants :
   ```bash
   sudo ss -ltnp | grep -E ':(9101|9102|9103)\b' || echo "ports Bareos non encore ouverts"
   ```
   👉 Explication : 9101 Director, 9102 File Daemon, 9103 Storage Daemon; les restreindre aux composants concernés.

3. Consigner : clients, FileSets, schedules, pools/volumes, rétention du catalogue, RPO/RTO.
   👉 Explication : chiffrer les communications (TLS) et prévoir le stockage hors site.

## 2. Production — Contrôles

Faire approuver capacité, séparation des rôles, stockage indépendant, rétention, chiffrement, fréquence des jobs, restauration et propriétaire de chaque donnée.

## 3. Production — Sécurité

- Ne pas inclure de données réelles avant un test de restauration concluant.
- Ne pas placer les secrets de ressources dans une documentation ou un dépôt.
- Limiter les ports Bareos aux composants concernés; exiger TLS selon la conception.
- Ne pas considérer Bareos seul comme un PRA complet.

## Validation et retour arrière

- **Validation** : architecture, clients, flux, RPO/RTO, sauvegardes et tests approuvés.
- **Arrêt** : ne pas déployer si stockage indépendant ou restauration testable n'est pas prévu.

## Si le problème n'est pas résolu

- [Bareos — éléments critiques avant production](https://docs.bareos.org/IntroductionAndTutorial/CriticalItemsToImplementBeforeProduction.html)
- [Bareos — démarrage](https://docs.bareos.org/IntroductionAndTutorial/GettingStartedWithBareos.html)
- [Guide complet Bareos Debian 13](/02-fiches-completes/debian/13/installation-deploiement/59-deploiement-bareos-25-debian-13#1-concevoir-larchitecture)