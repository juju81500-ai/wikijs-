# Fiche_Simple_-_VM_Debian_12_Wazuh_Sauvegarder_Mettre_A_Jour.md

- **Environnement** : plateforme Wazuh en exploitation; environnement séparé disponible pour tests
- **OS / Version** : Wazuh 4.x maintenu
- **Catégorie** : SIEM/XDR / sauvegarde et mise à jour
- **Tags** : `debian12`, `wazuh`, `backup`, `upgrade`, `restore`, `rollback`

---

## Problème précis à résoudre

Sauvegarder et mettre à niveau Wazuh dans l'ordre supporté, avec une restauration vérifiée et sans perdre les journaux utiles.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder configuration et certificats :
   ```bash
   sudo tar czf /root/wazuh-conf-$(date +%F).tgz /var/ossec/etc /var/ossec/api/configuration /etc/wazuh-indexer /etc/wazuh-dashboard
   ```
   👉 Explication : contient des secrets; copier vers un stockage chiffré hors serveur.

2. Sauvegarder les index (instantané) selon la procédure de la version, ou la VM entière :
   ```bash
   curl -sk -u admin https://127.0.0.1:9200/_cat/indices?v | head
   ```
   👉 Explication : relever les index à protéger; configurer un dépôt de snapshots OpenSearch selon la documentation officielle.

3. Tester une restauration sur un environnement séparé.
   👉 Explication : une sauvegarde non restaurée n'est pas prouvée.

4. Mise à jour : respecter l'ordre officiel (indexeur, manager, dashboard), après sauvegarde :
   ```bash
   apt-cache policy wazuh-manager wazuh-indexer wazuh-dashboard
   ```
   👉 Explication : suivre le guide de mise à niveau de la version; arrêter `filebeat` et les agents selon la procédure, vérifier la compatibilité manager/agent.

## 2. Production — Contrôles

Faire approuver versions source/cible, ordre de mise à niveau, fenêtre, sauvegarde, restauration testée, capacité et critères de reprise.

## 3. Production — Sécurité

- Ne pas mettre à jour un seul nœud hors séquence.
- Ne pas utiliser une procédure de sauvegarde d'index incompatible avec la version déployée.
- Ne pas réinstaller ou supprimer les index avant préservation des éléments d'incident.
- Protéger certificats, configurations et données de sécurité selon leur classification.

## Validation et retour arrière

- **Validation** : composants à jour selon procédure supportée, index lisibles, agents connectés et collecte contrôlée.
- **Retour arrière** : restaurer les composants, index, configuration et certificats à un point cohérent selon les procédures officielles.

## Si le problème n'est pas résolu

- [Wazuh — mise à niveau](https://documentation.wazuh.com/current/upgrade-guide/index.html)
- [Wazuh — sauvegarde et restauration](https://documentation.wazuh.com/current/user-manual/backup/index.html)
- [Guide complet Wazuh Debian 12](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/11_SIEM_XDR_Centralise_Wazuh_4x_Debian_12.md)
