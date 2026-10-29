# Fiche_Simple_-_Cloud_Datadog_Retour_Arriere.md

- **Environnement** : Datadog SaaS et hôte Linux administré
- **OS / Version** : Linux 64 bits supporté par l'Agent Datadog courant
- **Catégorie** : observabilité / métriques et journaux

---

## Problème précis à résoudre

Arrêter la collecte puis retirer l'Agent d'un hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Désactiver d'abord l'intégration/collecte concernée dans `/etc/datadog-agent/conf.d/` ou `logs_enabled: false`.
   👉 Explication : on réduit l'ingestion avant de retirer l'Agent.

2. Arrêter l'Agent :
   ```bash
   sudo systemctl stop datadog-agent
   sudo systemctl --no-pager status datadog-agent
   ```
   👉 Explication : la collecte cesse; l'état doit être `inactive`.

3. Désinstaller si le pilote doit être retiré (Debian/Ubuntu ; adapter à la distribution) :
   ```bash
   sudo apt remove datadog-agent
   ```
   👉 Explication : la configuration et les journaux peuvent rester : les conserver pour enquête ou les purger selon une décision de changement explicite.

4. Vérifier dans **Fleet Automation** que l'hôte disparaît et que les données ne remontent plus.
   👉 Explication : on confirme l'arrêt côté SaaS.

## 2. Production — Contrôles

Conserver les fichiers de configuration jusqu'à décision de changement explicite.

## 3. Production — Sécurité

- Révoquer la clé API si l'hôte est définitivement retiré.
- Ne pas purger journaux et configuration pendant une enquête.

## Validation et retour arrière

- **Validation** : L'Agent est arrêté/retiré et l'hôte n'envoie plus de données.
- **Retour arrière** : Réinstaller l'Agent via Fleet Automation et restaurer la configuration conservée.

## Si le problème n'est pas résolu

- [Datadog — Agent Linux](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/)
- [Datadog — Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation/)
- [Guide complet Datadog Agent Linux SaaS](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/52-deploiement-datadog-agent-linux-saas#6-retour-arriere)