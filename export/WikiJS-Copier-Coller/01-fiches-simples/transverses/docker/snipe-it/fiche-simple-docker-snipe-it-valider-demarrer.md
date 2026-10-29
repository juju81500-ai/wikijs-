# Fiche_Simple_-_Docker_Snipe-IT_Valider_Demarrer.md

- **Environnement** : Hôte Docker avec Docker Compose v2 et réseau Traefik existant
- **OS / Version** : Hôte Linux maintenu; Snipe-IT 8.8.3; MariaDB 11.4.7
- **Catégorie** : ITSM / gestion des actifs

---

## Problème précis à résoudre

Contrôler la configuration Compose puis démarrer la stack.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le réseau :
   ```bash
   docker network inspect traefik_proxy >/dev/null
   ```
   👉 Explication : Échoue si le réseau Traefik n'existe pas.

2. Valider et démarrer :
   ```bash
   cd /opt/docker/snipe-it
   sudo docker compose config --quiet
   sudo docker compose pull
   sudo docker compose up -d
   ```
   👉 Explication : Valide la syntaxe, récupère les images et démarre les conteneurs.

3. Contrôler :
   ```bash
   sudo docker compose ps
   sudo docker compose logs --tail=100 app db
   ```
   👉 Explication : Affiche l'état et les derniers journaux.

4. Ouvrir **https://assets.example.net**, terminer le prévol, créer un compte administrateur nominatif, puis configurer SMTP, rôles, catégories, modèles, statuts et lieux.
   👉 Explication : prépare la structure avant l'import d'inventaire.

## 2. Production — Contrôles

L'import d'inventaire vient après validation de cette structure.

## 3. Production — Sécurité

- Compte administrateur nominatif, pas de compte partagé.

## Validation et retour arrière

- **Validation** : conteneurs `Up`, page accessible en HTTPS.
- **Retour arrière** : `sudo docker compose down` (sans `-v`) pour arrêter sans perdre les volumes.

## Si le problème n'est pas résolu

- [Snipe-IT — Docker Compose](https://snipe-it.readme.io/docs/docker)
- [Guide complet — étape 4](/02-fiches-completes/transverses/docker/installation-deploiement/39-deploiement-snipe-it-8-docker-mariadb-traefik#4-valider-et-demarrer)