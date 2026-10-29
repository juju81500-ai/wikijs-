# Fiche_Simple_-_VM_Debian_13_Nginx_Installer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Nginx des dépôts Debian
- **Catégorie** : serveur Web / Nginx / Installer

---

## Problème précis à résoudre

Installer Nginx depuis les dépôts Debian 13 et confirmer version, service et utilisateur d'exécution.

## 1. Hors-Production (Lab / Test / POC)

1. Mettre à jour l'index et relever la version candidate :
   ```bash
   sudo apt update
   apt-cache policy nginx
   ```
   👉 Explication : consigner la version et l'origine (dépôt Debian) avant d'installer.

2. Installer le paquet :
   ```bash
   sudo apt install -y nginx
   ```
   👉 Explication : le paquet crée l'utilisateur `www-data`, l'unité systemd et l'arborescence `/etc/nginx`.

3. Activer et démarrer le service :
   ```bash
   sudo systemctl enable --now nginx
   systemctl status nginx --no-pager
   ```
   👉 Explication : le service doit être `active (running)`.

4. Vérifier la version et la configuration :
   ```bash
   nginx -v
   sudo nginx -t
   ```
   👉 Explication : `nginx -t` valide la syntaxe ; à refaire avant chaque rechargement.

## 2. Production — Contrôles

Consigner la version installée, la source des paquets et la cadence de mise à jour de sécurité (`unattended-upgrades` si retenu).

## 3. Production — Sécurité

- Installer uniquement depuis le dépôt Debian ou le dépôt officiel nginx.org approuvé, sans binaire d'origine inconnue.
- Ne pas ouvrir le pare-feu avant la validation de la configuration.
- Supprimer la page d'accueil par défaut si le serveur n'est pas public.

## Validation et retour arrière

- **Validation** : `systemctl is-active nginx` renvoie `active` et `curl -I http://127.0.0.1/` renvoie `HTTP/1.1 200 OK`.
- **Retour arrière** : `sudo systemctl disable --now nginx` puis `sudo apt purge nginx nginx-common` (conserver `/etc/nginx` sauvegardé si besoin).

## Si le problème n'est pas résolu

- [Nginx — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-prerequis-limites)
- [Nginx — Configurer un site](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-configurer)
- [Nginx — Sécuriser (TLS, en-têtes, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-securiser)
- [Nginx — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-valider)
- [Nginx — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-sauvegarder-restaurer)
- [Nginx — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-mettre-a-jour)
- [Guide complet LEMP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb)
- [Nginx — documentation officielle](https://nginx.org/en/docs/)