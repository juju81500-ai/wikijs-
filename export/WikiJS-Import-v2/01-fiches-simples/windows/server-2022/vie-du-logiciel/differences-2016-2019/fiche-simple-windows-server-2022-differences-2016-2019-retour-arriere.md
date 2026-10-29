---
title: "Fiche Simple - Windows Server 2022 Differences 2016 2019 Retour Arriere"
description: "Revenir à l'état 2016/2019 si la mise à niveau vers 2022 échoue ou si l'application ne fonctionne plus."
published: true
date: 2026-10-29T21:23:12Z
tags: ["windows-server", "windows-server-2016", "windows-server-2019", "windows-server-2022", "retour-arriere", "sauvegarde", "restauration"]
editor: markdown
dateCreated: 2026-10-29T21:23:12Z
dateModified: 2026-10-29T21:23:12Z
---

# Fiche_Simple_-_Windows_Server_2022_Differences_2016_2019_Retour_Arriere

- **Environnement** : Windows Server 2016 et 2019 (comparés à 2022), lab ou serveur de test
- **OS / Version** : Windows Server 2016 / 2019 (référence 2022)
- **Catégorie** : systèmes / différences de versions
- **Tags** : `windows-server`, `windows-server-2016`, `windows-server-2019`, `windows-server-2022`, `retour-arriere`, `sauvegarde`, `restauration`

---

## Problème précis à résoudre

Revenir à l'état 2016/2019 si la mise à niveau vers 2022 échoue ou si l'application ne fonctionne plus.

## 1. Hors-Production (Lab / Test / POC)

1. Avant l'opération : consigner l'emplacement de la sauvegarde complète et du snapshot de VM.
   👉 Explication : une mise à niveau en place n'a pas de désinstallation générale fiable : le retour arrière repose sur la sauvegarde ou le snapshot.
2. Si l'installation échoue en cours de route, laisser Windows annuler automatiquement la mise à niveau et redémarrer ; ne pas couper l'alimentation.
   👉 Explication : Windows Setup restaure l'ancien système en cas d'échec ; vérifier ensuite les journaux dans `C:\$WINDOWS.~BT\Sources\Panther`.
3. Si le système démarre mais est défectueux : restaurer le snapshot de VM (console de l'hyperviseur) ou restaurer la sauvegarde :
   ```powershell
   wbadmin get versions
   wbadmin start sysrecovery -version:VERSION_A_REMPLACER -backupTarget:E: -machineName:NOM_SERVEUR
   ```
   👉 Explication : `VERSION_A_REMPLACER` provient de `wbadmin get versions` ; `sysrecovery` s'exécute depuis l'environnement de récupération (WinRE).
4. Pour un contrôleur de domaine : suivre la procédure de restauration d'AD DS (état système) et ne pas restaurer un snapshot sans précautions USN/réplication.
   👉 Explication : une restauration incorrecte d'un DC peut causer un retour en arrière de la réplication (USN rollback) ; utiliser une VM compatible VM-GenerationID.

## 2. Production — Contrôles

- Conserver sauvegarde et snapshot jusqu'à validation métier complète puis supprimer le snapshot pour éviter une dérive de stockage.

## 3. Production — Sécurité

- Protéger l'accès aux sauvegardes ; contrôler que le serveur restauré est bien isolé tant qu'il n'est pas validé.

## Validation et retour arrière

- **Validation** : version initiale restaurée, services et réplication opérationnels. **Retour arrière** : sans objet (c'est l'opération de retour arrière).

## Si le problème n'est pas résolu

- [Fiche d'entrée Windows Server 2016 / 2019 / 2022](/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-windows-server-2016-2019-2022)
- [Microsoft Learn — wbadmin start sysrecovery](https://learn.microsoft.com/fr-fr/windows-server/administration/windows-commands/wbadmin-start-sysrecovery)
- [Microsoft Learn — Restauration d'AD DS](https://learn.microsoft.com/fr-fr/windows-server/identity/ad-ds/manage/ad-forest-recovery-guide)