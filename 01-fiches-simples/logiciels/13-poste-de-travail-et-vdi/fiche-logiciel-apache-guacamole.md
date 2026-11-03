# 📄 Apache Guacamole

- **Catégorie** : Poste de travail et [[Glossary:VDI]]
- **Plateforme** : Linux
- **Produit (matrice)** : Apache Guacamole
- **Statut dans le pack** : Guide complet — Guacamole 1.6.0 avec Docker Compose, PostgreSQL et reverse proxy HTTPS
- **Tags** : `logiciel`, `13-poste-de-travail-et-vdi`, `guide-complet`, `docker`, `administration`

## 📚 Couverture dans le pack

Guide borné à un déploiement Docker Compose avec authentification PostgreSQL et publication locale derrière un reverse proxy HTTPS. [[Glossary:MFA]]/SSO, haute disponibilité, connexions aux systèmes cibles et exigences de production restent à valider séparément.

## 🧭 Utilisation

Cette fiche est le point d'entrée du logiciel : elle indique si le pack contient une procédure et renvoie vers elle. Pour une procédure pas à pas, ouvrir le guide ou la fiche liée ci-dessus. Lorsque le statut est `Manquant`, aucune procédure dédiée n'existe encore dans le pack.

Procédure pas à pas du pack : [Déployer Apache Guacamole 1.6.0 avec Docker Compose](../../../02-fiches-completes/transverses/docker/installation-deploiement/121-deploiement-apache-guacamole-1-6-docker.md).

Fiches simples du guide : [cadrer le périmètre et les prérequis](../../transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-cadrer-prerequis.md), [préparer les secrets et la configuration](../../transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-preparer-secrets-compose.md), [initialiser le schéma PostgreSQL](../../transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-initialiser-schema-postgresql.md), [démarrer et configurer le reverse proxy](../../transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-demarrer-reverse-proxy.md), [sauvegarde et restauration](../../transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-sauvegarde-restauration.md), [validation et contrôle d'accès](../../transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-valider-controle-acces.md), [mise à jour et retour arrière](../../transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-mise-a-jour-retour-arriere.md).
