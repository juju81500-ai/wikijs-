---
title: "Fiche Simple - VM Debian 13 tcpdump Installer"
description: "Installer tcpdump depuis les dépôts Debian approuvés."
published: true
date: 2026-10-29T20:35:43Z
tags: ["tcpdump", "debian13", "vie-du-logiciel", "installer"]
editor: markdown
dateCreated: 2026-10-29T20:35:43Z
dateModified: 2026-10-29T20:35:43Z
---

# Fiche_Simple_-_VM_Debian_13_tcpdump_Installer

- **Environnement** : VM Debian 13 dédiée à tcpdump
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : tcpdump / installer
- **Tags** : `tcpdump`, `debian13`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer tcpdump depuis les dépôts Debian approuvés.

## 1. Hors-Production (Lab / Test / POC)

1. Actualiser les index et vérifier le candidat :
   ```bash
   sudo apt update
   apt-cache policy tcpdump
   ```
   👉 Explication : Confirmer la provenance du paquet.

2. Installer l’outil et consigner sa version :
   ```bash
   sudo apt install tcpdump
   tcpdump --version
   ```
   👉 Explication : Utiliser les mises à jour Debian et vérifier les avis de sécurité.

3. Lister les interfaces détectées :
   ```bash
   sudo tcpdump -D
   ```
   👉 Explication : La liste ne vaut pas autorisation; sélectionner l’interface explicitement approuvée.

## 2. Production — Contrôles

Consigner version et origine; identifier quel compte peut obtenir des privilèges de capture.

## 3. Production — Sécurité

- Ne pas attribuer de capacités root permanentes au binaire sans analyse de risque.

## Validation et retour arrière

- **Validation** : tcpdump --version répond et l’interface autorisée est identifiée.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [tcpdump — documentation officielle](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Étape suivante du guide](/01-fiches-simples/debian/13/vie-du-logiciel/tcpdump/fiche-simple-vm-debian-13-tcpdump-configurer)