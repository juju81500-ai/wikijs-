# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_27_Durcissement_De_L_Acces

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 27 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2025`, `vie-du-systeme`, `cycle-de-vie`, `etape-27`

---

## Problème précis à résoudre

Restreindre qui peut se connecter à distance et comment.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Propriétés système > Utilisation à distance > Sélectionner des utilisateurs** pour définir les membres autorisés.
   ```powershell
   Add-LocalGroupMember -Group 'Utilisateurs du Bureau à distance' -Member ADMIN_NOMINATIF
   Get-LocalGroupMember -Group 'Utilisateurs du Bureau à distance'
   ```
   👉 Explication : seuls les comptes listés se connectent; le groupe est `Remote Desktop Users` en anglais.

2. Limiter la source des connexions RDP (remplacer `IP_ADMIN` par l'adresse ou le sous-réseau d'administration) :
   ```powershell
   Set-NetFirewallRule -DisplayGroup 'Bureau à distance' -RemoteAddress IP_ADMIN
   ```
   👉 Explication : les règles RDP n'acceptent plus que cette source.

3. Limiter les sessions inactives (**gpedit.msc > Modèles d'administration > Composants Windows > Services Bureau à distance > Hôte de session > Limites de session**) :
   ```powershell
   Set-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services' MaxIdleTime 900000 -ErrorAction SilentlyContinue
   ```
   👉 Explication : déconnecte après 15 minutes d'inactivité (valeur en millisecondes); créer la clé si elle n'existe pas.

## 2. Production — Contrôles

Appliquer ces réglages par GPO sur l'ensemble des serveurs.

## 3. Production — Sécurité

Couper le RDP quand il n'est pas nécessaire.

## Validation et retour arrière

- **Validation** : Un compte non autorisé est refusé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2025](./Sommaire_-_Vie_du_systeme_Windows_Server_2025.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
