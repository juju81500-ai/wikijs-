# Fiche_Simple_-_VM_Windows_Server_2022_Veeam_Creer_Job_HyperV_Pilote.md

- **Environnement** : Serveur Windows Server 2022 dédié au serveur de sauvegarde Veeam (pilote autonome) et hôte Hyper-V autorisé
- **OS / Version** : Windows Server 2022; Veeam Backup & Replication 13.1.2.57
- **Catégorie** : sauvegarde VM / job
- **Tags** : `windows-server-2022`, `veeam`, `backup-replication`, `hyper-v`, `job`, `hyper-v`

---

## Problème précis à résoudre

Créer un premier job de sauvegarde sur une VM pilote non critique.

## 1. Hors-Production (Lab / Test / POC)

1. Ajouter l'hôte ou cluster Hyper-V autorisé : **Console Veeam > Inventory > Add Server > Microsoft Hyper-V**
   👉 Explication : valider le compte de connexion et les composants déployés.

2. Créer le job : **Home > Backup Job > Virtual machine > Hyper-V**
   👉 Explication : sélectionner une VM pilote non critique, le dépôt dédié, le calendrier, la rétention et éviter les chevauchements.

3. Activer le traitement cohérent avec les applications lorsqu'il est supporté : **Guest Processing > Enable application-aware processing**
   👉 Explication : examiner les journaux VSS et les identifiants invités.

4. Prévoir une copie indépendante selon la stratégie 3-2-1-1-0 :
   👉 Explication : destination distincte du serveur principal (Backup Copy Job).

## 2. Production — Contrôles

Limiter le périmètre à une VM pilote avant d'étendre.

## 3. Production — Sécurité

- Utiliser un compte de connexion à l'hôte au moindre privilège.

## Validation et retour arrière

- **Validation** : job créé, validé sans erreur de configuration.
- **Retour arrière** : **Home > Jobs > Backup > clic droit > Disable / Delete** du job pilote.

## Si le problème n'est pas résolu

- [Veeam 13 — guide utilisateur](https://helpcenter.veeam.com/docs/vbr/userguide/)
- [Veeam 13 — installer Backup & Replication](https://helpcenter.veeam.com/docs/vbr/userguide/install_vbr.html)
- [Veeam 13 — jobs Hyper-V](https://helpcenter.veeam.com/docs/vbr/userguide/backup_job_hv.html)
- [Guide complet Veeam Windows Server 2022](../../../../../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/58_Deploiement_Veeam_Backup_Replication_13_Windows_Server_2022.md#4-creer-le-job-hyper-v-pilote)
