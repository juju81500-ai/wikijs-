# Fiche_Simple_-_VM_Debian_13_Vault_Installer.md

- **Environnement** : Cluster Vault trois nœuds Raft sur Debian 13
- **OS / Version** : Debian 13 Trixie x86-64; Vault Community ou Enterprise selon canal validé
- **Catégorie** : coffre de secrets / installation

---

## Problème précis à résoudre

Installer une version Vault officielle et épinglée, avec utilisateur de service dédié.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les prérequis du dépôt signé HashiCorp :
   ```bash
   sudo apt update
   sudo apt install -y gpg curl lsb-release ca-certificates
   ```
   👉 Explication : on prépare la vérification de signature du dépôt.

2. Importer la clé du dépôt officiel et l'ajouter (procédure officielle HashiCorp) :
   ```bash
   curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
   echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
   ```
   👉 Explication : le dépôt est signé : APT refusera un paquet altéré. Si la documentation éditeur indique un autre nom de suite pour trixie, la suivre.

3. Lister les versions disponibles puis installer une version précise (version d'exemple à remplacer par celle validée) :
   ```bash
   sudo apt update
   apt-cache madison vault | head
   sudo apt install -y vault=1.20.0-1
   sudo apt-mark hold vault
   ```
   👉 Explication : on épingle la version validée au lieu de suivre `latest`; `apt-mark hold` évite une mise à jour involontaire.

4. Contrôler le compte de service et les droits :
   ```bash
   vault version
   id vault
   ls -ld /etc/vault.d /opt/vault
   ```
   👉 Explication : le paquet crée l'utilisateur `vault` et l'unité systemd; Vault ne doit pas tourner en root.

## 2. Production — Contrôles

Mettre à jour de façon planifiée : tester la nouvelle version sur un nœud de pré-production et conserver la version épinglée.

## 3. Production — Sécurité

- Ne pas installer par script `curl | sudo bash`.
- Vérifier la signature/checksum si le binaire est téléchargé manuellement.

## Validation et retour arrière

- **Validation** : `vault version` affiche la version attendue et l'utilisateur `vault` existe.
- **Retour arrière** : `sudo apt-mark unhold vault` puis `sudo apt remove vault` sur un nœud non initialisé; ne supprimer aucune donnée Raft existante sans sauvegarde.

## Si le problème n'est pas résolu

- [HashiCorp — Installer Vault](https://developer.hashicorp.com/vault/install)
- [HashiCorp — Déployer Vault avec Integrated Storage/Raft](https://developer.hashicorp.com/vault/tutorials/day-one-raft/raft-deployment-guide)
- [HashiCorp — Durcissement production](https://developer.hashicorp.com/vault/docs/concepts/production-hardening)
- [Guide complet — étape 2](/02-fiches-completes/debian/13/installation-deploiement/61-deploiement-hashicorp-vault-raft-debian-13#2-installer-vault)