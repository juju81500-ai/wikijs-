---
title: "Fiche Simple - VM OPNsense Vie Systeme 41 Supervision Metriques Et Inventaire"
description: "Surveiller l'état et les performances."
published: true
date: 2026-10-29T20:22:10Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-41"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_41_Supervision_Metriques_Et_Inventaire

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 41 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-41`

---

## Problème précis à résoudre

Surveiller l'état et les performances.

## 1. Hors-Production (Lab / Test / POC)

1. Activer SNMP : Services > Net-SNMP (plugin `os-net-snmp`), renseigner la communauté/utilisateur et limiter à l'adresse du serveur de supervision.
   👉 Explication : permet à la supervision de lire les métriques.

2. Consulter Rapports > Santé et Lobby > Tableau de bord; ou installer `os-telegraf` / `os-zabbix-agent` pour exporter les métriques.
   👉 Explication : affiche CPU, mémoire, trafic et état des passerelles.

3. Contrôler en shell :
   ```sh
   snmpwalk -v2c -c COMMUNAUTE IP_LAN system 2>/dev/null | head -3
   top -b -n1 | head -10
   ```
   👉 Explication : `COMMUNAUTE` est la chaîne de lecture SNMP; vérifie la réponse et la charge.

## 2. Production — Contrôles

Alerter sur la charge, l'espace disque, l'état des passerelles et des tunnels.

## 3. Production — Sécurité

Utiliser SNMPv3 si possible; ne jamais laisser la communauté `public`.

## Validation et retour arrière

- **Validation** : La supervision reçoit les métriques.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : Appliance OPNsense Supervision Syslog](</01-fiches-simples/opnsense/toutes-versions/vie-du-logiciel/supervision/fiche-simple-appliance-opnsense-supervision-syslog>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)