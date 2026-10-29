# Fiche_Simple_-_VM_Debian_13_Terraform_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13 de laboratoire avec fournisseur sandbox
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : infrastructure as code

---

## Problème précis à résoudre

Mettre à niveau CLI/providers en préproduction et éviter downgrade incompatible d’état.

## 1. Hors-Production (Lab / Test / POC)

1. Lire notes de version et compatibilités
   ```text
   Navigateur > ouvrir la documentation officielle : https://developer.hashicorp.com/terraform/install
   ```
   👉 Explication : ne pas effectuer plusieurs migrations majeures simultanément. Détail à confirmer dans la documentation officielle avant application : Comparer CLI, providers, modules et schéma d’état avant migration.

2. Sauvegarder état par backend sécurisé et verrouillage
   ```text
   Navigateur > ouvrir la documentation officielle : https://developer.hashicorp.com/terraform/install
   ```
   👉 Explication : ne pas rediriger `state pull` vers un fichier non protégé. Détail à confirmer dans la documentation officielle avant application : Créer point de restauration depuis les mécanismes de versionnage du backend et consigner le verrouillage courant.

3. Mettre à jour provider dans une branche de test
   ```bash
   terraform init -upgrade
   git diff -- .terraform.lock.hcl
   ```
   👉 Explication : ne valider que versions de providers approuvées.

4. Examiner plan avant application
   ```bash
   terraform plan -out=upgrade.tfplan
   terraform show upgrade.tfplan
   ```
   👉 Explication : interrompre si destructions ou mutations inattendues.

## 2. Production — Contrôles

Répéter sur sandbox et préproduction; sauvegarder, vérifier compatibilité d’état et approuver toute migration.

## 3. Production — Sécurité

- Ne pas supposer qu’un downgrade CLI annule une migration d’état.
- Ne pas valider le lockfile sans revue.
- Stopper pipeline si le plan change hors attente.

## Validation et retour arrière

- **Validation** : Plan demeure conforme et tests infra passent avec la cible.
- **Retour arrière** : Restaurer code/lockfile puis backend depuis version cohérente approuvée.

## Si le problème n'est pas résolu

- [HashiCorp — installation](https://developer.hashicorp.com/terraform/install)
- [Terraform — état distant](https://developer.hashicorp.com/terraform/language/state/remote)
- [Terraform — commandes CLI](https://developer.hashicorp.com/terraform/cli/commands)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/terraform/fiche-simple-vm-debian-13-terraform-prerequis-limites>)