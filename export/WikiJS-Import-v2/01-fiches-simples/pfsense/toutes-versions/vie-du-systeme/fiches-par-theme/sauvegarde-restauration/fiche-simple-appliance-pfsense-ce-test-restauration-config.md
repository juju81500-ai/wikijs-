---
title: "Fiche Simple - Appliance pfSense CE Test Restauration Config"
description: "Prouver qu'une sauvegarde chiffrée de configuration pfSense CE se restaure correctement, dans un environnement isolé, en comparant règles, interfaces et accès avant toute restauration en production."
published: true
date: 2026-10-29T20:22:42Z
tags: ["pfsense", "ce", "backup", "restore", "proxmox", "pra"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_Appliance_pfSense_CE_Test_Restauration_Config.md

- **Environnement** : pfSense CE en VM Proxmox VE, clone de test isolé de la production
- **OS / Version** : pfSense CE 2.x (base FreeBSD) - Toutes-versions
- **Catégorie** : Sauvegarde / Test de restauration (PRA)
- **Tags** : `pfsense`, `ce`, `backup`, `restore`, `proxmox`, `pra`

---

## 🎯 Problème précis à résoudre
Prouver qu'une sauvegarde chiffrée de configuration pfSense CE se restaure correctement, dans un environnement isolé, en comparant règles, interfaces et accès avant toute restauration en production.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Exporter la configuration chiffrée de la source :
   `Diagnostics > Backup & Restore` : Encrypt this configuration file, `Download configuration as XML`
   👉 Explication : Fournit le fichier à restaurer et sa phrase de passe.
2. Compter les règles de la source depuis le shell (option 8) :
   `grep -c '<rule>' /cf/conf/config.xml`
   👉 Explication : Donne une valeur de référence pour comparer après restauration.
3. Créer un clone isolé de la VM pfSense :
   `qm clone <vmid_pfsense> <vmid_test> --name pfsense-test-restore --full 1`
   👉 Explication : Copie complète, indépendante de la VM de production.
4. Placer le clone sur un bridge sans routage vers la production :
   `qm set <vmid_test> --net0 virtio,bridge=<bridge_isole>`
   `qm set <vmid_test> --net1 virtio,bridge=<bridge_isole_2>`
   👉 Explication : Empêche le clone de répondre sur les réseaux réels ou d'utiliser les mêmes adresses IP.
5. Démarrer le clone et restaurer l'export :
   `Diagnostics > Backup & Restore > Restore Configuration` : Choose File = `<fichier_chiffre>`, mot de passe de chiffrement, Restore area = `All configuration`
   👉 Explication : La restauration se termine par un redémarrage du clone.
6. Comparer le clone à la source :
   `grep -c '<rule>' /cf/conf/config.xml` (sur le clone) et `Interfaces > Assignments` (correspondance WAN/LAN)
   👉 Explication : Le nombre de règles et l'affectation des interfaces doivent correspondre.
7. Détruire le clone après validation :
   `qm stop <vmid_test> && qm destroy <vmid_test>` (sur l'hôte Proxmox)
   👉 Explication : Évite qu'une copie de configuration complète reste active sur le réseau.

---

## ⚡ 2. Production — Façon Simplifiée
1. Planifier un test de restauration trimestriel :
   `Diagnostics > Backup & Restore` sur le clone de test, consigné dans le dossier d'exploitation
   👉 Explication : Une sauvegarde non restaurée n'est pas une garantie.
2. Vérifier l'empreinte de la sauvegarde stockée :
   `sha256sum <fichier_chiffre>` sur `<serveur_sauvegarde>`
   👉 Explication : Confirme que le fichier n'a pas été altéré depuis l'export.

---

## 🔒 3. Production — Façon Sécurisée
1. Ne restaurer en production qu'une configuration de même version et après test sur clone :
   `pkg info pfSense-base` (comparer la version source et la version cible)
   👉 Explication : Une restauration entre versions différentes peut produire une configuration incohérente.
2. Restaurer en production dans une fenêtre de maintenance, console ouverte :
   `Diagnostics > Backup & Restore > Restore Configuration` : Restore area = `All configuration`
   👉 Explication : Garde un accès de secours si l'adresse IP ou le filtrage change après redémarrage.
3. Conserver le fichier de sauvegarde de production jusqu'à validation complète :
   `ls -l /cf/conf/backup/` avant la restauration
   👉 Explication : Permet de revenir à la configuration précédente si la restauration échoue.