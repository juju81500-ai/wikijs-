# 📄 Dovecot

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Dovecot 2.3.x (paquet des dépôts Debian 12, à vérifier sur la version déployée)
- **Catégorie** : Messagerie et collaboratif

## 🎯 Objectif
Installer le serveur IMAP Dovecot sur Debian 12, vérifier sur ce même serveur qu'une authentification de test réussit et qu'un client IMAP peut se connecter, puis le durcir (authentification interdite en clair, TLS obligatoire) avant de l'exposer aux postes de l'entreprise. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de Dovecot avec les protocoles IMAP et POP3 :
```bash
sudo apt update
sudo apt install -y dovecot-core dovecot-imapd dovecot-pop3d
```
👉 Explication : Installe le serveur Dovecot et les modules IMAP et POP3. Les paquets proviennent des dépôts Debian 12.

2. Vérification de la version et de la configuration :
```bash
dovecot --version
sudo doveconf -n
```
👉 Explication : `dovecot --version` affiche la version installée. `doveconf -n` relit la configuration et n'affiche que les paramètres modifiés par rapport aux valeurs par défaut. Une erreur de syntaxe s'affiche ici.

3. Démarrage du service et contrôle de son état :
```bash
sudo systemctl enable dovecot
sudo systemctl start dovecot
systemctl status dovecot --no-pager
```
👉 Explication : Active le démarrage automatique, lance le service puis affiche son état. La ligne `Active: active (running)` est attendue.

4. Création d'un utilisateur de test (compte système, mot de passe de lab) :
```bash
sudo useradd -m utilisateur_test
sudo passwd utilisateur_test
```
👉 Explication : Dovecot authentifie par défaut les comptes système Linux (PAM). `<mot_de_passe_test>` est saisi au prompt, il doit être un mot de passe de lab jamais réutilisé. Le format de boîte `Maildir` est à vérifier selon la configuration de `mail_location`.

5. Test d'authentification sur le serveur lui-même :
```bash
sudo doveadm auth test utilisateur_test
```
👉 Explication : Demande le mot de passe de `utilisateur_test` et indique si l'authentification réussit (`auth succeeded`) ou échoue (`auth failed`).

---

## ⚡ 2. Production — Façon Simplifiée
1. Définition du format et de l'emplacement des boîtes aux lettres :
```bash
sudo nano /etc/dovecot/conf.d/10-mail.conf
```
Régler la ligne suivante :
```
mail_location = maildir:~/Maildir
```
👉 Explication : Indique à Dovecot où stocker les boîtes au format `Maildir`, en cohérence avec la livraison Postfix. Le format et le chemin sont à vérifier sur la version déployée.

2. Déclaration de l'agent de livraison côté Postfix :
```bash
sudo postconf -e "mailbox_command ="
sudo postconf -e "home_mailbox = Maildir/"
sudo postconf -e "smtpd_sasl_type = dovecot"
sudo postconf -e "smtpd_sasl_path = private/auth"
sudo systemctl reload postfix
```
👉 Explication : Postfix livre dans les boîtes `Maildir` et délègue l'authentification SASL des clients SMTP à Dovecot via le socket `private/auth`. Ces paramètres sont à vérifier sur la version déployée.

3. Contrôle de la syntaxe puis redémarrage :
```bash
sudo doveconf -n > /dev/null && echo "syntaxe OK"
sudo systemctl restart dovecot
systemctl status dovecot --no-pager
```
👉 Explication : `doveconf -n` vérifie la configuration ; si elle est valide, la commande affiche `syntaxe OK`. Le service est ensuite redémarré et son état contrôlé.

4. Ouverture du pare-feu pour IMAP et administration :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow 143/tcp
sudo ufw allow 993/tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Ouvre SSH seulement pour `<adresse_ip_admin>` avant d'activer le pare-feu. Le port 993 (IMAPS) est le port à exposer ; le port 143 n'est à ouvrir que si le STARTTLS est utilisé.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Interdiction de l'authentification en clair :
```bash
sudo nano /etc/dovecot/conf.d/10-auth.conf
```
Régler les lignes suivantes :
```
disable_plaintext_auth = yes
auth_mechanisms = plain login
```
👉 Explication : `disable_plaintext_auth = yes` refuse l'envoi de mots de passe sans TLS. Ce réglage impose le chiffrement avant tout échange d'identifiants.

2. Imposition du TLS sur les connexions IMAP :
```bash
sudo nano /etc/dovecot/conf.d/10-ssl.conf
```
Régler les lignes suivantes, en remplaçant les valeurs entre chevrons :
```
ssl = required
ssl_cert = </etc/ssl/certs/<certificat_imap>.crt
ssl_key = </etc/ssl/private/<certificat_imap>.key
```
👉 Explication : `ssl = required` refuse toute connexion non chiffrée. `<certificat_imap>` est le nom du certificat émis pour le serveur IMAP, à vérifier sur la version déployée.

3. Contrôle de la configuration et rechargement :
```bash
sudo doveconf -n > /dev/null && echo "syntaxe OK"
sudo systemctl reload dovecot
sudo doveconf -n | grep -E "ssl|disable_plaintext_auth"
```
👉 Explication : Vérifie la syntaxe, recharge le service puis confirme que les réglages TLS sont actifs.

4. Contrôle du chiffrement côté client :
```bash
openssl s_client -connect <adresse_ip_serveur>:993 -quiet
```
👉 Explication : Ouvre une session TLS vers le port IMAPS. Une bannière `* OK` de Dovecot doit apparaître. Taper `a1 LOGOUT` pour fermer la session.

5. Contrôle des journaux d'authentification :
```bash
sudo grep -E "auth failed|Disconnected|ssl" /var/log/mail.log | tail -n 50
```
👉 Explication : Affiche les derniers échecs d'authentification et erreurs TLS. Une série d'échecs pour un même compte est à remonter au responsable sécurité.

6. Sauvegarde de la configuration avant toute évolution :
```bash
sudo tar czf /root/dovecot-conf-$(date +%F).tgz /etc/dovecot
sudo ls -l /root/dovecot-conf-*.tgz
```
👉 Explication : Crée une archive datée de toute la configuration Dovecot, à stocker hors du serveur et à protéger en lecture.

---