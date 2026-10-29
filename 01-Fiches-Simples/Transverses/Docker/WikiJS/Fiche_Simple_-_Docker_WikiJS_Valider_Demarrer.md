# Fiche_Simple_-_Docker_WikiJS_Valider_Demarrer.md

- **Environnement** : Hôte Linux avec Docker Engine, Compose v2 et Traefik déjà opérationnel
- **OS / Version** : Linux serveur; Wiki.js 2.x; PostgreSQL 17
- **Catégorie** : conteneurs / documentation
- **Tags** : `wikijs`, `docker`, `compose`, `postgresql`, `traefik`, `tls`

---

## Problème précis à résoudre

Démarrer la stack et terminer l'assistant initial de Wiki.js.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le réseau puis la configuration rendue :
   ```bash
   docker network inspect traefik_proxy >/dev/null
   cd /opt/docker/wikijs
   sudo docker compose config --quiet
   ```
   👉 Explication : on évite de démarrer avec un réseau ou un fichier invalide.

2. Télécharger les images et démarrer :
   ```bash
   sudo docker compose pull
   sudo docker compose up -d
   ```
   👉 Explication : les conteneurs `db` et `wiki` sont créés; `wiki` attend que la base soit healthy.

3. Contrôler l'état et les journaux :
   ```bash
   sudo docker compose ps
   sudo docker compose logs --tail=100 db wiki
   ```
   👉 Explication : `db` doit être healthy et `wiki` sans erreur persistante.

4. Ouvrir **https://wiki.example.net** (adresse d'exemple à remplacer), terminer l'assistant, créer le compte administrateur avec un mot de passe unique, puis définir l'URL publique canonique dans **Administration > General**.
   👉 Explication : l'URL canonique évite des liens erronés; configurer ensuite SMTP et l'authentification nécessaires.

## 2. Production — Contrôles

Planifier la mise en service en fenêtre approuvée et noter les versions d'images réellement déployées (`docker compose images`).

## 3. Production — Sécurité

- Ne pas laisser de compte administrateur partagé.
- Ne pas activer TLS dans Wiki.js : TLS est terminé par Traefik.

## Validation et retour arrière

- **Validation** : `docker compose ps` montre db healthy et wiki up, et la page HTTPS répond.
- **Retour arrière** : `cd /opt/docker/wikijs && sudo docker compose down` (sans `-v`) arrête la stack en conservant les volumes.

## Si le problème n'est pas résolu

- [Wiki.js — Docker](https://docs.requarks.io/install/docker)
- [Wiki.js — Prérequis](https://docs.requarks.io/install/requirements)
- [Guide complet Wiki.js Docker PostgreSQL Traefik](../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/28_Installation_WikiJS_Docker_PostgreSQL_Traefik.md#4-valider-et-demarrer)
