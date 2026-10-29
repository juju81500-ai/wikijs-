# Fiche_Simple_-_Docker_WikiJS_Preparer_Hote_DNS.md

- **Environnement** : Hôte Linux avec Docker Engine, Compose v2 et Traefik déjà opérationnel
- **OS / Version** : Linux serveur; Wiki.js 2.x; PostgreSQL 17
- **Catégorie** : conteneurs / documentation
- **Tags** : `wikijs`, `docker`, `compose`, `postgresql`, `traefik`, `tls`

---

## Problème précis à résoudre

Vérifier que l'hôte, le DNS et le réseau Traefik sont prêts avant de déployer Wiki.js.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier que Docker, Compose v2 et le réseau partagé de Traefik existent (le nom `traefik_proxy` est un exemple à remplacer par le vôtre) :
   ```bash
   docker --version
   docker compose version
   docker network ls
   docker network inspect traefik_proxy >/dev/null
   ```
   👉 Explication : les versions s'affichent et la dernière commande ne renvoie aucune erreur si le réseau existe.

2. Vérifier que le nom DNS prévu pointe vers le reverse proxy (`wiki.example.net` est un exemple à remplacer) :
   ```bash
   getent hosts wiki.example.net
   ```
   👉 Explication : l'adresse retournée doit être celle du reverse proxy; sinon créer l'enregistrement `A`/`AAAA`.

3. Vérifier que les ports 80 et 443 sont déjà servis par Traefik :
   ```bash
   sudo ss -tlnp | grep -E ':(80|443)\b'
   ```
   👉 Explication : Traefik doit déjà écouter; Wiki.js n'a pas besoin de publier de port.

4. Contrôler les ressources disponibles (au moins 2 vCPU et 1 Go de RAM) :
   ```bash
   nproc
   free -h
   df -h /opt
   ```
   👉 Explication : le stockage doit couvrir documents et pièces jointes à venir.

## 2. Production — Contrôles

Documenter le nom DNS, le réseau Traefik, le dimensionnement et le propriétaire du service; garder la console de l'hôte accessible pendant la mise en service.

## 3. Production — Sécurité

- Ne pas exposer PostgreSQL ni le port 3000 sur l'hôte.
- Vérifier que le certificat ACME fonctionne déjà pour un autre service avant d'ajouter Wiki.js.

## Validation et retour arrière

- **Validation** : Docker, Compose, réseau Traefik et DNS répondent comme attendu.
- **Retour arrière** : Aucune modification n'est faite à cette étape; rien à annuler.

## Si le problème n'est pas résolu

- [Wiki.js — Docker](https://docs.requarks.io/install/docker)
- [Wiki.js — Prérequis](https://docs.requarks.io/install/requirements)
- [Guide complet Wiki.js Docker PostgreSQL Traefik](../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/28_Installation_WikiJS_Docker_PostgreSQL_Traefik.md#1-preparer-lhote-et-le-dns)
