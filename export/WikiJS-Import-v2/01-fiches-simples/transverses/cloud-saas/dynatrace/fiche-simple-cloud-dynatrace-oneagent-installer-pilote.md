---
title: "Fiche Simple - Cloud Dynatrace OneAgent Installer Pilote"
description: "Installer OneAgent sur un seul hôte de test et vérifier son arrivée dans le tenant."
published: true
date: 2026-10-29T19:43:25Z
tags: ["dynatrace", "saas", "oneagent", "linux", "observabilite"]
editor: markdown
dateCreated: 2026-10-29T19:43:25Z
dateModified: 2026-10-29T19:43:25Z
---

# Fiche_Simple_-_Cloud_Dynatrace_OneAgent_Installer_Pilote.md

- **Environnement** : Dynatrace SaaS et hôte Linux administré
- **OS / Version** : Distribution et architecture Linux prises en charge par la version OneAgent du tenant
- **Catégorie** : observabilité / installation
- **Tags** : `dynatrace`, `saas`, `oneagent`, `linux`, `observabilite`

---

## Problème précis à résoudre

Installer OneAgent sur un seul hôte de test et vérifier son arrivée dans le tenant.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter sur l'hôte de test la commande fournie par l'interface de déploiement (jamais celle ou le token d'un autre environnement).
   👉 Explication : la commande est spécifique au tenant et à la version.

2. Contrôler le service :
   ```bash
   sudo systemctl --no-pager status oneagent
   ```
   👉 Explication : Vérifie que le service OneAgent est actif.

3. Dans Dynatrace, ouvrir **Infrastructure > Hosts** (nom du menu variable selon la version) et vérifier l'hôte, ses métadonnées et le mode choisi.
   👉 Explication : confirme l'arrivée de l'hôte dans le bon tenant.

4. Redémarrer les processus applicatifs seulement si nécessaire pour le monitoring profond, dans une fenêtre approuvée, puis contrôler CPU, mémoire et disponibilité.
   👉 Explication : mesure l'impact avant le déploiement à l'échelle.

## 2. Production — Contrôles

Utiliser d'abord un hôte de test.

## 3. Production — Sécurité

- Ne pas réutiliser un token d'un autre environnement.

## Validation et retour arrière

- **Validation** : service actif et hôte visible avec le bon mode.
- **Retour arrière** : suivre la désinstallation officielle de la version et confirmer que l'ingestion cesse.

## Si le problème n'est pas résolu

- [Dynatrace — Désinstaller OneAgent Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux)
- [Dynatrace — Installer OneAgent sur Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux)
- [Guide complet — étape 3](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/53-deploiement-dynatrace-oneagent-linux-saas#3-installer-un-pilote)