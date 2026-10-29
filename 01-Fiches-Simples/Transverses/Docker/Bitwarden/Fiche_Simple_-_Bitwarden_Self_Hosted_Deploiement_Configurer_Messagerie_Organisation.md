# Fiche_Simple_-_Bitwarden_Self_Hosted_Deploiement_Configurer_Messagerie_Organisation.md

- **Environnement** : Serveur Linux x86-64 avec Docker Engine et Compose (déploiement standard Bitwarden)
- **OS / Version** : Linux x86-64 supporté; Docker Engine 26+
- **Catégorie** : coffre de mots de passe / secrets
- **Tags** : `bitwarden`, `self-hosted`, `docker`, `linux`, `secrets`

---

## Problème précis à résoudre

Configurer SMTP et les paramètres d'organisation avant d'inviter des utilisateurs.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir `bwdata/env/global.override.env` :
   ```bash
   sudoedit /opt/bitwarden/bwdata/env/global.override.env
   ```
   👉 Explication : contient les paramètres SMTP; le mot de passe SMTP ne doit y être saisi que depuis le coffre.

2. Y renseigner serveur, port, SSL et compte SMTP selon la documentation Bitwarden.
   👉 Explication : nécessaire aux invitations et validations de compte.

3. Si nécessaire, créer ou lier la licence d'organisation self-hosted.
   👉 Explication : respecter les règles de licence Bitwarden.

4. Régler inscription publique, communication cloud, rôles, collections, SSO/MFA et policy avant d'inviter.
   👉 Explication : évite une ouverture non voulue.

5. Appliquer les modifications :
   ```bash
   sudo -iu bitwarden /opt/bitwarden/bitwarden.sh restart
   ```
   👉 Explication : utiliser `rebuild` selon le type de configuration modifiée.

## 2. Production — Contrôles

Garder HTTP/HTTPS cohérent et confirmer TLS pour l'accès client.

## 3. Production — Sécurité

- Fichier `global.override.env` lisible uniquement par `bitwarden`.

## Validation et retour arrière

- **Validation** : les e-mails d'invitation partent et les stratégies sont en place.
- **Retour arrière** : restaurer la copie précédente de `global.override.env` puis `restart`.

## Si le problème n'est pas résolu

- [Bitwarden — héberger une organisation](https://bitwarden.com/help/self-host-an-organization/)
- [Bitwarden — déploiement Linux](https://bitwarden.com/help/install-on-premise-linux/)
- [Guide complet](../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/62_Deploiement_Bitwarden_Self_Hosted_Linux_Docker.md#4-configurer-la-messagerie-et-lorganisation)
