---
title: "VM_Debian_12_Systeme_Reduction-Services"
description: "Identifier et désactiver les services Debian 12 inutiles au rôle du serveur (ex. avahi-daemon, cups-browsed, bluetooth) afin de réduire la surface d'attaque, sans couper les services indispensables (SSH, réseau, horloge, pare-feu)."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[debian12]", "[debian-family]", "[systemd]", "[services]", "[surface-attaque]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_Debian_12_Systeme_Reduction-Services.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Système & Services / Réduction de la surface d'attaque
- **Tags** : `[debian12]`, `[debian-family]`, `[systemd]`, `[services]`, `[surface-attaque]`, `[hardening]`

## 🎯 Problème précis à résoudre
Identifier et désactiver les services Debian 12 inutiles au rôle du serveur (ex. `avahi-daemon`, `cups-browsed`, `bluetooth`) afin de réduire la surface d'attaque, sans couper les services indispensables (SSH, réseau, horloge, pare-feu).

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Liste des services activés au démarrage :
   `systemctl list-unit-files --type=service --state=enabled`
   👉 Explication : Affiche tous les services qui démarrent automatiquement avec la machine.
2. Liste des services actuellement en cours d'exécution :
   `systemctl list-units --type=service --state=running`
   👉 Explication : Montre les démons actifs à l'instant T, utile pour repérer les services hérités d'une installation par tâches.
3. Corrélation avec les ports en écoute :
   `sudo ss -tulnp`
   👉 Explication : Associe chaque port ouvert à son processus, afin de savoir quel service expose quelle porte.

---

## ⚡ 2. Production — Façon Simplifiée
1. Arrêt et désactivation d'un service inutile :
   `sudo systemctl disable --now <nom_du_service_inutile>`
   👉 Explication : Stoppe le service immédiatement et l'empêche de démarrer au prochain boot. Exemple : `avahi-daemon`. Ne jamais toucher à `ssh`, à la gestion réseau ni à `nftables` ou `chrony` lorsqu'ils sont requis.
2. Vérification de l'absence d'unités en échec :
   `systemctl --failed`
   👉 Explication : Doit afficher `0 loaded units listed`. Une unité en échec peut indiquer qu'un service requis a été désactivé par erreur.

---

## 🔒 3. Production — Façon Sécurisée (Masquage & Contrôle)
1. Masquage du service pour empêcher tout démarrage, même par dépendance :
   `sudo systemctl mask <nom_du_service_inutile>`
   👉 Explication : Crée un lien vers `/dev/null` dans `/etc/systemd/system/` ; le service ne peut plus être lancé ni manuellement ni par un autre service.
2. Contrôle de l'état masqué :
   `systemctl is-enabled <nom_du_service_inutile>`
   👉 Explication : La réponse attendue est `masked`.
3. Contrôle final des ports exposés :
   `sudo ss -tulnp`
   👉 Explication : Vérifie que seuls les ports prévus dans la fiche serveur restent en écoute après la réduction.