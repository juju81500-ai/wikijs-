# Fiche_Simple_-_Cloud_Entra_ID_Connect_Health

- **Environnement** : Tenant Microsoft Entra ID (SaaS), poste d'administration avec PowerShell 7 et modules Microsoft.Graph
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer ; licences et fonctions à vérifier)
- **Catégorie** : systèmes, annuaires et services

---

## Problème précis à résoudre

Superviser la synchronisation avec Microsoft Entra Connect Health et détecter les erreurs.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les licences requises pour Connect Health (offre, nombre d'utilisateurs) dans Microsoft Learn avant déploiement.
   👉 Explication : licence à vérifier ; ne pas supposer qu'elle est incluse.

2. Portail : Microsoft Entra admin center → Entra ID → Entra Connect → Connect Health → Sync errors / Sync services.
   👉 Explication : les libellés évoluent ; se référer à la documentation Connect Health.

3. Installer l'agent Health sur le serveur selon la page Learn et vérifier les URL sortantes autorisées.
   👉 Explication : l'agent peut être inclus avec l'installation d'Entra Connect, sinon suivre la procédure officielle.

4. Configurer les alertes e-mail vers une boîte de groupe (EMAIL_SUPERVISION à remplacer).
   👉 Explication : éviter les boîtes personnelles.

5. Compléter côté Graph pour l'état de synchronisation des comptes :
   ```powershell
   Connect-MgGraph -Scopes 'User.Read.All' -ContextScope Process
   Get-MgUser -Filter 'onPremisesSyncEnabled eq true' -ConsistencyLevel eventual -CountVariable n -Top 5 -Property DisplayName,OnPremisesLastSyncDateTime
   $n
   ```
   👉 Explication : contrôle ponctuel de la dernière synchronisation ; la requête avancée exige `ConsistencyLevel`.

## 2. Production — Contrôles

Production : alertes routées vers le support, revue hebdomadaire des erreurs, journaux conservés selon la politique, seuils documentés.

## 3. Production — Sécurité

- Limiter le rôle de lecture Health aux exploitants.
- Ne pas transmettre les rapports contenant des identifiants d'utilisateurs hors périmètre.

## Validation et retour arrière

- **Validation** : la ressource affiche un état sain et la date de dernière synchronisation est récente.
- **Retour arrière** : désinstaller l'agent Health selon la procédure officielle ; aucune incidence sur la synchronisation.

## Si le problème n'est pas résolu

- [Entra Connect Health](https://learn.microsoft.com/entra/identity/hybrid/)
- [Documentation Microsoft Entra ID](https://learn.microsoft.com/entra/identity/)
- [Fiche d'entrée Microsoft Entra ID](/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-microsoft-entra-id)