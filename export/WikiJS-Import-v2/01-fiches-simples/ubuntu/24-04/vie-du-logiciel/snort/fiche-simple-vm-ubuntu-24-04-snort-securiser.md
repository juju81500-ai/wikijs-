---
title: "Fiche Simple - VM Ubuntu 24.04 Snort Securiser"
description: "Durcir Snort : compte dédié, droits minimaux, règles et journaux protégés."
published: true
date: 2026-10-29T21:00:24Z
tags: ["snort", "ubuntu24.04", "vie-du-logiciel", "securiser"]
editor: markdown
dateCreated: 2026-10-29T21:00:24Z
dateModified: 2026-10-29T21:00:24Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Snort_Securiser

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Snort
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Snort / sécurisation
- **Tags** : `snort`, `ubuntu24.04`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Durcir Snort : compte dédié, droits minimaux, règles et journaux protégés.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un compte de service :
   ```bash
   sudo useradd --system --no-create-home --shell /usr/sbin/nologin snort
   ```
   👉 Explication : Compte sans shell pour exécuter le capteur après acquisition; ne pas lui donner de sudo.

2. Fixer les droits :
   ```bash
   sudo chown -R root:snort /opt/snort3/etc /opt/snort3/rules
   sudo chmod -R o-rwx /opt/snort3/etc /opt/snort3/rules
   sudo chown snort:snort /var/log/snort
   sudo chmod 0750 /var/log/snort
   ```
   👉 Explication : Le compte lit la configuration mais ne peut pas la modifier; il écrit seulement dans les logs.

3. Donner uniquement les capacités de capture dans une unité systemd (à valider en lab) :
   ```bash
   sudo systemctl edit --force --full snort3-ids.service
   ```
   👉 Explication : Contenu type : `[Service]` `User=snort` `AmbientCapabilities=CAP_NET_RAW CAP_NET_ADMIN` `CapabilityBoundingSet=CAP_NET_RAW CAP_NET_ADMIN` `NoNewPrivileges=yes` `ExecStart=/opt/snort3/bin/snort -c /opt/snort3/etc/snort/snort.lua -i INTERFACE_AUTORISEE -A alert_fast -l /var/log/snort`. INTERFACE_AUTORISEE est à remplacer; unité à tester avant production.

4. Contrôler les ports :
   ```bash
   ss -tulpn | grep -i snort || echo "aucun port snort ouvert"
   ```
   👉 Explication : Un capteur passif n’écoute pas.

5. Règles et licences.
   👉 Explication : N’utiliser que des règles issues d’une source approuvée (par exemple l’archive de règles communautaires publiée par Snort, à vérifier sur snort.org); la clé d’accès (oinkcode) éventuelle se saisit via variable d’environnement ou fichier protégé, jamais dans la fiche.

## 2. Production — Contrôles

Revue trimestrielle des règles activées, des droits et de l’espace disque.

## 3. Production — Sécurité

- Journaux en 0750, rotation avec logrotate (à configurer).
- Transmettre les alertes vers un collecteur approuvé par canal chiffré (non détaillé).
- AppArmor : en cas de refus, `sudo journalctl -k | grep DENIED`.

## Validation et retour arrière

- **Validation** : Compte dédié, droits restrictifs, aucun port ouvert.
- **Retour arrière** : Supprimer l’unité (`sudo rm /etc/systemd/system/snort3-ids.service`, `sudo systemctl daemon-reload`) et restaurer les droits antérieurs.

## Si le problème n’est pas résolu

- [Snort — documentation officielle](https://www.snort.org/documents)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-snort)
- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-valider)
- [Étape précédente du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-configurer)