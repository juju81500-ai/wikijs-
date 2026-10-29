# Fiche_Simple_-_VM_Debian_13_OpenTofu_Verifier.md

- **Environnement** : projet OpenTofu pilote sans fournisseur
- **OS / Version** : Debian 13; OpenTofu 1.13.x
- **Catégorie** : infrastructure as code / contrôle qualité
- **Tags** : `debian13`, `opentofu`, `validate`, `format`, `plan`

---

## Problème précis à résoudre

Vérifier la version, le dépôt, le format HCL et la stabilité du plan du pilote OpenTofu.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la version et l'origine du paquet :
   ```bash
   tofu version
   apt-cache policy tofu
   ```
   👉 Explication : la version attendue et le dépôt `packages.opentofu.org` doivent apparaître.

2. Vérifier le format et la validité :
   ```bash
   cd ~/iac/pilote
   tofu fmt -check
   tofu validate
   ```
   👉 Explication : aucun écart de format; `validate` doit réussir.

3. Vérifier la reproductibilité du plan :
   ```bash
   tofu plan -input=false -detailed-exitcode; echo "code=$?"
   ```
   👉 Explication : le code `0` indique qu'aucun changement n'est prévu.

4. Rechercher des secrets dans les fichiers et l'historique :
   ```bash
   grep -rEn "(password|secret|token|apikey)\s*=" ~/iac || echo "aucun secret dans les fichiers"
   grep -En "TF_VAR|token|password" ~/.bash_history | head || true
   ```
   👉 Explication : aucun secret ne doit apparaître dans les fichiers, l'historique ou les journaux de CI.

## 2. Production — Contrôles

Intégrer format, validation, revue des providers et plan dans la chaîne CI contrôlée; conserver approbation et traçabilité du plan appliqué.

## 3. Production — Sécurité

- `validate` ne prouve pas l'innocuité d'un plan ni la conformité du provider.
- Ne pas lancer `apply` en cas de dérive ou de changement inattendu.
- Ne pas publier des plans ou journaux sans vérifier les valeurs sensibles.
- Versionner les verrous de dépendances et revoir tout changement de provider.

## Validation et retour arrière

- **Validation** : format et validation passent, provenance confirmée, plan compris et absence de secret vérifiée.
- **Retour arrière** : revenir à la version précédente du code et du verrou; ne pas appliquer pour « corriger » un plan inexpliqué.

## Si le problème n'est pas résolu

- [OpenTofu — commande validate](https://opentofu.org/docs/cli/commands/validate/)
- [OpenTofu — plan](https://opentofu.org/docs/cli/commands/plan/)
- [OpenTofu — fichier de verrouillage de dépendances](https://opentofu.org/docs/language/files/dependency-lock/)
- [Guide complet OpenTofu Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/120_Deploiement_OpenTofu_1.13_Debian_13.md#6-verifier)
