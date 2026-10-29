# 📄 Fiche_Simple_-_TrueNAS_SCALE_25.10_Systeme_Mise_A_Jour.md

- **Environnement** : TrueNAS SCALE 25.10 (Goldeye), NAS de lab ou de production, fenêtre de maintenance planifiée
- **OS / Version** : TrueNAS SCALE 25.10 Goldeye (base Debian)
- **Catégorie** : Système / Mises à jour

---

## 🎯 Problème précis à résoudre
Mettre à jour TrueNAS SCALE 25.10 sans perdre la configuration ni les pools, avec un environnement de démarrage précédent disponible pour revenir en arrière.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever la version installée :
   `midclt call system.version`
   👉 Explication : Renvoie la version de TrueNAS à comparer avec les notes de version.
2. Exporter la configuration du système :
   `System Settings > General > Manage Configuration` : Download File
   👉 Explication : Sauvegarde les réglages (partages, tâches, utilisateurs, réseau) avant mise à jour.
3. Vérifier le train de mise à jour :
   `System Settings > Update` : Train = `TrueNAS-SCALE-Goldeye` (à vérifier sur la version déployée)
   👉 Explication : Le train doit correspondre à la branche 25.10 ; un autre train peut proposer une version différente.
4. Rechercher les mises à jour disponibles :
   `midclt call update.check_available` (à vérifier sur la version déployée)
   👉 Explication : Interroge le serveur de mise à jour et indique la version cible.
5. Appliquer la mise à jour depuis l'interface :
   `System Settings > Update` : Update, puis redémarrage à la fin de l'opération
   👉 Explication : Installe la nouvelle image dans un environnement de démarrage distinct.
6. Vérifier après redémarrage :
   `midclt call system.version` et `zpool status -x`
   👉 Explication : Confirme la version finale et l'absence d'erreur sur les pools.

---

## ⚡ 2. Production — Façon Simplifiée
1. Activer la vérification automatique (notification seulement) :
   `System Settings > Update` : Automatically Check for Updates = coché
   👉 Explication : TrueNAS signale les mises à jour disponibles sans les installer.
2. Planifier l'installation dans une fenêtre de maintenance :
   `System Settings > Update` : Update
   👉 Explication : Les services (SMB, NFS, iSCSI) sont interrompus pendant le redémarrage.
3. Contrôler les environnements de démarrage conservés :
   `zfs list -r -t filesystem boot-pool/ROOT`
   👉 Explication : Liste les versions précédentes disponibles pour un retour arrière.

---

## 🔒 3. Production — Façon Sécurisée
1. Tester la version cible sur un NAS de lab avant la production :
   `System Settings > Update` sur `<nas_lab>` puis contrôle des partages et tâches
   👉 Explication : Valide la mise à jour sur une configuration identique.
2. Vérifier l'état des pools et des disques avant intervention :
   `zpool status -v` et `zpool list -o name,health,size,alloc,free`
   👉 Explication : Une mise à jour sur un pool dégradé augmente le risque de perte de données.
3. Revenir à l'environnement de démarrage précédent si la vérification échoue :
   `System Settings > Boot > Boot Environments` : Activate sur l'environnement précédent, puis redémarrer
   👉 Explication : Restaure la version précédente sans réinstallation ni perte des données.
4. Ne jamais lancer de mise à jour de paquets Debian à la main :
   `apt upgrade` est interdit sur TrueNAS
   👉 Explication : Les paquets système sont gérés par TrueNAS ; une mise à jour manuelle casse la cohérence de l'image.