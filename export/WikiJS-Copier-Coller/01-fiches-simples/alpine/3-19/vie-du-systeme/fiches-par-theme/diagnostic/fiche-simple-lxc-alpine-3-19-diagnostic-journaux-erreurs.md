# 📄 Fiche_Simple_-_LXC_Alpine_3.19_Diagnostic_Journaux_Erreurs.md

- **Environnement** : LXC (Proxmox VE)
- **OS / Version** : Alpine Linux 3.19 - Famille Alpine (OpenRC, apk)
- **Catégorie** : Diagnostic & Maintenance / Analyse des erreurs système

## 🎯 Problème précis à résoudre
Identifier les services en échec, les erreurs consignées par syslog et les messages noyau d'un conteneur Alpine Linux, à partir des outils disponibles par défaut (OpenRC, BusyBox, `dmesg`).

> Alpine 3.19 est en fin de support : valider cette procédure sur une branche maintenue avant tout usage en production.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lister les services en échec et l'état des runlevels :
   ```sh
   rc-status --crashed
   rc-status -a
   ```
   👉 Explication : `--crashed` ne liste que les services dont le processus s'est arrêté de façon anormale. `rc-status -a` affiche tous les services et leur runlevel.

2. Extraire les erreurs de `/var/log/messages` :
   ```sh
   grep -iE 'error|fail|critical|panic' /var/log/messages | tail -n 50
   ```
   👉 Explication : Les 50 dernières lignes contenant un mot-clé d'erreur. Adapter le motif au besoin (par exemple le nom d'un service).

3. Lire les messages du noyau :
   ```sh
   dmesg | grep -iE 'error|fail|oom|segfault' | tail -n 50
   ```
   👉 Explication : `dmesg` affiche le tampon du noyau. Dans un LXC, ce tampon appartient à l'hôte : si la commande renvoie `Operation not permitted`, lire les messages noyau sur l'hôte Proxmox.

---

## ⚡ 2. Production — Façon Simplifiée
1. Corréler une erreur avec un service précis :
   ```sh
   rc-service <nom_du_service> status
   grep '<nom_du_service>' /var/log/messages | tail -n 50
   ```
   👉 Explication : Le statut OpenRC indique l'état courant; les journaux indiquent la séquence qui a conduit à l'arrêt.

2. Vérifier l'espace disque et les inodes, causes fréquentes d'erreurs d'écriture :
   ```sh
   df -h
   df -i
   ```
   👉 Explication : Un volume plein ou sans inodes libres provoque des erreurs `No space left on device` dans les journaux, même si le service semble actif.

---

## 🔒 3. Production — Façon Sécurisée
1. Consulter les tentatives d'authentification refusées sur SSH :
   ```sh
   grep -E 'Failed password|Invalid user' /var/log/messages | tail -n 50
   ```
   👉 Explication : Ces lignes signalent une tentative de brute-force ou un mauvais utilisateur. Les comparer avec les adresses bannies par Fail2ban si ce service est installé.

2. Conserver l'extrait analysé dans le ticket d'incident ou la fiche serveur, en retirant les données personnelles avant tout partage.