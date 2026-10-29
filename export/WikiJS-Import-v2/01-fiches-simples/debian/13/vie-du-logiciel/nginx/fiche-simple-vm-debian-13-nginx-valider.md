---
title: "Fiche Simple - VM Debian 13 Nginx Valider"
description: "Prouver que Nginx fonctionne, est sécurisé et supervisable avant la mise en service."
published: true
date: 2026-10-29T20:32:41Z
tags: ["debian13", "nginx", "recette"]
editor: markdown
dateCreated: 2026-10-29T20:32:41Z
dateModified: 2026-10-29T20:32:41Z
---

# Fiche_Simple_-_VM_Debian_13_Nginx_Valider

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Nginx des dépôts Debian
- **Catégorie** : serveur Web / Nginx / Valider (recette)
- **Tags** : `debian13`, `nginx`, `recette`

---

## Problème précis à résoudre

Prouver que Nginx fonctionne, est sécurisé et supervisable avant la mise en service.

## 1. Hors-Production (Lab / Test / POC)

1. Tester la configuration et l'état du service :
   ```bash
   sudo nginx -T | head -40
   systemctl is-active nginx
   systemctl is-enabled nginx
   ```
   👉 Explication : `nginx -T` affiche la configuration effective (ne pas la diffuser : elle peut contenir des chemins ou des secrets).

2. Tester les réponses HTTP et HTTPS :
   ```bash
   curl -sI http://SITE.example.net/ | head -5
   curl -sI https://SITE.example.net/ | head -8
   ```
   👉 Explication : vérifier code 301/200, absence de version dans `Server`, présence des en-têtes de sécurité. Remplacer `SITE.example.net`.

3. Vérifier les ports et les journaux :
   ```bash
   sudo ss -tlnp | grep nginx
   sudo tail -n 20 /var/log/nginx/error.log
   ```
   👉 Explication : seuls 80 et 443 (et les ports prévus) doivent écouter ; aucune erreur récurrente.

4. Tester un rechargement sans coupure :
   ```bash
   sudo systemctl reload nginx
   curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1/
   ```
   👉 Explication : le rechargement ne doit pas interrompre le service.

## 2. Production — Contrôles

Conserver le résultat de la recette (date, version, commandes, opérateur) dans le dossier d'exploitation et ouvrir la supervision (HTTP 200, certificat, espace disque).

## 3. Production — Sécurité

- Ne pas laisser de contenu de test ni de certificat auto-signé en production.
- Ne jamais copier `nginx -T` dans un ticket public.
- Vérifier que les journaux ne contiennent pas de jetons dans les URL.

## Validation et retour arrière

- **Validation** : tous les contrôles ci-dessus réussis et consignés.
- **Retour arrière** : si un contrôle échoue, ne pas ouvrir au public ; revenir à la configuration sauvegardée (fiche Sauvegarder / restaurer).

## Si le problème n'est pas résolu

- [Nginx — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-prerequis-limites)
- [Nginx — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-installer)
- [Nginx — Configurer un site](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-configurer)
- [Nginx — Sécuriser (TLS, en-têtes, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-securiser)
- [Nginx — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-sauvegarder-restaurer)
- [Nginx — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-mettre-a-jour)
- [Guide complet LEMP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb)
- [Nginx — documentation officielle](https://nginx.org/en/docs/)