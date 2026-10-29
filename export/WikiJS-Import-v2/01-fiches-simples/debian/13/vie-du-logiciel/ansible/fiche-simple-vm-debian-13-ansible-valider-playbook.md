---
title: "Fiche Simple - VM Debian 13 Ansible Valider Playbook"
description: "Vérifier syntaxe, cibles et changements proposés d'un playbook avant toute exécution de modification."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "ansible", "playbook", "check-mode", "review"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Ansible_Valider_Playbook.md

- **Environnement** : projet Ansible versionné, hôte pilote explicitement autorisé
- **OS / Version** : Debian 13; Ansible Core
- **Catégorie** : automatisation / playbook
- **Tags** : `debian13`, `ansible`, `playbook`, `check-mode`, `review`

---

## Problème précis à résoudre

Vérifier syntaxe, cibles et changements proposés d'un playbook avant toute exécution de modification.

## 1. Hors-Production (Lab / Test / POC)

1. Créer `check.yml` :
   ```bash
   cd ~/ansible-lab
   cat > check.yml <<'EOF'
   ---
   - name: Collecter les faits d'un hôte pilote
     hosts: linux_lab
     gather_facts: true
     tasks:
       - name: Afficher la distribution détectée
         ansible.builtin.debug:
           msg: "{{ ansible_facts.distribution }} {{ ansible_facts.distribution_version }}"
   EOF
   ```
   👉 Explication : ce playbook ne modifie pas l'hôte.

2. Valider la syntaxe et lister les cibles :
   ```bash
   ansible-playbook -i inventory.ini --syntax-check check.yml
   ansible-playbook -i inventory.ini --list-hosts check.yml
   ```
   👉 Explication : confirmer que seuls les hôtes prévus sont ciblés.

3. Simuler :
   ```bash
   ansible-playbook -i inventory.ini --check --diff --limit serveur-test.example.net check.yml
   ```
   👉 Explication : `--check` simule et `--diff` montre les changements; la simulation est un effort au mieux, certains modules ne la supportent pas.

4. Pour un playbook de changement, sauvegarder la configuration distante avant exécution :
   ```bash
   ansible linux_lab -i inventory.ini --limit serveur-test.example.net -m ansible.builtin.fetch -a "src=/etc/FICHIER dest=./sauvegardes/"
   ```
   👉 Explication : remplacer le fichier; ne lancer le vrai changement qu'après un `--check --diff` relu sur un pilote.

## 2. Production — Contrôles

Faire relire le code par un pair, l'inventaire par le propriétaire du service et les effets par l'approbateur de changement. Définir la sauvegarde, fenêtre et procédure de restauration par tâche.

## 3. Production — Sécurité

- Le mode `--check` est une simulation best-effort et ne garantit pas l'absence de changement.
- Examiner chaque module, commande, template, handler et rôle avant exécution.
- Restreindre les cibles avec `--limit`; revérifier l'inventaire juste avant le lancement.
- Ne pas placer de secret en clair dans variables, arguments ou journaux.

## Validation et retour arrière

- **Validation** : syntaxe valide, liste d'hôtes attendue, diff relu et plan de restauration prêt.
- **Retour arrière** : ne pas exécuter si le mode check ne révèle pas les effets réels ou si le rollback n'est pas testé.

## Si le problème n'est pas résolu

- [Ansible — playbooks](https://docs.ansible.com/projects/ansible/latest/playbook_guide/index.html)
- [Ansible — mode check et diff](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_checkmode.html)
- [Guide complet Ansible Core Debian 13](/02-fiches-completes/debian/13/installation-deploiement/90-administration-ansible-core-debian-13#5-ecrire-et-valider-un-playbook-sans-changement)