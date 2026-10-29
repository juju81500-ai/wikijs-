---
title: "Fiche Simple - Cloud Datadog Securite Maintenance"
description: "Appliquer les contrôles de sécurité et de maintenance de l'Agent."
published: true
date: 2026-10-29T19:42:44Z
tags: ["datadog", "agent", "linux", "saas", "fleet-automation", "observabilite"]
editor: markdown
dateCreated: 2026-10-29T19:42:44Z
dateModified: 2026-10-29T19:42:44Z
---

# Fiche_Simple_-_Cloud_Datadog_Securite_Maintenance.md

- **Environnement** : Datadog SaaS et hôte Linux administré
- **OS / Version** : Linux 64 bits supporté par l'Agent Datadog courant
- **Catégorie** : observabilité / métriques et journaux
- **Tags** : `datadog`, `agent`, `linux`, `saas`, `fleet-automation`, `observabilite`

---

## Problème précis à résoudre

Appliquer les contrôles de sécurité et de maintenance de l'Agent.

## 1. Hors-Production (Lab / Test / POC)

1. Restreindre et contrôler les droits du fichier de configuration :
   ```bash
   ls -l /etc/datadog-agent/datadog.yaml
   sudo chmod 0640 /etc/datadog-agent/datadog.yaml
   ```
   👉 Explication : le fichier peut contenir des identifiants; vérifier d'abord propriétaire et groupe (`dd-agent`) pour ne pas bloquer l'Agent.

2. Dans Datadog, suivre l'usage des clés API et les faire tourner selon la politique interne : **Organization Settings > API Keys**.
   👉 Explication : une clé ancienne ou inutilisée est un risque.

3. Si un proxy sortant est requis, renseigner la section `proxy:` de `datadog.yaml` et n'autoriser que les FQDN/ports du site Datadog.
   👉 Explication : on limite les destinations.

4. Mettre à jour l'Agent avec le gestionnaire de paquets (Debian/Ubuntu ; adapter à la distribution), d'abord sur un groupe pilote :
   ```bash
   sudo apt update
   sudo apt install --only-upgrade datadog-agent
   ```
   👉 Explication : les mises à jour sont testées sur le pilote avant la flotte.

## 2. Production — Contrôles

Garder Agent et intégrations à jour; protéger les logs locaux et flares.

## 3. Production — Sécurité

- Ne pas partager un flare non inspecté.
- Mettre à jour sans interrompre toute la flotte.

## Validation et retour arrière

- **Validation** : Droits restreints, clés suivies, Agent à jour sur le pilote.
- **Retour arrière** : Réinstaller la version précédente du paquet si une mise à jour pose problème et restaurer la sauvegarde de configuration.

## Si le problème n'est pas résolu

- [Datadog — Agent Linux](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/)
- [Datadog — Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation/)
- [Guide complet Datadog Agent Linux SaaS](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/52-deploiement-datadog-agent-linux-saas#5-securite-et-maintenance)