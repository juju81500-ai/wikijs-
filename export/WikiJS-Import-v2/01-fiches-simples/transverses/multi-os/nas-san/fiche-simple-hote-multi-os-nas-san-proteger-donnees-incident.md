---
title: "Fiche Simple - Hote Multi-OS NAS SAN Proteger Donnees Incident"
description: "Limiter le risque de corruption et cadrer l'incident avant tout diagnostic."
published: true
date: 2026-10-29T19:42:44Z
tags: ["nas", "san", "samba", "nfs", "iscsi", "multipath", "diagnostic"]
editor: markdown
dateCreated: 2026-10-29T19:42:44Z
dateModified: 2026-10-29T19:42:44Z
---

# Fiche_Simple_-_Hote_Multi-OS_NAS_SAN_Proteger_Donnees_Incident.md

- **Environnement** : Hôte Linux client ou serveur de stockage (Samba, NFSv4, iSCSI) et baie/NAS
- **OS / Version** : Multi-OS; clients et serveurs Linux, appliance de stockage
- **Catégorie** : diagnostic / stockage
- **Tags** : `nas`, `san`, `samba`, `nfs`, `iscsi`, `multipath`, `diagnostic`

---

## Problème précis à résoudre

Limiter le risque de corruption et cadrer l'incident avant tout diagnostic.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier le service, le partage ou la LUN, les hôtes touchés, l'heure de début, les erreurs, les changements récents et l'état des sauvegardes.
   👉 Explication : un incident bien cadré évite des actions hasardeuses.

2. Suspendre les migrations et écritures non nécessaires si des erreurs I/O ou un risque de corruption sont observés.
   👉 Explication : on protège les données avant d'investiguer.

3. En cluster, vérifier le propriétaire actif et le mécanisme de réservation avant toute action.
   👉 Explication : un second hôte en écriture sur une LUN la corrompt.

## 2. Production — Contrôles

Noter la dernière sauvegarde vérifiée et le contact de l'équipe stockage.

## 3. Production — Sécurité

- Ne pas formater, forcer un démontage, réinitialiser une baie, supprimer une session iSCSI ni remonter une LUN en écriture depuis plusieurs hôtes.

## Validation et retour arrière

- **Validation** : L'incident est décrit et les écritures à risque sont suspendues.
- **Retour arrière** : Aucune modification technique; reprendre les écritures suspendues après validation.

## Si le problème n'est pas résolu

- [Samba — Documentation officielle](https://www.samba.org/samba/docs/)
- [Linux man-pages — exports(5)](https://man7.org/linux/man-pages/man5/exports.5.html)
- [open-iscsi — Documentation du projet](https://github.com/open-iscsi/open-iscsi)
- [Guide complet diagnostic NAS/SAN Samba NFS iSCSI](/02-fiches-completes/transverses/multi-os/diagnostic/38-diagnostic-nas-san-samba-nfs-iscsi#1-proteger-les-donnees-et-definir-lincident)