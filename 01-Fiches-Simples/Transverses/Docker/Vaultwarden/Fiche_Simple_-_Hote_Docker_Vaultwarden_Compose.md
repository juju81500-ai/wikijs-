# Fiche_Simple_-_Hote_Docker_Vaultwarden_Compose.md

- **Environnement** : Hôte Linux avec Docker Engine et plugin Compose, Vaultwarden SQLite derrière un reverse proxy HTTPS
- **OS / Version** : Hôte Linux + Docker; image vaultwarden/server (tag à figer après validation)
- **Catégorie** : gestionnaire de mots de passe auto-hébergé
- **Tags** : `docker`, `vaultwarden`, `compose`, `reverse-proxy`

---

## Problème précis à résoudre

Déployer Vaultwarden avec Compose, port limité à la boucle locale pour le reverse proxy.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un répertoire dédié :
   ```bash
   sudo mkdir -p /opt/vaultwarden
   cd /opt/vaultwarden
   ```
   👉 Explication : on isole la pile dans son propre dossier.

2. Créer `compose.yaml` avec ce contenu (remplacer `vault.example.net` par le vrai domaine) :
   ```yaml
   services:
     vaultwarden:
       image: vaultwarden/server:latest
       container_name: vaultwarden
       restart: always
       environment:
         DOMAIN: "https://vault.example.net"
         SIGNUPS_ALLOWED: "true"
         # ADMIN_TOKEN: "chaîne PHC avec chaque $ doublé"
       volumes:
         - ./vw-data:/data
       ports:
         - 127.0.0.1:11001:80
   ```
   👉 Explication : le port 11001 n'est joignable que depuis l'hôte, donc seul le reverse proxy y accède.

3. Valider le fichier :
   ```bash
   docker compose config
   ```
   👉 Explication : la commande signale toute erreur de syntaxe.

4. Démarrer et suivre les journaux :
   ```bash
   docker compose up -d
   docker compose logs -f
   ```
   👉 Explication : le conteneur démarre en arrière-plan; Ctrl+C quitte le suivi sans arrêter le service.

5. Configurer le reverse proxy pour envoyer le domaine vers `127.0.0.1:11001` avec un certificat valide.
   👉 Explication : c'est le seul chemin d'accès autorisé.

6. Après validation, noter la version ou le digest déployé et le figer à la place de `latest`.
   👉 Explication : cela rend le retour arrière possible.

## 2. Production — Contrôles

Figer le tag ou digest avant la production et documenter l'emplacement de `/opt/vaultwarden`.

## 3. Production — Sécurité

- Ne pas publier le port 11001 sur `0.0.0.0`.
- Ne pas laisser `latest` en production sans version notée.

## Validation et retour arrière

- **Validation** : `docker compose ps` montre le conteneur `running`.
- **Retour arrière** : `docker compose down` (n'efface pas `vw-data`).

## Si le problème n'est pas résolu

- [Vaultwarden — Using Docker Compose](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [Vaultwarden — Backing up your vault](https://github.com/dani-garcia/vaultwarden/wiki/Backing-up-your-vault)
- [Guide complet — créer le fichier Compose et démarrer](../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/94_Deploiement_Vaultwarden_Docker_Compose.md#3-compose)
