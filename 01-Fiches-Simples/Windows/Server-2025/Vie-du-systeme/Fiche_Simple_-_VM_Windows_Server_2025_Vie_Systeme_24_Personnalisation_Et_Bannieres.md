# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_24_Personnalisation_Et_Bannieres

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 24 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2025`, `vie-du-systeme`, `cycle-de-vie`, `etape-24`

---

## Problème précis à résoudre

Afficher un avertissement légal à la connexion.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **gpedit.msc > Configuration ordinateur > Paramètres Windows > Paramètres de sécurité > Stratégies locales > Options de sécurité > Ouverture de session interactive : titre / texte du message**.
   ```powershell
   $k='HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System'
   Set-ItemProperty $k legalnoticecaption 'Accès restreint'
   Set-ItemProperty $k legalnoticetext 'Système réservé aux personnes autorisées. Les actions sont journalisées.'
   ```
   👉 Explication : affiche un avertissement avant l'ouverture de session (console et RDP).

2. Contrôler :
   ```powershell
   Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' | Select-Object legalnoticecaption, legalnoticetext
   ```
   👉 Explication : la valeur est enregistrée.

3. Déconnecter et reconnecter pour voir le message.
   👉 Explication : la bannière s'affiche avant la saisie des identifiants.

## 2. Production — Contrôles

Faire valider le texte par le juridique et l'appliquer par GPO en domaine.

## 3. Production — Sécurité

La bannière ne doit divulguer ni version ni rôle du serveur.

## Validation et retour arrière

- **Validation** : La bannière s'affiche à la connexion.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2025](./Sommaire_-_Vie_du_systeme_Windows_Server_2025.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
