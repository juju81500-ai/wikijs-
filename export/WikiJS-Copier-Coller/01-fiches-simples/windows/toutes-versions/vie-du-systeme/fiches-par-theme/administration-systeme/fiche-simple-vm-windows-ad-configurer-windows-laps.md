# 📄 Fiche_Simple_-_VM_Windows_AD_Configurer_Windows_LAPS.md

- **Environnement** : Domaine Active Directory avec postes Windows gérés
- **OS / Version** : Windows Server 2022 et clients Windows compatibles avec Windows LAPS et à jour
- **Catégorie** : Sécurité / Administration des postes

## 🎯 Problème précis à résoudre
Déployer Windows LAPS pour gérer le mot de passe d'un compte administrateur local, sauvegarder ce secret dans Active Directory et déléguer sa lecture à un groupe autorisé.

> Cette procédure concerne un domaine AD. Vérifier la compatibilité des versions et mises à jour des contrôleurs et clients avant déploiement. L'extension du schéma AD est une opération sensible et durable.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Dans un environnement de test, vérifier la présence du module LAPS :
   ```powershell
   Get-Module -ListAvailable LAPS
   Get-Command Update-LapsADSchema, Set-LapsADComputerSelfPermission, Set-LapsADReadPasswordPermission
   ```
2. Sur un contrôleur de schéma, avec un compte habilité et une sauvegarde AD validée, mettre à jour le schéma :
   ```powershell
   Update-LapsADSchema -Verbose
   ```
3. Déléguer l'écriture des objets ordinateur et la lecture des mots de passe à des groupes distincts :
   ```powershell
   Set-LapsADComputerSelfPermission -Identity "OU=Postes-Test,DC=corp,DC=example"
   Set-LapsADReadPasswordPermission -Identity "OU=Postes-Test,DC=corp,DC=example" -AllowedPrincipals "CORP\GG-LAPS-Readers"
   ```
   👉 *Explication : adapter le DN et les groupes. La mise à jour de schéma affecte la forêt et ne se traite pas comme un simple retour arrière de GPO.*

## ⚡ 2. Production — Façon Simplifiée
1. Tester d'abord sur une OU dédiée et un poste pilote; confirmer que les clients ont les mises à jour requises.
2. Dans la GPMC, créer une GPO liée à l'OU de test : **Configuration ordinateur > Stratégies > Modèles d'administration > Système > LAPS**.
3. Configurer la sauvegarde du mot de passe dans Active Directory, le compte local géré, la longueur/complexité et la durée de rotation selon la politique de l'organisation.
4. Appliquer la stratégie au poste pilote et vérifier la mise à jour sans afficher le mot de passe :
   ```powershell
   Invoke-LapsPolicyProcessing
   Get-LapsADPassword -Identity "PC-TEST01" | Select-Object ComputerName, PasswordUpdateTime, ExpirationTimestamp
   ```
   👉 *Explication : l'objet de vérification ne sélectionne pas le champ Password; la lecture du secret doit passer par le processus d'accès approuvé.*

## 🔒 3. Production — Façon Sécurisée
1. Déléguer l'accès en lecture et réinitialisation à des groupes séparés et audités; ne pas accorder la lecture à tous les administrateurs du domaine par défaut.
2. Éviter de lier la GPO à tout le domaine avant validation des permissions, de la récupération et du journal opérationnel LAPS.
3. Protéger les événements LAPS et contrôler régulièrement les comptes, ACL et accès au secret.

## ✅ Validation et retour arrière
- Confirmer que le poste reçoit la stratégie, que `PasswordUpdateTime` est récent et que l'événement LAPS indique une sauvegarde réussie.
- En cas d'échec, examiner **Observateur d'événements > Applications et services > Microsoft > Windows > LAPS > Operational**, la réplication AD et les permissions OU.
- Pour annuler le déploiement pilote, délier la GPO et retirer les délégations créées après vérification; traiter toute évolution du schéma selon le plan de changement AD.