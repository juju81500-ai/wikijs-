# 📄 Fiche_Simple_-_LXC_Alpine_Migrer_3.19_Version_Maintenue.md

- **Environnement** : LXC Proxmox VE existant et nouveau LXC de remplacement
- **OS / Version** : Alpine Linux 3.19 vers une branche Alpine maintenue
- **Catégorie** : Système / Migration
- **Tags** : `[alpine]`, `[alpine3.19]`, `[lxc]`, `[proxmox]`, `[migration]`, `[maintenance]`

## 🎯 Problème précis à résoudre
Remplacer un conteneur Alpine Linux 3.19 ancien par un nouveau CT créé avec une version maintenue, en transférant services et données avec une possibilité de retour arrière.

> Préférer une migration côte à côte à une mise à niveau majeure en place. Vérifier la branche Alpine maintenue et la compatibilité des applications au moment de la migration.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Inventorier le CT et ses services :
   ```sh
   pct config <CTID_SOURCE>
   pct exec <CTID_SOURCE> -- cat /etc/alpine-release
   pct exec <CTID_SOURCE> -- rc-status
   pct exec <CTID_SOURCE> -- apk info -vv
   ```
2. Créer une sauvegarde indépendante du CT :
   ```sh
   vzdump <CTID_SOURCE> --mode stop --compress zstd --storage <STOCKAGE_SAUVEGARDE>
   ```
3. Créer un nouveau CT à partir d'un template Alpine maintenu, restaurer les configurations nécessaires et recopier les données applicatives après arrêt cohérent des services.
   👉 *Explication : ne pas réutiliser l'adresse IP de production tant que l'ancien CT est encore actif.*

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier la restauration de la sauvegarde et noter l'IP, le bridge/VLAN, les points de montage, les services OpenRC et les paquets du CT source.
2. Créer le nouveau CT avec la version Alpine maintenue, des ressources équivalentes ou ajustées, un accès console et une adresse temporaire.
3. Installer les paquets depuis les dépôts de la nouvelle branche, migrer les configurations une par une et copier les données avec les propriétaires et permissions requis.
4. Tester les services, DNS, routes, journaux et intégrations depuis un réseau de test; planifier ensuite une bascule d'IP/DNS pendant une fenêtre de maintenance.
   👉 *Explication : ne pas copier aveuglément tout `/etc` d'une version à l'autre; les fichiers de configuration et paquets peuvent avoir changé.*

## 🔒 3. Production — Façon Sécurisée
1. Garder le CT source arrêté mais intact après la bascule et jusqu'à la validation métier; éviter les démarrages simultanés avec la même IP ou les mêmes tâches planifiées.
2. Mettre à jour DNS, supervision, sauvegarde et règles réseau pour le nouveau CT.
3. Ne supprimer l'ancien CT qu'après validation, sauvegarde finale et délai de retour convenu.

## ✅ Validation et retour arrière
- Vérifier la version Alpine, les services `rc-status`, les ports, la résolution DNS et le parcours applicatif complet.
- En cas d'échec, arrêter le nouveau CT puis remettre en service le CT source et rétablir les enregistrements réseau/DNS.
- Conserver la sauvegarde et les journaux de bascule jusqu'à clôture documentée.