# Fiche_Simple_-_VM_Debian_13_MariaDB_Securiser

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MariaDB des dépôts Debian
- **Catégorie** : base de données / MariaDB / Sécuriser (TLS, comptes, pare-feu)

---

## Problème précis à résoudre

Chiffrer les connexions, durcir les comptes et limiter l'accès réseau à MariaDB.

## 1. Hors-Production (Lab / Test / POC)

1. Durcir l'installation :
   ```bash
   sudo mariadb-secure-installation
   ```
   👉 Explication : répondre : définir l'authentification, supprimer les comptes anonymes, interdire `root` distant, supprimer la base `test`.

2. Lab : générer un certificat TLS auto-signé :
   ```bash
   sudo install -d -o mysql -g mysql -m 0750 /etc/mysql/tls
   sudo openssl req -x509 -nodes -newkey rsa:3072 -days 90 -keyout /etc/mysql/tls/server.key -out /etc/mysql/tls/server.crt -subj '/CN=NOM_SERVEUR'
   sudo chown mysql:mysql /etc/mysql/tls/* && sudo chmod 0600 /etc/mysql/tls/server.key
   ```
   👉 Explication : remplacer `NOM_SERVEUR` (à remplacer) ; en production utiliser un certificat de l'AC interne.

3. Activer TLS et l'écoute sur l'interface d'administration :
   ```bash
   sudo tee /etc/mysql/mariadb.conf.d/70-tls.cnf >/dev/null <<'EOF'
   [mysqld]
   ssl_cert = /etc/mysql/tls/server.crt
   ssl_key  = /etc/mysql/tls/server.key
   tls_version = TLSv1.2,TLSv1.3
   bind-address = IP_SERVEUR
   EOF
   sudo systemctl restart mariadb
   ```
   👉 Explication : remplacer `IP_SERVEUR` par l'adresse d'écoute réelle (à remplacer) ; garder `127.0.0.1` si aucun client distant.

4. Imposer TLS aux comptes distants :
   ```bash
   sudo mariadb -e "CREATE USER 'APPUSER'@'IP_CLIENT' IDENTIFIED BY 'MOT_DE_PASSE_A_SAISIR' REQUIRE SSL;"
   ```
   👉 Explication : ne pas conserver ce mot de passe en clair : le remplacer par la saisie sécurisée de la fiche Configurer. Remplacer `IP_CLIENT`.

5. Filtrer le port 3306 :
   ```bash
   sudo nft list ruleset | head -20
   # si ufw est utilisé :
   sudo ufw allow from IP_CLIENT to any port 3306 proto tcp
   ```
   👉 Explication : seules les IP clientes autorisées atteignent le port 3306.

## 2. Production — Contrôles

Certificats d'AC avec échéance supervisée, comptes revus périodiquement, journaux d'erreurs surveillés.

## 3. Production — Sécurité

- Jamais de port 3306 ouvert à tout Internet.
- Clé privée en `0600`, propriétaire `mysql`.
- Pas de compte `root@%`.
- Tous les mots de passe saisis ou générés, jamais commités.

## Validation et retour arrière

- **Validation** : `SHOW VARIABLES LIKE 'have_ssl'` renvoie `YES` et un client sans TLS est refusé pour les comptes `REQUIRE SSL`.
- **Retour arrière** : supprimer `70-tls.cnf`, redémarrer, rétablir `bind-address` précédent.

## Si le problème n'est pas résolu

- [MariaDB — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-prerequis-limites)
- [MariaDB — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-configurer)
- [MariaDB — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-valider)
- [MariaDB — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-sauvegarder-restaurer)
- [MariaDB — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-mettre-a-jour)
- [Guide complet LEMP Debian 13 (MariaDB)](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb)
- [Installation MariaDB 11 (fiche du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-database-installation-mariadb-11)
- [Durcissement MariaDB (fiche du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-lemp-securiser-mariadb)
- [MariaDB — documentation officielle](https://mariadb.com/kb/en/documentation/)