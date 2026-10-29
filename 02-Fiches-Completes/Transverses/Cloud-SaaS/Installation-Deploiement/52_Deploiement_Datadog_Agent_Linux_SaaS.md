# Déployer Datadog Agent sur Linux avec Fleet Automation

- **OS / Version** : Linux 64 bits supporté par l'Agent Datadog courant
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Enrôlement d'un agent hôte dans un tenant Datadog SaaS
- **Catégorie** : Observabilité / métriques et journaux
- **Tags** : `datadog`, `agent`, `linux`, `saas`, `fleet-automation`, `observabilite`

## 1. Préparer l'enrôlement

Fiche simple : [préparer l'enrôlement](../../../../01-Fiches-Simples/Transverses/Cloud-SaaS/Datadog/Fiche_Simple_-_Cloud_Datadog_Preparer_Enrolement.md).

Vérifier la plateforme Linux, l'architecture et la version de l'Agent prises en charge. Définir tenant/site (US, EU ou autre), proxy éventuel, tags obligatoires, produits autorisés (infrastructure, logs, APM) et responsable de l'hôte. Confirmer le budget/quotas d'ingestion et la politique de rétention avant d'activer des collecteurs à fort volume.

Créer ou utiliser une clé API gérée par l'organisation. Ne pas utiliser une clé d'application dans la configuration Agent. Stocker les secrets dans le coffre et limiter les personnes autorisées à les administrer.

## 2. Déploiement d'un hôte pilote

Fiche simple : [déployer l'Agent sur un hôte pilote](../../../../01-Fiches-Simples/Transverses/Cloud-SaaS/Datadog/Fiche_Simple_-_Cloud_Datadog_Deployer_Hote_Pilote.md).

Dans Datadog **Fleet Automation**, ouvrir les instructions d'installation Agent pour Linux. Sélectionner la région correcte et les options organisationnelles, puis examiner la commande/script généré avant exécution. Le script peut modifier le système et s'exécuter avec des privilèges élevés : valider son contenu, les URL de téléchargement, le certificat TLS et les prérequis locaux.

Sur un hôte de laboratoire ou un pilote approuvé, exécuter la commande fournie par Fleet Automation. Ne pas recopier une API key dans l'historique shell ni dans la fiche. Si une automatisation centrale est utilisée, transmettre le secret depuis le gestionnaire de secrets au runtime et empêcher sa journalisation.

## 3. Configurer les tags et les intégrations

Fiche simple : [configurer les tags et les intégrations](../../../../01-Fiches-Simples/Transverses/Cloud-SaaS/Datadog/Fiche_Simple_-_Cloud_Datadog_Configurer_Tags_Integrations.md).

Le fichier principal Linux est `/etc/datadog-agent/datadog.yaml`; les checks d'intégration résident dans `/etc/datadog-agent/conf.d/<integration>.d/conf.yaml`. Utiliser les exemples fournis par le paquet et ne conserver que les intégrations nécessaires.

Définir des tags cohérents (`env`, `service`, `team`, `role`) et le champ `site` correspondant au tenant. Pour les logs, activer explicitement la collecte seulement après validation des sources; exclure secrets, données personnelles et fichiers sensibles. Pour APM, coordonner l'instrumentation et le redémarrage avec les propriétaires applicatifs.

## 4. Contrôler et généraliser

Fiche simple : [contrôler et généraliser](../../../../01-Fiches-Simples/Transverses/Cloud-SaaS/Datadog/Fiche_Simple_-_Cloud_Datadog_Controler_Generaliser.md).

```bash
sudo systemctl --no-pager status datadog-agent
sudo datadog-agent status
```

Vérifier dans la console le host, site, version Agent, tags, checks, métriques et logs attendus. Contrôler que les connexions sortantes respectent les destinations autorisées et qu'aucune donnée non prévue n'est remontée. Étendre par groupes de changements, surveiller erreurs et consommation, et utiliser Fleet Automation pour connaître l'historique et l'état des Agents.

## 5. Sécurité et maintenance

Fiche simple : [sécuriser et maintenir l'Agent](../../../../01-Fiches-Simples/Transverses/Cloud-SaaS/Datadog/Fiche_Simple_-_Cloud_Datadog_Securite_Maintenance.md).

- Restreindre les droits en lecture sur `datadog.yaml`, qui peut contenir des identifiants.
- Gérer les clés API depuis le tenant, suivre leur usage et les faire tourner selon la politique interne; mettre à jour les agents concernés sans interrompre toute la flotte.
- Utiliser un proxy sortant si requis et n'autoriser que les FQDN/ports publiés pour le site Datadog concerné.
- Garder Agent et intégrations à jour; tester les versions et changements de configuration sur un groupe pilote.
- Protéger les logs locaux et flares de support; inspecter le contenu avant partage.

## 6. Retour arrière

Fiche simple : [revenir en arrière et retirer l'Agent](../../../../01-Fiches-Simples/Transverses/Cloud-SaaS/Datadog/Fiche_Simple_-_Cloud_Datadog_Retour_Arriere.md).

Désactiver l'intégration/collecte ou arrêter l'Agent en premier pour réduire l'ingestion. Désinstaller via le gestionnaire de paquets de la distribution si le pilote doit être retiré. La suppression du paquet ne retire pas forcément les fichiers de configuration et journaux : les conserver pour enquête ou les purger selon une décision de changement explicite. Vérifier la disparition de l'hôte dans Fleet Automation et l'arrêt des données.

## Sources

- [Datadog — Agent Linux](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/)
- [Datadog — Gestion des Agents avec Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation/)
- [Datadog — Configuration de l'Agent](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/)
- [Datadog — Collecter les logs](https://docs.datadoghq.com/agent/logs/)
- [Datadog — Sécurité de l'Agent](https://docs.datadoghq.com/agent/security/)