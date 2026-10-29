# Fiche_Simple_-_Hote_Docker_Guacamole_Demarrer_Reverse_Proxy.md

- **Environnement** : Hôte Linux avec Docker Engine et plugin Compose (Guacamole, guacd, PostgreSQL, reverse proxy HTTPS)
- **OS / Version** : Docker Engine + Compose; images Apache Guacamole 1.6.0, PostgreSQL 16
- **Catégorie** : accès distant / démarrage
- **Tags** : `docker`, `apache-guacamole`, `compose`, `postgresql`, `reverse-proxy`, `https`

---

## Problème précis à résoudre

Démarrer la pile puis la publier derrière un reverse proxy HTTPS.

## 1. Hors-Production (Lab / Test / POC)

1. Valider puis démarrer :
   ```bash
   docker compose config --quiet
   docker compose up -d
   docker compose ps
   ```
   👉 Explication : la validation silencieuse évite d'afficher les secrets interpolés.

2. Lire les journaux récents :
   ```bash
   docker compose logs --tail=100 guacamole guacd db
   ```
   👉 Explication : aucune erreur de schéma ou d'authentification.

3. Configurer le reverse proxy (selon son produit) pour transmettre HTTPS vers `http://127.0.0.1:8080/guacamole/`, puis tester l'origine locale :
   ```bash
   curl -fsSI http://127.0.0.1:8080/guacamole/
   ```
   👉 Explication : si le proxy est conteneurisé, le placer sur un réseau privé dédié et retirer la publication loopback.

4. Ouvrir la page de connexion, puis changer immédiatement le mot de passe `guacadmin` : **guacadmin (menu en haut à droite) > Settings > Preferences > Change password**
   👉 Explication : les identifiants initiaux `guacadmin` / `guacadmin` sont publics dans la documentation.

## 2. Production — Contrôles

N'accepter les en-têtes du proxy que depuis le proxy de confiance; terminer TLS avec un certificat valide et n'autoriser que les réseaux clients approuvés.

## 3. Production — Sécurité

- Ne pas partager la sortie complète de `docker compose config`.
- Ne pas exposer directement le port 8080.

## Validation et retour arrière

- **Validation** : la page de connexion répond en HTTPS via le proxy et le mot de passe initial est changé.
- **Retour arrière** : `docker compose down` arrête la pile sans supprimer les volumes.

## Si le problème n'est pas résolu

- [Apache Guacamole — Docker](https://guacamole.apache.org/doc/gug/guacamole-docker.html)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet Apache Guacamole Docker](../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/121_Deploiement_Apache_Guacamole_1.6_Docker.md#4-demarrer-et-configurer-le-reverse-proxy)
