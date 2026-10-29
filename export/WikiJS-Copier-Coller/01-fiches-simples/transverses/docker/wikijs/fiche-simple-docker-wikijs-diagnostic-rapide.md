# Fiche_Simple_-_Docker_WikiJS_Diagnostic_Rapide.md

- **Environnement** : Hôte Linux avec Docker Engine, Compose v2 et Traefik déjà opérationnel
- **OS / Version** : Linux serveur; Wiki.js 2.x; PostgreSQL 17
- **Catégorie** : conteneurs / documentation

---

## Problème précis à résoudre

Identifier la cause d'une panne Wiki.js (base, 404/502, certificat, pièces jointes).

## 1. Hors-Production (Lab / Test / POC)

1. Lire l'état et les journaux :
   ```bash
   cd /opt/docker/wikijs
   sudo docker compose ps
   sudo docker compose logs --tail=200 wiki
   sudo docker compose logs --tail=200 db
   docker network inspect traefik_proxy
   ```
   👉 Explication : on repère les erreurs de connexion à la base ou au réseau.

2. Si Wiki.js ne joint pas PostgreSQL : vérifier `DB_HOST: db`, le réseau `backend`, l'état healthy et le montage `DB_PASS_FILE` dans `docker-compose.yml`.
   👉 Explication : ce sont les causes les plus fréquentes.

3. Si erreur 404 ou 502 : vérifier le DNS, les labels Traefik, le réseau Docker réellement partagé et le port amont 3000.
   👉 Explication : Traefik doit pouvoir joindre le conteneur.

4. Si certificat invalide : diagnostiquer Traefik et ACME, sans activer TLS dans Wiki.js.
   👉 Explication : TLS est terminé par le reverse proxy.

5. Si une pièce jointe disparaît après recréation : vérifier le module de stockage choisi et sa persistance.
   👉 Explication : le dump SQL seul peut ne pas contenir les fichiers.

## 2. Production — Contrôles

Capturer les journaux avant toute correction et ne corriger qu'une cause à la fois.

## 3. Production — Sécurité

- Ne pas publier de port pour « tester »; utiliser les journaux et `docker compose exec`.
- Ne pas partager de journaux contenant des secrets.

## Validation et retour arrière

- **Validation** : La cause est identifiée, corrigée et `docker compose ps` est sain.
- **Retour arrière** : Revenir à la configuration précédente du fichier Compose et relancer `docker compose up -d`.

## Si le problème n'est pas résolu

- [Wiki.js — Docker](https://docs.requarks.io/install/docker)
- [Wiki.js — Prérequis](https://docs.requarks.io/install/requirements)
- [Guide complet Wiki.js Docker PostgreSQL Traefik](/02-fiches-completes/transverses/docker/installation-deploiement/28-installation-wikijs-docker-postgresql-traefik#8-diagnostic-rapide)