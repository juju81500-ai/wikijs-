# Fiche_Simple_-_VM_Debian_12_Wazuh_Controles_Operationnels.md

- **Environnement** : plateforme Wazuh déployée; accès administrateur limité
- **OS / Version** : version Wazuh 4.x maintenue
- **Catégorie** : SIEM/XDR / exploitation

---

## Problème précis à résoudre

Vérifier la santé de la plateforme Wazuh, protéger les communications et maintenir l'observabilité des files et index.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l'état des composants :
   ```bash
   systemctl --no-pager status wazuh-manager wazuh-indexer wazuh-dashboard
   sudo /var/ossec/bin/wazuh-control status
   ```
   👉 Explication : aucun démon arrêté.

2. Vérifier la santé de l'indexeur et l'espace :
   ```bash
   curl -sk -u admin https://127.0.0.1:9200/_cluster/health?pretty
   df -h /var/lib/wazuh-indexer
   ```
   👉 Explication : saisir le mot de passe `admin` à l'invite; statut `green` (ou `yellow` en lab mono-nœud).

3. Contrôler les comptes du tableau de bord : **Dashboard management > Security > Internal users** et **Roles mapping**.
   👉 Explication : moindre privilège; supprimer les comptes inutiles.

4. Superviser file d'ingestion, certificats et horloge :
   ```bash
   sudo tail -20 /var/ossec/logs/ossec.log
   sudo openssl x509 -in /etc/wazuh-dashboard/certs/dashboard.pem -noout -enddate
   timedatectl | grep synchronized
   ```
   👉 Explication : anticiper l'expiration des certificats.

## 2. Production — Contrôles

Définir responsables, alertes, seuils, procédure de certificats, comptes, rétention et escalade en cas de perte d'ingestion.

## 3. Production — Sécurité

- Ne pas exposer le dashboard sans TLS et contrôle d'accès.
- Ne pas donner des droits d'administration globaux aux utilisateurs de consultation.
- Ne pas collecter davantage que les journaux autorisés.
- Protéger la configuration et les certificats contre les modifications non autorisées.

## Validation et retour arrière

- **Validation** : composants sains, communications chiffrées, comptes minimaux et alertes de capacité testées.
- **Retour arrière** : restaurer la configuration précédente validée sans désactiver les contrôles d'accès.

## Si le problème n'est pas résolu

- [Wazuh — documentation](https://documentation.wazuh.com/current/)
- [Wazuh — gestion du cluster](https://documentation.wazuh.com/current/user-manual/wazuh-server-cluster/index.html)
- [Guide complet Wazuh Debian 12](/02-fiches-completes/debian/12/installation-deploiement/11-siem-xdr-centralise-wazuh-4x-debian-12)