# Fiche_Simple_-_Windows_Client_11_OpenVPN_Securiser

- **Environnement** : Poste Windows 11 (client OpenVPN Community)
- **OS / Version** : Windows 11; version du client à vérifier sur la page de téléchargement officielle
- **Catégorie** : OpenVPN Community client / sécuriser
- **Tags** : `openvpn`, `windows11`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Protéger le profil, la clé et le poste.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les droits du dossier de profils :
   ```powershell
   icacls 'C:\Program Files\OpenVPN\config'
   ```
   👉 Explication : Seuls Administrateurs et SYSTEM doivent pouvoir modifier; aucun droit d'écriture pour les utilisateurs standard.

2. GUI : vérifier que le pare-feu Windows est actif (Sécurité Windows > Pare-feu et protection du réseau).
   👉 Explication : Le profil VPN ne doit pas désactiver le pare-feu.

3. Révoquer en cas de perte : prévenir immédiatement l'administrateur du serveur.
   👉 Explication : La révocation se fait côté PKI/serveur (CRL); supprimer ensuite le profil du poste.

## 2. Production — Contrôles

Utiliser BitLocker sur le poste; ne pas conserver de profil sur un poste partagé.

## 3. Production — Sécurité

- Un profil = un utilisateur; pas de transfert de clé par messagerie.

## Validation et retour arrière

- **Validation** : Droits conformes et pare-feu actif.
- **Retour arrière** : Rétablir les droits d'origine avec icacls si modifiés par erreur.

## Si le problème n'est pas résolu

- [Étape suivante du guide](./Fiche_Simple_-_Windows_Client_11_OpenVPN_Valider.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_OpenVPN.md)
- [OpenVPN Community — téléchargements officiels](https://openvpn.net/community-downloads/)
- [OpenVPN Community — documentation officielle](https://openvpn.net/community-resources/)
