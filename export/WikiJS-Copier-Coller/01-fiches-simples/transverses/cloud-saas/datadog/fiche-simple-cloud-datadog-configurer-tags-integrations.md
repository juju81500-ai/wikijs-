# Fiche_Simple_-_Cloud_Datadog_Configurer_Tags_Integrations.md

- **Environnement** : Datadog SaaS et hôte Linux administré
- **OS / Version** : Linux 64 bits supporté par l'Agent Datadog courant
- **Catégorie** : observabilité / métriques et journaux

---

## Problème précis à résoudre

Définir les tags et n'activer que les intégrations nécessaires.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder puis ouvrir le fichier principal :
   ```bash
   sudo cp -a /etc/datadog-agent/datadog.yaml /etc/datadog-agent/datadog.yaml.bak
   sudo nano /etc/datadog-agent/datadog.yaml
   ```
   👉 Explication : la copie permet un retour arrière; modifier `site:` (correspondant au tenant) et la section `tags:` (`env`, `service`, `team`, `role`).

2. Lister les exemples d'intégrations fournis par le paquet :
   ```bash
   ls /etc/datadog-agent/conf.d/
   ```
   👉 Explication : chaque intégration est dans `conf.d/NOM.d/` (fichier `conf.yaml`, copié depuis `conf.yaml.example`).

3. Pour les logs, activer explicitement la collecte (`logs_enabled: true` dans `datadog.yaml`) seulement après validation des sources; exclure secrets, données personnelles et fichiers sensibles.
   👉 Explication : la collecte de logs est désactivée par défaut.

4. Pour APM, coordonner l'instrumentation et le redémarrage avec les propriétaires applicatifs.
   👉 Explication : un redémarrage applicatif peut être nécessaire.

5. Redémarrer l'Agent pour appliquer :
   ```bash
   sudo systemctl restart datadog-agent
   sudo systemctl --no-pager status datadog-agent
   ```
   👉 Explication : le redémarrage charge la nouvelle configuration.

## 2. Production — Contrôles

Conserver uniquement les intégrations nécessaires et documenter les tags.

## 3. Production — Sécurité

- Restreindre la lecture de `datadog.yaml`, qui peut contenir des identifiants.
- Exclure secrets et données personnelles de la collecte de logs.

## Validation et retour arrière

- **Validation** : Tags et site visibles dans la console, intégrations attendues actives.
- **Retour arrière** : Restaurer `/etc/datadog-agent/datadog.yaml.bak` et redémarrer l'Agent.

## Si le problème n'est pas résolu

- [Datadog — Agent Linux](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/)
- [Datadog — Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation/)
- [Datadog — Configuration de l'Agent](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/)
- [Guide complet Datadog Agent Linux SaaS](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/52-deploiement-datadog-agent-linux-saas#3-configurer-les-tags-et-les-integrations)