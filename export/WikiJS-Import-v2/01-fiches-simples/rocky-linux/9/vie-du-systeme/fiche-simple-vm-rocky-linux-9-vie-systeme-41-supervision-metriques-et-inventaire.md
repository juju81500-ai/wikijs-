---
title: "Fiche Simple - VM Rocky Linux 9 Vie Systeme 41 Supervision Metriques Et Inventaire"
description: "Superviser la machine."
published: true
date: 2026-10-29T20:22:10Z
tags: ["rocky9", "vie-du-systeme", "cycle-de-vie", "etape-41"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_41_Supervision_Metriques_Et_Inventaire

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 41 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-41`

---

## Problème précis à résoudre

Superviser la machine.

## 1. Hors-Production (Lab / Test / POC)

1. Installer l'agent Zabbix (dépôt Zabbix déjà ajouté) :
   ```bash
   sudo dnf install -y zabbix-agent2
   sudo systemctl enable --now zabbix-agent2
   ```
   👉 Explication : agent de supervision; version 2 recommandée.

2. Configurer le serveur (adapter `ZBX.EXEMPLE.LAN`) :
   ```bash
   sudo sed -i 's/^Server=.*/Server=ZBX.EXEMPLE.LAN/; s/^ServerActive=.*/ServerActive=ZBX.EXEMPLE.LAN/' /etc/zabbix/zabbix_agent2.conf
   sudo systemctl restart zabbix-agent2
   ```
   👉 Explication : indique le serveur autorisé.

3. Ouvrir le port 10050 pour le serveur :
   ```bash
   sudo firewall-cmd --permanent --add-port=10050/tcp
   sudo firewall-cmd --reload
   ```
   👉 Explication : autorise la collecte.

## 2. Production — Contrôles

Seuils et alertes documentés.

## 3. Production — Sécurité

Restreindre la source autorisée au serveur de supervision.

## Validation et retour arrière

- **Validation** : L'hôte apparaît disponible dans l'outil de supervision.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Rocky 9 Supervision Zabbix Agent2](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/zabbix/fiche-simple-vm-rocky-9-supervision-zabbix-agent2>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)