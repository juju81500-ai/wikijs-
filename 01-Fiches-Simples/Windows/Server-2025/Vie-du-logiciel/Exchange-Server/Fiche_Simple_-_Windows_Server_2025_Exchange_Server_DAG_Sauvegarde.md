# Fiche_Simple_-_Windows_Server_2025_Exchange_Server_DAG_Sauvegarde

- **Environnement** : Windows Server 2025 Standard ou Datacenter; Exchange Server Subscription Edition
- **OS / Version** : Windows Server 2025; Exchange SE — valider le build et les prérequis publiés avant intervention
- **Catégorie** : messagerie / haute disponibilité
- **Tags** : `windows-server-2025`, `exchange-server-se`, `messagerie`, `dag-sauvegarde`

---

## Problème précis à résoudre

Contrôler l’état d’un Database Availability Group (DAG) et préparer une sauvegarde cohérente des bases Exchange SE.

## 1. Hors-Production (Lab / Test / POC)

1. Définir les nœuds, réseaux, quorum, sites et réplication attendus dans le plan de haute disponibilité avant de créer un DAG.
   👉 Explication : le dimensionnement et la procédure dépendent de l’architecture; ne pas réutiliser une topologie de laboratoire en production.

2. Lire l’état d’un DAG et de ses copies depuis Exchange Management Shell :
   ```powershell
   Get-DatabaseAvailabilityGroup -Status
   Get-MailboxDatabaseCopyStatus *
   ```
   👉 Explication : les commandes sont en lecture seule; investiguer toute copie non saine avant de modifier le cluster.

3. Choisir un logiciel ou une méthode de sauvegarde explicitement compatible avec Exchange SE et ses mécanismes de sauvegarde applicative.
   👉 Explication : une copie de fichiers ou un snapshot de stockage non coordonné ne remplace pas une sauvegarde Exchange cohérente.

4. Effectuer un test de restauration documenté dans un environnement isolé avant toute activation de production.
   👉 Explication : une sauvegarde n’est utile que si la restauration est testée et que les objectifs de reprise sont vérifiés.

## 2. Production — Contrôles

Planifier une fenêtre de changement, sauvegarder les configurations concernées, vérifier l’état AD/DNS et Exchange, puis appliquer les étapes d’abord en environnement pilote.

## 3. Production — Sécurité

- Utiliser des comptes nominatifs et les rôles minimaux requis; retirer les privilèges temporaires après l’opération.
- Restreindre EAC et Exchange Management Shell au réseau d’administration.
- Ne pas consigner de mot de passe, clé privée, jeton ou donnée de boîte aux lettres dans cette fiche.

## Validation et retour arrière

**Validation** : copies saines, sauvegarde applicative complétée et restauration d’essai contrôlée.
- **Retour arrière** : ne pas supprimer un membre ou une copie de base avant un plan de retour validé; restaurer selon la procédure de l’outil de sauvegarde retenu.

## Si le problème n’est pas résolu

- [Microsoft — DAG](https://learn.microsoft.com/en-us/exchange/high-availability/database-availability-groups/database-availability-groups)
- [Microsoft — Sauvegarde/restauration](https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/disaster-recovery)
- [Fiche d’entrée Exchange Server](../../../../Logiciels/12-Messagerie-et-collaboratif/Fiche_Logiciel_-_Exchange-Server.md)
