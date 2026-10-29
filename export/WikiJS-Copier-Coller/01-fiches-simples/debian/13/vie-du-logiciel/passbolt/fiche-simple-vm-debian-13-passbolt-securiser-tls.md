# Fiche_Simple_-_VM_Debian_13_Passbolt_Securiser_TLS

- **Environnement** : VM Debian 13 dédiée avec domaine, base et SMTP définis
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : gestionnaire de secrets / serveur

---

## Problème précis à résoudre

Installer certificat valide, restreindre base et protéger clés cryptographiques.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier résolution et écoute
   ```bash
   getent hosts passbolt.example.com
   sudo ss -lntp
   ```
   👉 Explication : remplacer le FQDN; confirmer l’interface attendue.

2. Configurer TLS dans Nginx ou proxy choisi
   ```text
   Navigateur > ouvrir la documentation officielle : https://www.passbolt.com/docs/hosting/install/ce/debian/
   ```
   👉 Explication : suivre doc correspondant au point de terminaison TLS. Détail à confirmer dans la documentation officielle avant application : Configurer certificat avec nom DNS, chaîne complète et renouvellement. Rediriger HTTP vers HTTPS après validation.

3. Valider certificat
   ```bash
   openssl s_client -connect passbolt.example.com:443 -servername passbolt.example.com </dev/null
   curl -I https://passbolt.example.com/
   ```
   👉 Explication : remplacer FQDN; contrôler chaîne, date et nom.

4. Limiter flux réseau
   ```text
   Navigateur > ouvrir la documentation officielle : https://www.passbolt.com/docs/hosting/install/ce/debian/
   ```
   👉 Explication : faire valider règles par réseau. Détail à confirmer dans la documentation officielle avant application : Autoriser HTTPS aux segments utilisateurs approuvés. Limiter SSH à l’administration et refuser base depuis les clients.

## 2. Production — Contrôles

Faire valider TLS, pare-feu, MFA, journaux, rotation de clés et séparation des rôles.

## 3. Production — Sécurité

- Protéger clé serveur et passphrases hors ligne et chiffrées.
- Ne pas désactiver les contrôles cryptographiques pour contourner une erreur.
- Activer MFA et retirer les comptes inutilisés.

## Validation et retour arrière

- **Validation** : HTTPS est valide et base inaccessible aux clients.
- **Retour arrière** : Rétablir le certificat/proxy précédent; ne jamais publier HTTP ouvert.

## Si le problème n'est pas résolu

- [Passbolt — installation Debian 13 CE](https://www.passbolt.com/docs/hosting/install/ce/debian/)
- [Passbolt — configuration serveur](https://www.passbolt.com/docs/hosting/configure/)
- [Passbolt — sauvegarde](https://www.passbolt.com/docs/hosting/backup/)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/passbolt/fiche-simple-vm-debian-13-passbolt-prerequis-limites>)