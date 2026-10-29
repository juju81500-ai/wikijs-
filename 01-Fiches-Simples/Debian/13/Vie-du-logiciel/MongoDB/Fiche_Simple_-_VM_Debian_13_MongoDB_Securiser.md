# Fiche_Simple_-_VM_Debian_13_MongoDB_Securiser

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MongoDB Community (dépôt officiel)
- **Catégorie** : base de données / MongoDB / Sécuriser (authentification, TLS, pare-feu)
- **Tags** : `debian13`, `mongodb`, `securite`

---

## Problème précis à résoudre

Activer l'authentification et TLS sur MongoDB et filtrer le port 27017.

## 1. Hors-Production (Lab / Test / POC)

1. Créer l'administrateur (mot de passe saisi) :
   ```bash
   mongosh admin --eval 'db.createUser({ user: "ADMIN_DB", pwd: passwordPrompt(), roles: [{ role: "root", db: "admin" }] })'
   ```
   👉 Explication : remplacer `ADMIN_DB` (à remplacer) ; `passwordPrompt()` demande le mot de passe sans l'écrire dans l'historique.

2. Activer l'autorisation :
   ```bash
   sudo sed -i '/^#security:/c\security:\n  authorization: enabled' /etc/mongod.conf
   sudo systemctl restart mongod
   ```
   👉 Explication : contrôler le fichier : la clé `security` ne doit apparaître qu'une fois.

3. Lab : préparer un certificat TLS (PEM = certificat + clé) :
   ```bash
   sudo install -d -o mongodb -g mongodb -m 0750 /etc/mongodb/tls
   sudo openssl req -x509 -nodes -newkey rsa:3072 -days 90 -keyout /etc/mongodb/tls/server.key -out /etc/mongodb/tls/server.crt -subj '/CN=NOM_SERVEUR'
   sudo sh -c 'cat /etc/mongodb/tls/server.crt /etc/mongodb/tls/server.key > /etc/mongodb/tls/server.pem'
   sudo chown mongodb:mongodb /etc/mongodb/tls/* && sudo chmod 0600 /etc/mongodb/tls/*
   ```
   👉 Explication : remplacer `NOM_SERVEUR` (à remplacer) ; certificat d'AC interne en production.

4. Activer TLS et l'écoute ciblée :
   ```bash
   # dans /etc/mongod.conf :
   #   net:
   #     port: 27017
   #     bindIp: 127.0.0.1,IP_SERVEUR
   #     tls:
   #       mode: requireTLS
   #       certificateKeyFile: /etc/mongodb/tls/server.pem
   sudo systemctl restart mongod
   ```
   👉 Explication : remplacer `IP_SERVEUR` (à remplacer) ; éditer le fichier avec un éditeur puis redémarrer.

5. Filtrer le port 27017 :
   ```bash
   sudo nft list ruleset | head -20
   # si ufw est utilisé :
   sudo ufw allow from IP_CLIENT to any port 27017 proto tcp
   ```
   👉 Explication : seules les IP clientes autorisées atteignent MongoDB.

## 2. Production — Contrôles

Certificats supervisés, rôles applicatifs minimaux, revue périodique des utilisateurs.

## 3. Production — Sécurité

- Jamais de MongoDB exposé sans authentification.
- Clé privée en `0600`, propriétaire `mongodb`.
- Un utilisateur par application avec le rôle `readWrite` sur sa base.
- Mots de passe saisis, jamais commités.

## Validation et retour arrière

- **Validation** : une connexion sans identifiants échoue aux commandes, avec identifiants et TLS elle réussit.
- **Retour arrière** : remettre `authorization: disabled` seulement en lab isolé, ou restaurer `mongod.conf.orig`.

## Si le problème n'est pas résolu

- [MongoDB — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_MongoDB_Prerequis_Limites.md)
- [MongoDB — Installer](Fiche_Simple_-_VM_Debian_13_MongoDB_Installer.md)
- [MongoDB — Configurer](Fiche_Simple_-_VM_Debian_13_MongoDB_Configurer.md)
- [MongoDB — Valider (recette)](Fiche_Simple_-_VM_Debian_13_MongoDB_Valider.md)
- [MongoDB — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_MongoDB_Sauvegarder_Restaurer.md)
- [MongoDB — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_MongoDB_Mettre_A_Jour.md)
- [MongoDB — installation sous Debian](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/)
- [MongoDB — sécurité](https://www.mongodb.com/docs/manual/security/)
