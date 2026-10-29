# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Graylog_Valider_Input_Syslog_Pilote.md

- **Environnement** : Graylog 7.2, Ubuntu Server 24.04, source de journaux administrée
- **OS / Version** : Ubuntu Server 24.04 LTS
- **Catégorie** : Journaux / ingestion
- **Tags** : `ubuntu2404`, `graylog`, `syslog`, `logs`, `tls`, `pilote`

---

## 🎯 Problème précis à résoudre

Valider la réception et la recherche d'un petit flux Syslog provenant d'une source autorisée.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Confirmer source, format, port et protocole avec le propriétaire du système.
   👉 Explication : exemple retenu : Syslog TCP/TLS 6514 depuis une seule IP.

2. Créer l'input : **System > Inputs > Select input : Syslog TCP > Launch new input** (titre « pilote-syslog », bind address de l'interface interne, port 6514, TLS activé).
   👉 Explication : seules les options nécessaires.

3. Restreindre le réseau :
   ```bash
   sudo ufw allow from IP_SOURCE to any port 6514 proto tcp
   sudo ufw status numbered
   ```
   👉 Explication : remplacer par l'IP du serveur pilote.

4. Envoyer un événement de test depuis la source :
   ```bash
   logger -n IP_GRAYLOG -P 6514 -T "Test pilote Graylog non sensible"
   ```
   👉 Explication : TLS requiert un client compatible (rsyslog avec `StreamDriver`); sinon tester d'abord en TCP clair sur un input de lab. Rechercher le message dans **Search** (`message:"Test pilote Graylog"`) : hôte, horodatage et champs.


## ⚡ 2. Production — Façon Simplifiée

1. Étendre par source validée : nommer les inputs `protocole-environnement-source`, documenter responsable, port, certificat et règle de pare-feu :
   ```bash
   sudo ufw status numbered
   sudo ss -ltnp | grep 6514
   ```
   👉 Explication : vérifier l'ingestion dans **System > Inputs** (débit) après chaque activation.


## 🔒 3. Production — Façon Sécurisée

- N'exposer aucun input à Internet; appliquer une ACL source côté réseau et écouter uniquement sur l'interface requise.
- Chiffrer le transport des journaux sensibles et valider les certificats; ne pas collecter mots de passe, tokens ou données personnelles non autorisées.
- Définir les droits de recherche par équipe et une politique de rétention approuvée.

## ✅ Validation et retour arrière

- **Validation** : input actif, événement pilote trouvé, origine et champs cohérents, aucune source non prévue.
- **Retour arrière** : désactiver l'input, supprimer la règle réseau associée et confirmer l'arrêt des événements.

## 🔗 Si le problème n'est pas résolu

- **Fiche de résolution complémentaire** : consulter la documentation officielle Graylog ci-dessous.
- [Graylog — Sécuriser l'environnement](https://go2docs.graylog.org/current/planning_your_deployment/secure_your_graylog_environment.htm)