---
title: "VM_Debian_12_Automatisation_Installation-Ansible"
description: "Installer le moteur d'automatisation Ansible, générer une paire de clés SSH dédiées et sécuriser le nœud de contrôle sur Debian 12."
published: true
date: 2026-10-29T19:55:10Z
tags: ["[debian12]", "[debian-family]", "[ansible]", "[automation]", "[ssh-keys]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# 📄 VM_Debian_12_Automatisation_Installation-Ansible.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Automatisation & IaC
- **Tags** : `[debian12]`, `[debian-family]`, `[ansible]`, `[automation]`, `[ssh-keys]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer le moteur d'automatisation Ansible, générer une paire de clés SSH dédiées et sécuriser le nœud de contrôle sur Debian 12.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation rapide du paquet Ansible de base :
   `apt-get update && apt-get install -y ansible`
   👉 Explication : Installe la version paquet Debian d'Ansible et ses dépendances Python minimales.
2. Exécution d'un ping ad-hoc sur la machine locale :
   `ansible localhost -m ping`
   👉 Explication : Valide que le moteur Ansible fonctionne correctement en sollicitant l'hôte local via le module ping.

---

## ⚡ 2. Production — Façon Simplifiée
1. Installer la version Ansible empaquetée pour Debian 12 ou choisir un dépôt explicitement compatible Debian depuis la documentation officielle. Ne pas ajouter un PPA Ubuntu à Debian.
   `sudo apt update && sudo apt install ansible`
   👉 Explication : Vérifier la version avec `ansible --version` et planifier une mise à niveau si les collections exigent une version plus récente.
2. Création d'un fichier d'inventaire statique `/etc/ansible/hosts` :
   `echo -e "[servers]\nsrv-app-01 ansible_host=192.168.1.50\nsrv-db-01 ansible_host=192.168.1.60" > /etc/ansible/hosts`
   👉 Explication : Structure la liste des nœuds cibles gérés par Ansible.
3. Test d'inventaire global :
   `ansible all -m ping`
   👉 Explication : Vérifie la portée et la joignabilité de l'ensemble des serveurs du parc.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Création d'un compte utilisateur dédié sans privilège `ansible-admin` :
   `useradd -m -s /bin/bash ansible-admin && passwd -l ansible-admin`
   👉 Explication : Isole l'exécution d'Ansible hors du compte `root` et verrouille la connexion directe par mot de passe.
2. Générer une clé SSH ED25519 protégée par phrase secrète dans une session du compte de contrôle ; conserver la clé privée sur le nœud de contrôle et utiliser `ssh-agent` pour les automatisations interactives. Pour les exécutions non interactives, documenter explicitement la gestion du secret dans un coffre.
3. Restriction stricte des permissions sur le dossier SSH et le fichier de configuration `/etc/ansible/ansible.cfg` :
   `chmod 700 /home/ansible-admin/.ssh && chmod 600 /home/ansible-admin/.ssh/id_ed25519 && chmod 644 /etc/ansible/ansible.cfg`
   👉 Explication : Garantit qu'aucun autre utilisateur du système ne peut lire ou dérober la clé privée de contrôle.
4. Chiffrement des variables sensibles (mots de passe, jetons) via Ansible Vault :
   `sudo -u ansible-admin ansible-vault create /home/ansible-admin/credentials.yml`
   👉 Explication : Force le chiffrement AES-256 des identifiants stockés dans le code d'automatisation.