# Fiche_Simple_-_Windows_Server_2025_Exchange_Server_Mise_A_Jour_CU

- **Environnement** : Windows Server 2025 Standard ou Datacenter; Exchange Server Subscription Edition
- **OS / Version** : Windows Server 2025; Exchange SE — valider le build et les prérequis publiés avant intervention
- **Catégorie** : messagerie / maintenance
- **Tags** : `windows-server-2025`, `exchange-server-se`, `messagerie`, `mise-a-jour-cu`

---

## Problème précis à résoudre

Planifier et valider l’application d’une mise à jour cumulative (CU) ou de sécurité (SU) Exchange SE sur Windows Server 2025.

## 1. Hors-Production (Lab / Test / POC)

1. Relever le build Exchange SE installé :
   ```powershell
   Get-ExchangeServer | Format-Table Name,Edition,AdminDisplayVersion
   ```
   👉 Explication : identifier précisément le point de départ avant de choisir un paquet de mise à jour.

2. Vérifier la page Microsoft des versions, builds et mises à jour publiées; sélectionner uniquement le paquet applicable à la version installée.
   👉 Explication : vérifier les notes, prérequis, ordre d’installation et éventuelles opérations de schéma avant toute mise à jour.

3. Réaliser une sauvegarde vérifiée, confirmer l’état sain des bases et planifier une fenêtre de maintenance avec une possibilité de restauration.
   👉 Explication : ne pas commencer une mise à jour Exchange avec une copie de base dégradée ou une sauvegarde non vérifiée.

4. Installer la CU/SU à l’aide de la méthode Microsoft propre à ce paquet et suivre les contrôles post-installation documentés.
   👉 Explication : cette fiche n’invente pas de commande d’installation; options et redémarrages varient selon le paquet.

5. Comparer à nouveau le build et exécuter les contrôles de service et de flux de courrier après maintenance.

## 2. Production — Contrôles

Planifier une fenêtre de changement, sauvegarder les configurations concernées, vérifier l’état AD/DNS et Exchange, puis appliquer les étapes d’abord en environnement pilote.

## 3. Production — Sécurité

- Utiliser des comptes nominatifs et les rôles minimaux requis; retirer les privilèges temporaires après l’opération.
- Restreindre EAC et Exchange Management Shell au réseau d’administration.
- Ne pas consigner de mot de passe, clé privée, jeton ou donnée de boîte aux lettres dans cette fiche.

## Validation et retour arrière

**Validation** : build attendu visible, services, bases, connecteurs et tests de messagerie sains; consigner les journaux d’installation.
- **Retour arrière** : utiliser uniquement le plan de restauration Microsoft/organisation préparé pour cette CU/SU; ne pas tenter un downgrade non documenté.

## Si le problème n’est pas résolu

- [Microsoft — Versions et builds Exchange](https://learn.microsoft.com/en-us/exchange/new-features/build-numbers-and-release-dates)
- [Microsoft — Matrice de support](https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix)
- [Fiche d’entrée Exchange Server](../../../../Logiciels/12-Messagerie-et-collaboratif/Fiche_Logiciel_-_Exchange-Server.md)
