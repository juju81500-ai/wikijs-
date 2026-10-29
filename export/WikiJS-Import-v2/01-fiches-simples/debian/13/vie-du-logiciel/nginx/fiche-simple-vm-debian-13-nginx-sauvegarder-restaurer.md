---
title: "Fiche Simple - VM Debian 13 Nginx Sauvegarder Restaurer"
description: "Sauvegarder la configuration, les certificats et le contenu de Nginx, et prouver qu'ils sont restaurables."
published: true
date: 2026-10-29T20:32:41Z
tags: ["debian13", "nginx", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T20:32:41Z
dateModified: 2026-10-29T20:32:41Z
---

# Fiche_Simple_-_VM_Debian_13_Nginx_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Nginx des dépôts Debian
- **Catégorie** : serveur Web / Nginx / Sauvegarder et restaurer
- **Tags** : `debian13`, `nginx`, `sauvegarde`

---

## Problème précis à résoudre

Sauvegarder la configuration, les certificats et le contenu de Nginx, et prouver qu'ils sont restaurables.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une archive de configuration et de contenu :
   ```bash
   sudo install -d -m 0700 /var/backups/nginx
   sudo tar -czpf /var/backups/nginx/nginx-$(date +%F).tar.gz /etc/nginx /etc/ssl/nginx /var/www
   ```
   👉 Explication : l'archive contient aussi la clé privée : droits `0700` sur le dossier, copie hors machine chiffrée.

2. Lister le contenu pour contrôle :
   ```bash
   sudo tar -tzf /var/backups/nginx/nginx-$(date +%F).tar.gz | head -20
   ```
   👉 Explication : un fichier de sauvegarde jamais relu n'est pas une sauvegarde.

3. Restaurer sur une VM de test :
   ```bash
   sudo systemctl stop nginx
   sudo tar -xzpf /var/backups/nginx/nginx-DATE.tar.gz -C /
   sudo nginx -t && sudo systemctl start nginx
   ```
   👉 Explication : remplacer `DATE` par la date de l'archive (à remplacer) ; tester d'abord sur une VM pilote.

4. Copier la sauvegarde hors de la VM :
   ```bash
   sudo rsync -a /var/backups/nginx/ SAUVEGARDE_HOTE:/chemin/nginx/
   ```
   👉 Explication : remplacer `SAUVEGARDE_HOTE` et le chemin par la cible approuvée (voir fiches Restic / rsync du pack).

## 2. Production — Contrôles

Planifier la sauvegarde (cron ou timer), conserver plusieurs générations, chiffrer la copie externe et tester une restauration complète à chaque changement majeur.

## 3. Production — Sécurité

- Chiffrer toute copie contenant des clés privées.
- Droits `0700` sur `/var/backups/nginx`.
- Ne pas stocker la sauvegarde sur le même disque que le serveur.

## Validation et retour arrière

- **Validation** : restauration testée sur VM pilote : `nginx -t` OK et site accessible.
- **Retour arrière** : si la restauration échoue, repartir de l'archive précédente ; ne jamais écraser la dernière sauvegarde saine.

## Si le problème n'est pas résolu

- [Nginx — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-prerequis-limites)
- [Nginx — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-installer)
- [Nginx — Configurer un site](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-configurer)
- [Nginx — Sécuriser (TLS, en-têtes, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-securiser)
- [Nginx — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-valider)
- [Nginx — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-mettre-a-jour)
- [Guide complet LEMP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb)
- [Nginx — documentation officielle](https://nginx.org/en/docs/)