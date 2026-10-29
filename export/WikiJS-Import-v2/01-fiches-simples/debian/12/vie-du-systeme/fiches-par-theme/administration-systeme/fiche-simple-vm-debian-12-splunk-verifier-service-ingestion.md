---
title: "Fiche Simple - VM Debian 12 Splunk Verifier Service Ingestion"
description: "Contrôler l'état de Splunk et d'une ingestion pilote sans exposer de secrets ni relancer la collecte générale."
published: true
date: 2026-10-29T20:22:42Z
tags: ["debian12", "splunk", "siem", "logs", "systemd", "diagnostic"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Debian_12_Splunk_Verifier_Service_Ingestion.md

- **Environnement** : Splunk Enterprise 10.2 sur Debian 12 x86-64
- **OS / Version** : Debian 12 Bookworm
- **Catégorie** : SIEM / exploitation
- **Tags** : `debian12`, `splunk`, `siem`, `logs`, `systemd`, `diagnostic`

---

## 🎯 Problème précis à résoudre

Contrôler l'état de Splunk et d'une ingestion pilote sans exposer de secrets ni relancer la collecte générale.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Contrôler le service :
   ```bash
   sudo -H -u splunk /opt/splunk/bin/splunk status
   ```
   👉 Explication : exécuté sous le compte `splunk`, jamais en root.

2. Lire les journaux de démarrage :
   ```bash
   sudo journalctl -u Splunkd -b --no-pager
   tail -50 /opt/splunk/var/log/splunk/splunkd.log
   ```
   👉 Explication : si l'unité porte un autre nom, `systemctl list-units | grep -i splunk`.

3. Dans Splunk Web : **Settings > Monitoring Console > Health Check**, puis **Search & Reporting** avec la recherche bornée :
   ```
   index=INDEX_PILOTE "EVENEMENT_SYNTHETIQUE" earliest=-15m
   ```
   👉 Explication : remplacer index et texte; l'événement du pilote doit apparaître.


## ⚡ 2. Production — Façon Simplifiée

1. Vérifier le Web en HTTPS, le service et l'espace :
   ```bash
   curl -fsSI https://splunk.example.net:8000/ | head -1
   sudo -H -u splunk /opt/splunk/bin/splunk status
   df -h /opt/splunk/var
   ```
   👉 Explication : remplacer le nom; distinguer panne d'instance et défaut d'input, de forwarder, de licence ou de droits.

2. Rechercher les erreurs de parsing récentes :
   ```bash
   sudo grep -E 'ERROR|WARN' /opt/splunk/var/log/splunk/splunkd.log | tail -20
   ```
   👉 Explication : ne pas purger d'index pour régler une alerte disque.


## 🔒 3. Production — Façon Sécurisée

- Ne pas utiliser `root` ou le compte superutilisateur Splunk pour le contrôle courant.
- Ne pas redémarrer tout le service ni modifier les inputs sans changement approuvé.
- Restreindre les ports Web/management aux réseaux autorisés; ne jamais joindre des identifiants dans une commande.
- Ne pas purger les index pour résoudre une alerte disque; appliquer la politique de rétention avec validation du propriétaire.

## ✅ Validation et retour arrière

- **Validation** : service actif sous le compte prévu, UI en TLS accessible, événement test présent dans le bon index et pas d'erreur persistante.
- **Retour arrière** : restaurer la configuration précédemment sauvegardée et redémarrer selon la méthode de gestion approuvée.

## 🔗 Si le problème n'est pas résolu

- [Splunk — Démarrage initial et dépannage](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/start-using-splunk-enterprise/start-splunk-enterprise-for-the-first-time)
- [Splunk — Sécuriser l'installation](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/secure-your-splunk-enterprise-installation)