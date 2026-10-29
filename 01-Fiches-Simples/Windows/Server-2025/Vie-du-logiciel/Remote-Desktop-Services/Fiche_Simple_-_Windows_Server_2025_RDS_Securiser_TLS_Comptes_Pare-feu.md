# Fiche_Simple_-_Windows_Server_2025_RDS_Securiser_TLS_Comptes_Pare-feu

- **Environnement** : Hôte de session RDS Windows Server 2025
- **OS / Version** : Windows Server 2025 Desktop Experience
- **Catégorie** : Vie du logiciel / Sécurité RDS (TLS, comptes, pare-feu)
- **Tags** : `windows-server-2025`, `rds`, `tls`, `nla`, `pare-feu`, `comptes`

---

## Problème précis à résoudre

Limiter l'exposition et les droits des connexions RDS : certificat TLS approuvé, NLA, groupe d'accès restreint et règle de pare-feu bornée.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier que NLA est exigée :
   ```powershell
   Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name UserAuthentication
   ```
   👉 Explication : La valeur 1 signifie que l'authentification au niveau du réseau est requise. GUI : **Gestionnaire de serveur** > **Serveur local** > **Bureau à distance** > case NLA.
2. Autoriser un groupe dédié plutôt que des comptes individuels :
   ```powershell
   Add-LocalGroupMember -Group 'Utilisateurs du Bureau à distance' -Member 'DOMAINE\GROUPE_RDS'
   Get-LocalGroupMember -Group 'Utilisateurs du Bureau à distance'
   ```
   👉 Explication : DOMAINE et GROUPE_RDS sont à remplacer par le domaine et le groupe approuvé; le nom du groupe local est `Remote Desktop Users` sur un système en anglais. GUI : **Propriétés système** > **Utilisation à distance** > **Sélectionner des utilisateurs**.
3. Importer le certificat TLS de l'organisation (déploiement avec Broker), le mot de passe du PFX étant saisi à l'invite :
   ```powershell
   $MdpPfx = Read-Host 'Mot de passe du PFX' -AsSecureString
   Set-RDCertificate -Role RDRedirector -ImportPath CHEMIN_PFX -Password $MdpPfx -ConnectionBroker NOM_BROKER -Force
   Get-RDCertificate -ConnectionBroker NOM_BROKER
   ```
   👉 Explication : CHEMIN_PFX (fichier PFX émis par l'AC interne ou publique) et NOM_BROKER sont à remplacer; répéter pour les rôles `RDPublishing`, `RDWebAccess` et `RDGateway` si présents. GUI : **Services Bureau à distance** > **Vue d'ensemble** > **Tâches** > **Modifier les propriétés de déploiement** > **Certificats**.
4. Contrôler les règles de pare-feu RDP (noms selon la langue) :
   ```powershell
   Get-NetFirewallRule -DisplayGroup 'Bureau à distance' -ErrorAction SilentlyContinue | Select-Object DisplayName, Enabled, Profile
   Get-NetFirewallRule -DisplayGroup 'Remote Desktop' -ErrorAction SilentlyContinue | Select-Object DisplayName, Enabled, Profile
   ```
   👉 Explication : Examine les règles actives; dans `wf.msc` > règle RDP > **Propriétés** > **Étendue**, limiter les adresses distantes au sous-réseau SOUS_RESEAU_ADMIN (à remplacer par le réseau d'administration approuvé).

## 2. Production — Contrôles

- Utiliser RD Gateway ou un VPN approuvé; vérifier NLA, certificat, correctifs, groupes et journaux.
- Auditer l'appartenance au groupe d'accès et les verrouillages de compte via la stratégie du domaine.
- Tester depuis un poste hors périmètre : la connexion doit échouer.

## 3. Production — Sécurité

- Ne jamais exposer TCP/UDP 3389 directement sur Internet.
- Aucun mot de passe de PFX ou de compte dans les scripts; saisie à l'invite ou coffre.
- Aucun compte administrateur partagé; comptes nominatifs et journalisés.

## Validation et retour arrière

- **Validation** : connexion pilote réussie depuis le réseau autorisé, NLA exigée, échec hors périmètre, certificat sans avertissement.
- **Retour arrière** : conserver l'accès console; réimporter l'ancien certificat, rétablir les règles et groupes précédents puis retester.

## Si le problème n'est pas résolu

- [Microsoft Learn — Sécuriser le déploiement RDS](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-security-guidance)
- [Installer et configurer RDS 2025](./Fiche_Simple_-_Windows_Server_2025_RDS_Installer_Configurer.md)
- [Valider la recette](./Fiche_Simple_-_Windows_Server_2025_RDS_Valider_Recette.md)
- [Équivalent Windows Server 2022](../../../Server-2022/Vie-du-logiciel/Remote-Desktop-Services/Fiche_Simple_-_Windows_Server_2022_RDS_Securiser_Acces.md)
