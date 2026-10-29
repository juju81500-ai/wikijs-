# Fiche_Simple_-_Docker_Snipe-IT_Recuperer_Fichiers_Officiels.md

- **Environnement** : Hôte Docker avec Docker Compose v2 et réseau Traefik existant
- **OS / Version** : Hôte Linux maintenu; Snipe-IT 8.8.3; MariaDB 11.4.7
- **Catégorie** : ITSM / gestion des actifs
- **Tags** : `snipe-it`, `docker`, `mariadb`, `traefik`, `inventaire`

---

## Problème précis à résoudre

Télécharger le Compose et le `.env` officiels dans un dossier protégé.

## 1. Hors-Production (Lab / Test / POC)

1. Préparer le dossier :
   ```bash
   sudo install -d -m 0750 /opt/docker/snipe-it
   cd /opt/docker/snipe-it
   ```
   👉 Explication : Crée le dossier du projet avec des droits restreints.

2. Télécharger les fichiers :
   ```bash
   sudo curl -fL https://raw.githubusercontent.com/grokability/snipe-it/master/docker-compose.yml -o docker-compose.yml
   sudo curl -fL https://raw.githubusercontent.com/grokability/snipe-it/master/.env.docker -o .env
   sudo chmod 0600 .env
   ```
   👉 Explication : Récupère les fichiers amont et protège `.env`, qui contiendra des secrets.

3. Relire `docker-compose.yml` et `.env` avant tout démarrage.
   👉 Explication : les fichiers amont évoluent; ne jamais lancer un fichier non contrôlé.

## 2. Production — Contrôles

Conserver une copie des fichiers tels que téléchargés pour comparer lors des mises à jour.

## 3. Production — Sécurité

- `.env` en mode 0600 et hors dépôt Git.

## Validation et retour arrière

- **Validation** : les deux fichiers existent et `.env` est en 0600.
- **Retour arrière** : `sudo rm -rf /opt/docker/snipe-it` si rien n'a encore été démarré (vérifier le chemin).

## Si le problème n'est pas résolu

- [Snipe-IT — Docker Compose](https://snipe-it.readme.io/docs/docker)
- [Guide complet — étape 2](../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/39_Deploiement_Snipe_IT_8_Docker_MariaDB_Traefik.md#2-recuperer-les-fichiers-officiels)
