# Fiche_Simple_-_VM_Debian_12_Wazuh_Enroler_Agents.md

- **Environnement** : Wazuh manager et hôtes pilotes autorisés; enrôlement suivant la version installée
- **OS / Version** : Wazuh 4.x maintenu; agents compatibles avec leurs systèmes
- **Catégorie** : SIEM/XDR / agents
- **Tags** : `debian12`, `wazuh`, `agent`, `enrollment`, `firewall`

---

## Problème précis à résoudre

Enrôler un agent pilote et confirmer la collecte avant de déployer l'agent à plus grande échelle.

## 1. Hors-Production (Lab / Test / POC)

1. Autoriser les flux entre agents et manager selon la version (généralement 1514/TCP événements et 1515/TCP enrôlement; 55000/TCP API) :
   ```bash
   sudo ss -ltnp | grep -E ':(1514|1515|55000)\b'
   ```
   👉 Explication : n'ouvrir ces ports qu'entre les réseaux et hôtes concernés.

2. Sur l'hôte à superviser, installer l'agent depuis le dépôt signé Wazuh (procédure officielle de la version) puis renseigner le manager :
   ```bash
   sudo WAZUH_MANAGER="wazuh.example.net" apt install wazuh-agent
   sudo systemctl enable --now wazuh-agent
   ```
   👉 Explication : la version de l'agent ne doit pas dépasser celle du manager.

3. Vérifier l'enrôlement côté manager :
   ```bash
   sudo /var/ossec/bin/agent_control -l
   ```
   👉 Explication : l'agent doit apparaître `Active`; sinon voir `/var/ossec/logs/ossec.log` sur l'agent.

4. Vérifier qu'une modification produit un événement : modifier un fichier surveillé (FIM) :
   ```bash
   echo test | sudo tee -a /etc/wazuh-test.txt
   ```
   👉 Explication : consulter ensuite le tableau de bord **Threat Hunting / Events**; arrêter l'agent et contrôler que l'alerte « agent déconnecté » est émise.

## 2. Production — Contrôles

Documenter propriétaires d'hôtes, méthode d'enrôlement, inventaire, ports, groupes, supervision, alertes et processus de retrait.

## 3. Production — Sécurité

- Ne pas enrôler d'hôte sans autorisation et propriétaire identifié.
- Ne pas ouvrir les ports d'enrôlement/événements à des réseaux non concernés.
- Ne pas déployer massivement avant validation du pilote.
- Ne pas utiliser de méthode d'enrôlement qui contourne l'authentification officielle.

## Validation et retour arrière

- **Validation** : agent visible, événement de test reçu et alerte hors ligne contrôlée.
- **Retour arrière** : retirer l'agent pilote selon la procédure de l'éditeur et fermer uniquement les règles temporaires ajoutées.

## Si le problème n'est pas résolu

- [Wazuh — déploiement des agents](https://documentation.wazuh.com/current/installation-guide/wazuh-agent/index.html)
- [Wazuh — référence ports réseau](https://documentation.wazuh.com/current/getting-started/architecture.html)
- [Guide complet Wazuh Debian 12](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/11_SIEM_XDR_Centralise_Wazuh_4x_Debian_12.md)
