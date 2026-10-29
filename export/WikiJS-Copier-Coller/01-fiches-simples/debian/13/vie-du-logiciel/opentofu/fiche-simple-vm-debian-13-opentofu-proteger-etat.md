# Fiche_Simple_-_VM_Debian_13_OpenTofu_Proteger_Etat.md

- **Environnement** : projet OpenTofu avec état local ou backend approuvé
- **OS / Version** : Debian 13; OpenTofu
- **Catégorie** : infrastructure as code / état et secrets

---

## Problème précis à résoudre

Protéger l'état, les plans et les secrets OpenTofu, et choisir un mode partagé avec verrouillage si nécessaire.

## 1. Hors-Production (Lab / Test / POC)

1. Constater l'état local et ses droits :
   ```bash
   ls -l terraform.tfstate* 2>/dev/null
   chmod 0600 terraform.tfstate* 2>/dev/null
   ```
   👉 Explication : l'état peut contenir des valeurs sensibles en clair; limiter l'accès au seul exécutant.

2. Exclure état, plans et secrets du dépôt :
   ```bash
   printf '%s\n' 'terraform.tfstate*' '*.tfplan' '*.tfvars' '.terraform/' >> .gitignore
   git check-ignore -v terraform.tfstate pilote.tfplan 2>/dev/null
   ```
   👉 Explication : `.terraform.lock.hcl` reste versionné lorsqu'un fournisseur est utilisé; l'état, les plans et les variables secrètes ne le sont jamais.

3. Avant d'activer le chiffrement, faire une copie temporaire de l'état :
   ```bash
   install -m 0600 terraform.tfstate /tmp/tfstate-avant-chiffrement
   ```
   👉 Explication : sans la clé, l'état chiffré devient illisible; sauvegarder la clé séparément et tester la restauration, puis détruire la copie temporaire.

4. Configurer le chiffrement par variable d'environnement (exemple de clé en phrase secrète, saisie masquée) :
   ```bash
   read -rsp 'Phrase secrète : ' TF_PASS; echo
   export TF_ENCRYPTION="key_provider \"pbkdf2\" \"main\" { passphrase = \"$TF_PASS\" }
   method \"aes_gcm\" \"main\" { keys = key_provider.pbkdf2.main }
   state { method = method.aes_gcm.main }"
   unset TF_PASS
   ```
   👉 Explication : le bloc de chiffrement se déclare aussi dans `terraform { encryption { ... } }`; avec un KMS, utiliser une clé distincte par état. Vérifier la syntaxe dans la documentation officielle avant usage.

5. Pour un usage partagé, choisir un backend distant avec verrouillage : voir `https://opentofu.org/docs/language/settings/backends/configuration/`.
   👉 Explication : le verrou évite deux `apply` simultanés.

## 2. Production — Contrôles

Faire approuver le backend, la résidence des données, l'identité des exécutants, le verrouillage, sauvegarde, chiffrement et rétention avant toute utilisation d'équipe.

## 3. Production — Sécurité

- Ajouter `terraform.tfstate`, `*.tfplan` et fichiers sensibles au `.gitignore`.
- Ne pas partager ou envoyer l'état dans un ticket; il peut contenir des valeurs sensibles.
- Garder les clés de chiffrement séparées de l'état et planifier leur récupération.
- Ne pas activer un backend distant sans ACL, verrouillage et sauvegarde testés.

## Validation et retour arrière

- **Validation** : aucun état/plan sensible commité; accès au backend limité et restauration testée.
- **Retour arrière** : conserver une copie vérifiée de l'état et de ses clés avant migration; si perte de clé, ne pas supprimer la sauvegarde chiffrée.

## Si le problème n'est pas résolu

- [OpenTofu — chiffrement de l'état](https://opentofu.org/docs/language/state/encryption/)
- [OpenTofu — verrouillage de l'état](https://opentofu.org/docs/language/state/locking/)
- [OpenTofu — backends](https://opentofu.org/docs/language/settings/backends/configuration/)
- [Guide complet OpenTofu Debian 13](/02-fiches-completes/debian/13/installation-deploiement/120-deploiement-opentofu-1-13-debian-13#5-gerer-letat-les-verrous-et-les-secrets)