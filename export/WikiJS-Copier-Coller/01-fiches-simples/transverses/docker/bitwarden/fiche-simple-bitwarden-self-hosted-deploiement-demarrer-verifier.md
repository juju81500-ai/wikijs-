# Fiche_Simple_-_Bitwarden_Self_Hosted_Deploiement_Demarrer_Verifier.md

- **Environnement** : Serveur Linux x86-64 avec Docker Engine et Compose (déploiement standard Bitwarden)
- **OS / Version** : Linux x86-64 supporté; Docker Engine 26+
- **Catégorie** : coffre de mots de passe / secrets

---

## Problème précis à résoudre

Démarrer Bitwarden et valider le service avec un compte de test.

## 1. Hors-Production (Lab / Test / POC)

1. Démarrer :
   ```bash
   sudo -iu bitwarden /opt/bitwarden/bitwarden.sh start
   ```
   👉 Explication : lance les conteneurs Bitwarden.

2. Contrôler les conteneurs :
   ```bash
   sudo -iu bitwarden docker ps
   ```
   👉 Explication : tous doivent être en état healthy/Up.

3. Ouvrir **https://** suivi du FQDN depuis un poste pilote et vérifier le certificat.
   👉 Explication : confirme TLS valide.

4. Inscrire un compte de test, se connecter depuis un client approuvé et valider synchronisation, import de test et invitations SMTP.
   👉 Explication : valide le cycle complet.

## 2. Production — Contrôles

Ne jamais tester avec des secrets réels avant d'avoir validé sauvegarde et restauration.

## 3. Production — Sécurité

- Données de test uniquement.

## Validation et retour arrière

- **Validation** : conteneurs sains, TLS valide, compte de test synchronisé.
- **Retour arrière** : `sudo -iu bitwarden /opt/bitwarden/bitwarden.sh stop` puis restaurer la dernière sauvegarde.

## Si le problème n'est pas résolu

- [Bitwarden — déploiement Linux](https://bitwarden.com/help/install-on-premise-linux/)
- [Bitwarden — déploiement Linux](https://bitwarden.com/help/install-on-premise-linux/)
- [Guide complet](/02-fiches-completes/transverses/docker/installation-deploiement/62-deploiement-bitwarden-self-hosted-linux-docker#5-demarrer-et-verifier)