---
title: "Fiche Simple - Cloud Dynatrace OneAgent Preparer Hote Tenant"
description: "Valider hôte, flux réseau et choix de supervision avant d'installer OneAgent."
published: true
date: 2026-10-29T19:43:25Z
tags: ["dynatrace", "saas", "oneagent", "linux", "observabilite"]
editor: markdown
dateCreated: 2026-10-29T19:43:25Z
dateModified: 2026-10-29T19:43:25Z
---

# Fiche_Simple_-_Cloud_Dynatrace_OneAgent_Preparer_Hote_Tenant.md

- **Environnement** : Dynatrace SaaS et hôte Linux administré
- **OS / Version** : Distribution et architecture Linux prises en charge par la version OneAgent du tenant
- **Catégorie** : observabilité / préparation
- **Tags** : `dynatrace`, `saas`, `oneagent`, `linux`, `observabilite`

---

## Problème précis à résoudre

Valider hôte, flux réseau et choix de supervision avant d'installer OneAgent.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les caractéristiques de l'hôte :
   ```bash
   cat /etc/os-release
   uname -m
   df -h /opt
   free -h
   ```
   👉 Explication : Relève distribution, architecture, disque et mémoire à comparer au support OneAgent.

2. Confirmer si l'hôte joint Dynatrace SaaS directement ou via ActiveGate et n'ouvrir que les flux sortants indiqués par le tenant.
   👉 Explication : évite d'ouvrir des flux inutiles.

3. Choisir groupe d'hôtes, tags, zone réseau et mode (Full-Stack, Infrastructure ou Discovery).
   👉 Explication : prépare l'extension par lots.

4. Identifier l'impact de l'injection automatique sur les processus et prévoir une fenêtre de redémarrage si nécessaire.
   👉 Explication : évite une coupure applicative surprise.

## 2. Production — Contrôles

Vérifier la prise en charge OS/architecture dans la documentation de support des technologies.

## 3. Production — Sécurité

- Flux sortants limités à ceux du tenant.

## Validation et retour arrière

- **Validation** : plateforme supportée, flux et mode décidés.
- **Retour arrière** : aucun changement n'a été fait.

## Si le problème n'est pas résolu

- [Dynatrace — Support des technologies](https://docs.dynatrace.com/docs/ingest-from/technology-support)
- [Dynatrace — Installer OneAgent sur Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux)
- [Guide complet — étape 1](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/53-deploiement-dynatrace-oneagent-linux-saas#1-preparer-lhote-et-le-tenant)