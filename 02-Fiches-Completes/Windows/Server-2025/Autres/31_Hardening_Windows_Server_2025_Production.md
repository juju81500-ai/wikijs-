# Hardening de Windows Server 2025 avant production

- **Type de fiche** : Autres — sécurité / compatibilité
- **Environnement** : Serveur membre ou contrôleur de domaine en laboratoire avant déploiement
- **OS / Version** : Windows Server 2025 Standard ou Datacenter
- **Rôle** : Vérifier les nouveaux comportements de sécurité et éviter les régressions de compatibilité
- **Tags** : `windows-server-2025`, `hardening`, `smb`, `ldap`, `openssh`, `securite`

## 1. Préparer la baseline

Fiche simple : [préparer la baseline de hardening](../../../../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiches-par-theme/Hardening/Fiche_Simple_-_VM_Windows_Server_2025_Hardening_Preparer_Baseline.md).

Inventorier le rôle, les clients, NAS, applications, mécanismes LDAP/SMB, outils de sauvegarde et dépendances d'authentification. Déployer d'abord en laboratoire représentatif. Ne pas désactiver une protection nouvelle pour résoudre une incompatibilité sans analyse et dérogation formelle.

Appliquer une baseline Microsoft adaptée au rôle, conserver un compte de secours testé et vérifier la restauration avant les changements de politique.

## 2. Vérifier SMB et les équipements tiers

Fiche simple : [vérifier SMB et les équipements tiers](../../../../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiches-par-theme/Hardening/Fiche_Simple_-_VM_Windows_Server_2025_Hardening_SMB_Equipements_Tiers.md).

Server 2025 renforce les valeurs par défaut SMB, notamment la signature sortante et le chiffrement des connexions clientes. Inventorier et tester clients, NAS et appliances avant migration; utiliser les événements d'audit de compatibilité lorsqu'ils sont disponibles.

```powershell
Get-SmbClientConfiguration
Get-SmbServerConfiguration
Get-SmbConnection
```

Confirmer que les partages nécessaires négocient un dialecte moderne et que les contrôles de signature/chiffrement correspondent à la politique. Ne pas réactiver SMB1 pour contourner un matériel obsolète.

## 3. Vérifier LDAP et AD DS

Fiche simple : [vérifier LDAP et AD DS](../../../../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiches-par-theme/Hardening/Fiche_Simple_-_VM_Windows_Server_2025_Hardening_LDAP_AD_DS.md).

Pour une nouvelle forêt AD DS, vérifier la compatibilité des applications avec la signature LDAP appliquée par défaut pour les clients SASL. Auditer d'abord les événements et les clients concernés, migrer les applications vers des connexions sécurisées, puis contrôler l'authentification et la réplication.

Ne pas activer les nouvelles options AD DS, notamment la taille de page ESE 32K ou le niveau fonctionnel 2025, sans plan de compatibilité et validation de tous les contrôleurs de domaine.

## 4. Réduire les accès d'administration

Fiche simple : [réduire les accès d'administration](../../../../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiches-par-theme/Hardening/Fiche_Simple_-_VM_Windows_Server_2025_Hardening_Reduire_Acces_Administration.md).

- Vérifier que `sshd` n'écoute pas ou n'accepte pas de connexions non requises; filtrer au réseau d'administration si SSH est utilisé.
- Conserver WinRM/RDP seulement selon le modèle d'administration retenu, avec NLA, pare-feu à portée limitée et comptes dédiés.
- Utiliser Windows LAPS et des comptes nominatifs; retirer les rôles locaux non requis.
- Examiner Credential Guard, VBS, Secure Boot et Microsoft Defender selon la compatibilité du rôle.

```powershell
Get-Service sshd -ErrorAction SilentlyContinue
Get-NetFirewallProfile | Select-Object Name, Enabled
Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled
```

## 5. Mises à jour et audit

Fiche simple : [mises à jour et audit](../../../../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiches-par-theme/Hardening/Fiche_Simple_-_VM_Windows_Server_2025_Hardening_Mises_A_Jour_Audit.md).

Gérer les mises à jour via le mécanisme de parc, tester les mises à jour sur un groupe pilote et planifier les redémarrages. Centraliser événements sécurité, Defender, SMB et AD DS; vérifier que l'heure et la rétention des journaux sont conformes.

## 6. Validation et retour arrière

Fiche simple : [validation et retour arrière du hardening](../../../../01-Fiches-Simples/Windows/Server-2025/Vie-du-systeme/Fiches-par-theme/Hardening/Fiche_Simple_-_VM_Windows_Server_2025_Hardening_Validation_Retour_Arriere.md).

Tester authentification, SMB, LDAP, sauvegarde, applications, gestion à distance et redémarrage depuis des clients représentatifs. Conserver les stratégies précédentes et procéder par changements réversibles; toute exception doit être limitée, documentée, datée et revue.

## Sources

- [Microsoft Learn — Nouveautés de Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
- [Microsoft Learn — Sécuriser le trafic SMB](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)
- [Microsoft Learn — Signature LDAP pour AD DS](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/ldap-signing)
- [Microsoft Learn — OpenSSH pour Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_overview)