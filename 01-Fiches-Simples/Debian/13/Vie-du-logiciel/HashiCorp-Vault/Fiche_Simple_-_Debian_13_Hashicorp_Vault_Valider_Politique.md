# 📄 Fiche_Simple_-_Debian_13_Hashicorp_Vault_Valider_Politique.md

- **Environnement** : HashiCorp Vault avec TLS, authentification et policy de test
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Secrets / contrôle d'accès
- **Tags** : `debian13`, `vault`, `secrets`, `policy`, `tls`, `audit`

---

## 🎯 Problème précis à résoudre

Vérifier qu'une identité applicative ne peut lire que le chemin de secrets explicitement autorisé.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Confirmer l'endpoint HTTPS et la CA approuvée :
   ```bash
   export VAULT_ADDR=https://vault.example.net:8200
   export VAULT_CACERT=/etc/vault.d/tls/ca.crt
   vault status
   ```
   👉 Explication : remplacer URL et chemin; ne jamais désactiver la validation TLS (`VAULT_SKIP_VERIFY`).

2. Créer un secret synthétique, une policy minimale et un token temporaire (avec un compte administrateur de test) :
   ```bash
   vault kv put secret/test/appli cle=valeur-synthetique
   vault policy write test-appli - <<'EOF'
   path "secret/data/test/appli" { capabilities = ["read"] }
   EOF
   vault token create -policy=test-appli -ttl=15m -format=json | jq -r .auth.client_token > /tmp/vault-test-token
   chmod 0600 /tmp/vault-test-token
   ```
   👉 Explication : le token est écrit dans un fichier protégé et non affiché; il expire en 15 minutes.

3. Tester la lecture autorisée puis un chemin voisin interdit :
   ```bash
   VAULT_TOKEN=$(cat /tmp/vault-test-token) vault kv get secret/test/appli
   VAULT_TOKEN=$(cat /tmp/vault-test-token) vault kv get secret/test/autre
   ```
   👉 Explication : la première réussit; la seconde doit retourner `permission denied`.

4. Vérifier l'audit et la révocation :
   ```bash
   sudo tail -5 /var/log/vault/audit.log
   vault token revoke "$(cat /tmp/vault-test-token)"
   VAULT_TOKEN=$(cat /tmp/vault-test-token) vault kv get secret/test/appli
   rm -f /tmp/vault-test-token
   ```
   👉 Explication : l'accès apparaît dans l'audit log; après révocation la lecture doit échouer.


## ⚡ 2. Production — Façon Simplifiée

1. Lister les policies et vérifier TTL et propriétaire :
   ```bash
   vault policy list
   vault policy read NOM_POLICY
   vault read auth/APPROLE_OU_METHODE/role/NOM_ROLE
   ```
   👉 Explication : une policy par application, token court; revoir périodiquement chemins, TTL et dernière utilisation.


## 🔒 3. Production — Façon Sécurisée

- Ne pas utiliser le token root pour l'accès applicatif; le révoquer après bootstrap.
- Ne pas mettre token, unseal key ou secret en argument CLI, dans l'historique ou dans le pipeline de logs.
- Tester le refus d'accès comme une assertion obligatoire avant changement de policy.

## ✅ Validation et retour arrière

- **Validation** : accès au seul chemin attendu, refus vérifié hors périmètre, audit reçu, révocation effective.
- **Retour arrière** : retirer le token de test et restaurer la policy versionnée précédente si l'accès applicatif échoue.

## 🔗 Si le problème n'est pas résolu

- [HashiCorp — Durcissement production](https://developer.hashicorp.com/vault/docs/concepts/production-hardening)
- [HashiCorp — Tokens](https://developer.hashicorp.com/vault/docs/concepts/tokens)