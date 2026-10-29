---
title: "Fiche Simple - VM Ubuntu 24.04 tcpdump Mise A Jour Retour Arriere"
description: "Mettre à jour tcpdump et libpcap, et revenir à la version précédente en cas de régression."
published: true
date: 2026-10-29T20:58:07Z
tags: ["tcpdump", "ubuntu24.04", "vie-du-logiciel", "mise-a-jour-retour-arriere"]
editor: markdown
dateCreated: 2026-10-29T20:58:07Z
dateModified: 2026-10-29T20:58:07Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_tcpdump_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à tcpdump
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : tcpdump / mise à jour et retour arrière
- **Tags** : `tcpdump`, `ubuntu24.04`, `vie-du-logiciel`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour tcpdump et libpcap, et revenir à la version précédente en cas de régression.

## 1. Hors-Production (Lab / Test / POC)

1. Consigner la version actuelle :
   ```bash
   tcpdump --version 2>&1 | head -n 2
   ```
   👉 Explication : Point de comparaison avant changement.

2. Mettre à jour le paquet :
   ```bash
   sudo apt update
   apt list --upgradable 2>/dev/null | grep -E "^(tcpdump|libpcap)"
   sudo apt install --only-upgrade tcpdump
   ```
   👉 Explication : Applique la version publiée par le dépôt du système; lire les notes de sécurité avant production.

3. Contrôler après mise à jour :
   ```bash
   tcpdump --version
   sudo tcpdump -D
   ```
   👉 Explication : Confirme que l’outil fonctionne et voit les interfaces.

4. Revenir en arrière si nécessaire :
   ```bash
   apt-cache madison tcpdump
   sudo apt install tcpdump=VERSION_ANTERIEURE
   ```
   👉 Explication : VERSION_ANTERIEURE est une version listée par `apt-cache madison` (à remplacer); elle doit encore être présente dans un dépôt autorisé. Sinon, restaurer le paquet depuis le miroir interne.

## 2. Production — Contrôles

Tester en lab, planifier la fenêtre, conserver la version précédente disponible.

## 3. Production — Sécurité

- Mettre à jour régulièrement : tcpdump analyse des données non fiables.
- Utiliser les dépôts approuvés uniquement.

## Validation et retour arrière

- **Validation** : La nouvelle version est installée et la capture de recette réussit.
- **Retour arrière** : Appliquer l’étape de retour arrière ci-dessus, puis relancer la recette.

## Si le problème n’est pas résolu

- [tcpdump — documentation officielle](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-tcpdump)
- [Étape précédente du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/tcpdump/fiche-simple-vm-ubuntu-24-04-tcpdump-sauvegarder-restaurer)