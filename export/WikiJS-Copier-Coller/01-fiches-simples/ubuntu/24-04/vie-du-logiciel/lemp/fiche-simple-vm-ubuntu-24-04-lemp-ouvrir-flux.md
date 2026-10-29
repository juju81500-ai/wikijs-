# Fiche_Simple_-_VM_Ubuntu_24.04_LEMP_Ouvrir_Flux.md

- **Environnement** : VM Ubuntu Server 24.04 dédiée à une application Web PHP
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble); Nginx, PHP 8.3, MariaDB 10.11
- **Catégorie** : web / pare-feu

---

## Problème précis à résoudre

Autoriser seulement les flux Web utiles.

## 1. Hors-Production (Lab / Test / POC)

1. Lire l'état du pare-feu réellement géré (UFW d'après la fiche du même OS) :
   ```bash
   sudo ufw status verbose
   ```
   👉 Explication : identifie les règles actuelles avant modification.

2. Autoriser HTTP (ACME/redirection) et HTTPS :
   ```bash
   sudo ufw allow 80/tcp
   sudo ufw allow 443/tcp
   ```
   👉 Explication : ouvre uniquement 80 et 443.

3. Contrôler les ports en écoute :
   ```bash
   sudo ss -tlnp | grep -E ':(80|443|3306)\b'
   ```
   👉 Explication : 3306 ne doit pas être publié.

## 2. Production — Contrôles

Restreindre SSH au réseau d'administration.

## 3. Production — Sécurité

- Ne pas ajouter de règle `nft` runtime comme configuration finale.
- Ne pas désactiver UFW globalement.

## Validation et retour arrière

- **Validation** : 80 et 443 joignables, 3306 non exposé.
- **Retour arrière** : `sudo ufw delete allow 80/tcp` et `sudo ufw delete allow 443/tcp`.

## Si le problème n'est pas résolu

- [Nginx — documentation](https://nginx.org/en/docs/)
- [Ubuntu 24.04 — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
- [Guide complet LEMP Ubuntu 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/20-pile-lemp-ubuntu-server-24-04-nginx-php83-mariadb#6-ouvrir-les-flux-necessaires)