# Fiche_Simple_-_Docker_Snipe-IT_Preparer_Architecture.md

- **Environnement** : Hôte Docker avec Docker Compose v2 et réseau Traefik existant
- **OS / Version** : Hôte Linux maintenu; Snipe-IT 8.8.3; MariaDB 11.4.7
- **Catégorie** : ITSM / gestion des actifs
- **Tags** : `snipe-it`, `docker`, `mariadb`, `traefik`, `inventaire`

---

## Problème précis à résoudre

Valider l'architecture avant de déployer Snipe-IT derrière Traefik.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les prérequis :
   ```bash
   docker --version
   docker compose version
   docker network ls | grep traefik_proxy
   ```
   👉 Explication : Vérifie Docker, Compose v2 et la présence du réseau proxy Traefik existant.

2. Prévoir le DNS (exemple `assets.example.net`, à remplacer), TLS terminé par Traefik, volumes sauvegardés hors hôte et envoi SMTP.
   👉 Explication : ces éléments conditionnent la suite du déploiement.

3. Retenir l'image officielle `snipe/snipe-it` épinglée à `v8.8.3`; revalider la dernière version maintenue avant un nouveau déploiement.
   👉 Explication : garantit un déploiement reproductible.

## 2. Production — Contrôles

Garder la base dans un réseau privé et ne pas publier son port.

## 3. Production — Sécurité

- Utiliser uniquement l'image officielle.
- Ne pas exposer MariaDB.

## Validation et retour arrière

- **Validation** : Docker, Compose et réseau Traefik présents; DNS, TLS et SMTP prévus.
- **Retour arrière** : aucun changement n'a été fait.

## Si le problème n'est pas résolu

- [Snipe-IT — Docker Compose](https://snipe-it.readme.io/docs/docker)
- [Guide complet — étape 1](../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/39_Deploiement_Snipe_IT_8_Docker_MariaDB_Traefik.md#1-preparer-larchitecture)
