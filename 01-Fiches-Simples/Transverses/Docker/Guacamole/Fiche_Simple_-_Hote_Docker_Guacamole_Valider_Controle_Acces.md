# Fiche_Simple_-_Hote_Docker_Guacamole_Valider_Controle_Acces.md

- **Environnement** : Hôte Linux avec Docker Engine et plugin Compose (Guacamole, guacd, PostgreSQL, reverse proxy HTTPS)
- **OS / Version** : Docker Engine + Compose; images Apache Guacamole 1.6.0, PostgreSQL 16
- **Catégorie** : accès distant / validation
- **Tags** : `docker`, `apache-guacamole`, `compose`, `postgresql`, `mfa`, `acces`

---

## Problème précis à résoudre

Valider le déploiement et les contrôles d'accès avant ouverture aux utilisateurs.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les services et les journaux :
   ```bash
   docker compose ps
   docker compose logs --tail=50 guacamole
   ```
   👉 Explication : les services attendus sont actifs.

2. Vérifier que les ports internes ne sont pas joignables depuis le réseau (depuis une autre machine, IP d'exemple à remplacer) :
   ```bash
   nc -zv 192.0.2.10 8080
   nc -zv 192.0.2.10 4822
   nc -zv 192.0.2.10 5432
   ```
   👉 Explication : 8080, 4822 et 5432 doivent être fermés.

3. **Interface Guacamole > Paramètres > Utilisateurs** : créer des comptes nominatifs puis supprimer ou désactiver `guacadmin`.
   👉 Explication : retire le compte de démonstration.

## 2. Production — Contrôles

Contrôler MFA/SSO et groupes, tester une connexion pilote vers un système de laboratoire autorisé.

## 3. Production — Sécurité

- Ne pas connecter de systèmes réels avant validation.

## Validation et retour arrière

- **Validation** : comptes nominatifs actifs, ports internes fermés, connexion pilote réussie.
- **Retour arrière** : désactiver l'accès utilisateur via le proxy ou le pare-feu.

## Si le problème n'est pas résolu

- [Apache Guacamole — Docker](https://guacamole.apache.org/doc/gug/guacamole-docker.html)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet Apache Guacamole Docker](../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/121_Deploiement_Apache_Guacamole_1.6_Docker.md#6-validation-et-controle-dacces)
