---
title: "Fiche Simple - VM Debian 13 Apache Mettre A Jour"
description: "Mettre à jour Apache et revenir en arrière en cas de régression."
published: true
date: 2026-10-29T20:32:41Z
tags: ["debian13", "apache", "mise-a-jour"]
editor: markdown
dateCreated: 2026-10-29T20:32:41Z
dateModified: 2026-10-29T20:32:41Z
---

# Fiche_Simple_-_VM_Debian_13_Apache_Mettre_A_Jour

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Apache HTTP Server
- **Catégorie** : serveur Web / Apache / Mise à jour et retour arrière
- **Tags** : `debian13`, `apache`, `mise-a-jour`

---

## Problème précis à résoudre

Mettre à jour Apache et revenir en arrière en cas de régression.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration :
   ```bash
   sudo tar -czpf /var/backups/apache2/avant-maj-$(date +%F).tar.gz /etc/apache2
   ```
   👉 Explication : base du retour arrière.

2. Identifier la mise à jour :
   ```bash
   sudo apt update
   apt list --upgradable 2>/dev/null | grep -i apache2
   apt-cache policy apache2
   ```
   👉 Explication : noter version actuelle et cible.

3. Appliquer et contrôler :
   ```bash
   sudo apt install --only-upgrade apache2
   sudo apache2ctl configtest && sudo systemctl restart apache2
   apache2 -v
   ```
   👉 Explication : tester la syntaxe avant le redémarrage.

4. Revenir en arrière :
   ```bash
   sudo apt install apache2=VERSION_PRECEDENTE apache2-bin=VERSION_PRECEDENTE apache2-data=VERSION_PRECEDENTE apache2-utils=VERSION_PRECEDENTE
   sudo apt-mark hold apache2
   ```
   👉 Explication : remplacer `VERSION_PRECEDENTE` par la version relevée (vérifier sa disponibilité) ; lever le blocage avec `apt-mark unhold apache2` ensuite.

## 2. Production — Contrôles

Pilote d'abord, fenêtre approuvée, sauvegarde préalable et surveillance des journaux ensuite.

## 3. Production — Sécurité

- Pas de mise à jour directe en production sans pilote.
- Consigner tout `apt-mark hold`.
- Relire les avis de sécurité Debian.

## Validation et retour arrière

- **Validation** : `apache2 -v` affiche la version cible et le site répond.
- **Retour arrière** : réinstaller la version précédente, restaurer `/etc/apache2`, `configtest`, redémarrer.

## Si le problème n'est pas résolu

- [Apache — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-valider)
- [Apache — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-sauvegarder-restaurer)
- [Guide complet Apache Debian 13](/02-fiches-completes/debian/13/installation-deploiement/124-deploiement-apache-http-server-debian-13)
- [Apache HTTP Server — documentation](https://httpd.apache.org/docs/2.4/)