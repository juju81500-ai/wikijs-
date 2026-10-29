---
title: "Fiche Simple - Appliance OPNsense Systeme Mise A Jour"
description: "Mettre à jour OPNsense (correctifs et version) avec sauvegarde préalable, point de retour arrière et vérification après redémarrage."
published: true
date: 2026-10-29T20:22:42Z
tags: ["opnsense", "freebsd", "update", "firmware", "pkg", "maintenance"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_Appliance_OPNsense_Systeme_Mise_A_Jour.md

- **Environnement** : OPNsense sur VM Proxmox VE ou appliance dédiée, fenêtre de maintenance planifiée
- **OS / Version** : OPNsense (base FreeBSD) - Toutes-versions
- **Catégorie** : Système / Mises à jour
- **Tags** : `opnsense`, `freebsd`, `update`, `firmware`, `pkg`, `maintenance`

---

## 🎯 Problème précis à résoudre
Mettre à jour OPNsense (correctifs et version) avec sauvegarde préalable, point de retour arrière et vérification après redémarrage.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever la version installée depuis le shell (option 8) :
   `opnsense-version`
   👉 Explication : Affiche la version et le numéro de build à comparer avec les notes de version OPNsense.
2. Rechercher les mises à jour disponibles :
   `System > Firmware > Status` : cliquer sur `Check for updates`
   👉 Explication : Interroge le dépôt OPNsense et liste les paquets et le noyau à mettre à jour.
3. Lister les paquets obsolètes depuis le shell :
   `pkg version -vl '<'`
   👉 Explication : Affiche les paquets dont la version installée est inférieure à celle du dépôt.
4. Exporter la configuration avant intervention :
   `System > Configuration > Backups` : `Download configuration`
   👉 Explication : Point de retour arrière au format XML, indépendant de l'hyperviseur.
5. Créer un point de retour arrière côté hyperviseur (sur l'hôte Proxmox) :
   `qm snapshot <vmid_opnsense> avant-maj-opnsense`
   👉 Explication : Permet de restaurer la VM entière si la mise à jour échoue.
6. Lancer la mise à jour depuis l'interface :
   `System > Firmware > Status` : `Update` puis redémarrage si demandé
   👉 Explication : Applique les correctifs dans l'ordre recommandé par l'interface.
7. Vérifier après redémarrage :
   `opnsense-version` et `System > Firmware > Status`
   👉 Explication : Confirme la version finale et l'absence de mise à jour en attente.

---

## ⚡ 2. Production — Façon Simplifiée
1. Appliquer les mises à jour de correctifs dans une fenêtre de maintenance :
   `System > Firmware > Status` : `Update`
   👉 Explication : Les correctifs de sécurité doivent être appliqués rapidement, mais pendant une fenêtre connue.
2. Vérifier la configuration des miroirs et des alertes :
   `System > Firmware > Settings` (à vérifier sur la version déployée)
   👉 Explication : Une source de mise à jour incorrecte bloque l'opération.
3. Planifier une vérification régulière :
   `System > Settings > Cron` : tâche de contrôle à définir selon la politique (à vérifier sur la version déployée)
   👉 Explication : Rappelle les mises à jour disponibles sans les appliquer seul.

---

## 🔒 3. Production — Façon Sécurisée
1. Tester la mise à jour sur un clone de lab avant la production :
   `qm clone <vmid_opnsense> <vmid_test> --name opnsense-test-maj --full 1`
   👉 Explication : Valide la mise à jour et les règles sur une copie isolée.
2. Ne jamais mettre à niveau la version majeure sans test :
   `System > Firmware > Status` : bouton de mise à niveau de version, uniquement après validation sur clone
   👉 Explication : Un changement de version majeure peut modifier les règles et les services.
3. Revenir en arrière si la vérification échoue :
   `qm rollback <vmid_opnsense> avant-maj-opnsense` (sur l'hôte Proxmox)
   👉 Explication : Restaure la VM à l'état précédant la mise à jour.
4. Éviter les mises à jour de paquets non contrôlées depuis le shell :
   `pkg upgrade -y` est interdit en production
   👉 Explication : Met à jour sans vérification ni fenêtre de maintenance, et peut désynchroniser l'interface web.