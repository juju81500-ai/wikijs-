# Fiche_Simple_-_Hote_Proxmox_Backup_Server_Tester_Restauration.md

- **Environnement** : Serveur de sauvegarde Proxmox Backup Server dédié, séparé du cluster protégé
- **OS / Version** : Proxmox Backup Server 3.x (appliquer une version encore supportée) avec Proxmox VE
- **Catégorie** : sauvegarde / restauration
- **Tags** : `proxmox-backup-server`, `pbs3`, `proxmox`, `sauvegarde`, `restauration`

---

## Problème précis à résoudre

Prouver qu'une sauvegarde est restaurable.

## 1. Hors-Production (Lab / Test / POC)

1. Dans PVE : **Stockage PBS > Sauvegardes**, sélectionner un point de sauvegarde puis **Restore**.
   👉 Explication : une tâche verte n'est pas une preuve de restaurabilité.

2. Restaurer vers un identifiant temporaire (remplacer 9200 par un identifiant libre) et un réseau isolé.
   👉 Explication : évite tout conflit avec la VM d'origine.

3. Équivalent en commande (remplacer STOCKAGE_PBS, 9200 et SNAPSHOT par vos valeurs) :
   ```bash
   sudo qmrestore STOCKAGE_PBS:backup/SNAPSHOT 9200 --unique 1
   ```
   👉 Explication : restaure la VM sous un nouvel identifiant avec de nouvelles adresses MAC; ne pas démarrer avant d'avoir isolé le réseau.

4. Démarrer la VM, vérifier application, permissions et cohérence métier, puis documenter le résultat.
   👉 Explication : c'est le test d'acceptation.

5. Supprimer la VM de test.
   👉 Explication : nettoyage.

## 2. Production — Contrôles

Répéter régulièrement ce test et conserver la preuve.

## 3. Production — Sécurité

- Réseau isolé obligatoire pour la VM restaurée.

## Validation et retour arrière

- **Validation** : la VM restaurée démarre et l'application répond.
- **Retour arrière** : arrêter puis supprimer la VM temporaire; la VM d'origine n'est pas touchée.

## Si le problème n'est pas résolu

- [Proxmox Backup Server — restauration](https://pbs.proxmox.com/docs/backup-client.html)
- [Proxmox Backup Server — documentation](https://pbs.proxmox.com/docs/)
- [Guide complet](../../../../../02-Fiches-Completes/Proxmox/Toutes-versions/Autres/12_Proxmox_Backup_Server_3x_PBS_Deduplication.md#4-tester-la-restauration)
