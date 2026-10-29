# 📄 OpenLDAP

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : OpenLDAP 2.5.x (paquet `slapd` des dépôts Debian 12, à vérifier sur la version déployée)
- **Catégorie** : Systèmes, annuaires et services

## 🎯 Problème précis à résoudre
Installer un annuaire OpenLDAP (`slapd`) sur Debian 12, créer un domaine et un utilisateur de test, vérifier les liaisons (bind) et les requêtes LDAP, puis le durcir (anonymat désactivé, LDAPS, pare-feu restreint) avant de le rendre utilisable par un service de l'entreprise. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du serveur et des outils clients :
```bash
sudo apt update
sudo apt install -y slapd ldap-utils
dpkg -s slapd | grep -E '^(Version|Status)'
```
👉 Explication : Installe `slapd` (le serveur) et `ldap-utils` (`ldapsearch`, `ldapadd`, `ldapwhoami`). Pendant l'installation, Debian demande le mot de passe administrateur : le noter pour le lab.

2. Reconfiguration du domaine (suffixe `dc=lab,dc=local`) et de l'organisation :
```bash
sudo dpkg-reconfigure -plow slapd
```
Réponses à saisir : `Omettre la configuration du serveur DNS` = Non, nom de domaine = `lab.local`, nom de l'organisation = `Lab`, mot de passe administrateur, base de données = `MDB`, purge de la base à la suppression = Non.
👉 Explication : Crée le suffixe `dc=lab,dc=local` utilisé dans tous les DN suivants. Le DN administrateur devient `cn=admin,dc=lab,dc=local`.

3. Contrôle du service et de la racine de l'annuaire (requête anonyme, lab uniquement) :
```bash
systemctl status slapd --no-pager
ldapsearch -x -H ldap://127.0.0.1 -b "" -s base namingContexts
```
👉 Explication : La requête sur le rootDSE doit renvoyer `namingContexts: dc=lab,dc=local`. Une réponse vide ou une erreur `Can't contact LDAP server` indique que `slapd` n'écoute pas sur ce port.

4. Création de l'unité d'organisation et d'un utilisateur de test :
```bash
sudo nano /root/ou-people.ldif
```
Contenu :
```
dn: ou=people,dc=lab,dc=local
objectClass: organizationalUnit
ou: people
```
```bash
ldapadd -x -D "cn=admin,dc=lab,dc=local" -W -f /root/ou-people.ldif
sudo nano /root/user-jdupont.ldif
```
Contenu :
```
dn: uid=jdupont,ou=people,dc=lab,dc=local
objectClass: inetOrgPerson
cn: Jean Dupont
sn: Dupont
uid: jdupont
```
```bash
ldapadd -x -D "cn=admin,dc=lab,dc=local" -W -f /root/user-jdupont.ldif
```
👉 Explication : Le premier fichier crée l'OU `people`, le second l'utilisateur `jdupont`. `-W` demande le mot de passe admin. Les deux fichiers contiennent des données de lab et ne doivent pas servir en production.

5. Définition du mot de passe de l'utilisateur et test de liaison :
```bash
ldappasswd -x -D "cn=admin,dc=lab,dc=local" -W -S "uid=jdupont,ou=people,dc=lab,dc=local"
ldapwhoami -x -D "uid=jdupont,ou=people,dc=lab,dc=local" -W
```
👉 Explication : `ldappasswd -S` demande le nouveau mot de passe de façon interactive, sans le laisser dans l'historique. `ldapwhoami` doit répondre `dn:uid=jdupont,ou=people,dc=lab,dc=local` : la liaison fonctionne.

---

## ⚡ 2. Production — Façon Simplifiée
1. Ouverture du service LDAP et LDAPS uniquement pour le réseau de l'entreprise :
```bash
sudo apt install -y ufw
sudo ufw allow from 192.168.10.0/24 to any port 22 proto tcp
sudo ufw allow from 192.168.10.0/24 to any port 389 proto tcp
sudo ufw allow from 192.168.10.0/24 to any port 636 proto tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : SSH est autorisé avant l'activation du pare-feu. Le port 389 (LDAP) et 636 (LDAPS) ne sont accessibles qu'au sous-réseau `192.168.10.0/24`. Adapter le sous-réseau à l'entreprise.

2. Test depuis un client du sous-réseau :
```bash
ldapsearch -x -H ldap://192.168.10.20 -b "dc=lab,dc=local" -s sub "(uid=jdupont)" dn
```
👉 Explication : Recherche l'utilisateur `jdupont` depuis un autre poste. Remplacer `192.168.10.20` par l'adresse IP réelle du serveur. Une réponse vide indique un filtre ou une règle pare-feu à revoir.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Désactivation des liaisons anonymes (la configuration globale est dans `cn=config`) :
```bash
sudo nano /root/no-anon.ldif
```
Contenu :
```
dn: cn=config
changetype: modify
add: olcDisallows
olcDisallows: bind_anon
```
```bash
sudo ldapmodify -Y EXTERNAL -H ldapi:/// -f /root/no-anon.ldif
```
👉 Explication : `-Y EXTERNAL` utilise l'accès root local via le socket `ldapi:///`, sans mot de passe LDAP. Après cette modification, une requête sans identifiant est refusée. Tester à nouveau `ldapsearch` sans `-D` : l'accès doit être refusé.

2. Activation de LDAPS avec un certificat (exemple : certificat émis par l'autorité interne de l'entreprise) :
```bash
sudo mkdir -p /etc/ldap/certs
sudo cp /root/ldap-srv.crt /etc/ldap/certs/ldap-srv.crt
sudo cp /root/ldap-srv.key /etc/ldap/certs/ldap-srv.key
sudo chown root:openldap /etc/ldap/certs/ldap-srv.key
sudo chmod 640 /etc/ldap/certs/ldap-srv.key
```
👉 Explication : Les fichiers `ldap-srv.crt` et `ldap-srv.key` sont produits par l'autorité interne de l'entreprise (ou par un certificat de lab). Le groupe `openldap` doit pouvoir lire la clé privée, personne d'autre. Le nom du groupe est à vérifier sur la version déployée.

3. Déclaration des fichiers de certificat dans `cn=config` :
```bash
sudo nano /root/tls-ldap.ldif
```
Contenu :
```
dn: cn=config
changetype: modify
add: olcTLSCertificateFile
olcTLSCertificateFile: /etc/ldap/certs/ldap-srv.crt
-
add: olcTLSCertificateKeyFile
olcTLSCertificateKeyFile: /etc/ldap/certs/ldap-srv.key
```
```bash
sudo ldapmodify -Y EXTERNAL -H ldapi:/// -f /root/tls-ldap.ldif
sudo systemctl restart slapd
ldapsearch -x -H ldaps://lab-srv.lab.local -b "" -s base namingContexts
```
👉 Explication : Enregistre le certificat et la clé dans la configuration, redémarre `slapd` et teste LDAPS. Le nom `lab-srv.lab.local` doit figurer dans le certificat. Si la vérification échoue, la confiance dans l'autorité interne n'est pas installée sur le poste client.

4. Sauvegarde de l'annuaire et de la configuration :
```bash
sudo slapcat -n 0 -l /root/ldap-config-$(date +%F).ldif
sudo slapcat -n 1 -l /root/ldap-data-$(date +%F).ldif
sudo ls -l /root/ldap-*-*.ldif
```
👉 Explication : `-n 0` exporte `cn=config`, `-n 1` exporte les données du domaine. Ces exports contiennent des hachages de mots de passe : les stocker hors du serveur, dans un coffre-fort, et les protéger en lecture. Le numéro de base `-n 1` est à vérifier avec `sudo slapcat -n` sur la version déployée.

---