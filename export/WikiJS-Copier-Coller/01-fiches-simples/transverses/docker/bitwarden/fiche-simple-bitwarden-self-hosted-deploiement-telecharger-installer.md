# Fiche_Simple_-_Bitwarden_Self_Hosted_Deploiement_Telecharger_Installer.md

- **Environnement** : Serveur Linux x86-64 avec Docker Engine et Compose (déploiement standard Bitwarden)
- **OS / Version** : Linux x86-64 supporté; Docker Engine 26+
- **Catégorie** : coffre de mots de passe / secrets

---

## Problème précis à résoudre

Télécharger le script officiel, le contrôler puis lancer l'installation sous le bon compte.

## 1. Hors-Production (Lab / Test / POC)

1. Se placer dans le répertoire sous le compte de service :
   ```bash
   sudo -iu bitwarden
   cd /opt/bitwarden
   ```
   👉 Explication : le script ne doit pas être lancé avec root.

2. Télécharger `bitwarden.sh` depuis l'URL officielle indiquée dans la documentation Bitwarden (remplacer URL_OFFICIELLE_BITWARDEN par cette URL) :
   ```bash
   curl -Lso bitwarden.sh URL_OFFICIELLE_BITWARDEN && chmod 700 bitwarden.sh
   ```
   👉 Explication : enregistre le fichier sans l'exécuter directement depuis le réseau.

3. Contrôler le contenu et la provenance du script :
   ```bash
   less bitwarden.sh
   ```
   👉 Explication : relecture avant exécution.

4. Lancer l'assistant :
   ```bash
   ./bitwarden.sh install
   ```
   👉 Explication : demande FQDN, option de certificat (Let's Encrypt si les prérequis publics sont réunis, sinon certificat d'entreprise), installation ID, clé et région.

## 2. Production — Contrôles

Obtenir installation ID et clé sur le portail officiel et les transmettre depuis le coffre.

## 3. Production — Sécurité

- Éviter les secrets dans l'historique shell.
- Ne pas archiver l'ID ni la clé dans une fiche.

## Validation et retour arrière

- **Validation** : l'assistant se termine et `/opt/bitwarden/bwdata` est créé.
- **Retour arrière** : en lab, `./bitwarden.sh uninstall` puis suppression de `bwdata`, après sauvegarde si des données existent.

## Si le problème n'est pas résolu

- [Bitwarden — déploiement Linux](https://bitwarden.com/help/install-on-premise-linux/)
- [Bitwarden — déploiement Linux](https://bitwarden.com/help/install-on-premise-linux/)
- [Guide complet](/02-fiches-completes/transverses/docker/installation-deploiement/62-deploiement-bitwarden-self-hosted-linux-docker#3-telecharger-et-installer-bitwarden)