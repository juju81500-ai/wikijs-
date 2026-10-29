# Fiche_Simple_-_VM_Debian_13_OpenTofu_Limites.md

- **Environnement** : revue d'architecture OpenTofu/Terraform, sans exécution
- **OS / Version** : Debian 13; OpenTofu 1.13.x
- **Catégorie** : infrastructure as code / limites et compatibilité

---

## Problème précis à résoudre

Déterminer les éléments non couverts par le pilote avant de sélectionner un provider ou d'automatiser une infrastructure.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les fournisseurs réellement utilisés :
   ```bash
   cd ~/iac/pilote
   tofu providers
   ls .terraform.lock.hcl 2>/dev/null || echo "aucun fournisseur externe verrouillé"
   ```
   👉 Explication : sans fournisseur externe, aucune compatibilité fournisseur n'est validée.

2. Vérifier la compatibilité d'un module Terraform éventuel :
   ```bash
   grep -rn 'source *=' --include='*.tf' .
   ```
   👉 Explication : un module écrit pour Terraform doit être testé avec `tofu init` et `tofu validate` avant tout usage.

3. Consigner les points non couverts : pas de CI, de revue, d'état distant ni d'approbation multi-équipes.
   👉 Explication : ces éléments doivent être définis par l'organisation avant la production.

4. Vérifier le backend actuel :
   ```bash
   grep -rn 'backend' --include='*.tf' . || echo "backend local par défaut"
   ```
   👉 Explication : un backend local n'est pas adapté à un usage partagé.

## 2. Production — Contrôles

Créer une fiche de déploiement distincte par provider, backend et cible réelle; obtenir une revue technique, sécurité et financière.

## 3. Production — Sécurité

- Ne pas réutiliser le pilote sans adapter les contrôles d'identité et de portée.
- Ne pas publier un plan vers un environnement réel sans validation de la cible.
- Éviter les providers non maintenus ou non vérifiés.
- Traiter états, journaux et sorties comme potentiellement sensibles.

## Validation et retour arrière

- **Validation** : limitations et dépendances explicitement recensées; aucune cible réelle non documentée.
- **Arrêt** : demander une procédure spécialisée si le projet nécessite un fournisseur, un backend distant ou des garanties multi-équipes.

## Si le problème n'est pas résolu

- [OpenTofu — providers](https://opentofu.org/docs/language/providers/)
- [OpenTofu — backends](https://opentofu.org/docs/language/settings/backends/configuration/)
- [Guide complet OpenTofu Debian 13](/02-fiches-completes/debian/13/installation-deploiement/120-deploiement-opentofu-1-13-debian-13#8-limites)