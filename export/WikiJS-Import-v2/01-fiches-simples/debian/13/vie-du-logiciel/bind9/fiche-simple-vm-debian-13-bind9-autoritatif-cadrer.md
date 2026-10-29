---
title: "Fiche Simple - VM Debian 13 BIND9 Autoritatif Cadrer"
description: "Définir le périmètre du serveur DNS autoritatif et vérifier les prérequis avant toute installation."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "bind9", "dns", "cadrage"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_BIND9_Autoritatif_Cadrer.md

- **Environnement** : VM Debian 13 pour un DNS autoritatif de laboratoire
- **OS / Version** : Debian 13 Trixie; paquets bind9 de la distribution
- **Catégorie** : dns / cadrage
- **Tags** : `debian13`, `bind9`, `dns`, `cadrage`

---

## Problème précis à résoudre

Définir le périmètre du serveur DNS autoritatif et vérifier les prérequis avant toute installation.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier qu'aucun service n'écoute déjà sur le port 53 :
   ```bash
   sudo ss -lntup '( sport = :53 )'
   ```
   👉 Explication : la commande ne doit rien afficher; sinon un autre service occupe déjà DNS et doit être traité avant.

2. Relever l'adresse IP statique du serveur :
   ```bash
   ip -br address
   ```
   👉 Explication : on note l'adresse à utiliser pour `listen-on`; les valeurs `lab.example.test`, `192.0.2.0/24` et `192.0.2.53` du guide sont des exemples à remplacer par votre plan réel.

3. Sauvegarder la configuration existante avant modification :
   ```bash
   sudo tar -czf "$HOME/bind-avant-changement.tar.gz" /etc/bind
   ```
   👉 Explication : on garde une copie de `/etc/bind` pour pouvoir revenir en arrière (ignorer l'erreur si le dossier n'existe pas encore).

4. Prévoir une console hors bande ou une session d'administration indépendante du DNS.
   👉 Explication : si la configuration DNS échoue, l'accès d'administration ne doit pas en dépendre.

## 2. Production — Contrôles

Décider du rôle exact (autoritatif seulement, sans résolveur récursif ni mises à jour dynamiques), du plan d'adressage, de la zone et du propriétaire de la zone.

## 3. Production — Sécurité

- Ne pas reprendre les valeurs d'exemple (`192.0.2.0/24`) comme plan réel.
- Ne pas mélanger autoritatif et récursif sur le même serveur.
- Garder un accès d'administration indépendant du DNS.

## Validation et retour arrière

- **Validation** : Aucun autre service sur le port 53; adresse statique relevée; sauvegarde de `/etc/bind` disponible.
- **Retour arrière** : Rien n'a été modifié à cette étape; supprimer l'archive de sauvegarde si elle est inutile.

## Si le problème n'est pas résolu

- [ISC BIND 9 — Configurations and Zone Files](https://bind9.readthedocs.io/en/latest/chapter3.html)
- [Debian — paquet bind9 Trixie](https://packages.debian.org/trixie/bind9)
- [Guide complet BIND9 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/63-deploiement-bind9-autoritatif-debian-13#1-perimetre-et-prerequis)