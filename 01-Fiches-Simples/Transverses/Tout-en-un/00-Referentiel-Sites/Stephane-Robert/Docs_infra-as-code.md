# Référentiel — Stéphane Robert : infra-as-code

- **Tags** : `transverse`, `tout-en-un`, `referentiel`, `stephane-robert`, `infra-as-code`

Catégorie **infra-as-code** du site stephane-robert.info (47 pages). Page d'entrée : [Infra as code](https://www.stephane-robert.info/docs/infra-as-code/).

Ce référentiel ne reproduit **aucun contenu pédagogique** : il liste uniquement les titres publics, les catégories et les liens, à des fins de navigation. Les droits sur les cours restent à leurs auteurs ; pour les lire, utiliser le lien vers le site d'origine. Les titres sont relevés le 2026-11-01 ; ils peuvent évoluer côté éditeur.

## Gestion de configuration

- [Alternatives à Ansible : Salt, Chef, Puppet ou Rudder ?](https://www.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/alternatives-ansible/)
    - [Le fichier ansible.cfg : ordre de chargement, sections et paramètres clés](https://www.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/ansible/decouvrir/ansible-config-fichier/)
      - [Boucles Ansible (loop) : itérer sur listes, dicts et résultats de lookup](https://www.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/ansible/ecrire-code/controle-flux/boucles-loop/)
      - [Inventaire dynamique Proxmox VE avec community.proxmox.proxmox](https://www.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/ansible/inventaires/dynamiques/plugin-proxmox/)
    - [group_vars et host_vars : structurer les variables d'inventaire Ansible](https://www.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/ansible/inventaires/group-vars-host-vars/)
    - [Vérifier un inventaire Ansible : ansible-inventory --graph, --list, --host](https://www.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/ansible/inventaires/verifier-inventaire/)
      - [Module blockinfile Ansible : insérer un bloc multi-lignes idempotent](https://www.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/ansible/modules/fichiers/module-blockinfile/)
    - [Modules système Ansible : pare-feu, SELinux, stockage et noyau](https://www.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/ansible/modules/systeme/)
      - [LVM avec Ansible : pipeline pv → vg → lv → filesystem → mount](https://www.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/ansible/modules/systeme/lvm-storage/)
      - [Module mount Ansible : gérer fstab et montages](https://www.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/ansible/modules/systeme/module-mount/)
      - [Module Ansible parted : créer une partition disque sur Linux](https://www.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/ansible/modules/systeme/module-parted/)
      - [Module SELinux Ansible : modes, booléens, contextes](https://www.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/ansible/modules/systeme/module-selinux/)
      - [Module sysctl Ansible : paramètres kernel persistés](https://www.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/ansible/modules/systeme/module-sysctl/)
    - [ansible-lint profile production : configuration stricte pour rôles publiés](https://www.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/ansible/roles/ansible-lint-production-profile/)
    - [RHEL System Roles : la bibliothèque de rôles maintenue par Red Hat](https://www.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/ansible/roles/rhel-system-roles/)
    - [Idempotence cassée et tuning performances : creates, changed_when, pipelining, forks](https://www.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/ansible/troubleshooting/idempotence-cassee/)

## Provisionnement

- [OpenTofu : ce qui change vraiment par rapport à Terraform](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/opentofu/)
  - [Chiffrer le state et les plans avec OpenTofu](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/opentofu/chiffrer-state-plans/)
  - [Migrer de Terraform vers OpenTofu sans casser votre workflow](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/opentofu/migrer-depuis-terraform/)
  - [OpenTofu : refactor, import, moved et removed](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/opentofu/refactor-import-moved-removed/)
  - [Registry OpenTofu, .tofurc et distribution OCI](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/opentofu/registry-cli-oci/)
  - [OpenTofu : variables dans backend et sources de modules](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/opentofu/variables-backend-sources-modules/)
- [Formation Terraform : apprendre l'Infrastructure as Code](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terraform/)
  - [Certification Terraform : Associate ou Professional ?](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terraform/certifications/)
    - [Terraform Professional, Guide de préparation complet](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terraform/certifications/professional/)
    - [Installer Terraform sur Linux et gérer les versions](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terraform/decouvrir/installer-terraform/)
    - [Providers, resources et data sources dans Terraform](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terraform/decouvrir/providers-resources-data-sources/)
    - [Terraform vs OpenTofu : quelles différences en pratique ?](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terraform/decouvrir/terraform-vs-opentofu/)
    - [Fichiers tfvars Terraform : précédence et pièges](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terraform/ecrire-code/fichiers-tfvars/)
      - [Lire des secrets Vault depuis Terraform sans les figer dans le state](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terraform/ecrire-code/gestion-donnees-sensibles/vault-secrets/)
    - [Locals Terraform : valeurs locales et leurs pièges](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terraform/ecrire-code/locals-terraform/)
    - [Outputs Terraform : type, sensibilité et precondition](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terraform/ecrire-code/outputs-terraform/)
    - [Variables Terraform : types, validation, nullable et précédence](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terraform/ecrire-code/variables-terraform/)
    - [Contraintes de version Terraform : opérateurs, lock file et pièges](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terraform/ecrire-code/version-constraints-terraform/)
- [Terragrunt pour structurer Terraform et OpenTofu](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terragrunt/)
  - [Terragrunt : catalogues, scaffold et industrialisation](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terragrunt/catalogues-et-scaffold/)
  - [Centraliser backend et provider avec Terragrunt](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terragrunt/centraliser-backend-provider/)
  - [Déboguer Terragrunt : cache, chemins relatifs, hooks et logs](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terragrunt/debug-cache-hooks-logs/)
  - [Terragrunt : dépendances et mock_outputs](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terragrunt/dependances-et-mock-outputs/)
  - [Installer Terragrunt avec mise](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terragrunt/installer-terragrunt/)
  - [Pourquoi utiliser Terragrunt avec Terraform ou OpenTofu ?](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terragrunt/pourquoi-utiliser-terragrunt/)
  - [Premier projet Terragrunt : votre premier unit](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terragrunt/premier-projet-terragrunt/)
  - [Terragrunt : run --all, run queue et filtres](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terragrunt/run-all-run-queue-filtres/)
  - [Terragrunt : stacks implicites ou explicites ?](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terragrunt/stacks-implicites-explicites/)
  - [Structurer un live repo Terragrunt avec root.hcl et _env](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terragrunt/structurer-live-repo/)
  - [Terragrunt en CI/CD : cibler, limiter le blast radius, promouvoir](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terragrunt/terragrunt-cicd/)
  - [Utiliser terragrunt.stack.hcl pour une stack explicite](https://www.stephane-robert.info/docs/infra-as-code/provisionnement/terragrunt/terragrunt-stack-hcl/)
