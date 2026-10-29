# Fiche_Simple_-_Windows_Server_2022_MECM_Securisation

- **Environnement** : Windows Server 2022, site primaire MECM/SCCM en service
- **OS / Version** : Windows Server 2022; Configuration Manager : vérifier la version publiée
- **Catégorie** : Automatisation, déploiement et IaC

---

## Problème précis à résoudre

Réduire la surface d'attaque d'un site MECM/SCCM : administration déléguée (RBAC), comptes à moindre privilège, communications chiffrées, pare-feu.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les administrateurs et rôles de sécurité. GUI : `Administration > Sécurité > Utilisateurs administratifs`.
   ```powershell
   Get-CMAdministrativeUser | Select-Object LogonName, RoleNames
   Get-CMSecurityRole | Select-Object RoleName
   ```
   👉 Explication : on identifie qui a le rôle « Full Administrator ». Ce rôle doit rester limité à très peu de comptes.

2. Ajouter un administrateur délégué avec un rôle restreint (à remplacer) :
   ```powershell
   New-CMAdministrativeUser -Name "DOMAINE\GROUPE-ADMIN-DEPLOIEMENT" -RoleName "Application Administrator" -CollectionName "COLLECTION-TEST"
   ```
   👉 Explication : on délègue à un groupe AD, limité à une collection. Le nom du rôle est celui de la console (langue à vérifier).

3. Contrôler le mode de communication. GUI : `Administration > Configuration du site > Sites > Propriétés > Sécurité des communications`.
   👉 Explication : choisir « HTTPS ou HTTP amélioré » (Enhanced HTTP) plutôt que HTTP seul; l'HTTPS complet exige une PKI et des certificats : vérifier la version publiée et la documentation PKI.

4. Contrôler les comptes configurés (accès réseau, push client). GUI : `Administration > Configuration du site > Sites > Paramètres du site > Configurer les composants du site`.
   👉 Explication : supprimer les comptes inutiles; aucun compte ne doit être administrateur de domaine.

5. Contrôler le pare-feu du serveur de site :
   ```powershell
   Get-NetFirewallProfile | Select-Object Name, Enabled
   Get-NetFirewallRule -Enabled True -Direction Inbound | Where-Object DisplayName -like "*SMS*" | Select-Object DisplayName, Profile
   ```
   👉 Explication : le pare-feu doit être actif; ouvrir seulement les ports requis par les rôles installés (vérifier la page Microsoft « Ports used » de la version).

## 2. Production — Contrôles

Revue trimestrielle des administrateurs, comptes et rôles; relever les écarts au référentiel de sécurité de l'entreprise.

## 3. Production — Sécurité

- Journaliser les actions d'administration (`Surveillance > Messages d'état` et audit).
- Mots de passe de comptes de service dans un coffre-fort, jamais dans les fiches.
- Console installée uniquement sur des postes d'administration dédiés.

## Validation et retour arrière

- **Validation** : seuls les groupes prévus ont un rôle; communication HTTPS/HTTP amélioré; pare-feu actif.
- **Retour arrière** : `Remove-CMAdministrativeUser -Name "DOMAINE\GROUPE-ADMIN-DEPLOIEMENT"`; rétablir l'ancien mode de communication via les propriétés du site; en dernier recours, restaurer la sauvegarde de site.

## Si le problème n'est pas résolu

- [Fiche d'entrée MECM/SCCM](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-microsoft-mecm-sccm)
- [Microsoft Learn — Bonnes pratiques de sécurité](https://learn.microsoft.com/en-us/intune/configmgr/core/plan-design/hierarchy/best-practices-for-security)
- [Microsoft Learn — Administration basée sur les rôles](https://learn.microsoft.com/en-us/intune/configmgr/core/understand/fundamentals-of-role-based-administration)