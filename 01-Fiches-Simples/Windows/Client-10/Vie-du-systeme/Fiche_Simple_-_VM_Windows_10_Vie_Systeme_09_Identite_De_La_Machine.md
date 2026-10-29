# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_09_Identite_De_La_Machine

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 09 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows10`, `vie-du-systeme`, `cycle-de-vie`, `etape-09`

---

## Problème précis à résoudre

Nommer le poste selon la convention et le rattacher à l'annuaire (Active Directory ou Entra ID).

## 1. Hors-Production (Lab / Test / POC)

1. Renommer : **Paramètres > Système > À propos de > Renommer ce PC** (ou **Panneau de configuration > Système > Modifier les paramètres**). Le nom compte au plus 15 caractères, selon la convention (`PC-SITE-NUMERO`).
   ```powershell
   Rename-Computer -NewName 'NOM_POSTE' -Restart
   ```
   👉 Explication : applique le nouveau nom (`NOM_POSTE`, conforme à la convention de l'entreprise) et redémarre.

2. Joindre un domaine Active Directory : **Paramètres > Comptes > Accès Professionnel ou scolaire > Se connecter > Joindre cet appareil à un domaine Active Directory local**.
   ```powershell
   Add-Computer -DomainName 'DOMAINE.LOCAL' -OUPath 'OU=Postes,DC=DOMAINE,DC=LOCAL' -Credential (Get-Credential) -Restart
   ```
   👉 Explication : joint le poste (`DOMAINE.LOCAL` est le domaine, `OU=Postes,...` l'unité d'organisation cible); le mot de passe est saisi à l'invite, jamais écrit dans le script.

3. Variante Entra ID : **Paramètres > Comptes > Accès Professionnel ou scolaire > Se connecter > Joindre cet appareil à Microsoft Entra ID**, avec le compte de l'entreprise.
   ```powershell
   dsregcmd /status | Select-String 'AzureAdJoined|DomainJoined|TenantName'
   ```
   👉 Explication : `AzureAdJoined : YES` confirme la jonction; la jonction hybride combine les deux.

4. Vérifier l'enregistrement du poste dans l'annuaire.
   ```powershell
   (Get-CimInstance Win32_ComputerSystem) | Select-Object Name,Domain,PartOfDomain
   nltest /dsgetdc:DOMAINE.LOCAL
   ```
   👉 Explication : montre le nom, le domaine et le contrôleur de domaine contacté.

## 2. Production — Contrôles

Pré-créer le compte ordinateur dans la bonne unité d'organisation; en Intune, utiliser Autopilot pour enregistrer le poste.

## 3. Production — Sécurité

Jonction avec un compte délégué disposant de droits limités; ne jamais conserver le mot de passe dans un script.

## Validation et retour arrière

- **Validation** : `PartOfDomain : True` (ou `AzureAdJoined : YES`) et nom conforme.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 10](./Sommaire_-_Vie_du_systeme_Windows_10.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
