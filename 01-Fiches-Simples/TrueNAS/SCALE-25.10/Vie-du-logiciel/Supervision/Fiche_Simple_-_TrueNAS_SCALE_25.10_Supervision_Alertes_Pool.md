# 📄 Fiche_Simple_-_TrueNAS_SCALE_25.10_Supervision_Alertes_Pool.md

- **Environnement** : TrueNAS SCALE 25.10 (Goldeye), NAS de lab ou de production avec pools ZFS
- **OS / Version** : TrueNAS SCALE 25.10 Goldeye (base Debian)
- **Catégorie** : Supervision / Alertes et surveillance des pools
- **Tags** : `truenas`, `scale2510`, `zfs`, `pool`, `scrub`, `smart`, `alerts`

---

## 🎯 Problème précis à résoudre
Configurer l'envoi des alertes ZFS et SMART par courriel, planifier les scrubs et les tests SMART, puis vérifier que chaque alerte est réellement reçue.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Configurer le serveur de messagerie :
   `System Settings > Email` : Send Mail Method = `SMTP`, From Email = `<adresse_expediteur>`, Outgoing Mail Server = `<serveur_smtp>`, Port = `587`
   👉 Explication : Les alertes sont envoyées par ce canal ; sans serveur SMTP valide, aucune notification n'arrive.
2. Activer le service d'alerte par courriel :
   `Alerts (icône cloche) > Alert Settings` : ajouter le service E-Mail, niveau minimal = `WARNING` (à vérifier sur la version déployée)
   👉 Explication : Définit qui reçoit quelles alertes et à partir de quel niveau.
3. Planifier le scrub hebdomadaire ou mensuel :
   `Data Protection > Scrub Tasks > Add` : Pool = `<nom_pool>`, Schedule = `mensuel`, Threshold days = `35`
   👉 Explication : Le scrub relit les données et vérifie les sommes de contrôle ZFS.
4. Planifier des tests SMART :
   `Data Protection > S.M.A.R.T. Tests > Add` : Disks = tous, Type = `SHORT`, Schedule = `hebdomadaire` (à vérifier sur la version déployée)
   👉 Explication : Détecte l'usure ou les secteurs défaillants avant la panne.
5. Vérifier l'état des pools depuis le shell :
   `zpool status -x` et `zpool list -o name,health,size,alloc,free`
   👉 Explication : `zpool status -x` n'affiche que les pools en erreur ; une sortie « all pools are healthy » est attendue.

---

## ⚡ 2. Production — Façon Simplifiée
1. Tester l'envoi d'une alerte :
   `Alerts (icône cloche) > Alert Settings` : envoi d'une alerte de test (libellé à vérifier sur la version déployée)
   👉 Explication : Confirme que le courriel arrive réellement dans la boîte de l'administrateur.
2. Contrôler l'historique des alertes :
   `midclt call alert.list`
   👉 Explication : Liste les alertes actives et leur niveau, pour les traiter sans attendre un rapport.
3. Contrôler les événements ZFS récents :
   `zpool events -v | tail -n 50`
   👉 Explication : Affiche les erreurs d'E/S et les changements d'état survenus récemment.

---

## 🔒 3. Production — Façon Sécurisée
1. Contrôler la santé SMART de chaque disque :
   `sudo smartctl -H /dev/<disque>` et `sudo smartctl -A /dev/<disque>`
   👉 Explication : Le statut global et les attributs (secteurs réalloués, temps de réponse) signalent une défaillance imminente.
2. Remplacer un disque uniquement après diagnostic :
   `zpool status -v <nom_pool>` puis `System Settings > Storage` (remplacement) selon la procédure de reprise
   👉 Explication : Un remplacement mal préparé peut dégrader un pool sain ; ne jamais exporter ou recréer un pool pour corriger une alerte.
3. Journaliser les alertes sur un syslog distant :
   `System Settings > Advanced` : section Syslog, serveur = `<adresse_ip_syslog>` (à vérifier sur la version déployée)
   👉 Explication : Les alertes restent disponibles même si le NAS est compromis.
