# Fiche_Simple_-_VM_Debian_13_Terraform_Valider_Recette

- **Environnement** : VM Debian 13 de laboratoire avec fournisseur sandbox
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : infrastructure as code
- **Tags** : `debian13`, `terraform`, `iac`, `state`, `securite`
---

## Problème précis à résoudre

Inspecter chaque changement avant apply et vérifier l’état final dans un compte sandbox.

## 1. Hors-Production (Lab / Test / POC)

1. Formater et valider HCL
   ```bash
   terraform fmt -check -recursive
   terraform validate
   ```
   👉 Explication : corriger erreurs avant fournisseur.

2. Générer et lire plan
   ```bash
   terraform plan -out=plan.tfplan
   terraform show plan.tfplan
   ```
   👉 Explication : contrôler compte/région, ressources, coût et destructions.

3. Appliquer uniquement après approbation sandbox
   ```bash
   terraform apply plan.tfplan
   ```
   👉 Explication : cette commande modifie infrastructure; autorisation et compte test requis.

4. Préparer plan de destruction sans l’exécuter
   ```bash
   terraform plan -destroy
   ```
   👉 Explication : inspecter et approuver chaque destruction.

## 2. Production — Contrôles

Production exige revue par un second opérateur, approbation, sauvegarde d’état, budget et validation de dérive.

## 3. Production — Sécurité

- Ne jamais appliquer un plan obsolète ou d’origine inconnue.
- Vérifier toutes destructions et identités actives.
- Masquer secrets dans CI et sorties.

## Validation et retour arrière

- **Validation** : Ressources correspondent au plan approuvé et tests fonctionnels réussissent.
- **Retour arrière** : Restaurer état/importer selon guide du backend; ne pas lancer destroy en urgence.

## Si le problème n'est pas résolu

- [HashiCorp — installation](https://developer.hashicorp.com/terraform/install)
- [Terraform — état distant](https://developer.hashicorp.com/terraform/language/state/remote)
- [Terraform — commandes CLI](https://developer.hashicorp.com/terraform/cli/commands)
- [Fiche connexe](<Fiche_Simple_-_VM_Debian_13_Terraform_Prerequis_Limites.md>)
