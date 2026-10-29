# Fiche_Simple_-_VM_Debian_13_OpenTofu_Projet_Pilote.md

- **Environnement** : projet OpenTofu local `terraform_data`, sans provider ni infrastructure distante
- **OS / Version** : Debian 13; OpenTofu 1.13.x
- **Catégorie** : infrastructure as code / validation pilote
- **Tags** : `debian13`, `opentofu`, `terraform-data`, `plan`, `apply`, `destroy`

---

## Problème précis à résoudre

Valider le cycle de vie OpenTofu sans créer de ressource dans un fournisseur d'infrastructure.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le projet et `main.tf` :
   ```bash
   mkdir -p ~/iac/pilote && cd ~/iac/pilote
   cat > main.tf <<'EOF'
   terraform {
     required_version = ">= 1.13.0, < 1.14.0"
   }

   variable "service_name" {
     type        = string
     description = "Nom logique du service de test"
     default     = "pilote-iac"
   }

   resource "terraform_data" "pilote" {
     input = {
       nom  = var.service_name
       etat = "valide"
     }
   }

   output "pilote" {
     value = terraform_data.pilote.output
   }
   EOF
   ```
   👉 Explication : la ressource intégrée `terraform_data` ne nécessite aucun compte cloud.

2. Valider le format et la configuration :
   ```bash
   tofu fmt -check
   tofu init -input=false
   tofu validate
   ```
   👉 Explication : `Success! The configuration is valid.` doit s'afficher.

3. Planifier puis appliquer le plan enregistré :
   ```bash
   tofu plan -input=false -out=pilote.tfplan
   tofu apply -input=false pilote.tfplan
   tofu state list
   ```
   👉 Explication : appliquer un plan enregistré garantit que seul le plan relu est exécuté; `terraform_data.pilote` doit apparaître.

4. Vérifier l'idempotence :
   ```bash
   tofu plan -detailed-exitcode; echo "code=$?"
   ```
   👉 Explication : `0` = aucun changement; `2` = dérive à analyser.

5. Nettoyer le pilote jetable :
   ```bash
   tofu destroy -auto-approve
   ```
   👉 Explication : `-auto-approve` ne convient qu'à ce pilote; en production, relire chaque plan.

## 2. Production — Contrôles

En production, chaque plan doit faire l'objet d'une revue, d'une approbation et d'une vérification de cible; le cycle `destroy` du pilote n'est pas une procédure de suppression d'infrastructure métier.

## 3. Production — Sécurité

- Ne pas ajouter provider, credentials ou ressource réelle à ce test.
- Ne pas appliquer un plan dont la provenance, le répertoire ou le contenu n'est pas confirmé.
- Ne pas commiter les fichiers d'état ou de plan.
- Éviter `-auto-approve` hors ressource explicitement jetable en laboratoire.

## Validation et retour arrière

- **Validation** : ressource `terraform_data` visible, plan sans changement après apply, destruction limitée au projet de test.
- **Retour arrière** : arrêter si le plan affiche une cible inattendue; ne pas lancer `destroy` dans un répertoire ambigu.

## Si le problème n'est pas résolu

- [OpenTofu — plan](https://opentofu.org/docs/cli/commands/plan/)
- [OpenTofu — apply](https://opentofu.org/docs/cli/commands/apply/)
- [Guide complet OpenTofu Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/120_Deploiement_OpenTofu_1.13_Debian_13.md#4-valider-avec-un-projet-pilote-sans-fournisseur)
