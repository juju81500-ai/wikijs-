# Fiche_Simple_-_VM_Debian_13_Terraform_Prerequis_Limites

- **Environnement** : VM Debian 13 de laboratoire avec fournisseur sandbox
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : infrastructure as code
- **Tags** : `debian13`, `terraform`, `iac`, `state`, `securite`
---

## Problème précis à résoudre

Définir fournisseur cloud, sandbox, coût, état et version CLI avant toute application Terraform.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier OS et version
   ```bash
   cat /etc/os-release
   dpkg --print-architecture
   terraform version
   ```
   👉 Explication : consigner version et architecture.

2. Définir sandbox, région et plafond de coût
   ```text
   Navigateur > ouvrir la documentation officielle : https://developer.hashicorp.com/terraform/install
   ```
   👉 Explication : ne pas utiliser compte production pour pilote. Détail à confirmer dans la documentation officielle avant application : Documenter compte de test, région autorisée, ressources permises, budget et propriétaire.

3. Vérifier notes de version et contraintes providers
   ```text
   Navigateur > ouvrir la documentation officielle : https://developer.hashicorp.com/terraform/install
   ```
   👉 Explication : ne pas supposer compatibilité entre versions. Détail à confirmer dans la documentation officielle avant application : Consulter installation Terraform et support Debian officiel; figer CLI, providers et modules.

## 2. Production — Contrôles

Faire valider identité cloud, coût, état, sauvegarde, verrouillage et approbation avant apply.

## 3. Production — Sécurité

- Ne pas appliquer sans revue du plan et sandbox.
- Traiter état et plans comme des secrets.
- Limiter droits IAM du compte Terraform.

## Validation et retour arrière

- **Validation** : Compte, plafond, versions et sauvegarde sont documentés.
- **Retour arrière** : Ne pas lancer Terraform si le compte cible ou l’état est ambigu.

## Si le problème n'est pas résolu

- [HashiCorp — installation](https://developer.hashicorp.com/terraform/install)
- [Terraform — état distant](https://developer.hashicorp.com/terraform/language/state/remote)
- [Terraform — commandes CLI](https://developer.hashicorp.com/terraform/cli/commands)
- [Fiche connexe](<Fiche_Simple_-_VM_Debian_13_Terraform_Installer.md>)
