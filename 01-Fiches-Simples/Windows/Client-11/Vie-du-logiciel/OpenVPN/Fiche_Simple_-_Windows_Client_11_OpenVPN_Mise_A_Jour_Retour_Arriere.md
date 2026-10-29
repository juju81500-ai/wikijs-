# Fiche_Simple_-_Windows_Client_11_OpenVPN_Mise_A_Jour_Retour_Arriere

- **Environnement** : Poste Windows 11 (client OpenVPN Community)
- **OS / Version** : Windows 11; version du client à vérifier sur la page de téléchargement officielle
- **Catégorie** : OpenVPN Community client / mise à jour / retour arrière
- **Tags** : `openvpn`, `windows11`, `vie-du-logiciel`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour le client OpenVPN avec retour arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Noter la version actuelle (Paramètres > Applications > Applications installées > OpenVPN) et conserver le MSI actuel.
   👉 Explication : La version de référence sert au retour arrière.

2. Télécharger le nouveau MSI sur la page officielle, vérifier l'empreinte puis installer par-dessus :
   ```powershell
   Get-FileHash -Algorithm SHA256 .\FICHIER_MSI
   msiexec /i .\FICHIER_MSI /qb
   ```
   👉 Explication : FICHIER_MSI est le nouveau MSI (à remplacer); les profils existants sont conservés.

3. Retour arrière : désinstaller puis réinstaller la version précédente conservée :
   ```powershell
   msiexec /x .\FICHIER_MSI_NOUVEAU /qb
   msiexec /i .\FICHIER_MSI_ANCIEN /qb
   ```
   👉 Explication : FICHIER_MSI_NOUVEAU et FICHIER_MSI_ANCIEN sont les MSI correspondants (à remplacer); réimporter les profils si nécessaire.

## 2. Production — Contrôles

Tester sur un poste pilote avant le déploiement.

## 3. Production — Sécurité

- Source unique : openvpn.net.

## Validation et retour arrière

- **Validation** : Nouvelle version installée et connexion fonctionnelle.
- **Retour arrière** : Réinstaller la version précédente comme à l'étape 3.

## Si le problème n'est pas résolu

- [Première étape du guide](./Fiche_Simple_-_Windows_Client_11_OpenVPN_Prerequis_Limites.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_OpenVPN.md)
- [OpenVPN Community — téléchargements officiels](https://openvpn.net/community-downloads/)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)
