# Fiche_Simple_-_VM_Debian_13_Terraform_Installer

- **Environnement** : VM Debian 13 de laboratoire avec fournisseur sandbox
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : infrastructure as code
- **Tags** : `debian13`, `terraform`, `iac`, `state`, `securite`
---

## Problème précis à résoudre

Installer Terraform selon le dépôt officiel HashiCorp et vérifier signatures/provenance APT.

## 1. Hors-Production (Lab / Test / POC)

1. Installer outils de vérification
   ```bash
   sudo apt update
   sudo apt install -y ca-certificates curl gnupg
   ```
   👉 Explication : utiliser un canal Debian approuvé.

2. Configurer clé/repository selon la procédure HashiCorp
   ```text
   Navigateur > ouvrir la documentation officielle : https://developer.hashicorp.com/terraform/install
   ```
   👉 Explication : ne pas désactiver APT Secure; vérifier support Debian 13 avant ajout. Détail à confirmer dans la documentation officielle avant application : Suivre les instructions officielles HashiCorp pour Debian 13; limiter la clé avec signed-by et confirmer l’empreinte officielle.

3. Contrôler origine puis installer
   ```bash
   sudo apt update
   apt-cache policy terraform
   sudo apt install terraform
   ```
   👉 Explication : n’installer que si apt-cache confirme le dépôt HashiCorp attendu.

4. Vérifier version
   ```bash
   terraform version
   ```
   👉 Explication : consigner et épingler la version pour les pipelines.

## 2. Production — Contrôles

Déployer CLI depuis source approuvée, épingler version et tester providers en préproduction.

## 3. Production — Sécurité

- Ne pas installer un binaire non vérifié ou exécuter un script distant en root.
- Limiter confiance de la clé au dépôt concerné.
- Gérer les versions de CLI/pipelines de façon reproductible.

## Validation et retour arrière

- **Validation** : APT et terraform version confirment version/origine attendues.
- **Retour arrière** : Restaurer version supportée via gestion APT après test de régression.

## Si le problème n'est pas résolu

- [HashiCorp — installation](https://developer.hashicorp.com/terraform/install)
- [Terraform — état distant](https://developer.hashicorp.com/terraform/language/state/remote)
- [Terraform — commandes CLI](https://developer.hashicorp.com/terraform/cli/commands)
- [Fiche connexe](<Fiche_Simple_-_VM_Debian_13_Terraform_Prerequis_Limites.md>)
