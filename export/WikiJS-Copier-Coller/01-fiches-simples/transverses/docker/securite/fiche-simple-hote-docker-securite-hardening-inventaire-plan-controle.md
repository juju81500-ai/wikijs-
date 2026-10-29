# Fiche_Simple_-_Hote_Docker_Securite_Hardening_Inventaire_Plan_Controle.md

- **Environnement** : Hôte Linux dédié exécutant Docker Engine et des stacks Compose
- **OS / Version** : Distribution Linux maintenue; Docker Engine supporté
- **Catégorie** : docker / sécurité

---

## Problème précis à résoudre

Savoir qui contrôle Docker et ce qui est exposé.

## 1. Hors-Production (Lab / Test / POC)

1. Relever version, configuration et conteneurs :
   ```bash
   docker version
   docker info
   docker ps --no-trunc
   ```
   👉 Explication : inventaire du moteur et des conteneurs en cours.

2. Lister les ports en écoute :
   ```bash
   ss -lntup
   ```
   👉 Explication : repère l'exposition réseau, notamment une API Docker en TCP.

3. Lister les membres du groupe `docker` :
   ```bash
   getent group docker
   ```
   👉 Explication : l'appartenance à ce groupe équivaut à un accès root.

4. Noter utilisateurs autorisés, ports publiés, volumes, images, réseaux et tâches de maintenance.
   👉 Explication : base de référence pour la suite.

## 2. Production — Contrôles

Utiliser un compte d'administration nominatif et une console de secours.

## 3. Production — Sécurité

- Ne jamais monter le socket Docker dans une application ordinaire.
- Éviter l'exposition TCP de l'API; traiter le groupe `docker` comme root.

## Validation et retour arrière

- **Validation** : Inventaire écrit et accès au socket limités.
- **Retour arrière** : Aucune modification n'est faite ici.

## Si le problème n'est pas résolu

- [Docker — sécurité du moteur](https://docs.docker.com/engine/security/)
- [Docker — bonnes pratiques de build](https://docs.docker.com/build/building/best-practices/)
- [Guide complet — 1. Inventorier et protéger le plan de contrôle](/02-fiches-completes/transverses/docker/autres/32-hardening-hote-docker-production#1-inventorier-et-proteger-le-plan-de-controle)