# Fiche_Simple_-_Cloud_Datadog_Deployer_Hote_Pilote.md

- **Environnement** : Datadog SaaS et hôte Linux administré
- **OS / Version** : Linux 64 bits supporté par l'Agent Datadog courant
- **Catégorie** : observabilité / métriques et journaux
- **Tags** : `datadog`, `agent`, `linux`, `saas`, `fleet-automation`, `observabilite`

---

## Problème précis à résoudre

Installer l'Agent sur un seul hôte pilote avec la commande générée par Datadog.

## 1. Hors-Production (Lab / Test / POC)

1. Dans Datadog, ouvrir **Fleet Automation > Install Agents** (instructions Linux), choisir la région et les options organisationnelles.
   👉 Explication : la commande générée contient le site correct.

2. Examiner la commande/script généré avant exécution : contenu, URL de téléchargement, certificat TLS et prérequis.
   👉 Explication : le script peut modifier le système avec des privilèges élevés.

3. Sur l'hôte pilote approuvé, exécuter la commande fournie par Fleet Automation en transmettant la clé API depuis le gestionnaire de secrets (variable d'environnement non journalisée).
   👉 Explication : la clé ne doit pas rester dans l'historique shell ni dans la fiche.

4. Contrôler que le service est installé et démarré :
   ```bash
   sudo systemctl --no-pager status datadog-agent
   ```
   👉 Explication : l'état doit être `active (running)`.

## 2. Production — Contrôles

Si une automatisation centrale est utilisée, injecter le secret au runtime et empêcher sa journalisation.

## 3. Production — Sécurité

- Ne pas recopier la clé API dans l'historique ou dans un script versionné.
- Commencer par un seul hôte de laboratoire ou pilote.

## Validation et retour arrière

- **Validation** : Le service `datadog-agent` est actif et l'hôte apparaît dans Fleet Automation.
- **Retour arrière** : Arrêter l'Agent (`sudo systemctl stop datadog-agent`), puis le désinstaller via le gestionnaire de paquets de la distribution.

## Si le problème n'est pas résolu

- [Datadog — Agent Linux](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/)
- [Datadog — Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation/)
- [Guide complet Datadog Agent Linux SaaS](../../../../02-Fiches-Completes/Transverses/Cloud-SaaS/Installation-Deploiement/52_Deploiement_Datadog_Agent_Linux_SaaS.md#2-deploiement-dun-hote-pilote)
