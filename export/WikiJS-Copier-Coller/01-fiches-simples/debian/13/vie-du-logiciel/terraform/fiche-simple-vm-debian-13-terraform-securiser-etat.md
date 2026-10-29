# Fiche_Simple_-_VM_Debian_13_Terraform_Securiser_Etat

- **Environnement** : VM Debian 13 de laboratoire avec fournisseur sandbox
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : infrastructure as code

---

## Problème précis à résoudre

Protéger l’état, les plans et les identifiants des fournisseurs cloud.

## 1. Hors-Production (Lab / Test / POC)

1. Restreindre permissions et umask
   ```bash
   umask 077
   ls -ld . ~/.terraform.d 2>/dev/null || true
   ```
   👉 Explication : dossier et credentials doivent être réservés à l’identité autorisée.

2. Créer un plan protégé en sandbox
   ```bash
   umask 077
   terraform plan -out=plan.tfplan
   chmod 0600 plan.tfplan
   ```
   👉 Explication : plan peut contenir des données sensibles; ne pas versionner ni partager.

3. Vérifier identités sans afficher leurs secrets
   ```bash
   env | cut -d= -f1 | grep -E "^(TF_|AWS_|AZURE_|GOOGLE_)"
   ```
   👉 Explication : lister noms uniquement; ne pas afficher les valeurs.

4. Vérifier chiffrement et verrouillage backend
   ```text
   Navigateur > ouvrir la documentation officielle : https://developer.hashicorp.com/terraform/install
   ```
   👉 Explication : les détails dépendent du fournisseur; suivre son guide officiel. Détail à confirmer dans la documentation officielle avant application : Confirmer chiffrement au repos, versionnage, verrouillage, IAM et journaux dans le backend choisi.

## 2. Production — Contrôles

Faire valider chiffrement, IAM, verrouillage, rotation, journalisation et restauration d’état par l’équipe plateforme.

## 3. Production — Sécurité

- Ne jamais partager plans/états en clair.
- Ne pas contourner verrouillage concurrent.
- Révoquer immédiatement les credentials exposés.

## Validation et retour arrière

- **Validation** : Seules identités autorisées accèdent à état et plan; aucune valeur secrète n’est versionnée.
- **Retour arrière** : Révoquer credentials et restaurer version d’état sécurisée selon procédure du backend.

## Si le problème n'est pas résolu

- [HashiCorp — installation](https://developer.hashicorp.com/terraform/install)
- [Terraform — état distant](https://developer.hashicorp.com/terraform/language/state/remote)
- [Terraform — commandes CLI](https://developer.hashicorp.com/terraform/cli/commands)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/terraform/fiche-simple-vm-debian-13-terraform-prerequis-limites>)