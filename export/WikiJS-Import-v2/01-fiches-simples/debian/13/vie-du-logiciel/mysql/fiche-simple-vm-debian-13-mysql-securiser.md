---
title: "Fiche Simple - VM Debian 13 MySQL Securiser"
description: "Durcir les comptes, imposer TLS et filtrer le port 3306 de MySQL."
published: true
date: 2026-10-29T20:37:00Z
tags: ["debian13", "mysql", "securite"]
editor: markdown
dateCreated: 2026-10-29T20:37:00Z
dateModified: 2026-10-29T20:37:00Z
---

# Fiche_Simple_-_VM_Debian_13_MySQL_Securiser

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MySQL Community (dépôt officiel Oracle)
- **Catégorie** : base de données / MySQL / Sécuriser (TLS, comptes, pare-feu)
- **Tags** : `debian13`, `mysql`, `securite`

---

## Problème précis à résoudre

Durcir les comptes, imposer TLS et filtrer le port 3306 de MySQL.

## 1. Hors-Production (Lab / Test / POC)

1. Durcir l'installation :
   ```bash
   sudo mysql_secure_installation
   ```
   👉 Explication : supprimer les comptes anonymes, interdire `root` distant, supprimer la base `test`, activer la validation des mots de passe.

2. Contrôler le chiffrement disponible :
   ```bash
   mysql -u root -p -e "SHOW VARIABLES LIKE 'have_ssl'; SHOW VARIABLES LIKE 'ssl_ca';"
   ```
   👉 Explication : MySQL génère des certificats auto-signés dans `/var/lib/mysql` ; en production, utiliser un certificat de l'AC interne via `ssl_ca`, `ssl_cert`, `ssl_key`.

3. Imposer TLS et versions récentes :
   ```bash
   sudo tee /etc/mysql/mysql.conf.d/70-tls.cnf >/dev/null <<'EOF'
   [mysqld]
   require_secure_transport = ON
   tls_version = TLSv1.2,TLSv1.3
   bind-address = IP_SERVEUR
   EOF
   sudo systemctl restart mysql
   ```
   👉 Explication : remplacer `IP_SERVEUR` (à remplacer) ; `require_secure_transport` n'impose pas TLS aux connexions par socket UNIX.

4. Filtrer le port 3306 :
   ```bash
   sudo nft list ruleset | head -20
   # si ufw est utilisé :
   sudo ufw allow from IP_CLIENT to any port 3306 proto tcp
   ```
   👉 Explication : seules les IP clientes autorisées atteignent le port.

## 2. Production — Contrôles

Certificats supervisés, comptes revus, journaux d'erreurs surveillés.

## 3. Production — Sécurité

- Jamais de port 3306 ouvert à Internet.
- Clé privée en `0600` propriétaire `mysql`.
- Pas de `root@%`.
- Mots de passe saisis ou générés.

## Validation et retour arrière

- **Validation** : `SHOW STATUS LIKE 'Ssl_cipher'` non vide depuis un client distant ; une connexion sans TLS est refusée.
- **Retour arrière** : supprimer `70-tls.cnf`, redémarrer.

## Si le problème n'est pas résolu

- [MySQL — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-prerequis-limites)
- [MySQL — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-installer)
- [MySQL — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-configurer)
- [MySQL — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-valider)
- [MySQL — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-sauvegarder-restaurer)
- [MySQL — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-mettre-a-jour)
- [MySQL — documentation officielle](https://dev.mysql.com/doc/)
- [Alternative MariaDB (fiches du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-prerequis-limites)