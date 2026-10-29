---
title: "Fiche Simple - VM Debian 13 Ansible Installer Core"
description: "Installer Ansible Core depuis les dépôts Debian et consigner sa version et sa provenance."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "ansible-core", "apt", "installation", "version"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Ansible_Installer_Core.md

- **Environnement** : VM Debian 13 Trixie, dépôts Debian approuvés
- **OS / Version** : Debian 13; Ansible Core
- **Catégorie** : automatisation / installation
- **Tags** : `debian13`, `ansible-core`, `apt`, `installation`, `version`

---

## Problème précis à résoudre

Installer Ansible Core depuis les dépôts Debian et consigner sa version et sa provenance.

## 1. Hors-Production (Lab / Test / POC)

1. Relever la version et l'origine du paquet :
   ```bash
   sudo apt update
   apt-cache policy ansible-core
   ```
   👉 Explication : la version provient des dépôts Debian configurés; la consigner.

2. Installer :
   ```bash
   sudo apt install ansible-core openssh-client
   ```
   👉 Explication : installe Ansible Core et le client SSH.

3. Vérifier :
   ```bash
   ansible --version
   ```
   👉 Explication : on contrôle la version et le chemin du module Python utilisé.

4. Pour une autre version, utiliser un environnement virtuel, jamais `pip` sur le Python système :
   ```bash
   sudo apt install python3-venv
   python3 -m venv ~/venv-ansible && ~/venv-ansible/bin/pip install 'ansible-core==X.Y.Z'
   ```
   👉 Explication : remplacer `X.Y.Z`; l'isolement évite de casser les paquets Debian.

## 2. Production — Contrôles

Épingler la version au processus de gestion de configuration, évaluer les notes de version et tester les collections requises avant mise à jour des nœuds de contrôle.

## 3. Production — Sécurité

- Installer uniquement depuis un dépôt Debian approuvé.
- Ne pas ajouter de dépôt tiers ou contourner APT Secure.
- Protéger le compte utilisateur et le répertoire de travail; ne pas exécuter Ansible depuis un compte partagé.
- Maintenir une méthode de mise à jour et de retour arrière vérifiée.

## Validation et retour arrière

- **Validation** : paquet, origine et version confirmés; binaire accessible au compte autorisé.
- **Retour arrière** : conserver la version et les dépendances consignées; ne pas supprimer l'installation avant d'avoir migré les playbooks et collections.

## Si le problème n'est pas résolu

- [Ansible — installation sur Debian](https://docs.ansible.com/projects/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-debian)
- [Debian — paquet ansible-core Trixie](https://packages.debian.org/trixie/ansible-core)
- [Guide complet Ansible Core Debian 13](/02-fiches-completes/debian/13/installation-deploiement/90-administration-ansible-core-debian-13#2-installer-ansible-core-depuis-debian)