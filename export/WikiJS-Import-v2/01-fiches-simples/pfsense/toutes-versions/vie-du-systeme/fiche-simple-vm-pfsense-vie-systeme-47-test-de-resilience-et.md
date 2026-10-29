---
title: "Fiche Simple - VM pfSense Vie Systeme 47 Test De Resilience Et"
description: "Vérifier le comportement lors d'une panne et les alertes."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-47"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_47_Test_De_Resilience_Et

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 47 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-47`

---

## Problème précis à résoudre

Vérifier le comportement lors d'une panne et les alertes.

## 1. Hors-Production (Lab / Test / POC)

1. Simuler la perte du WAN (désactiver l'interface virtuelle) et observer Status > Gateways.
   👉 Explication : la bascule (groupe de passerelles) ou l'alerte doit se produire.

2. Avec CARP (si HA, Firewall > Virtual IPs et System > High Avail. Sync) : Status > CARP (failover) > Enter Persistent CARP Maintenance Mode. En shell :
   ```sh
   sysctl net.inet.carp.allow
   ifconfig vtnet0 | grep carp
   ```
   👉 Explication : montre l'état MASTER/BACKUP des adresses virtuelles.

3. Confirmer que la supervision a émis l'alerte attendue.
   👉 Explication : valide la chaîne d'alerte de bout en bout.

## 2. Production — Contrôles

Documenter le temps de bascule mesuré.

## 3. Production — Sécurité

Réaliser le test hors des heures de production.

## Validation et retour arrière

- **Validation** : Alerte reçue et service rétabli dans le délai prévu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)