# Fiche_Simple_-_VM_Debian_13_OCS_Inventory_Comptes.md

- **Environnement** : VM Debian 13 dédiée, OCS Inventory 3.0 (Nginx, uWSGI, PostgreSQL local)
- **OS / Version** : Debian 13 Trixie; OCS Inventory 3.0; PostgreSQL 17
- **Catégorie** : inventaire de parc / ITSM
- **Tags** : `debian13`, `ocs-inventory`, `ocs3`, `postgresql`, `nginx`, `rbac`

---

## Problème précis à résoudre

Créer des comptes nominatifs et un compte agent distinct avec le minimum de permissions.

## 1. Hors-Production (Lab / Test / POC)

1. Se connecter à la console `https://ocs.example.net/` (nom d'exemple à remplacer) avec le compte administrateur initial.
   👉 Explication : ce compte sert seulement à créer les autres.

2. Dans la console, créer un compte nominatif par opérateur.
   👉 Explication : chaque action reste attribuable à une personne.

3. Créer un compte agent de service distinct, limité à consulter les inventaires et déposer les remontées.
   👉 Explication : un compte dédié limite l'impact d'une fuite du secret agent.

4. Réserver les droits d'administration et de déploiement aux opérateurs habilités.
   👉 Explication : ce guide n'active pas le déploiement distant de paquets.

## 2. Production — Contrôles

Revue périodique des comptes, rôle par personne, procédure d'arrivée et de départ.

## 3. Production — Sécurité

- Appliquer le moindre privilège.
- Ne pas partager le compte administrateur ni le secret du compte agent.

## Validation et retour arrière

- **Validation** : Chaque compte n'accède qu'aux fonctions prévues.
- **Retour arrière** : Désactiver ou supprimer le compte créé par erreur dans la console.

## Si le problème n'est pas résolu

- [OCS Inventory — Installation essentielle](https://documentation.ocsinventory-ng.org/quickstart-guides/for-administrators/installation-essentials.md)
- [Guide complet OCS Inventory 3 Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/41_Deploiement_OCS_Inventory_3_Debian_13.md#6-creer-les-comptes-et-les-permissions)
