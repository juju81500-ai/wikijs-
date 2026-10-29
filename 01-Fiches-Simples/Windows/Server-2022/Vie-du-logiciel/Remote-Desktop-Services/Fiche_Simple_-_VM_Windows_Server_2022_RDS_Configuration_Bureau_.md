# Fiche_Simple_-_VM_Windows_Server_2022_RDS_Configuration_Bureau_

- **Environnement** : Hôte de session Windows Server 2022 et poste d'administration autorisé
- **OS / Version** : Windows Server 2022 Desktop Experience
- **Catégorie** : Vie du logiciel / Configuration des accès RDS
- **Tags** : `windows-server-2022`, `rds`, `groupes`, `pare-feu`, `powershell`

---

## Problème précis à résoudre

Limiter les connexions RDP aux utilisateurs et adresses réseau approuvés sans modifier inutilement le port RDP par défaut.

## 1. Hors-Production (Lab / Test / POC)

1. Dans **Paramètres système avancés** > **Utilisation à distance** > **Sélectionner des utilisateurs**, ajouter uniquement un groupe de lab autorisé.
   👉 Explication : Les administrateurs sont déjà autorisés par défaut; n'ajouter que les comptes ou groupes nécessaires.
2. Équivalent PowerShell :
   ```powershell
   $rdpGroup = Get-LocalGroup -SID 'S-1-5-32-555'
   Add-LocalGroupMember -Group $rdpGroup.Name -Member 'LAB\GRP_RDS_ACCESS'
   Get-LocalGroupMember -Group $rdpGroup.Name
   ```
   👉 Explication : Le SID identifie le groupe local « Utilisateurs du Bureau à distance » indépendamment de la langue; `LAB\GRP_RDS_ACCESS` est un exemple à remplacer par le groupe autorisé.
3. Dans `wf.msc` > **Règles de trafic entrant** > règles Bureau à distance > **Propriétés** > **Étendue**, limiter les adresses distantes au réseau d'administration.
   👉 Explication : Le sous-réseau est à remplacer par le réseau de lab approuvé. Ne pas ouvrir les règles vers Internet.
4. Vérifier les réglages RDP/NLA :
   ```powershell
   Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server' -Name fDenyTSConnections
   Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name UserAuthentication
   ```
   👉 Explication : RDP doit être activé (`fDenyTSConnections` à 0) et NLA exigé (`UserAuthentication` à 1).

## 2. Production — Contrôles

- Piloter les changements sur un seul serveur et confirmer les membres du groupe avec le propriétaire métier.
- Garder un compte administrateur de secours contrôlé et un accès console hors bande.
- Si le serveur appartient à un déploiement RDS complet, configurer collection, droits et certificats dans les outils du déploiement plutôt que modifier localement sans coordination.

## 3. Production — Sécurité

- Préférer VPN/RD Gateway approuvée, NLA, certificat TLS valide et filtrage réseau par source.
- Ne pas compter sur le changement du port 3389 pour protéger le service; il ne remplace pas les contrôles d'accès.
- Ne pas ajouter des utilisateurs au groupe Administrateurs pour leur donner seulement le droit RDP.

## Validation et retour arrière

- **Validation** : le groupe pilote se connecte depuis le réseau prévu; un compte et une adresse hors périmètre sont refusés.
- **Retour arrière** : retirer le groupe ajouté avec `Remove-LocalGroupMember -Group $rdpGroup.Name -Member 'LAB\GRP_RDS_ACCESS'` (valeur à remplacer) puis rétablir les adresses de pare-feu précédentes.

## Si le problème n'est pas résolu

- [Microsoft Learn — Autoriser l'accès au Bureau à distance](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remotepc/remote-desktop-allow-access)
- [Microsoft Learn — Sécurité RDS](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-security)
- [Activer le Bureau à distance](./Fiche_Simple_-_VM_Windows_Server_2022_RDS_Activer_Bureau_a_Dist.md)
