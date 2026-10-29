# Fiche_Simple_-_VM_Debian_13_OpenTofu_Mise_A_Jour_Rollback.md

- **Environnement** : projet OpenTofu sauvegardé, clone de test disponible
- **OS / Version** : Debian 13; OpenTofu 1.13.x
- **Catégorie** : infrastructure as code / maintenance

---

## Problème précis à résoudre

Mettre à jour OpenTofu sans perdre l'état ni accepter une dérive non comprise.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder l'état (et la clé si le chiffrement est actif) :
   ```bash
   cd ~/iac/pilote
   install -d -m 0700 ~/iac/sauvegardes
   cp -a terraform.tfstate ~/iac/sauvegardes/terraform.tfstate.$(date +%F-%H%M)
   ```
   👉 Explication : après une montée de version, l'état peut ne plus être lisible par l'ancienne version.

2. Noter la version actuelle et celles disponibles :
   ```bash
   tofu version
   apt-cache madison tofu
   ```
   👉 Explication : lire les notes de version avant de choisir la cible.

3. Tester d'abord sur une copie du projet :
   ```bash
   cp -a ~/iac/pilote /tmp/pilote-test && cd /tmp/pilote-test
   tofu init -input=false -upgrade
   tofu plan -detailed-exitcode; echo "code=$?"
   ```
   👉 Explication : un plan inattendu bloque la mise à niveau.

4. Mettre à jour après approbation :
   ```bash
   sudo apt-mark unhold tofu
   sudo apt-get install -y tofu
   sudo apt-mark hold tofu
   ```
   👉 Explication : à faire dans la fenêtre de changement.

5. Revenir en arrière si nécessaire :
   ```bash
   sudo apt-get install -y --allow-downgrades tofu=VERSION_PRECEDENTE
   cp -a ~/iac/sauvegardes/terraform.tfstate.AAAA-MM-JJ-HHMM ~/iac/pilote/terraform.tfstate
   ```
   👉 Explication : remplacer version et fichier; pour un retrait complet : `sudo apt-get remove tofu`, puis supprimer `/etc/apt/sources.list.d/opentofu.list` et `/etc/apt/keyrings/opentofu*.gpg`.

## 2. Production — Contrôles

Approuver la fenêtre, la sauvegarde, les changements de provider, le plan de retour arrière et les critères de validation métier.

## 3. Production — Sécurité

- Ne pas mettre à niveau directement un projet de production sans clone.
- Ne pas supposer qu'un état migré est lisible par l'ancienne version.
- Protéger séparément les sauvegardes d'état et clés; tester leur restauration.
- Ne pas supprimer le dépôt ou les clés APT tant que d'autres paquets en dépendent.

## Validation et retour arrière

- **Validation** : version maîtrisée, plan compris, état sauvegardé et tests de restauration réussis.
- **Retour arrière** : restaurer ensemble binaire, projet, fournisseurs et état compatibles; ne pas rétrograder le binaire seul si le format d'état a changé.

## Si le problème n'est pas résolu

- [OpenTofu — versions publiées](https://github.com/opentofu/opentofu/releases)
- [OpenTofu — chiffrement d'état](https://opentofu.org/docs/language/state/encryption/)
- [Guide complet OpenTofu Debian 13](/02-fiches-completes/debian/13/installation-deploiement/120-deploiement-opentofu-1-13-debian-13#7-mettre-a-jour-sauvegarder-et-revenir-en-arriere)