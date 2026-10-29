---
title: "Fiche Simple - VM Ubuntu 24.04 Snort Configurer"
description: "Configurer Snort 3 en détection passive avec HOMENET et des règles approuvées."
published: true
date: 2026-10-29T21:00:24Z
tags: ["snort", "ubuntu24.04", "vie-du-logiciel", "configurer"]
editor: markdown
dateCreated: 2026-10-29T21:00:24Z
dateModified: 2026-10-29T21:00:24Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Snort_Configurer

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Snort
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Snort / configuration IDS passif
- **Tags** : `snort`, `ubuntu24.04`, `vie-du-logiciel`, `configurer`

---

## Problème précis à résoudre

Configurer Snort 3 en détection passive avec HOME_NET et des règles approuvées.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration livrée :
   ```bash
   sudo cp -a /opt/snort3/etc/snort/snort.lua /opt/snort3/etc/snort/snort.lua.before-change
   ```
   👉 Explication : Retour arrière possible.

2. Créer le répertoire de règles et de logs :
   ```bash
   sudo install -d -m 0750 /opt/snort3/rules /var/log/snort
   ```
   👉 Explication : Sépare règles et alertes avec des droits restreints.

3. Éditer la configuration :
   ```bash
   sudoedit /opt/snort3/etc/snort/snort.lua
   ```
   👉 Explication : Définir `HOME_NET = 'HOME_NET_AUTORISE'` (à remplacer), `EXTERNAL_NET = '!$HOME_NET'`, charger les règles dans le bloc `ips` (`include = RULE_PATH .. '/local.rules'`) et configurer `alert_fast = { file = true }`. Laisser le mode détection : aucune action de blocage ni module inline.

4. Créer une règle locale de test inoffensive :
   ```bash
   echo 'alert icmp any any -> any any (msg:"TEST Snort ICMP lab"; sid:1000001; rev:1;)' | sudo tee /opt/snort3/rules/local.rules
   ```
   👉 Explication : Alerte sur ICMP pour la recette; sid ≥ 1000000 est réservé aux règles locales. Retirer cette règle après la recette.

5. Tester la configuration :
   ```bash
   sudo /opt/snort3/bin/snort -c /opt/snort3/etc/snort/snort.lua -T
   ```
   👉 Explication : `-T` valide configuration et règles sans capturer; il doit se terminer sans erreur. Selon la release, des chemins de plug-ins/règles peuvent nécessiter un ajustement (voir README).

## 2. Production — Contrôles

Faire relire HOME_NET, source de règles et sortie d’alerte par le propriétaire du réseau.

## 3. Production — Sécurité

- Séparer interface de gestion et de capture.
- Pas de mode inline ni d’action de blocage.
- AppArmor : en cas de refus, `sudo journalctl -k | grep DENIED`.

## Validation et retour arrière

- **Validation** : `snort -T` réussit; le capteur n’est pas encore démarré.
- **Retour arrière** : Restaurer `/opt/snort3/etc/snort/snort.lua.before-change` et relancer `snort -T`.

## Si le problème n’est pas résolu

- [Snort — documentation officielle](https://www.snort.org/documents)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-snort)
- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-securiser)
- [Étape précédente du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-installer)