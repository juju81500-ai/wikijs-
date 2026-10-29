# Fiche_Simple_-_Windows_Client_11_OpenVPN_Sauvegarder_Restaurer

- **Environnement** : Poste Windows 11 (client OpenVPN Community)
- **OS / Version** : Windows 11; version du client à vérifier sur la page de téléchargement officielle
- **Catégorie** : OpenVPN Community client / sauvegarder / restaurer

---

## Problème précis à résoudre

Conserver le nécessaire pour reconstruire le poste sans exposer les clés.

## 1. Hors-Production (Lab / Test / POC)

1. Noter la liste des profils sans copier la clé :
   ```powershell
   Get-ChildItem 'C:\Program Files\OpenVPN\config' | Select-Object Name,Length,LastWriteTime
   ```
   👉 Explication : Seule la liste est conservée; la clé privée reste dans le profil protégé fourni.

2. Restaurer : réinstaller le client puis réimporter le profil.
   👉 Explication : Si le profil est perdu, demander l'émission d'un nouveau certificat; ne pas chercher à récupérer une clé.

## 2. Production — Contrôles

Le profil original est redemandé à l'administrateur du serveur, qui en assure la sauvegarde.

## 3. Production — Sécurité

- Ne pas stocker un profil dans un cloud personnel ni dans un dépôt Git.

## Validation et retour arrière

- **Validation** : Le client réinstallé se reconnecte avec le profil réimporté.
- **Retour arrière** : Supprimer le profil si le poste est perdu et demander la révocation.

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/windows/client-11/vie-du-logiciel/openvpn/fiche-simple-windows-client-11-openvpn-mise-a-jour-retour-arriere)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-openvpn)
- [OpenVPN Community — téléchargements officiels](https://openvpn.net/community-downloads/)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)