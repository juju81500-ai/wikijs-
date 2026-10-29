# Fiche_Simple_-_Windows_Server_2025_Exchange_Server_Configurer_Connecteurs

- **Environnement** : Windows Server 2025 Standard ou Datacenter; Exchange Server Subscription Edition
- **OS / Version** : Windows Server 2025; Exchange SE — valider le build et les prérequis publiés avant intervention
- **Catégorie** : messagerie / flux de courrier

---

## Problème précis à résoudre

Configurer les flux entrants et sortants d’Exchange SE sur Windows Server 2025 en limitant le relais aux sources autorisées.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir le Centre d’administration Exchange (**EAC**) depuis le réseau d’administration, puis **Flux de courrier > Connecteurs**.
   👉 Explication : vérifier le nom des menus dans la version déployée; ne pas exposer l’EAC publiquement pour cette opération.

2. Créer ou modifier un connecteur de réception seulement pour les sources et usages requis, conformément à la documentation Microsoft.
   👉 Explication : ne pas activer un relais anonyme général; limiter les adresses IP et les autorisations au périmètre prévu.

3. Configurer le connecteur d’envoi vers la destination approuvée et documenter les domaines, DNS/MX et relais autorisés.
   👉 Explication : valider le routage avec les propriétaires DNS et messagerie avant une bascule.

4. Dans Exchange Management Shell, examiner les connecteurs configurés :
   ```powershell
   Get-ReceiveConnector | Format-Table Name,Bindings,RemoteIPRanges,PermissionGroups
   Get-SendConnector | Format-Table Name,AddressSpaces,SmartHosts,Enabled
   ```
   👉 Explication : ces commandes sont en lecture seule et permettent de contrôler les plages et destinations.

## 2. Production — Contrôles

Planifier une fenêtre de changement, sauvegarder les configurations concernées, vérifier l’état AD/DNS et Exchange, puis appliquer les étapes d’abord en environnement pilote.

## 3. Production — Sécurité

- Utiliser des comptes nominatifs et les rôles minimaux requis; retirer les privilèges temporaires après l’opération.
- Restreindre EAC et Exchange Management Shell au réseau d’administration.
- Ne pas consigner de mot de passe, clé privée, jeton ou donnée de boîte aux lettres dans cette fiche.

## Validation et retour arrière

**Validation** : les tests d’envoi/réception prévus fonctionnent; les files d’attente et journaux ne montrent pas de relais non autorisé.
- **Retour arrière** : restaurer la configuration précédente documentée du connecteur et refaire les tests de flux.

## Si le problème n’est pas résolu

- [Microsoft — Connecteurs de réception](https://learn.microsoft.com/en-us/exchange/mail-flow/connectors/receive-connectors)
- [Microsoft — Connecteurs d’envoi](https://learn.microsoft.com/en-us/exchange/mail-flow/connectors/send-connectors)
- [Fiche d’entrée Exchange Server](/01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-exchange-server)