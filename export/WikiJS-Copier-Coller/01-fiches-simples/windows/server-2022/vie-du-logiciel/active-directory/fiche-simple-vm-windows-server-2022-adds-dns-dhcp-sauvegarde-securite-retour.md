# Fiche_Simple_-_VM_Windows_Server_2022_ADDS_DNS_DHCP_Sauvegarde_Securite_Retour.md

- **Environnement** : VM ou serveur dédié Windows Server 2022, domaine de laboratoire ou d'entreprise
- **OS / Version** : Windows Server 2022; rôles AD DS, DNS et DHCP
- **Catégorie** : annuaire / services réseau

---

## Problème précis à résoudre

Protéger l'annuaire et prévoir la reprise.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder l'état système avec une solution compatible AD DS (ex. **Sauvegarde Windows Server**) et tester une restauration hors production.
   👉 Explication : une sauvegarde AD non testée n'est pas fiable.

2. Contrôler les membres des groupes privilégiés :
   ```powershell
   Get-ADGroupMember -Identity 'Domain Admins' | Select-Object Name, SamAccountName
   ```
   👉 Explication : la liste doit rester minimale; administrer avec des comptes séparés.

3. Restreindre les flux aux réseaux nécessaires avec le pare-feu.
   👉 Explication : LDAP, Kerberos, DNS et DHCP ne sont pas à exposer à Internet.

4. Conserver les journaux en cas d'échec de promotion et suivre la procédure de rétrogradation/nettoyage AD DS adaptée.
   👉 Explication : une promotion ne se défait pas par simple désinstallation de rôle.

## 2. Production — Contrôles

Protéger le mot de passe DSRM et planifier les sauvegardes.

## 3. Production — Sécurité

- Limiter les groupes privilégiés.
- Ne pas exposer les services AD à Internet.

## Validation et retour arrière

- **Validation** : Sauvegarde restaurable testée, groupes privilégiés revus.
- **Retour arrière** : Restaurer l'état système selon la procédure AD DS validée.

## Si le problème n'est pas résolu

- [Microsoft Learn — Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)
- [Microsoft Learn — Install-ADDSForest](https://learn.microsoft.com/en-us/powershell/module/addsdeployment/install-addsforest)
- [Guide complet AD DS, DNS et DHCP Windows Server 2022](/02-fiches-completes/windows/server-2022/installation-deploiement/01-active-directory-ds-dns-dhcp-windows-server-2022#5-sauvegarde-securite-et-retour-arriere)