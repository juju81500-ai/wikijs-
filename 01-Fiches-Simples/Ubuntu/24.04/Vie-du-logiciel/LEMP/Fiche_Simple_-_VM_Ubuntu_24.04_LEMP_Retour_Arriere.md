# Fiche_Simple_-_VM_Ubuntu_24.04_LEMP_Retour_Arriere.md

- **Environnement** : VM Ubuntu Server 24.04 dédiée à une application Web PHP
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble); Nginx, PHP 8.3, MariaDB 10.11
- **Catégorie** : web / retour arrière
- **Tags** : `ubuntu24.04`, `nginx`, `php8.3`, `mariadb`, `lemp`, `rollback`

---

## Problème précis à résoudre

Pouvoir revenir à l'état précédent après un changement applicatif ou PHP.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration Nginx avant changement :
   ```bash
   sudo cp -a /etc/nginx /etc/nginx.avant-changement
   ```
   👉 Explication : copie datée pour restauration.

2. Sauvegarder la base (le mot de passe est demandé interactivement; remplacer `appdb`) :
   ```bash
   sudo mariadb-dump --single-transaction appdb > appdb-avant.sql
   ```
   👉 Explication : indispensable avant une migration de schéma.

3. En cas d'échec, restaurer le site précédent puis tester et recharger :
   ```bash
   sudo nginx -t
   sudo systemctl reload nginx
   ```
   👉 Explication : ne recharge qu'une configuration valide.

## 2. Production — Contrôles

Prévoir un plan de restauration cohérent code + base.

## 3. Production — Sécurité

- Protéger le fichier de dump (`chmod 600`) et le transférer hors VM chiffré.

## Validation et retour arrière

- **Validation** : ancien site rétabli, `nginx -t` OK.
- **Retour arrière** : revenir uniquement à l'ancien code peut ne pas suffire après migration de schéma: restaurer aussi la base sauvegardée.

## Si le problème n'est pas résolu

- [Nginx — documentation](https://nginx.org/en/docs/)
- [Ubuntu 24.04 — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
- [Guide complet LEMP Ubuntu 24.04](../../../../../02-Fiches-Completes/Ubuntu/24.04/Installation-Deploiement/20_Pile_LEMP_Ubuntu_Server_24.04_Nginx_PHP83_MariaDB.md#8-retour-arriere)
