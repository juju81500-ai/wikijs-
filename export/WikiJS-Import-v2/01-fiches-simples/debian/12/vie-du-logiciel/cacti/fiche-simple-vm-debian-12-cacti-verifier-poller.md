---
title: "Fiche Simple - VM Debian 12 Cacti Verifier Poller"
description: "Déterminer pourquoi un appareil pilote ne reçoit plus de données/graphes dans Cacti."
published: true
date: 2026-10-29T19:55:10Z
tags: ["debian12", "cacti", "poller", "snmp", "rrdtool"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# 📄 Fiche_Simple_-_VM_Debian_12_Cacti_Verifier_Poller.md

- **Environnement** : Cacti 1.2.31 sur Debian 12, poller local
- **OS / Version** : Debian 12 Bookworm
- **Catégorie** : Supervision / diagnostic
- **Tags** : `debian12`, `cacti`, `poller`, `snmp`, `rrdtool`

---

## 🎯 Problème précis à résoudre

Déterminer pourquoi un appareil pilote ne reçoit plus de données/graphes dans Cacti.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Vérifier que l'hôte répond depuis le poller :
   ```bash
   ping -c 3 IP_HOTE
   ```
   👉 Explication : remplacer par l'IP de l'appareil pilote; vérifier l'adresse saisie dans **Console > Management > Devices**.

2. Vérifier horloge et services :
   ```bash
   timedatectl | grep synchronized
   systemctl --no-pager status apache2 mariadb
   pgrep -af poller.php || echo "poller non actif"
   ```
   👉 Explication : une horloge décalée ou un service arrêté suffit à interrompre les graphes.

3. Consulter le journal et l'état SNMP : **Console > Utilities > System Utilities > View Cacti Log File**, filtre `POLLER`, puis **Console > Management > Devices > hôte** (état, dernière collecte).
   👉 Explication : repérer l'heure de la dernière collecte réussie.

4. Tester SNMPv3 en lecture seule sans secret en argument :
   ```bash
   read -rsp "Phrase SNMPv3 : " SPW; echo
   snmpget -v3 -l authPriv -u UTILISATEUR_RO -a SHA -A "$SPW" -x AES -X "$SPW" IP_HOTE 1.3.6.1.2.1.1.3.0
   unset SPW
   ```
   👉 Explication : remplacer utilisateur et IP; utiliser des phrases distinctes si le profil l'exige.

5. Vérifier espace disque et droits RRD :
   ```bash
   df -h /var/lib/cacti
   ls -ld /var/lib/cacti/rra
   sudo tail -20 /var/log/apache2/error.log
   ```
   👉 Explication : le dossier `rra` doit être modifiable par `www-data`.


## ⚡ 2. Production — Façon Simplifiée

1. Isoler la portée : un appareil, un template, tout le poller, ou le stockage :
   ```bash
   sudo -u www-data php /usr/share/cacti/site/poller.php --force --debug 2>&1 | tail -30
   ```
   👉 Explication : exécuter sous le compte web; corriger la cause minimale puis attendre une collecte suivante avant d'agir globalement.


## 🔒 3. Production — Façon Sécurisée

- N'utiliser que des adresses et identifiants autorisés; aucune découverte de réseau sans périmètre validé.
- Ne pas supprimer de RRD ni réinitialiser la base pour masquer une anomalie.
- Avant toute modification DB, cron ou permissions, sauvegarder la configuration et ouvrir un changement traçable.

## ✅ Validation et retour arrière

- **Validation** : collecte récente, courbes mises à jour, pas d'erreur répétée dans le poller log.
- **Retour arrière** : restaurer la configuration précédente et sa permission, puis vérifier un cycle de polling.

## 🔗 Si le problème n'est pas résolu

- [Cacti — Débogage](https://docs.cacti.net/Debugging.md)
- [Cacti — Data Debug](https://docs.cacti.net/Data-Debug.md)