# Fiche_Simple_-_Hote_Proxmox_Backup_Server_Relier_PVE_PBS.md

- **Environnement** : Serveur de sauvegarde Proxmox Backup Server dédié, séparé du cluster protégé
- **OS / Version** : Proxmox Backup Server 3.x (appliquer une version encore supportée) avec Proxmox VE
- **Catégorie** : sauvegarde / restauration
- **Tags** : `proxmox-backup-server`, `pbs3`, `proxmox`, `sauvegarde`, `restauration`

---

## Problème précis à résoudre

Ajouter PBS comme stockage de sauvegarde dans Proxmox VE et tester une petite tâche.

## 1. Hors-Production (Lab / Test / POC)

1. Dans PVE : **Datacenter > Storage > Add > Proxmox Backup Server**.
   👉 Explication : déclare le stockage PBS dans le cluster.

2. Renseigner serveur, datastore, compte ou token dédié (secret saisi dans le formulaire, jamais en argument) et **Fingerprint** (empreinte du certificat).
   👉 Explication : vérifier l'empreinte depuis un canal fiable.

3. Choisir le chiffrement côté client si la stratégie l'exige et sauvegarder séparément la clé de déchiffrement.
   👉 Explication : sans clé, la restauration est impossible.

4. Vérifier l'état du stockage :
   ```bash
   pvesm status
   ```
   👉 Explication : affiche le stockage PBS actif dans PVE.

5. **Datacenter > Backup > Add** sur un petit groupe de VM/CT, puis lancer **Run now**.
   👉 Explication : vérifier résultat, rétention, vérification d'intégrité et alertes avant généralisation.

## 2. Production — Contrôles

Généraliser seulement après validation du premier job.

## 3. Production — Sécurité

- Compte ou token dédié; empreinte du certificat vérifiée.
- Clé de chiffrement stockée hors de PBS.

## Validation et retour arrière

- **Validation** : la sauvegarde pilote se termine sans erreur et apparaît dans le datastore.
- **Retour arrière** : désactiver la tâche de sauvegarde pilote et retirer le stockage PBS de PVE si nécessaire.

## Si le problème n'est pas résolu

- [Proxmox VE — stockage PBS](https://pve.proxmox.com/wiki/Backup_and_Restore)
- [Proxmox Backup Server — documentation](https://pbs.proxmox.com/docs/)
- [Guide complet](../../../../../02-Fiches-Completes/Proxmox/Toutes-versions/Autres/12_Proxmox_Backup_Server_3x_PBS_Deduplication.md#3-relier-proxmox-ve-a-pbs)
