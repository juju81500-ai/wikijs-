---
title: "Fiche Simple - VM Debian 13 Vault Acces Audit"
description: "Limiter l'usage du token root, créer des politiques à moindre privilège et activer l'audit."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "vault", "policy", "audit", "token"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Vault_Acces_Audit.md

- **Environnement** : Cluster Vault trois nœuds Raft sur Debian 13
- **OS / Version** : Debian 13 Trixie x86-64; Vault Community ou Enterprise selon canal validé
- **Catégorie** : coffre de secrets / IAM et audit
- **Tags** : `debian13`, `vault`, `policy`, `audit`, `token`

---

## Problème précis à résoudre

Limiter l'usage du token root, créer des politiques à moindre privilège et activer l'audit.

## 1. Hors-Production (Lab / Test / POC)

1. S'authentifier avec le token root uniquement pour le bootstrap :
   ```bash
   vault login
   ```
   👉 Explication : la saisie du token est masquée; ne pas le passer en argument.

2. Activer un audit device fichier avant tout usage :
   ```bash
   sudo install -d -o vault -g vault -m 0750 /var/log/vault
   vault audit enable file file_path=/var/log/vault/audit.log
   vault audit list
   ```
   👉 Explication : chaque requête est journalisée; expédier ensuite ce fichier vers un stockage central protégé.

3. Écrire une politique explicite (chemin d'exemple à remplacer) :
   ```bash
   vault policy write app-lecture - <<'EOF'
   path "secret/data/app/*" {
     capabilities = ["read"]
   }
   EOF
   ```
   👉 Explication : la politique n'autorise que la lecture du chemin de l'application.

4. Tester avec un secret synthétique et un token court :
   ```bash
   vault secrets enable -path=secret kv-v2
   vault kv put secret/app/test valeur=synthetique
   vault token create -policy=app-lecture -ttl=15m
   ```
   👉 Explication : le token créé expire en 15 minutes; il sert à vérifier l'accès autorisé et le refus hors politique.

5. Révoquer le token d'essai (jeton à copier depuis la sortie précédente) :
   ```bash
   vault token revoke -self
   ```
   👉 Explication : la révocation confirme que le cycle de vie fonctionne; exécuter après `vault login` avec le token d'essai.

## 2. Production — Contrôles

Méthode d'authentification d'entreprise (OIDC/LDAP), politiques revues, TTL courts, audit expédié, comptes sortants révoqués.

## 3. Production — Sécurité

- Token root utilisé uniquement au bootstrap puis révoqué.
- Ne jamais mettre de secret réel dans les politiques de test.
- L'interface Web n'est pas un substitut à l'IAM ni à l'audit.

## Validation et retour arrière

- **Validation** : `vault audit list` montre l'audit actif, un accès hors politique est refusé (permission denied).
- **Retour arrière** : `vault audit disable file/` si l'audit est mal configuré (seulement en lab; en production, garder au moins un audit actif); `vault policy delete app-lecture`.

## Si le problème n'est pas résolu

- [HashiCorp — Installer Vault](https://developer.hashicorp.com/vault/install)
- [HashiCorp — Déployer Vault avec Integrated Storage/Raft](https://developer.hashicorp.com/vault/tutorials/day-one-raft/raft-deployment-guide)
- [HashiCorp — Durcissement production](https://developer.hashicorp.com/vault/docs/concepts/production-hardening)
- [Guide complet — étape 5](/02-fiches-completes/debian/13/installation-deploiement/61-deploiement-hashicorp-vault-raft-debian-13#5-creer-les-acces-et-audit)