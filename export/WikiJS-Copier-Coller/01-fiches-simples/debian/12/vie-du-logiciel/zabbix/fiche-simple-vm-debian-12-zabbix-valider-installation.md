# Fiche_Simple_-_VM_Debian_12_Zabbix_Valider_Installation.md

- **Environnement** : console Web Zabbix en HTTPS et hôte de test autorisé
- **OS / Version** : Debian 12; Zabbix 7.0 LTS
- **Catégorie** : supervision / validation

---

## Problème précis à résoudre

Valider la collecte et l'alerte de bout en bout sans laisser les comptes initiaux ni les ports exposés par défaut.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir l'assistant Web : **https://FQDN/zabbix** puis suivre les étapes (prérequis, base, serveur, résumé).
   👉 Explication : utiliser HTTPS; renseigner les paramètres de base saisis plus tôt.

2. Changer le compte par défaut : **Utilisateurs > Utilisateurs > Admin > Mot de passe**.
   👉 Explication : le mot de passe par défaut `zabbix` doit être remplacé immédiatement.

3. Vérifier les services :
   ```bash
   systemctl --no-pager status zabbix-server zabbix-agent
   sudo ss -ltnp | grep -E ':(10050|10051)\b'
   ```
   👉 Explication : serveur sur 10051, agent sur 10050; ne pas ouvrir 10051 à tout Internet.

4. Vérifier la réception des données et une alerte de test : **Surveillance > Hôtes** (l'hôte « Zabbix server » doit être disponible), puis **Surveillance > Problèmes**.
   👉 Explication : déclencher une alerte de test et vérifier sa réception.

5. Contrôler l'heure et la base :
   ```bash
   timedatectl | grep synchronized
   sudo mariadb -e "SELECT table_schema, ROUND(SUM(data_length+index_length)/1024/1024) AS Mo FROM information_schema.tables WHERE table_schema='zabbix' GROUP BY table_schema;"
   ```
   👉 Explication : surveiller la taille de la base et les alertes de capacité.

## 2. Production — Contrôles

Faire valider accès, comptes, données reçues, alertes, flux réseau, fuseau horaire, stockage et responsables d'astreinte.

## 3. Production — Sécurité

- Ne pas garder les identifiants initiaux ou comptes d'installation.
- N'autoriser que les flux nécessaires entre agents/proxies et serveur.
- Ne pas ouvrir le port 10051 à tout Internet.
- Protéger les vues et informations de supervision qui révèlent l'infrastructure.

## Validation et retour arrière

- **Validation** : données reçues, alerte de test vérifiée, identifiants changés et exposition réseau conforme.
- **Retour arrière** : restreindre l'accès Web ou arrêter la bascule tout en conservant la base et les journaux pour analyse.

## Si le problème n'est pas résolu

- [Zabbix — documentation 7.0](https://www.zabbix.com/documentation/7.0/en/manual)
- [Zabbix — chiffrement TLS](https://www.zabbix.com/documentation/7.0/en/manual/encryption)
- [Guide complet Zabbix Debian 12](/02-fiches-completes/debian/12/installation-deploiement/04-supervision-centralisee-zabbix-70-lts-debian-12)