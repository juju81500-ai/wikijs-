# Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Restaurer_Premiers_DC.md

- **Environnement** : Forêt AD DS d'entreprise; laboratoire isolé recommandé
- **OS / Version** : Windows Server 2022 pour les contrôleurs de domaine concernés
- **Catégorie** : Active Directory / reprise après sinistre

---

## Problème précis à résoudre

Restaurer les premiers DC en réseau isolé en suivant le runbook Microsoft.

## 1. Hors-Production (Lab / Test / POC)

1. Suivre le runbook Microsoft officiel pour chaque domaine (liens de la section « Si le problème n'est pas résolu »).
   👉 Explication : aucune commande n'est reprise ici : elles dépendent du scénario et du DC.

2. Restaurer d'abord un DC inscriptible du domaine racine de forêt, isolé du réseau de production, puis les domaines parents avant les enfants, avec une sauvegarde AD-aware.
   👉 Explication : ordre prévu par la procédure officielle.

3. Appliquer les consignes précises relatives à AD DS et SYSVOL; la procédure autoritative SYSVOL ne s'applique qu'au DC désigné.
   👉 Explication : une mauvaise restauration introduit des conflits de réplication.

## 2. Production — Contrôles

Ne pas exécuter de séquences `ntdsutil`, `wbadmin` ou de registre copiées sans confirmer qu'elles correspondent au scénario et au DC concernés.

## 3. Production — Sécurité

- Réseau de reprise strictement isolé de la production.

## Validation et retour arrière

- **Validation** : les premiers DC démarrent en isolation avec AD DS fonctionnel.
- **Retour arrière** : recommencer la restauration depuis la sauvegarde; la production n'est pas touchée.

## Si le problème n'est pas résolu

- [Microsoft Learn — Reprise initiale d'une forêt AD](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-initial-recovery)
- [Microsoft Learn — Étapes de reprise d'une forêt AD](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-steps-for-restoring-the-forest)
- [Guide complet — étape 3](/02-fiches-completes/windows/server-2022/autres/26-reprise-foret-ad-ds-windows-server-2022#3-restaurer-les-premiers-controleurs-en-isolation)