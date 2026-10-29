# Fiche_Simple_-_Docker_WikiJS_Recette.md

- **Environnement** : Hôte Linux avec Docker Engine, Compose v2 et Traefik déjà opérationnel
- **OS / Version** : Linux serveur; Wiki.js 2.x; PostgreSQL 17
- **Catégorie** : conteneurs / documentation

---

## Problème précis à résoudre

Valider le fonctionnement complet de Wiki.js après déploiement.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le certificat présenté et la redirection HTTP vers HTTPS (domaine d'exemple à remplacer) :
   ```bash
   curl -sSI http://wiki.example.net | head -n 5
   curl -sSI https://wiki.example.net | head -n 5
   ```
   👉 Explication : le certificat doit correspondre au nom DNS et HTTP doit rediriger vers HTTPS selon la politique Traefik.

2. Dans Wiki.js, créer une page de test, la modifier puis y joindre un fichier : **Pages > New Page** (menu de la barre supérieure).
   👉 Explication : on vérifie l'écriture en base et sur le stockage.

3. Redémarrer les services puis confirmer que la page et la pièce jointe sont toujours là :
   ```bash
   cd /opt/docker/wikijs
   sudo docker compose restart
   sudo docker compose ps
   ```
   👉 Explication : la persistance des volumes est prouvée.

4. Confirmer qu'aucun port PostgreSQL ou 3000 n'est publié :
   ```bash
   sudo ss -tlnp | grep -E ':(5432|3000)\b' || echo 'aucun port expose'
   ```
   👉 Explication : la base et Wiki.js ne doivent être joignables que par Docker.

5. Créer un utilisateur non administrateur et tester ses permissions : **Administration > Users > New User**.
   👉 Explication : on vérifie qu'un compte standard ne peut pas administrer le wiki.

## 2. Production — Contrôles

Consigner le résultat de la recette avec date, version d'image et opérateur.

## 3. Production — Sécurité

- Ne pas supprimer la page de test sans l'identifier clairement.
- Pas de port base de données exposé.

## Validation et retour arrière

- **Validation** : Certificat valide, page créée et modifiée, pièce jointe conservée après redémarrage, aucun port exposé.
- **Retour arrière** : Supprimer la page et l'utilisateur de test depuis l'interface d'administration.

## Si le problème n'est pas résolu

- [Wiki.js — Docker](https://docs.requarks.io/install/docker)
- [Wiki.js — Prérequis](https://docs.requarks.io/install/requirements)
- [Guide complet Wiki.js Docker PostgreSQL Traefik](/02-fiches-completes/transverses/docker/installation-deploiement/28-installation-wikijs-docker-postgresql-traefik#5-recette)