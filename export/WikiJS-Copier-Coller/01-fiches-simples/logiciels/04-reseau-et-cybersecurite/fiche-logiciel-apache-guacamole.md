# 📄 Apache Guacamole

- **Catégorie** : Réseau et cybersécurité
- **Plateforme** : Linux
- **Produit (matrice)** : Apache Guacamole
- **Statut dans le pack** : Documentation défensive — administration et gouvernance

## 📚 Couverture dans le pack

Fiche défensive d’administration et de gouvernance. Elle ne remplace pas le guide éditeur spécifique à la version déployée et ne fournit pas de procédure offensive.

## 🧭 Périmètre

Guide de déploiement : [Apache Guacamole 1.6.0 avec Docker Compose](/02-fiches-completes/transverses/docker/installation-deploiement/121-deploiement-apache-guacamole-1-6-docker). Celui-ci couvre le socle PostgreSQL et l'accès derrière reverse proxy HTTPS; MFA/SSO, haute disponibilité et connexions cibles ne sont pas inclus. Exposer l’accès via TLS et un frontal pris en charge, protéger le compte d’administration, activer MFA via une extension d’authentification approuvée, appliquer des droits par connexion et utilisateur, et ne pas activer presse-papiers/transfert de fichiers sans besoin validé. Stocker les secrets de connexion dans un mécanisme protégé et journaliser les accès selon la politique de confidentialité.

## ✅ Autorisation et préparation

Avant toute modification, consigner le propriétaire du service, les actifs et utilisateurs concernés, le ticket de changement, l’approbateur, la fenêtre, les dépendances, les critères d’arrêt et la personne à contacter. Toute évaluation active ou action sur un terminal/équipement exige une autorisation écrite explicite, limitée au périmètre et à la durée approuvés. Sans accord, rester sur l’inventaire géré, les journaux et les contrôles de configuration passifs.

## 🔎 Validation

Tester un compte pilote et une seule connexion approuvée, vérifier le TLS, le contrôle d’accès, les journaux et l’expiration de session. Pour rollback, désactiver le changement d’authentification ou de proxy selon le plan approuvé sans exposer l’interface directement; révoquer les secrets affectés. Vérifier aussi l’horodatage, la journalisation et l’absence de secrets dans les tickets ou exports; faire approuver le résultat par le propriétaire du service.

## ↩️ Retour arrière

Avant changement, conserver une sauvegarde ou un état de référence protégé, vérifier la possibilité réelle de restauration et garder un accès d’administration de secours approuvé. Si la validation échoue, interrompre le déploiement, restaurer la dernière configuration/package supporté selon la procédure éditeur, vérifier les services dépendants et consigner la cause. Ne pas improviser une procédure de restauration non documentée.

## 🚨 Alertes et remédiation

Préserver les journaux utiles, corréler avec les sources de supervision autorisées et ouvrir un incident/ticket attribué. Prioriser selon impact métier, exposition et avis éditeur; appliquer une correction supportée après validation, puis documenter le résultat. Toute action de confinement, révocation ou blocage doit suivre le plan d’incident approuvé et être traçable.

## 📚 Sources officielles

- [Apache Guacamole documentation](https://guacamole.apache.org/doc/gug/) — choisir la version, l’édition et le modèle correspondant au déploiement réel.
- [CIS Controls — documentation officielle](https://www.cisecurity.org/controls) — repères de gouvernance et gestion des actifs; adapter au contexte.

> Aucun numéro de version, niveau de licence ni prérequis produit n’est présumé dans cette fiche. Vérifier ces éléments dans le portail éditeur et le contrat de l’organisation avant toute mise en œuvre.

Fiches simples du guide : [cadrer le périmètre et les prérequis](/01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-cadrer-prerequis), [préparer les secrets et la configuration](/01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-preparer-secrets-compose), [initialiser le schéma PostgreSQL](/01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-initialiser-schema-postgresql), [démarrer et configurer le reverse proxy](/01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-demarrer-reverse-proxy), [sauvegarde et restauration](/01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-sauvegarde-restauration), [validation et contrôle d'accès](/01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-valider-controle-acces), [mise à jour et retour arrière](/01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-mise-a-jour-retour-arriere).