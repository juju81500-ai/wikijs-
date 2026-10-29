# Fiche_Simple_-_Hote_Docker_Guacamole_Cadrer_Prerequis.md

- **Environnement** : Hôte Linux avec Docker Engine et plugin Compose (Guacamole, guacd, PostgreSQL, reverse proxy HTTPS)
- **OS / Version** : Docker Engine + Compose; images Apache Guacamole 1.6.0, PostgreSQL 16
- **Catégorie** : accès distant / cadrage
- **Tags** : `docker`, `apache-guacamole`, `compose`, `postgresql`, `prerequis`

---

## Problème précis à résoudre

Vérifier que l'hôte Docker est prêt avant de déployer la passerelle d'accès distant.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler Docker et Compose :
   ```bash
   docker --version
   docker compose version
   ```
   👉 Explication : les deux doivent répondre.

2. Contrôler les ports locaux libres :
   ```bash
   sudo ss -tlnp | grep -E ':(8080|4822|5432)\b' || echo 'ports libres'
   ```
   👉 Explication : 8080 sera publié sur la boucle locale pour le reverse proxy.

## 2. Production — Contrôles

Prévoir DNS dédié, reverse proxy HTTPS géré, stockage persistant sauvegardé, comptes personnels, MFA ou SSO approuvé et liste des cibles autorisées.

## 3. Production — Sécurité

- Traiter Guacamole comme une passerelle privilégiée.
- Ne pas connecter de systèmes réels avant validation des comptes et contrôles d'accès.

## Validation et retour arrière

- **Validation** : Docker et Compose disponibles, ports libres.
- **Retour arrière** : lecture seule: rien à annuler.

## Si le problème n'est pas résolu

- [Apache Guacamole — Docker](https://guacamole.apache.org/doc/gug/guacamole-docker.html)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet Apache Guacamole Docker](../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/121_Deploiement_Apache_Guacamole_1.6_Docker.md#1-perimetre-et-prerequis)
