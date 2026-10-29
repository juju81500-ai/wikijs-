# 📄 Fiche_Simple_-_Cloud_Datadog_Installer_Agent_Linux_Pilote.md

- **Environnement** : Datadog SaaS et hôte Linux administré
- **OS / Version** : Distribution Linux supportée par la version actuelle de l'Agent
- **Catégorie** : Observabilité / métriques
- **Tags** : `datadog`, `saas`, `agent`, `linux`, `observabilite`, `api-key`

---

## 🎯 Problème précis à résoudre

Enrôler un seul hôte pilote dans Datadog et confirmer la remontée des métriques sans exposer de clé API.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Vérifier la plateforme :
   ```bash
   cat /etc/os-release | head -3
   uname -m
   ```
   👉 Explication : comparer à la liste des plateformes supportées par Datadog.

2. Dans Datadog : **Integrations > Fleet Automation > Install Agents** (ou **Integrations > Agent**), choisir **Linux** et le **site Datadog** exact.
   👉 Explication : la commande générée contient la clé API du tenant; ne pas la partager.

3. Examiner le script avant exécution :
   ```bash
   curl -fsSL https://install.datadoghq.com/scripts/install_script_agent7.sh -o /tmp/install_datadog.sh
   less /tmp/install_datadog.sh
   ```
   👉 Explication : relire privilèges et actions; ne jamais `curl | sh` sans lecture.

4. Exécuter sur l'hôte de test avec la clé saisie sans l'écrire dans l'historique :
   ```bash
   read -rsp "Clé API Datadog : " DD_API_KEY; echo
   DD_API_KEY="$DD_API_KEY" DD_SITE="datadoghq.eu" sudo -E bash /tmp/install_datadog.sh
   unset DD_API_KEY
   ```
   👉 Explication : remplacer `datadoghq.eu` par le site exact du tenant.

5. Vérifier :
   ```bash
   systemctl status datadog-agent --no-pager
   sudo datadog-agent status | head -30
   ```
   👉 Explication : dans la console **Infrastructure > Infrastructure List**, confirmer l'hôte et ses métriques; désactiver les intégrations inutiles (`/etc/datadog-agent/conf.d`).


## ⚡ 2. Production — Façon Simplifiée

1. Définir tags, proxy et site dans `/etc/datadog-agent/datadog.yaml` :
   ```yaml
   site: datadoghq.eu
   tags:
     - service:NOM
     - env:production
     - owner:EQUIPE
   proxy:
     https: http://proxy.example.net:3128
   ```
   👉 Explication : remplacer les valeurs; déployer par groupe via l'outil de configuration approuvé, puis `sudo systemctl restart datadog-agent`.


## 🔒 3. Production — Façon Sécurisée

- Ne jamais écrire la clé API dans une commande, un fichier partagé, une capture ou un dépôt; la stocker dans le coffre et utiliser uniquement le canal d'installation généré pour l'organisation.
- Limiter l'egress aux domaines et ports documentés par Datadog; l'Agent initie les connexions vers le SaaS.
- Collecter uniquement les logs et métriques autorisés, masquer les données personnelles/secrets et éviter les logs sensibles.
- Conserver les permissions par défaut de l'Agent, restreindre l'accès à `/etc/datadog-agent/` et planifier rotation des clés.

## ✅ Validation et retour arrière

- **Validation** : service actif, statut sans erreur, host visible dans le bon site, tags et métriques attendus reçus.
- **Retour arrière** : arrêter le service puis désinstaller le paquet selon la procédure Linux Datadog; garder la configuration jusqu'à décision explicite de purge.

## 🔗 Si le problème n'est pas résolu

- **Fiche de résolution complémentaire** : consulter la documentation officielle Datadog ci-dessous.
- [Datadog — Agent Linux](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/)
- [Datadog — Documentation Agent](https://docs.datadoghq.com/agent/)