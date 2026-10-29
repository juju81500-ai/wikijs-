# Fiche_Simple_-_Windows_Server_2025_Exchange_Server_Installer

- **Environnement** : Windows Server 2025 Standard ou Datacenter; Exchange Server Subscription Edition
- **OS / Version** : Windows Server 2025; Exchange SE — valider le build et les prérequis publiés avant intervention
- **Catégorie** : messagerie / installation
- **Tags** : `windows-server-2025`, `exchange-server-se`, `messagerie`, `installer`

---

## Problème précis à résoudre

Déployer Exchange Server Subscription Edition sur un serveur Windows Server 2025 admissible, sans appliquer de procédure Exchange 2019 non vérifiée.

## 1. Hors-Production (Lab / Test / POC)

1. Avant l’installation, terminer les contrôles de la fiche [prérequis et limites](Fiche_Simple_-_Windows_Server_2025_Exchange_Server_Prerequis_Limites.md), dont l’exigence Windows Server 2025 sur le Schema Master avant PrepareAD.
   👉 Explication : la préparation Active Directory est une modification durable; elle doit être planifiée et validée avant le serveur Exchange.

2. Télécharger le média Exchange SE depuis les pages Microsoft officielles et suivre la procédure de nouveau déploiement publiée pour la version visée.
   👉 Explication : ne pas utiliser un média Exchange 2019/2016 ni une commande copiée d’une version/CU différente.

3. Préparer le schéma, l’organisation et les domaines uniquement selon le parcours de déploiement Microsoft, avec les comptes et rôles AD requis.
   👉 Explication : faire ces opérations depuis le site AD approprié, après sauvegarde de l’annuaire et réplication saine.

4. Installer le rôle Mailbox en utilisant l’assistant ou les commandes explicitement documentées pour le média SE courant; vérifier les prérequis de l’assistant avant de poursuivre.
   👉 Explication : les options et composants dépendent du média et du niveau de mise à jour; aucune ligne d’installation non vérifiée n’est proposée ici.

5. Après redémarrage, ouvrir Exchange Management Shell et contrôler l’instance :
   ```powershell
   Get-ExchangeServer | Format-List Name,Edition,AdminDisplayVersion
   ```
   👉 Explication : confirme le nom, l’édition et le build remontés par Exchange.

## 2. Production — Contrôles

Planifier une fenêtre de changement, sauvegarder les configurations concernées, vérifier l’état AD/DNS et Exchange, puis appliquer les étapes d’abord en environnement pilote.

## 3. Production — Sécurité

- Utiliser des comptes nominatifs et les rôles minimaux requis; retirer les privilèges temporaires après l’opération.
- Restreindre EAC et Exchange Management Shell au réseau d’administration.
- Ne pas consigner de mot de passe, clé privée, jeton ou donnée de boîte aux lettres dans cette fiche.

## Validation et retour arrière

**Validation** : l’installation termine sans échec, le serveur Exchange SE apparaît dans la configuration et l’EAC est accessible depuis le réseau d’administration.
- **Retour arrière** : avant la mise en service, suivre le plan de retour arrière du changement; la désinstallation ne retire pas les extensions déjà apportées à Active Directory.

## Si le problème n’est pas résolu

- [Prérequis Exchange SE](https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites)
- [Déploiement Exchange](https://learn.microsoft.com/en-us/exchange/plan-and-deploy/deploy-new-installations/deploy-new-installations)
- [Fiche d’entrée Exchange Server](../../../../Logiciels/12-Messagerie-et-collaboratif/Fiche_Logiciel_-_Exchange-Server.md)
