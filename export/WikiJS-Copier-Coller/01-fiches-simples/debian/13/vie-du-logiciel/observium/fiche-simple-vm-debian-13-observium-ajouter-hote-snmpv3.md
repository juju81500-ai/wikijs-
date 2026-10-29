# Fiche_Simple_-_VM_Debian_13_Observium_Ajouter_Hote_SNMPv3.md

- **Environnement** : Observium Community sur Debian 13, un équipement autorisé, SNMPv3
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Supervision / SNMP

---

## Problème précis à résoudre

Ajouter un équipement pilote au périmètre Observium et confirmer que la découverte et l'interrogation SNMP fonctionnent sans exposer de secrets.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer autorisation, DNS et IP :
   ```bash
   getent hosts equipement.example.net
   ping -c 2 equipement.example.net
   ```
   👉 Explication : remplacer le nom; noter aussi le modèle de l'équipement.

2. Sur l'équipement (ou l'agent Linux net-snmp), créer un utilisateur SNMPv3 `authPriv` en lecture seule :
   ```bash
   sudo systemctl stop snmpd
   read -rsp "Phrase SNMPv3 (>= 8 car.) : " SPW; echo
   sudo net-snmp-create-v3-user -ro -A "$SPW" -a SHA -X "$SPW" -x AES observium
   unset SPW
   sudo systemctl start snmpd
   ```
   👉 Explication : sur un équipement réseau, utiliser sa CLI constructeur; restreindre la source à l'adresse du serveur Observium (`rouser observium priv` et ACL `agentaddress`/pare-feu). Utiliser deux phrases distinctes en production.

3. Filtrer le réseau :
   ```bash
   sudo nft add rule inet filter input ip saddr IP_OBSERVIUM udp dport 161 accept
   ```
   👉 Explication : remplacer l'IP; UDP 161 seulement entre poller et appareil; HTTPS vers Observium seulement depuis le réseau d'administration. Table et chaîne supposées existantes.

4. Ajouter l'hôte : sur le serveur Observium (ligne de commande) :
   ```bash
   cd /opt/observium
   ./add_device.php equipement.example.net ANY v3 observium PHRASE_AUTH PHRASE_PRIV sha aes
   ```
   👉 Explication : alternative GUI : **Devices > Add Device** (version SNMP v3, niveau authPriv, identifiants). Saisir les phrases via l'interface plutôt qu'en argument pour éviter l'historique shell. Vérifier modèle, `sysObjectID`, interfaces et date de dernière interrogation.

5. Découverte et poll manuel :
   ```bash
   sudo -u www-data ./discovery.php -h equipement.example.net
   sudo -u www-data ./poller.php -h equipement.example.net
   ```
   👉 Explication : contrôler journaux et graphiques après un cycle de cinq minutes.

## 2. Production — Contrôles

Superviser uniquement les équipements approuvés. Vérifier régulièrement la fraîcheur du poller, les erreurs SNMP, la capacité RRD/MariaDB, les tâches cron et les sauvegardes restaurables. Respecter l'intervalle de poller Observium de cinq minutes.

## 3. Production — Sécurité

- Préférer SNMPv3 `authPriv` à SNMPv1/v2c; ne jamais réutiliser `public`.
- Limiter l'utilisateur SNMP à la lecture et à l'IP du poller.
- Ne pas placer les secrets dans l'historique shell, la ligne de commande ou les journaux.
- Utiliser HTTPS, limiter l'accès à l'interface au réseau de gestion et sauvegarder `config.php` de manière protégée.
- Vérifier l'édition : les alertes et autres fonctionnalités de Subscription ne sont pas présumées disponibles en Community.

## Validation et retour arrière

- **Validation** : appareil reconnu, poll/discovery sans erreur, données et graphes récents, secrets absents des journaux.
- **Retour arrière** : retirer le pilote d'Observium, révoquer son utilisateur SNMPv3 et fermer les règles réseau temporaires.

## Si le problème n'est pas résolu

- [Observium — ajout d'équipement](https://docs.observium.org/add_device/)
- [Observium — configuration SNMP](https://docs.observium.org/config_options/#snmp-settings)
- [Observium — documentation Debian/Ubuntu](https://docs.observium.org/install_debian/)
- [Guide complet Observium Community Debian 13](/02-fiches-completes/debian/13/installation-deploiement/69-deploiement-observium-community-debian-13)