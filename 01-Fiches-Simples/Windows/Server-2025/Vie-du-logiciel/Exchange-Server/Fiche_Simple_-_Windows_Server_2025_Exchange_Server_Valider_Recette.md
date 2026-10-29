# Fiche_Simple_-_Windows_Server_2025_Exchange_Server_Valider_Recette

- **Environnement** : Windows Server 2025 Standard ou Datacenter; Exchange Server Subscription Edition
- **OS / Version** : Windows Server 2025; Exchange SE — valider le build et les prérequis publiés avant intervention
- **Catégorie** : messagerie / validation
- **Tags** : `windows-server-2025`, `exchange-server-se`, `messagerie`, `valider-recette`

---

## Problème précis à résoudre

Vérifier l’état des services, bases, files d’attente et flux de courrier après le déploiement Exchange SE.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter les contrôles de service depuis Exchange Management Shell :
   ```powershell
   Test-ServiceHealth
   ```
   👉 Explication : signale les services Exchange requis qui ne sont pas démarrés.

2. Vérifier les bases et les copies :
   ```powershell
   Get-MailboxDatabase -Status | Format-Table Name,Mounted,Server
   Get-MailboxDatabaseCopyStatus *
   ```
   👉 Explication : confirme que les bases prévues sont montées et que les copies attendues sont disponibles.

3. Envoyer un message de test entre boîtes aux lettres de recette puis vers/depuis un domaine externe approuvé; examiner les files :
   ```powershell
   Get-Queue | Format-Table Identity,Status,MessageCount,NextHopDomain
   ```
   👉 Explication : un test réel confirme le trajet complet, pas seulement la présence d’un service.

4. Consigner le résultat des contrôles dans la recette, sans y copier de message confidentiel ni d’identifiant.

## 2. Production — Contrôles

Planifier une fenêtre de changement, sauvegarder les configurations concernées, vérifier l’état AD/DNS et Exchange, puis appliquer les étapes d’abord en environnement pilote.

## 3. Production — Sécurité

- Utiliser des comptes nominatifs et les rôles minimaux requis; retirer les privilèges temporaires après l’opération.
- Restreindre EAC et Exchange Management Shell au réseau d’administration.
- Ne pas consigner de mot de passe, clé privée, jeton ou donnée de boîte aux lettres dans cette fiche.

## Validation et retour arrière

**Validation** : EAC accessible depuis le réseau prévu, services requis actifs, base(s) montée(s), flux internes/externes testés, alertes traitées.
- **Retour arrière** : si la recette échoue, suspendre la mise en service et appliquer le plan de changement approuvé.

## Si le problème n’est pas résolu

- [Microsoft — Déploiement Exchange](https://learn.microsoft.com/en-us/exchange/plan-and-deploy/deploy-new-installations/deploy-new-installations)
- [Microsoft — Matrice de support](https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix)
- [Fiche d’entrée Exchange Server](../../../../Logiciels/12-Messagerie-et-collaboratif/Fiche_Logiciel_-_Exchange-Server.md)
