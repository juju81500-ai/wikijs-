---
title: "fiche-simple-vm-windows-server-2022-reprise-foret-ad-ds-preparer-sauvegardes"
description: "S'assurer de disposer de sauvegardes AD-aware saines et d'un runbook documenté."
published: true
date: 2026-11-03T14:22:28Z
tags: ["windows-server-2022", "active-directory", "ad-ds", "forest-recovery"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# fiche-simple-vm-windows-server-2022-reprise-foret-ad-ds-preparer-sauvegardes.md

- **Environnement** : Forêt [[Glossary:AD]] DS d'entreprise; laboratoire isolé recommandé
- **OS / Version** : Windows Server 2022 pour les contrôleurs de domaine concernés
- **Catégorie** : Active Directory / sauvegarde
- **Tags** : `windows-server-2022`, `active-directory`, `ad-ds`, `forest-recovery`

---

## Problème précis à résoudre

S'assurer de disposer de sauvegardes AD-aware saines et d'un runbook documenté.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les sauvegardes locales :
   ```powershell
   wbadmin get versions
   ```
   👉 Explication : Liste les sauvegardes Windows Server Backup disponibles sur ce serveur (lecture seule).

2. Relever les rôles [[Glossary:FSMO]] :
   ```powershell
   netdom query fsmo
   ```
   👉 Explication : Affiche les détenteurs des rôles FSMO à documenter (lecture seule).

3. Documenter par domaine : [[Glossary:DC]] retenu, date de sauvegarde, méthode de restauration, rôles FSMO, dépendances [[Glossary:DNS]]/SYSVOL.
   👉 Explication : nécessaire pour restaurer dans le bon ordre.

4. Conserver supports, comptes de secours, clés et procédures hors ligne ou dans un coffre distinct du domaine.
   👉 Explication : ils doivent rester accessibles si le domaine est perdu.

5. Vérifier que la sauvegarde est antérieure à la compromission présumée et que sa restauration a déjà été testée en laboratoire.
   👉 Explication : sinon arrêter et escalader au responsable AD/éditeur.

## 2. Production — Contrôles

Un snapshot [[Glossary:VM]] ne remplace pas une sauvegarde AD-aware, sauf scénario explicitement pris en charge par Microsoft (hyperviseur compatible VM-Generation ID) avec le runbook correspondant.

## 3. Production — Sécurité

- Sauvegardes protégées contre l'altération et testées régulièrement.

## Validation et retour arrière

- **Validation** : sauvegardes saines, testées et documentées.
- **Retour arrière** : conserver les sauvegardes existantes; ne rien supprimer avant validation des nouvelles.

## Si le problème n'est pas résolu

- [Microsoft Learn — Étapes de reprise d'une forêt AD](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-steps-for-restoring-the-forest)
- [Guide complet — étape 2](/fr/02-fiches-completes/windows/server-2022/autres/26-reprise-foret-ad-ds-windows-server-2022#2-preparer-et-qualifier-les-sauvegardes)