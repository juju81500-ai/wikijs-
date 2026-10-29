---
title: "Fiche Simple - Cloud Datadog Preparer Enrolement"
description: "Préparer les prérequis et la clé API avant d'installer l'Agent."
published: true
date: 2026-10-29T19:42:44Z
tags: ["datadog", "agent", "linux", "saas", "fleet-automation", "observabilite"]
editor: markdown
dateCreated: 2026-10-29T19:42:44Z
dateModified: 2026-10-29T19:42:44Z
---

# Fiche_Simple_-_Cloud_Datadog_Preparer_Enrolement.md

- **Environnement** : Datadog SaaS et hôte Linux administré
- **OS / Version** : Linux 64 bits supporté par l'Agent Datadog courant
- **Catégorie** : observabilité / métriques et journaux
- **Tags** : `datadog`, `agent`, `linux`, `saas`, `fleet-automation`, `observabilite`

---

## Problème précis à résoudre

Préparer les prérequis et la clé API avant d'installer l'Agent.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier la plateforme et l'architecture de l'hôte :
   ```bash
   cat /etc/os-release
   uname -m
   ```
   👉 Explication : comparer à la liste des plateformes supportées par l'Agent courant.

2. Définir le site Datadog (US, EU ou autre), le proxy éventuel, les tags obligatoires (`env`, `service`, `team`, `role`), les produits autorisés (infrastructure, logs, APM) et le responsable de l'hôte.
   👉 Explication : ces choix sont à décider avant l'installation.

3. Dans Datadog, créer ou utiliser une **clé API** gérée par l'organisation : **Organization Settings > API Keys**. Stocker sa valeur dans le coffre de secrets.
   👉 Explication : on n'utilise pas de clé d'application dans la configuration de l'Agent.

4. Confirmer le budget/quotas d'ingestion et la politique de rétention avant d'activer des collecteurs à fort volume.
   👉 Explication : on évite une facturation imprévue.

## 2. Production — Contrôles

Limiter les personnes autorisées à administrer les clés et documenter site, tags et responsable.

## 3. Production — Sécurité

- Ne jamais coller une clé API dans un ticket, un historique shell ou une fiche.
- Utiliser une clé dédiée par usage pour pouvoir la révoquer.

## Validation et retour arrière

- **Validation** : Plateforme supportée, site et tags décidés, clé API disponible dans le coffre.
- **Retour arrière** : Aucune modification n'est faite sur l'hôte; au besoin révoquer la clé créée.

## Si le problème n'est pas résolu

- [Datadog — Agent Linux](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/)
- [Datadog — Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation/)
- [Guide complet Datadog Agent Linux SaaS](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/52-deploiement-datadog-agent-linux-saas#1-preparer-lenrolement)