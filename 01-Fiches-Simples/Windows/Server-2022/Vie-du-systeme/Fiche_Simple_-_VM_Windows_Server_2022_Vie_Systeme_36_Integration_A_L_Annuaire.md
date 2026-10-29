# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_36_Integration_A_L_Annuaire

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 36 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-36`

---

## Problème précis à résoudre

Joindre le serveur au domaine Active Directory.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Gestionnaire de serveur > Serveur local > Groupe de travail > Modifier > Membre d'un domaine**.
   ```powershell
   Add-Computer -DomainName EXEMPLE.LOCAL -OUPath 'OU=Serveurs,DC=EXEMPLE,DC=LOCAL' -Credential (Get-Credential) -Restart
   ```
   👉 Explication : `EXEMPLE.LOCAL` est le domaine; le compte demandé doit avoir le droit de joindre des machines; le DNS du serveur doit pointer vers un contrôleur de domaine.

2. Après redémarrage, contrôler l'appartenance :
   ```powershell
   (Get-CimInstance Win32_ComputerSystem).Domain
   Test-ComputerSecureChannel -Verbose
   ```
   👉 Explication : confirme le domaine et le canal sécurisé.

3. Appliquer les stratégies et valider :
   ```powershell
   gpupdate /force
   gpresult /r
   ```
   👉 Explication : télécharge et affiche les GPO appliquées.

## 2. Production — Contrôles

Placer le serveur dans l'OU adaptée et gérer le mot de passe administrateur par Windows LAPS.

## 3. Production — Sécurité

Utiliser un compte de jonction délégué, pas Administrateur du domaine.

## Validation et retour arrière

- **Validation** : `Test-ComputerSecureChannel` renvoie `True`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Windows Server 2022 ADDS Joindre ou Sortir Do](<../Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_ADDS_Joindre_ou_Sortir_Do.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2022](./Sommaire_-_Vie_du_systeme_Windows_Server_2022.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
