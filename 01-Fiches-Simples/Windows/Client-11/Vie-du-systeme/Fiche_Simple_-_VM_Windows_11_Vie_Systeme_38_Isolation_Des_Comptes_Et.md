# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_38_Isolation_Des_Comptes_Et

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 38 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-38`

---

## Problème précis à résoudre

Faire tourner les services avec des comptes à moindres privilèges (gMSA ou comptes de service).

## 1. Hors-Production (Lab / Test / POC)

1. Lister les services et leurs comptes : **services.msc > propriétés > Connexion**.
   ```powershell
   Get-CimInstance Win32_Service | Where-Object StartName -notmatch 'LocalSystem|LocalService|NetworkService' | Select-Object Name,StartName,State
   ```
   👉 Explication : repère les services qui utilisent un compte nommé.

2. Préférer un compte de service géré (gMSA) quand l'annuaire le permet; sinon un compte local sans droit d'ouverture de session interactive.
   ```powershell
   Test-ADServiceAccount -Identity 'GMSA_SERVICE$'
   Set-Service -Name NOM_SERVICE -Credential (Get-Credential)
   ```
   👉 Explication : `GMSA_SERVICE$` est le compte géré fourni par l'équipe annuaire; la saisie reste interactive.

3. Retirer les droits superflus : **secpol.msc > Stratégies locales > Attribution des droits utilisateur > Interdire l'ouverture d'une session locale**.
   ```powershell
   secedit /export /cfg "$env:USERPROFILE\secpol.cfg" /areas USER_RIGHTS
   Select-String "$env:USERPROFILE\secpol.cfg" -Pattern 'SeDenyInteractiveLogonRight'
   ```
   👉 Explication : exporte et lit les droits d'ouverture de session.

4. Appliquer le durcissement d'un service (SID restreint).
   ```powershell
   sc.exe sidtype NOM_SERVICE restricted
   ```
   👉 Explication : limite l'accès du service aux seules ressources autorisées.

## 2. Production — Contrôles

Un compte par service, avec la liste des droits documentée.

## 3. Production — Sécurité

Aucun service applicatif en `LocalSystem` sans justification; mots de passe jamais stockés en clair.

## Validation et retour arrière

- **Validation** : Chaque service tourne avec le compte attendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 11](./Sommaire_-_Vie_du_systeme_Windows_11.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
