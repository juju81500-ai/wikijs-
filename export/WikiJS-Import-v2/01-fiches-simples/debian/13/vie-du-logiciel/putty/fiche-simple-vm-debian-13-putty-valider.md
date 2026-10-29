---
title: "Fiche Simple - VM Debian 13 PuTTY Valider"
description: "Valider l'installation et la connexion de bout en bout."
published: true
date: 2026-10-29T21:24:09Z
tags: ["putty", "putty-tools", "plink", "puttygen", "ssh", "recette", "validation"]
editor: markdown
dateCreated: 2026-10-29T21:24:09Z
dateModified: 2026-10-29T21:24:09Z
---

# Fiche_Simple_-_VM_Debian_13_PuTTY_Valider

- **Environnement** : VM Debian 13 (Trixie), poste d'administration en ligne de commande
- **OS / Version** : Debian 13 (Trixie) — paquet putty-tools
- **Catégorie** : outils d'administration / SSH
- **Tags** : `putty`, `putty-tools`, `plink`, `puttygen`, `ssh`, `recette`, `validation`

---

## Problème précis à résoudre

Valider l'installation et la connexion de bout en bout.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les binaires :
   ```bash
   dpkg -L putty-tools | grep /usr/bin
   ```
   👉 Explication : cinq binaires attendus.
2. Tester la connexion `-batch` vers un serveur de lab :
   ```bash
   plink -batch -i ~/.ssh/CLE_A_REMPLACER.ppk UTILISATEUR@SERVEUR_SSH 'echo OK'
   ```
   👉 Explication : doit afficher OK.
3. Tester un transfert :
   ```bash
   echo test > essai.txt
   pscp -batch -i ~/.ssh/CLE_A_REMPLACER.ppk essai.txt UTILISATEUR@SERVEUR_SSH:/tmp/
   ```
   👉 Explication : le fichier doit être présent côté serveur.

## 2. Production — Contrôles

- Consigner la version et le résultat dans la recette.

## 3. Production — Sécurité

- Supprimer les fichiers de test.

## Validation et retour arrière

- **Validation** : les trois tests réussissent. **Retour arrière** : supprimer les fichiers de test.

## Si le problème n'est pas résolu

- [Fiche d'entrée PuTTY](/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-putty)
- [Debian — paquet putty-tools](https://packages.debian.org/trixie/putty-tools)
- [Documentation officielle PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html)