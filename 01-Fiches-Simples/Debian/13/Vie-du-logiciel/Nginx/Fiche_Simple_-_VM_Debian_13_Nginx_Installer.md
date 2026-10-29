# Fiche_Simple_-_VM_Debian_13_Nginx_Installer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Nginx des dépôts Debian
- **Catégorie** : serveur Web / Nginx / Installer
- **Tags** : `debian13`, `nginx`, `installation`

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

- [Nginx — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_Nginx_Prerequis_Limites.md)
- [Nginx — Configurer un site](Fiche_Simple_-_VM_Debian_13_Nginx_Configurer.md)
- [Nginx — Sécuriser (TLS, en-têtes, pare-feu)](Fiche_Simple_-_VM_Debian_13_Nginx_Securiser.md)
- [Nginx — Valider (recette)](Fiche_Simple_-_VM_Debian_13_Nginx_Valider.md)
- [Nginx — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_Nginx_Sauvegarder_Restaurer.md)
- [Nginx — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_Nginx_Mettre_A_Jour.md)
- [Guide complet LEMP Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/02_Pile_LEMP_Debian_13_Nginx_PHP_MariaDB.md)
- [Nginx — documentation officielle](https://nginx.org/en/docs/)
