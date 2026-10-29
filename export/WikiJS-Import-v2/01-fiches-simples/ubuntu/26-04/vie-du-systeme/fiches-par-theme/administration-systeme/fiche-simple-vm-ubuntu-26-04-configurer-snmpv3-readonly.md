---
title: "Fiche Simple - VM Ubuntu 26.04 Configurer SNMPv3 ReadOnly"
description: "Activer SNMPv3 en lecture seule sur un serveur Linux et n'accepter les requêtes que depuis un poller autorisé."
published: true
date: 2026-10-29T20:22:42Z
tags: ["ubuntu2604", "snmpv3", "snmpd", "supervision", "securite"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_26.04_Configurer_SNMPv3_ReadOnly.md

- **Environnement** : VM Ubuntu supervisée par LibreNMS ou un poller SNMP autorisé
- **OS / Version** : Ubuntu Server 26.04 LTS
- **Catégorie** : Supervision / SNMPv3
- **Tags** : `ubuntu2604`, `snmpv3`, `snmpd`, `supervision`, `securite`

---

## 🎯 Problème précis à résoudre

Activer SNMPv3 en lecture seule sur un serveur Linux et n'accepter les requêtes que depuis un poller autorisé.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Installer :
   ```bash
   sudo apt update
   sudo apt install snmpd snmp
   ```
   👉 Explication : `snmpd` est le démon, `snmp` fournit les outils de test.

2. Créer l'utilisateur SNMPv3 authPriv SHA/AES (secrets saisis, non écrits dans l'historique) :
   ```bash
   sudo systemctl stop snmpd
   read -rsp "Secret auth : " SA; echo; read -rsp "Secret priv : " SP; echo
   echo "createUser UTILISATEUR_LAB SHA \"$SA\" AES \"$SP\"" | sudo tee -a /var/lib/snmp/snmpd.conf >/dev/null
   unset SA SP
   ```
   👉 Explication : le démon consomme cette ligne au démarrage; ne jamais réutiliser les secrets entre environnements.

3. Tester depuis le poller de lab :
   ```bash
   snmpwalk -v3 -l authPriv -u UTILISATEUR_LAB -a SHA -A SECRET_AUTH -x AES -X SECRET_PRIV IP_SERVEUR 1.3.6.1.2.1.1
   ```
   👉 Explication : valeurs de lab uniquement; en production, utiliser un fichier de configuration `~/.snmp/snmp.conf` plutôt que des secrets en argument.


## ⚡ 2. Production — Façon Simplifiée

1. Préparer l'utilisateur dans `/var/lib/snmp/snmpd.conf` (éditeur root, services arrêtés) :
   ```bash
   sudo systemctl stop snmpd
   sudoedit /var/lib/snmp/snmpd.conf
   ```
   Ligne à ajouter :
   ```text
   createUser UTILISATEUR_SNMP SHA "SECRET_AUTH" AES "SECRET_PRIV"
   ```
   👉 Explication : remplacer; le démon remplace la ligne par sa forme persistante; fichier protégé selon les permissions du paquet.

2. Dans `/etc/snmp/snmpd.conf` (`sudoedit`), limiter l'accès :
   ```text
   agentAddress udp:IP_GESTION:161
   rouser UTILISATEUR_SNMP priv
   sysLocation EMPLACEMENT
   sysContact CONTACT_EXPLOITATION
   ```
   👉 Explication : lecture seule, niveau `priv`, écoute limitée à l'interface d'administration.

3. Vérifier la configuration et redémarrer :
   ```bash
   sudo systemctl restart snmpd
   sudo systemctl --no-pager status snmpd
   sudo ss -lunp | grep ':161'
   ```
   👉 Explication : le port 161 doit écouter uniquement sur l'IP de gestion.


## 🔒 3. Production — Façon Sécurisée

- Restreindre UDP/161 dans le pare-feu à l'adresse IP du poller uniquement.
- Ne pas configurer `rwuser`, SNMPv1/v2c ou une communauté publique pour cette supervision.
- Déposer les secrets au clavier dans l'éditeur et les transmettre par coffre sécurisé; ne pas les ajouter à l'historique shell.
- Installer les règles firewall persistantes selon la politique de la VM et vérifier qu'aucune écoute ne subsiste sur l'interface publique.

## ✅ Validation et retour arrière

- **Précontrôles** : IP de gestion, route du poller, secrets SNMPv3 et console de secours.
- **Validation** : test `snmpwalk` depuis le poller avec authPriv; confirmer refus depuis une autre adresse et lecture de sysName/sysUpTime.
- **Retour arrière** : restaurer la copie de `snmpd.conf` et de la configuration persistante de l'utilisateur, puis redémarrer `snmpd`.

## 🔗 Si le problème n'est pas résolu

- **Fiche de résolution complémentaire** : [[Ubuntu26_SNMPv3_Poller_Aucune_Reponse]]
- [LibreNMS — Exemples de configuration SNMP](https://docs.librenms.org/Support/SNMP-Configuration-Examples/)