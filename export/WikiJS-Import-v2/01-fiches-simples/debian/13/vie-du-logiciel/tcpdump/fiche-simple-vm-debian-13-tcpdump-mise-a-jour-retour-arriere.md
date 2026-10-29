---
title: "Fiche Simple - VM Debian 13 tcpdump Mise A Jour Retour Arriere"
description: "Mettre tcpdump à jour tout en préservant les captures existantes et la possibilité de diagnostic."
published: true
date: 2026-10-29T20:35:43Z
tags: ["tcpdump", "debian13", "vie-du-logiciel", "mise_a_jour_retour_arriere"]
editor: markdown
dateCreated: 2026-10-29T20:35:43Z
dateModified: 2026-10-29T20:35:43Z
---

# Fiche_Simple_-_VM_Debian_13_tcpdump_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13 dédiée à tcpdump
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : tcpdump / mise à jour et retour arrière
- **Tags** : `tcpdump`, `debian13`, `vie-du-logiciel`, `mise_a_jour_retour_arriere`

---

## Problème précis à résoudre

Mettre tcpdump à jour tout en préservant les captures existantes et la possibilité de diagnostic.

## 1. Hors-Production (Lab / Test / POC)

1. Consigner version installée, candidat et avis Debian :
   ```bash
   dpkg-query -W tcpdump
   apt-cache policy tcpdump
   apt list --upgradable
   ```
   👉 Explication : Vérifier que le candidat provient des dépôts approuvés.

2. Vérifier les captures en cours et sauvegarder les paramètres nécessaires avant changement.
   👉 Explication : Arrêter proprement une capture finie; ne pas interrompre un diagnostic actif sans coordination.

3. Après approbation, mettre à jour et valider la version :
   ```bash
   sudo apt update
   sudo apt install --only-upgrade tcpdump
   tcpdump --version
   ```
   👉 Explication : Effectuer une petite capture locale approuvée puis relire un pcap test.

## 2. Production — Contrôles

Planifier la fenêtre et contrôler compatibilité libpcap, permissions et procédure d’analyse.

## 3. Production — Sécurité

- Ne pas rétrograder à une version vulnérable sans dérogation; conserver les captures selon leur politique, pas par défaut.

## Validation et retour arrière

- **Validation** : Version attendue, capture d’essai relue et droits de fichier conformes.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [tcpdump — documentation officielle](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Étape suivante du guide](/01-fiches-simples/debian/13/vie-du-logiciel/tcpdump/fiche-simple-vm-debian-13-tcpdump-prerequis-limites)