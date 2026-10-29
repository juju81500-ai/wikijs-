# Fiche_Simple_-_VM_Debian_13_Redis_Securiser

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Redis des dépôts Debian
- **Catégorie** : base clé-valeur / Redis / Sécuriser (ACL, TLS, pare-feu)
- **Tags** : `debian13`, `redis`, `securite`

---

## Problème précis à résoudre

Imposer l'authentification par ACL, activer TLS et filtrer le port 6379.

## 1. Hors-Production (Lab / Test / POC)

1. Générer un mot de passe fort et créer un utilisateur ACL :
   ```bash
   PW=$(openssl rand -base64 32)
   echo "$PW"   # à enregistrer immédiatement dans le coffre, puis fermer le terminal
   redis-cli ACL SETUSER APPUSER on ">$PW" '~APP:*' '+@read' '+@write' '-@dangerous'
   unset PW
   ```
   👉 Explication : remplacer `APPUSER` et le préfixe `APP:*` (à remplacer) ; le mot de passe est généré, jamais écrit dans un fichier du dépôt.

2. Désactiver l'utilisateur par défaut et persister les ACL :
   ```bash
   redis-cli ACL SETUSER default off
   redis-cli ACL SAVE
   ```
   👉 Explication : exige `aclfile /etc/redis/users.acl` dans la configuration (créer le fichier en `0640 redis:redis`) ; vérifier ensuite que l'accès administrateur reste possible avant de désactiver `default`.

3. Lab : préparer un certificat TLS :
   ```bash
   sudo install -d -o redis -g redis -m 0750 /etc/redis/tls
   sudo openssl req -x509 -nodes -newkey rsa:3072 -days 90 -keyout /etc/redis/tls/redis.key -out /etc/redis/tls/redis.crt -subj '/CN=NOM_SERVEUR'
   sudo chown redis:redis /etc/redis/tls/* && sudo chmod 0600 /etc/redis/tls/redis.key
   ```
   👉 Explication : remplacer `NOM_SERVEUR` (à remplacer) ; AC interne en production.

4. Activer TLS :
   ```bash
   sudo tee -a /etc/redis/redis-local.conf >/dev/null <<'EOF'
   port 0
   tls-port 6379
   tls-cert-file /etc/redis/tls/redis.crt
   tls-key-file /etc/redis/tls/redis.key
   tls-ca-cert-file /etc/redis/tls/redis.crt
   tls-auth-clients no
   bind 127.0.0.1 -::1 IP_SERVEUR
   EOF
   sudo systemctl restart redis-server
   ```
   👉 Explication : remplacer `IP_SERVEUR` (à remplacer) ; vérifier que le paquet Debian est compilé avec TLS (`redis-server --tls-port 6379` échoue sinon) ; en production, fournir une vraie AC dans `tls-ca-cert-file`.

5. Filtrer le port 6379 :
   ```bash
   sudo nft list ruleset | head -20
   # si ufw est utilisé :
   sudo ufw allow from IP_CLIENT to any port 6379 proto tcp
   ```
   👉 Explication : seules les IP clientes autorisées atteignent Redis.

## 2. Production — Contrôles

Mots de passe dans le coffre, ACL minimales par application, certificats supervisés, commandes dangereuses interdites.

## 3. Production — Sécurité

- Jamais de Redis sans authentification accessible hors loopback.
- Clés privées en `0600`.
- Mots de passe générés ou saisis, jamais commités.
- Interdire `CONFIG`, `FLUSHALL`, `DEBUG` aux comptes applicatifs.

## Validation et retour arrière

- **Validation** : `redis-cli --tls --cacert ... --user APPUSER ping` répond `PONG` avec le mot de passe, et échoue sans.
- **Retour arrière** : restaurer `redis.conf.orig` et supprimer `redis-local.conf` seulement après avoir réactivé un accès administrateur.

## Si le problème n'est pas résolu

- [Redis — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_Redis_Prerequis_Limites.md)
- [Redis — Installer](Fiche_Simple_-_VM_Debian_13_Redis_Installer.md)
- [Redis — Configurer](Fiche_Simple_-_VM_Debian_13_Redis_Configurer.md)
- [Redis — Valider (recette)](Fiche_Simple_-_VM_Debian_13_Redis_Valider.md)
- [Redis — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_Redis_Sauvegarder_Restaurer.md)
- [Redis — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_Redis_Mettre_A_Jour.md)
- [Redis — documentation officielle](https://redis.io/docs/latest/)
- [Redis — sécurité](https://redis.io/docs/latest/operate/oss_and_stack/management/security/)
- [Installation Redis avec NetBox (fiche du pack)](../PostgreSQL/Fiche_Simple_-_VM_Debian_13_NetBox_Installer_PostgreSQL_Redis.md)
