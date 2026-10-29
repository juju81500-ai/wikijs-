---
title: "VM_Rocky_9_Services_Installation-Et-Configuration-Cockpit"
description: "Installer la console d'administration Web Cockpit sur Rocky Linux 9, autoriser les flux dans firewalld, configurer l'accès sécurisé et la gestion des abonnements/stockage LVM."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[rocky9]", "[redhat-family]", "[cockpit]", "[firewalld]", "[selinux]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_Rocky_9_Services_Installation-Et-Configuration-Cockpit.md

- **Environnement** : VM (Rocky Linux 9 / RHEL 9)
- **OS / Version** : Rocky Linux 9 - Famille RedHat
- **Catégorie** : Administration & Web Console / Cockpit
- **Tags** : `[rocky9]`, `[redhat-family]`, `[cockpit]`, `[firewalld]`, `[selinux]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer la console d'administration Web Cockpit sur Rocky Linux 9, autoriser les flux dans firewalld, configurer l'accès sécurisé et la gestion des abonnements/stockage LVM.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du paquet cockpit de base :
   `dnf install -y cockpit && systemctl enable --now cockpit.socket`
   👉 Explication : Installe l'interface Cockpit et active le socket d'écoute sur le port 9090.
2. Ouverture temporaire du port dans le pare-feu :
   `firewall-cmd --add-service=cockpit && firewall-cmd --reload`
   👉 Explication : Autorise les connexions Web d'essai sur l'interface Cockpit.

---

## ⚡ 2. Production — Façon Simplifiée
1. Installation de Cockpit avec les modules de gestion de stockage (LVM/Podman) et réseau :
   `dnf install -y cockpit cockpit-storaged cockpit-podman cockpit-networkmanager && systemctl enable --now cockpit.socket`
   👉 Explication : Ajoute les extensions d'administration graphique des conteneurs, des disques et du réseau.
2. Ouverture permanente du service dans firewalld :
   `firewall-cmd --add-service=cockpit --permanent && firewall-cmd --reload`
   👉 Explication : Maintient l'accès à la console Web après redémarrage.
3. Contrôle du statut du socket :
   `systemctl status cockpit.socket`
   👉 Explication : Vérifie l'état d'écoute du service Cockpit.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restriction du port d'accès Cockpit à un sous-réseau d'administration dédié via firewalld Rich Rules :
   `firewall-cmd --permanent --remove-service=cockpit && firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" service name="cockpit" accept' && firewall-cmd --reload`
   👉 Explication : Interdit toute tentative de connexion à la console Web hors du sous-réseau des techniciens.
2. Surcharge des permissions sur le répertoire des certificats SSL Cockpit :
   `chmod 600 /etc/cockpit/ws-certs.d/*.crt`
   👉 Explication : Sécurise la chaîne de confiance et les clés privées du serveur Web.
3. Configuration du délai d'expiration automatique des sessions inactives :
   `echo '[Session]' > /etc/cockpit/cockpit.conf && echo 'IdleTimeoutMinutes = 15' >> /etc/cockpit/cockpit.conf`
   👉 Explication : Déconnecte automatiquement les sessions d'administration inactives après 15 minutes.