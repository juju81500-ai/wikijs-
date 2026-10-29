---
title: "Fiche Simple - VM Windows Server 2022 PRTG Ajouter Appareil Pilote"
description: "Ajouter un actif autorisé dans PRTG et valider un nombre réduit de capteurs avant d'étendre la supervision."
published: true
date: 2026-10-29T19:26:46Z
tags: ["windows-server", "prtg", "supervision", "snmp", "wmi", "scan-pilote"]
editor: markdown
dateCreated: 2026-10-29T19:26:46Z
dateModified: 2026-10-29T19:26:46Z
---

# 📄 Fiche_Simple_-_VM_Windows_Server_2022_PRTG_Ajouter_Appareil_Pilote.md

- **Environnement** : Serveur Windows exécutant PRTG Network Monitor
- **OS / Version** : Windows Server 2022/2025; PRTG version maintenue
- **Catégorie** : Supervision / configuration
- **Tags** : `windows-server`, `prtg`, `supervision`, `snmp`, `wmi`, `scan-pilote`

---

## 🎯 Problème précis à résoudre

Ajouter un actif autorisé dans PRTG et valider un nombre réduit de capteurs avant d'étendre la supervision.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Confirmer adresse et protocole activé sur l'appareil de lab :
   ```powershell
   Test-NetConnection IP_APPAREIL -Port 161
   ping IP_APPAREIL
   ```
   👉 Explication : le port 161 (UDP) ne se teste pas par `Test-NetConnection`; ping confirme au moins la joignabilité, SNMP se valide par le capteur.

2. Créer l'objet Device : **Devices > clic droit sur le groupe de test > Add Device**, nom, **IPv4 Address/DNS Name**, puis dans **Credentials for SNMP Devices** (v3, authPriv, lecture seule) ou **Credentials for Windows Systems**.
   👉 Explication : credentials en lecture seule, héritées du groupe de test.

3. Ajouter les capteurs : clic droit sur le device > **Add Sensor** > **Ping**, puis un seul capteur adapté (**SNMP System Uptime** ou **WMI Memory**).
   👉 Explication : un capteur à la fois.

4. Vérifier : onglets **Overview** et **Log** du device (valeurs, état `Up`), puis supprimer l'objet de test (**Delete**).
   👉 Explication : contrôler que les valeurs arrivent avant de supprimer.


## ⚡ 2. Production — Façon Simplifiée

1. Après approbation du propriétaire, ajouter l'appareil à la bonne hiérarchie : **Devices > groupe > Add Device**, credentials dédiés en lecture seule.
   👉 Explication : adresse, protocole et fenêtre de collecte approuvés.

2. Ajouter les capteurs nécessaires : **Add Sensor**, intervalle dans **Settings > Scanning Interval**, notifications : **Settings > Notification Triggers** limitées à l'équipe responsable.
   👉 Explication : vérifier état et données sur au moins deux cycles avant d'élargir.


## 🔒 3. Production — Façon Sécurisée

- Désactiver l'auto-discovery générale; limiter chaque tâche à un ensemble d'IP/hosts autorisé.
- Restreindre SNMP/WMI depuis les cibles au Core/Probe PRTG; ne pas désactiver le pare-feu endpoint.
- Éviter les secrets réutilisés et les comptes Domain Admin. Protéger les credentials dans PRTG et auditer les droits de modification.
- Ne pas activer packet sniffing ou NetFlow sans accord réseau et définition du volume de données.

## ✅ Validation et retour arrière

- **Précontrôles** : périmètre signé/autorisé, credentials de lecture, ports requis et sauvegarde PRTG.
- **Validation** : device répond, capteur `Up`, valeur cohérente, charge et intervalle acceptables.
- **Retour arrière** : mettre en pause ou supprimer les capteurs et la tâche de découverte concernés; révoquer les credentials temporaires.

## 🔗 Si le problème n'est pas résolu

- **Fiche de résolution complémentaire** : [[PRTG_Appareil_Pilote_Capteur_Down]]
- [Paessler — Appareils et capteurs](https://www.paessler.com/manuals/prtg/device_and_sensor_setup)