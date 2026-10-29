# Fiche_Simple_-_Windows_Client_11_OpenVPN_Installer

- **Environnement** : Poste Windows 11 (client OpenVPN Community)
- **OS / Version** : Windows 11; version du client à vérifier sur la page de téléchargement officielle
- **Catégorie** : OpenVPN Community client / installer
- **Tags** : `openvpn`, `windows11`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer le client OpenVPN Community depuis la source officielle.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : télécharger l'installateur MSI Windows 64 bits sur la page officielle des téléchargements, puis le lancer en administrateur (clic droit > Installer).
   👉 Explication : Utiliser uniquement openvpn.net; conserver la version choisie dans le ticket.

2. Vérifier l'empreinte du fichier puis installer en PowerShell élevé :
   ```powershell
   Get-FileHash -Algorithm SHA256 .\FICHIER_MSI
   msiexec /i .\FICHIER_MSI /qb
   ```
   👉 Explication : FICHIER_MSI est le nom du MSI téléchargé (à remplacer). Comparer l'empreinte à celle publiée par l'éditeur avant msiexec; /qb affiche une interface minimale.

3. Contrôler le service :
   ```powershell
   Get-Service | Where-Object { $_.Name -like '*OpenVPN*' }
   ```
   👉 Explication : Le service OpenVPN doit exister; l'icône OpenVPN GUI apparaît dans la zone de notification au premier lancement.

## 2. Production — Contrôles

Consigner la version installée (Paramètres > Applications > Applications installées).

## 3. Production — Sécurité

- Ne pas installer de pilote ou de client depuis un site tiers.

## Validation et retour arrière

- **Validation** : Application listée et service présent.
- **Retour arrière** : Paramètres > Applications > OpenVPN > Désinstaller, ou msiexec /x .\FICHIER_MSI /qb.

## Si le problème n'est pas résolu

- [Étape suivante du guide](./Fiche_Simple_-_Windows_Client_11_OpenVPN_Configurer.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_OpenVPN.md)
- [OpenVPN Community — téléchargements officiels](https://openvpn.net/community-downloads/)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)
