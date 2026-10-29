# Fiche_Simple_-_VM_Debian_13_OpenTofu_Installer.md

- **Environnement** : Debian 13 Trixie amd64, dépôts APT approuvés
- **OS / Version** : Debian 13; OpenTofu
- **Catégorie** : infrastructure as code / installation

---

## Problème précis à résoudre

Installer OpenTofu depuis le dépôt APT officiel en vérifiant clés, source et version du paquet.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les prérequis et préparer le dossier des clés :
   ```bash
   sudo apt-get update
   sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
   sudo install -m 0755 -d /etc/apt/keyrings
   ```
   👉 Explication : on évite d'exécuter en root un script distant non relu; les étapes manuelles sont explicites.

2. Télécharger les clés officielles :
   ```bash
   curl -fsSL https://get.opentofu.org/opentofu.gpg | sudo tee /etc/apt/keyrings/opentofu.gpg >/dev/null
   curl -fsSL https://packages.opentofu.org/opentofu/tofu/gpgkey | sudo gpg --no-tty --batch --dearmor -o /etc/apt/keyrings/opentofu-repo.gpg >/dev/null
   sudo chmod a+r /etc/apt/keyrings/opentofu.gpg /etc/apt/keyrings/opentofu-repo.gpg
   ```
   👉 Explication : les deux clés servent à signer le dépôt et ses métadonnées.

3. Déclarer le dépôt :
   ```bash
   echo "deb [signed-by=/etc/apt/keyrings/opentofu.gpg,/etc/apt/keyrings/opentofu-repo.gpg] https://packages.opentofu.org/opentofu/tofu/any/ any main" | sudo tee /etc/apt/sources.list.d/opentofu.list >/dev/null
   sudo chmod a+r /etc/apt/sources.list.d/opentofu.list
   ```
   👉 Explication : `signed-by` limite la confiance de ces clés à ce dépôt.

4. Installer et vérifier :
   ```bash
   sudo apt-get update
   sudo apt-get install -y tofu
   tofu version
   apt-cache policy tofu
   ```
   👉 Explication : `tofu version` doit afficher la version attendue; `apt-cache policy` doit montrer `packages.opentofu.org`.

5. Figer la version en production :
   ```bash
   apt-cache madison tofu
   sudo apt-mark hold tofu
   ```
   👉 Explication : empêche une mise à jour hors fenêtre de changement.

## 2. Production — Contrôles

Figer la version approuvée avec le processus APT d'entreprise et tester chaque mise à jour dans une VM de contrôle avant diffusion.

## 3. Production — Sécurité

- Ne pas exécuter un script d'installation non relu en tant que root.
- Ne pas désactiver APT Secure ni utiliser une clé provenant d'une source non officielle.
- Ne pas réutiliser les clés comme autorisation pour des dépôts non concernés.
- Ne pas installer sur un nœud de production sans revue de changement.

## Validation et retour arrière

- **Validation** : paquet candidat issu du dépôt approuvé et version attendue affichée.
- **Retour arrière** : conserver la version antérieure approuvée; si les clés ou l'origine ne correspondent pas, arrêter l'installation.

## Si le problème n'est pas résolu

- [OpenTofu — installation Debian/Ubuntu](https://opentofu.org/docs/intro/install/deb/)
- [OpenTofu — versions publiées](https://github.com/opentofu/opentofu/releases)
- [Guide complet OpenTofu Debian 13](/02-fiches-completes/debian/13/installation-deploiement/120-deploiement-opentofu-1-13-debian-13#2-installer-depuis-le-depot-apt-officiel)