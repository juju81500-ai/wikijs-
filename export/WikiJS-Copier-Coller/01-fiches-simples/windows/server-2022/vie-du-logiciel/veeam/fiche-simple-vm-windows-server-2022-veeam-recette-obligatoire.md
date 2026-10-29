# Fiche_Simple_-_VM_Windows_Server_2022_Veeam_Recette_Obligatoire.md

- **Environnement** : Serveur Windows Server 2022 dédié au serveur de sauvegarde Veeam (pilote autonome) et hôte Hyper-V autorisé
- **OS / Version** : Windows Server 2022; Veeam Backup & Replication 13.1.2.57
- **Catégorie** : sauvegarde VM / recette

---

## Problème précis à résoudre

Prouver la récupérabilité par une restauration réelle.

## 1. Hors-Production (Lab / Test / POC)

1. Lire l'état des services Veeam :
   ```powershell
   Get-Service Veeam* | Select-Object Name, Status, StartType
   ```
   👉 Explication : les services doivent être démarrés.

2. Lancer le job pilote : **Home > Jobs > Backup > clic droit > Start**
   👉 Explication : confirmer résultat, durée, taille, points de restauration et alerte en cas d'échec.

3. Restaurer un fichier : **Home > Backups > Disk > clic droit sur la VM > Restore guest files**
   👉 Explication : vérifier le contenu obtenu.

4. Restaurer la VM en réseau isolé : **Backups > clic droit > Restore entire VM**
   👉 Explication : vérifier OS, application, données et permissions avant de généraliser.

## 2. Production — Contrôles

Contrôler aussi les sessions et points de restauration dans la console.

## 3. Production — Sécurité

- Une tâche terminée avec succès n'est pas une preuve suffisante de récupérabilité.

## Validation et retour arrière

- **Validation** : restauration fichier et VM validées en réseau isolé.
- **Retour arrière** : supprimer la VM de recette restaurée sur l'hôte isolé.

## Si le problème n'est pas résolu

- [Veeam 13 — guide utilisateur](https://helpcenter.veeam.com/docs/vbr/userguide/)
- [Veeam 13 — installer Backup & Replication](https://helpcenter.veeam.com/docs/vbr/userguide/install_vbr.html)
- [Guide complet Veeam Windows Server 2022](/02-fiches-completes/windows/server-2022/installation-deploiement/58-deploiement-veeam-backup-replication-13-windows-server-2022#5-recette-obligatoire)