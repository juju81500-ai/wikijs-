# Fiche_Simple_-_VM_Debian_13_PostgreSQL_Securiser

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; PostgreSQL 17 des dépôts Debian
- **Catégorie** : base de données / PostgreSQL / Sécuriser (TLS, pg_hba, pare-feu)
- **Tags** : `debian13`, `postgresql`, `securite`

---

## Problème précis à résoudre

Chiffrer les connexions PostgreSQL, restreindre `pg_hba.conf` et filtrer le port 5432.

## 1. Hors-Production (Lab / Test / POC)

1. Lab : générer un certificat TLS :
   ```bash
   sudo install -d -o postgres -g postgres -m 0750 /etc/postgresql/tls
   sudo openssl req -x509 -nodes -newkey rsa:3072 -days 90 -keyout /etc/postgresql/tls/server.key -out /etc/postgresql/tls/server.crt -subj '/CN=NOM_SERVEUR'
   sudo chown postgres:postgres /etc/postgresql/tls/* && sudo chmod 0600 /etc/postgresql/tls/server.key
   ```
   👉 Explication : remplacer `NOM_SERVEUR` (à remplacer) ; en production, certificat de l'AC interne.

2. Activer TLS et le chiffrement SCRAM :
   ```bash
   sudo tee /etc/postgresql/17/main/conf.d/70-tls.conf >/dev/null <<'EOF'
   ssl = on
   ssl_cert_file = '/etc/postgresql/tls/server.crt'
   ssl_key_file = '/etc/postgresql/tls/server.key'
   ssl_min_protocol_version = 'TLSv1.2'
   password_encryption = 'scram-sha-256'
   listen_addresses = 'IP_SERVEUR'
   EOF
   sudo systemctl restart postgresql
   ```
   👉 Explication : remplacer `IP_SERVEUR` (à remplacer) ; garder `localhost` s'il n'y a pas de client distant.

3. Restreindre pg_hba.conf :
   ```bash
   sudo cp -a /etc/postgresql/17/main/pg_hba.conf /etc/postgresql/17/main/pg_hba.conf.orig
   echo 'hostssl APPDB APPUSER IP_CLIENT/32 scram-sha-256' | sudo tee -a /etc/postgresql/17/main/pg_hba.conf
   sudo systemctl reload postgresql
   ```
   👉 Explication : remplacer `APPDB`, `APPUSER`, `IP_CLIENT` (à remplacer) ; aucune ligne `trust` ni `0.0.0.0/0`.

4. Filtrer le port 5432 :
   ```bash
   sudo nft list ruleset | head -20
   # si ufw est utilisé :
   sudo ufw allow from IP_CLIENT to any port 5432 proto tcp
   ```
   👉 Explication : seules les IP clientes autorisées atteignent PostgreSQL.

## 2. Production — Contrôles

Certificats supervisés, `pg_hba.conf` revu à chaque changement, journaux centralisés.

## 3. Production — Sécurité

- Jamais de méthode `trust` ni de port ouvert à Internet.
- Clé privée en `0600` propriétaire `postgres`.
- Mots de passe saisis ou générés, jamais commités.

## Validation et retour arrière

- **Validation** : `psql 'host=IP_SERVEUR sslmode=require dbname=APPDB user=APPUSER'` fonctionne depuis le client et un accès sans TLS est refusé.
- **Retour arrière** : restaurer `pg_hba.conf.orig`, supprimer `70-tls.conf`, redémarrer.

## Si le problème n'est pas résolu

- [PostgreSQL — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Prerequis_Limites.md)
- [PostgreSQL — Configurer](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Configurer.md)
- [PostgreSQL — Valider (recette)](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Valider.md)
- [PostgreSQL — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Sauvegarder_Restaurer.md)
- [PostgreSQL — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Mettre_A_Jour.md)
- [Installation PostgreSQL 17 (fiche du pack)](Fiche_Simple_-_VM_Debian_13_Database_Installation_PostgreSQL_17.md)
- [PostgreSQL — documentation officielle](https://www.postgresql.org/docs/)
