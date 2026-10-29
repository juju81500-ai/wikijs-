# Fiche_Simple_-_VM_Debian_13_Vault_Initialiser.md

- **Environnement** : Cluster Vault trois nœuds Raft sur Debian 13
- **OS / Version** : Debian 13 Trixie x86-64; Vault Community ou Enterprise selon canal validé
- **Catégorie** : coffre de secrets / initialisation

---

## Problème précis à résoudre

Démarrer les nœuds, initialiser le cluster une seule fois et joindre les autres nœuds.

## 1. Hors-Production (Lab / Test / POC)

1. Définir l'adresse et la CA de confiance dans le shell (valeurs d'exemple à remplacer) :
   ```bash
   export VAULT_ADDR=https://vault1.example.invalid:8200
   export VAULT_CACERT=/etc/ssl/certs/ca-entreprise.pem
   ```
   👉 Explication : le client vérifie le certificat; `VAULT_SKIP_VERIFY` n'est jamais utilisé.

2. Activer et démarrer le service :
   ```bash
   sudo systemctl enable --now vault
   sudo systemctl --no-pager status vault
   ```
   👉 Explication : Vault démarre scellé (sealed), c'est normal avant l'initialisation.

3. Initialiser une seule fois, sur le premier nœud, dans une cérémonie avec les détenteurs de parts :
   ```bash
   vault operator init -key-shares=5 -key-threshold=3
   ```
   👉 Explication : la commande affiche 5 parts de déverrouillage et le token root initial; les noter hors ligne, une part par détenteur, sans les enregistrer dans un fichier, un ticket ou l'historique. Seuils d'exemple à adapter au plan.

4. Déverrouiller (répéter avec trois détenteurs différents; Vault demande la part sans qu'elle apparaisse en argument) :
   ```bash
   vault operator unseal
   ```
   👉 Explication : chaque exécution fournit une part jusqu'au seuil; ne jamais passer la part sur la ligne de commande.

5. Sur les autres nœuds, joindre le cluster (nom du leader d'exemple à remplacer) puis déverrouiller :
   ```bash
   vault operator raft join https://vault1.example.invalid:8200
   vault operator unseal
   ```
   👉 Explication : le nœud rejoint le groupe Raft; l'unseal est nécessaire sur chacun sans auto-unseal.

6. Contrôler quorum et leader :
   ```bash
   vault login
   vault operator raft list-peers
   ```
   👉 Explication : `vault login` demande le token en saisie masquée; la liste doit montrer un leader et les suiveurs.

## 2. Production — Contrôles

Cérémonie d'initialisation tracée, parts remises à des détenteurs séparés, auto-unseal via KMS/HSM supporté si retenu (identité machine, pas de credential en clair dans `vault.hcl`).

## 3. Production — Sécurité

- Ne jamais conserver les parts ou le token root en clair (historique, Wiki, ticket).
- Révoquer le token root initial après la mise en place des accès.

## Validation et retour arrière

- **Validation** : `vault status` montre `Initialized true`, `Sealed false` et `vault operator raft list-peers` affiche tous les nœuds.
- **Retour arrière** : avant toute donnée utile, arrêter les nœuds et vider les données Raft du lab pour ré-initialiser; en production, restaurer un snapshot.

## Si le problème n'est pas résolu

- [HashiCorp — Installer Vault](https://developer.hashicorp.com/vault/install)
- [HashiCorp — Déployer Vault avec Integrated Storage/Raft](https://developer.hashicorp.com/vault/tutorials/day-one-raft/raft-deployment-guide)
- [HashiCorp — Durcissement production](https://developer.hashicorp.com/vault/docs/concepts/production-hardening)
- [Guide complet — étape 4](/02-fiches-completes/debian/13/installation-deploiement/61-deploiement-hashicorp-vault-raft-debian-13#4-demarrer-initialiser-et-joindre-raft)