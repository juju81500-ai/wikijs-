---
title: "Fiche Simple - VM Debian 13 Apache Retour Arriere"
description: "Retirer proprement le site pilote ou annuler une modification sans perturber les autres hôtes virtuels."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "apache", "rollback", "configuration", "changement"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Apache_Retour_Arriere.md

- **Environnement** : VM Debian 13 Trixie avec configuration Apache sauvegardée
- **OS / Version** : Debian 13 Trixie; Apache HTTP Server
- **Catégorie** : serveur Web / gestion du changement
- **Tags** : `debian13`, `apache`, `rollback`, `configuration`, `changement`

---

## Problème précis à résoudre

Retirer proprement le site pilote ou annuler une modification sans perturber les autres hôtes virtuels.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder avant le changement :
   ```bash
   sudo apache2ctl -S > /tmp/apache-S-avant.txt 2>&1
   sudo cp -a /etc/apache2/sites-available /root/apache-sites-available.bak
   ```
   👉 Explication : conserve l'état des hôtes virtuels.

2. Désactiver les sites pilote :
   ```bash
   sudo a2dissite pilote-ssl.conf
   sudo a2dissite pilote.conf
   ```
   👉 Explication : ne pas désactiver un site ou module partagé sans vérifier ses dépendances.

3. Tester et recharger :
   ```bash
   sudo apache2ctl configtest
   sudo systemctl reload apache2
   ```
   👉 Explication : si le service ne revient pas, couper la publication par le mécanisme réseau approuvé et restaurer les fichiers sauvegardés.

## 2. Production — Contrôles

Toute restauration de production doit avoir une fenêtre approuvée, un responsable, une sauvegarde vérifiée et une procédure coordonnée avec les propriétaires applicatifs et réseau.

## 3. Production — Sécurité

- Ne pas supprimer ni désactiver un vhost, module, certificat ou site partagé sans analyse de dépendances.
- Ne pas exécuter de nettoyage large de `/etc/apache2` ou de `/var/www`.
- Conserver les journaux utiles à l'analyse et protéger les copies de configuration contenant des informations sensibles.
- Si le service ne revient pas, limiter les flux avec le pare-feu approuvé plutôt que d'improviser une exposition.

## Validation et retour arrière

- **Validation** : configuration syntaxiquement valide, service actif, site concerné retiré et autres sites disponibles.
- **Retour arrière** : réappliquer le dernier fichier approuvé et revalider; ne pas répéter des opérations destructives.

## Si le problème n'est pas résolu

- [Apache HTTP Server — apachectl](https://httpd.apache.org/docs/2.4/programs/apachectl.html)
- [Apache HTTP Server — hôtes virtuels](https://httpd.apache.org/docs/2.4/vhosts/)
- [Guide complet Apache Debian 13](/02-fiches-completes/debian/13/installation-deploiement/124-deploiement-apache-http-server-debian-13#6-retour-arriere)