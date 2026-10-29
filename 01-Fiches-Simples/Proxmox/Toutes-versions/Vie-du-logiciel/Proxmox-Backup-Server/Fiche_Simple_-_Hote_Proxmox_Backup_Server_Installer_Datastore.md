# Fiche_Simple_-_Hote_Proxmox_Backup_Server_Installer_Datastore.md

- **Environnement** : Serveur de sauvegarde Proxmox Backup Server dédié, séparé du cluster protégé
- **OS / Version** : Proxmox Backup Server 3.x (appliquer une version encore supportée) avec Proxmox VE
- **Catégorie** : sauvegarde / restauration
- **Tags** : `proxmox-backup-server`, `pbs3`, `proxmox`, `sauvegarde`, `restauration`

---

## Problème précis à résoudre

Installer PBS et créer un datastore avec des accès minimaux.

## 1. Hors-Production (Lab / Test / POC)

1. Installer PBS depuis le média ou le dépôt officiel.
   👉 Explication : suivre l'assistant de `pbs.proxmox.com`.

2. Ouvrir l'interface d'administration `https://IP_DU_PBS:8007` (remplacer IP_DU_PBS par l'adresse réelle).
   👉 Explication : console web de PBS.

3. **Administration > Storage / Disks > Directory** ou **ZFS** pour créer le stockage, puis **Datastore > Add Datastore**.
   👉 Explication : crée un datastore sur un système de fichiers pris en charge; ne pas utiliser de commandes génériques de formatage ou montage sur un stockage actif.

4. Vérifier capacité, alertes et politique de nettoyage (prune/GC).
   👉 Explication : évite le remplissage du datastore.

5. **Configuration > Access Control > User Management**, puis **API Token**: créer utilisateurs et tokens dédiés avec permissions minimales sur les namespaces et datastores requis.
   👉 Explication : évite l'usage de `root@pam`.

## 2. Production — Contrôles

Documenter le datastore, les permissions et les clés de chiffrement côté client.

## 3. Production — Sécurité

- Protéger secrets et clés de chiffrement des sauvegardes côté client.
- Accorder le moindre privilège aux tokens.

## Validation et retour arrière

- **Validation** : le datastore apparaît avec sa capacité et les tokens ont des permissions limitées.
- **Retour arrière** : retirer un datastore vide via **Datastore > Remove** seulement s'il ne contient aucune sauvegarde.

## Si le problème n'est pas résolu

- [Proxmox Backup Server — datastore](https://pbs.proxmox.com/docs/storage.html)
- [Proxmox Backup Server — documentation](https://pbs.proxmox.com/docs/)
- [Guide complet](../../../../../02-Fiches-Completes/Proxmox/Toutes-versions/Autres/12_Proxmox_Backup_Server_3x_PBS_Deduplication.md#2-installer-et-creer-le-datastore)
