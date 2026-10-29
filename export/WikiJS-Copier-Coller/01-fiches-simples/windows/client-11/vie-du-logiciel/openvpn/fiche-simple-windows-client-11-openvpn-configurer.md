# Fiche_Simple_-_Windows_Client_11_OpenVPN_Configurer

- **Environnement** : Poste Windows 11 (client OpenVPN Community)
- **OS / Version** : Windows 11; version du client à vérifier sur la page de téléchargement officielle
- **Catégorie** : OpenVPN Community client / configurer

---

## Problème précis à résoudre

Importer le profil fourni et le protéger.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : clic droit sur l'icône OpenVPN GUI > Importer un fichier > sélectionner NOM_PROFIL.ovpn.
   👉 Explication : NOM_PROFIL est le profil fourni (à remplacer). Le profil est copié dans le dossier de configuration de l'utilisateur.

2. Alternative en PowerShell élevé : copier le profil dans le dossier global :
   ```powershell
   Copy-Item .\NOM_PROFIL.ovpn 'C:\Program Files\OpenVPN\config\'
   Get-ChildItem 'C:\Program Files\OpenVPN\config'
   ```
   👉 Explication : Le dossier C:\Program Files\OpenVPN\config est lu par le client; l'écriture exige l'élévation.

3. Supprimer la copie de téléchargement du profil :
   ```powershell
   Remove-Item .\NOM_PROFIL.ovpn
   ```
   👉 Explication : Ne laisser aucune copie non protégée dans Téléchargements.

## 2. Production — Contrôles

Vérifier que la directive remote pointe vers le serveur approuvé (SERVER_FQDN).

## 3. Production — Sécurité

- Si la clé privée est protégée par une phrase de passe, la saisir à la connexion; ne jamais l'écrire dans le profil.

## Validation et retour arrière

- **Validation** : Le profil apparaît dans le menu de l'icône OpenVPN GUI.
- **Retour arrière** : Supprimer le profil importé du dossier config.

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-securiser)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-openvpn)
- [OpenVPN Community — téléchargements officiels](https://openvpn.net/community-downloads/)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)