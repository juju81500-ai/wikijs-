---
title: "Fiche Simple - VM Debian 13 rsync Cadrer Besoin"
description: "Définir le périmètre et les limites de la copie avant toute synchronisation afin de ne pas confondre miroir et sauvegarde historisée."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "rsync", "sauvegarde", "cadrage", "rpo"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_rsync_Cadrer_Besoin.md

- **Environnement** : Debian 13 Trixie; copie locale ou transfert SSH vers une destination autorisée
- **OS / Version** : Debian 13; rsync depuis les dépôts Debian
- **Catégorie** : sauvegarde de fichiers / cadrage
- **Tags** : `debian13`, `rsync`, `sauvegarde`, `cadrage`, `rpo`

---

## Problème précis à résoudre

Définir le périmètre et les limites de la copie avant toute synchronisation afin de ne pas confondre miroir et sauvegarde historisée.

## 1. Hors-Production (Lab / Test / POC)

1. Mesurer la source et l'espace de destination :
   ```bash
   du -sh /srv/data
   df -h /srv/backup
   ```
   👉 Explication : la destination doit pouvoir contenir la source et sa croissance.

2. Relever propriétaires, ACL et attributs à préserver :
   ```bash
   getfacl -R /srv/data | head
   lsattr -R /srv/data 2>/dev/null | head
   ```
   👉 Explication : détermine l'usage de `-A` (ACL) et `-X` (attributs étendus) à l'étape de copie.

3. Consigner : source, destination, fréquence, RPO/RTO, besoin d'historique.
   👉 Explication : `rsync` produit une copie miroir et non une sauvegarde historisée; une suppression ou un chiffrement par ransomware se propage au passage suivant. Pour des versions, déduplication et chiffrement, utiliser BorgBackup.

## 2. Production — Contrôles

Faire approuver source/destination, chemins, capacité, exclusions, fréquence, fenêtre, propriétaire et procédure de restauration.

## 3. Production — Sécurité

- Une synchronisation miroir peut propager suppression ou chiffrement malveillant.
- Ne jamais traiter une copie unique rsync comme une sauvegarde historisée.
- Ne pas copier une base active sans dump ou méthode cohérente approuvée.
- N'autoriser que les hôtes et destinations appartenant au périmètre.

## Validation et retour arrière

- **Validation** : périmètre, rétention, cible, accès SSH et test de restauration approuvés.
- **Arrêt** : ne pas lancer de copie destructive si source, destination ou méthode de reprise est ambiguë.

## Si le problème n'est pas résolu

- [rsync — page de manuel officielle](https://download.samba.org/pub/rsync/rsync.1.html)
- [Guide complet rsync Debian 13](/02-fiches-completes/debian/13/autres/92-sauvegarde-fichiers-rsync-debian-13#1-perimetre-et-limites)