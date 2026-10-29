---
title: "Fiche Simple - Cloud Datadog Controler Generaliser"
description: "Vérifier la remontée des données du pilote puis étendre par groupes."
published: true
date: 2026-10-29T19:42:44Z
tags: ["datadog", "agent", "linux", "saas", "fleet-automation", "observabilite"]
editor: markdown
dateCreated: 2026-10-29T19:42:44Z
dateModified: 2026-10-29T19:42:44Z
---

# Fiche_Simple_-_Cloud_Datadog_Controler_Generaliser.md

- **Environnement** : Datadog SaaS et hôte Linux administré
- **OS / Version** : Linux 64 bits supporté par l'Agent Datadog courant
- **Catégorie** : observabilité / métriques et journaux
- **Tags** : `datadog`, `agent`, `linux`, `saas`, `fleet-automation`, `observabilite`

---

## Problème précis à résoudre

Vérifier la remontée des données du pilote puis étendre par groupes.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le service et l'état de l'Agent :
   ```bash
   sudo systemctl --no-pager status datadog-agent
   sudo datadog-agent status
   ```
   👉 Explication : la sortie indique la connectivité, les checks et les erreurs éventuelles.

2. Dans la console, vérifier le host, le site, la version de l'Agent, les tags, les checks, les métriques et les logs attendus (**Infrastructure > Infrastructure List** et **Fleet Automation**).
   👉 Explication : la donnée doit arriver côté SaaS.

3. Contrôler que les connexions sortantes respectent les destinations autorisées et qu'aucune donnée non prévue n'est remontée.
   👉 Explication : on évite toute fuite de données.

4. Étendre par groupes de changements, surveiller erreurs et consommation, et suivre l'historique dans Fleet Automation.
   👉 Explication : un déploiement progressif limite l'impact.

## 2. Production — Contrôles

Définir des critères de passage (aucune erreur, consommation conforme) avant chaque nouveau groupe.

## 3. Production — Sécurité

- Autoriser seulement les FQDN/ports publiés pour le site Datadog concerné.
- Examiner le contenu des flares avant partage.

## Validation et retour arrière

- **Validation** : Le pilote remonte les données attendues sans erreur ni donnée non prévue.
- **Retour arrière** : Revenir à l'étape de retour arrière : arrêter l'Agent sur les hôtes concernés.

## Si le problème n'est pas résolu

- [Datadog — Agent Linux](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/)
- [Datadog — Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation/)
- [Guide complet Datadog Agent Linux SaaS](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/52-deploiement-datadog-agent-linux-saas#4-controler-et-generaliser)