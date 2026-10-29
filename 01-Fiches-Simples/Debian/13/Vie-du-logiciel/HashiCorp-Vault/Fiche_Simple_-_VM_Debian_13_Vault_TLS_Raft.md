# Fiche_Simple_-_VM_Debian_13_Vault_TLS_Raft.md

- **Environnement** : Cluster Vault trois nœuds Raft sur Debian 13
- **OS / Version** : Debian 13 Trixie x86-64; Vault Community ou Enterprise selon canal validé
- **Catégorie** : coffre de secrets / configuration
- **Tags** : `debian13`, `vault`, `tls`, `raft`, `configuration`

---

## Problème précis à résoudre

Chiffrer l'API et le cluster et configurer le stockage Raft persistant sur chaque nœud.

## 1. Hors-Production (Lab / Test / POC)

1. Placer le certificat du nœud et sa clé (émis par l'autorité approuvée, SAN = nom DNS du nœud) avec des droits stricts :
   ```bash
   sudo install -d -o vault -g vault -m 0750 /opt/vault/tls
   sudo install -o vault -g vault -m 0640 vault1-fullchain.pem /opt/vault/tls/vault.crt
   sudo install -o vault -g vault -m 0600 vault1.key /opt/vault/tls/vault.key
   ```
   👉 Explication : les fichiers `vault1-fullchain.pem` et `vault1.key` sont des exemples à remplacer; la clé privée reste lisible uniquement par `vault`.

2. Sauvegarder la configuration d'origine puis éditer `/etc/vault.d/vault.hcl` :
   ```bash
   sudo cp -a /etc/vault.d/vault.hcl /etc/vault.d/vault.hcl.orig
   sudoedit /etc/vault.d/vault.hcl
   ```
   👉 Explication : la copie permet le retour arrière.

3. Y mettre (noms et chemins d'exemple à remplacer, `node_id` unique par nœud) :
   ```bash
   ui = false
   api_addr = "https://vault1.example.invalid:8200"
   cluster_addr = "https://vault1.example.invalid:8201"
   storage "raft" {
     path    = "/opt/vault/data"
     node_id = "vault1"
   }
   listener "tcp" {
     address         = "0.0.0.0:8200"
     cluster_address = "0.0.0.0:8201"
     tls_cert_file   = "/opt/vault/tls/vault.crt"
     tls_key_file    = "/opt/vault/tls/vault.key"
   }
   ```
   👉 Explication : ces lignes (bloc de fichier, à enregistrer dans `vault.hcl`) activent TLS sur l'API 8200 et le cluster 8201 et un stockage Raft persistant.

4. Restreindre le pare-feu et désactiver les core dumps (selon vos outils; exemple systemd) :
   ```bash
   sudo mkdir -p /etc/systemd/system/vault.service.d
   printf '[Service]\nLimitCORE=0\n' | sudo tee /etc/systemd/system/vault.service.d/nocore.conf
   sudo systemctl daemon-reload
   ```
   👉 Explication : on évite qu'un plantage écrive des secrets en mémoire dans un fichier core; n'ouvrir 8200/8201 qu'aux clients et nœuds du cluster.

## 2. Production — Contrôles

Un certificat par nœud avec renouvellement planifié, pare-feu 8200/8201 limité, stockage dédié et sauvegardé.

## 3. Production — Sécurité

- Ne jamais copier une configuration de développement (`-dev`).
- Ne pas définir `tls_disable = true` ni `VAULT_SKIP_VERIFY`.
- Clé privée en 0600, propriétaire `vault`.

## Validation et retour arrière

- **Validation** : `sudo -u vault vault operator diagnose -config=/etc/vault.d/vault.hcl` ne signale pas d'erreur bloquante.
- **Retour arrière** : restaurer `/etc/vault.d/vault.hcl.orig` et recharger la configuration; ne pas supprimer `/opt/vault/data` sans snapshot.

## Si le problème n'est pas résolu

- [HashiCorp — Installer Vault](https://developer.hashicorp.com/vault/install)
- [HashiCorp — Déployer Vault avec Integrated Storage/Raft](https://developer.hashicorp.com/vault/tutorials/day-one-raft/raft-deployment-guide)
- [HashiCorp — Durcissement production](https://developer.hashicorp.com/vault/docs/concepts/production-hardening)
- [Guide complet — étape 3](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/61_Deploiement_Hashicorp_Vault_Raft_Debian_13.md#3-configurer-tls-et-stockage)
