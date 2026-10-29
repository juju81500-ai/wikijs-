# Fiche_Simple_-_Windows_Server_2022_RDS_Valider_Recette

- **Environnement** : Pilote RDS isolé et poste client de test autorisé
- **OS / Version** : Windows Server 2022 et client Windows pris en charge
- **Catégorie** : Vie du logiciel / Validation RDS
- **Tags** : `windows-server-2022`, `rds`, `recette`, `validation`

---

## Problème précis à résoudre

Vérifier le chemin d'accès, les droits, la collection et les licences avant la mise en service des utilisateurs.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le rôle, service et écoute locale :
   ```powershell
   Get-WindowsFeature RDS-RD-Server
   Get-Service TermService
   Get-NetTCPConnection -State Listen -LocalPort 3389 -ErrorAction SilentlyContinue
   ```
   👉 Explication : Confirme que le rôle est installé, que le service est actif et qu'un socket écoute; ne prouve pas l'accessibilité de bout en bout.
2. Depuis le client du lab, tester le nom DNS et le port :
   ```powershell
   Resolve-DnsName RDS-HOTE.FQDN
   Test-NetConnection -ComputerName RDS-HOTE.FQDN -Port 3389
   ```
   👉 Explication : `RDS-HOTE.FQDN` est un placeholder à remplacer par le nom réel du pilote; un test de port ne valide pas l'authentification, les CAL ni une collection.
3. Lancer **Connexion Bureau à distance** (`mstsc`), saisir le nom publié ou la passerelle approuvée, puis tester un compte pilote autorisé.
   👉 Explication : Valide l'expérience réelle du client et le chemin d'authentification du lab.
4. Dans **Gestionnaire de serveur** > **Services Bureau à distance** > **Collections**, vérifier la collection et les groupes autorisés.
   👉 Explication : Confirme la cible et l'affectation des utilisateurs au pilote.

## 2. Production — Contrôles

- Vérifier les rapports de licences dans **Gestionnaire de licences Bureau à distance** et l'absence d'alerte de période de grâce.
- Consulter **Observateur d'événements** > **Journaux des applications et des services** > **Microsoft** > **Windows** > **TerminalServices**; les journaux disponibles varient par rôle.
- Faire signer la recette par le propriétaire du service avant élargissement.

## 3. Production — Sécurité

- Répéter les essais depuis un poste hors périmètre et confirmer le refus d'accès.
- Ne pas utiliser un compte administrateur quotidien comme compte utilisateur pilote.
- Vérifier les redirections de presse-papiers, disques et périphériques.

## Validation et retour arrière

- **Validation** : connexion autorisée réussie, droits et applications conformes, licences disponibles, accès hors périmètre refusé.
- **Retour arrière** : suspendre l'ouverture aux utilisateurs, retirer l'affectation pilote et rétablir les règles réseau précédentes.

## Si le problème n'est pas résolu

- [Microsoft Learn — Résoudre les problèmes RDS](https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/remote-desktop-services-troubleshoot)
- [Microsoft Learn — Licences des hôtes de session](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-license-session-hosts)
- [Sécuriser les accès RDS](./Fiche_Simple_-_Windows_Server_2022_RDS_Securiser_Acces.md)
