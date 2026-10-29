# Fiche_Simple_-_Docker_Snipe-IT_Recette.md

- **Environnement** : Hôte Docker avec Docker Compose v2 et réseau Traefik existant
- **OS / Version** : Hôte Linux maintenu; Snipe-IT 8.8.3; MariaDB 11.4.7
- **Catégorie** : ITSM / gestion des actifs
- **Tags** : `snipe-it`, `docker`, `mariadb`, `traefik`, `inventaire`

---

## Problème précis à résoudre

Vérifier le déploiement de bout en bout.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier certificat, URL publique et cookies sécurisés dans le navigateur.
   👉 Explication : confirme TLS et `SECURE_COOKIES`.

2. Vérifier l'absence d'accès direct à la base :
   ```bash
   sudo docker compose ps
   ```
   👉 Explication : Aucun port de MariaDB ne doit être publié sur l'hôte.

3. Créer un modèle, un statut déployable, un lieu et un actif de test : **Admin** puis les menus correspondants.
   👉 Explication : valide le fonctionnement de base.

4. Tester les permissions d'un compte non administrateur et l'envoi d'une notification.
   👉 Explication : contrôle les rôles et SMTP.

5. Tester la persistance :
   ```bash
   sudo docker compose restart
   sudo docker compose ps
   ```
   👉 Explication : Après redémarrage, base, images et pièces jointes doivent persister.

## 2. Production — Contrôles

Documenter le résultat de la recette.

## 3. Production — Sécurité

- Supprimer l'actif de test et les comptes de test avant l'import réel.

## Validation et retour arrière

- **Validation** : tous les points de la recette sont validés.
- **Retour arrière** : supprimer les données de test depuis l'interface.

## Si le problème n'est pas résolu

- [Snipe-IT — Docker Compose](https://snipe-it.readme.io/docs/docker)
- [Guide complet — étape 5](../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/39_Deploiement_Snipe_IT_8_Docker_MariaDB_Traefik.md#5-recette)
