---
title: "Fiche Simple - VM Debian 13 Snort Securiser"
description: "Protéger règles, configuration et alertes d’un capteur passif."
published: true
date: 2026-10-29T20:35:43Z
tags: ["snort", "debian13", "vie-du-logiciel", "securiser"]
editor: markdown
dateCreated: 2026-10-29T20:35:43Z
dateModified: 2026-10-29T20:35:43Z
---

# Fiche_Simple_-_VM_Debian_13_Snort_Securiser

- **Environnement** : VM Debian 13 dédiée à Snort IDS passif
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : Snort IDS passif / sécuriser
- **Tags** : `snort`, `debian13`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Protéger règles, configuration et alertes d’un capteur passif.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler propriétaire et permissions du répertoire installé :
   ```bash
   sudo stat -c "%a %U:%G %n" /etc/snort
   ```
   👉 Explication : Seules les identités d’administration doivent modifier règles et configuration.

2. Vérifier que l’interface de capture n’a pas d’adresse d’administration :
   ```bash
   ip -br address
   ```
   👉 Explication : Maintenir l’accès d’administration sur une interface distincte; ne pas modifier le réseau sans fenêtre approuvée.

3. Contrôler destination et permissions des journaux livrés par le paquet.
   👉 Explication : Protéger alertes et captures selon leur classification, leur rétention et les droits approuvés.

## 2. Production — Contrôles

Vérifier comptes de service, permissions effectives, rotation des journaux, horloge et flux autorisés.

## 3. Production — Sécurité

- Capteur passif seulement; ne pas activer NFQUEUE, bridge inline, drop/reject ni réponse automatique.

## Validation et retour arrière

- **Validation** : Règles protégées, capture passive et journaux accessibles aux seuls rôles autorisés.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [Snort IDS passif — documentation officielle](https://www.snort.org/documents)
- [Étape suivante du guide](/01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-valider)