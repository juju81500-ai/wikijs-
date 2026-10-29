# Fiche_Simple_-_VM_Debian_13_Postfix_Securiser

- **Environnement** : VM Debian 13; Postfix depuis les dépôts de la distribution
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Postfix — Sécuriser

---

## Problème précis à résoudre

Activer TLS, limiter l'exposition (SMTP/Submission) et réduire les abus sur Postfix.

## 1. Hors-Production (Lab / Test / POC)

1. Obtenir un certificat valide pour le FQDN (voir la fiche Certbot du pack) puis renseigner Postfix :
   ```bash
   sudo postconf -e 'smtpd_tls_cert_file = /etc/letsencrypt/live/MAIL.EXAMPLE.NET/fullchain.pem'
   sudo postconf -e 'smtpd_tls_key_file = /etc/letsencrypt/live/MAIL.EXAMPLE.NET/privkey.pem'
   sudo postconf -e 'smtpd_tls_security_level = may'
   sudo postconf -e 'smtp_tls_security_level = may'
   sudo postconf -e 'smtpd_tls_protocols = >=TLSv1.2'
   sudo postconf -e 'smtp_tls_protocols = >=TLSv1.2'
   ```
   👉 Explication : `may` = TLS opportuniste en SMTP serveur-à-serveur (le chiffrement obligatoire casserait la réception) ; le chemin est à adapter à la gestion de certificats retenue.

2. Désactiver la commande VRFY et exiger un HELO valide :
   ```bash
   sudo postconf -e 'disable_vrfy_command = yes'
   sudo postconf -e 'smtpd_helo_required = yes'
   ```
   👉 Explication : limite l'énumération d'adresses et les clients mal formés.

3. Ouvrir le service Submission (587) avec TLS obligatoire et authentification (nécessite SASL, fiche Dovecot) :
   ```bash
   sudo postconf -M 'submission/inet = submission inet n - y - - smtpd'
   sudo postconf -P 'submission/inet/syslog_name=postfix/submission'
   sudo postconf -P 'submission/inet/smtpd_tls_security_level=encrypt'
   sudo postconf -P 'submission/inet/smtpd_sasl_auth_enable=yes'
   sudo postconf -P 'submission/inet/smtpd_sasl_type=dovecot'
   sudo postconf -P 'submission/inet/smtpd_sasl_path=private/auth'
   sudo postconf -P 'submission/inet/smtpd_relay_restrictions=permit_sasl_authenticated,reject'
   ```
   👉 Explication : les utilisateurs envoient via le 587 authentifié et chiffré ; le port 25 reste réservé à la réception.

4. Filtrer le pare-feu (ex. ufw) :
   ```bash
   sudo ufw allow 25/tcp
   sudo ufw allow 587/tcp
   sudo ufw allow OUTIL_ADMIN_SSH_PORT/tcp
   ```
   👉 Explication : `OUTIL_ADMIN_SSH_PORT` est à remplacer par le port SSH réel, à autoriser avant `ufw enable`. Restreindre 587 aux sources attendues si possible.

5. Recharger après contrôle :
   ```bash
   sudo postfix check && sudo systemctl reload postfix
   ```
   👉 Explication : ne recharger que si le contrôle réussit.

## 2. Production — Contrôles

Vérifier la validité du certificat et son renouvellement, la présence de SPF/DKIM/DMARC (hors périmètre de cette fiche), et que le port 587 n'accepte que l'authentification chiffrée.

## 3. Production — Sécurité

- Protéger la clé privée (droits 0600 root) et ne jamais la copier hors du serveur.
- Coupler avec Fail2ban (jail `postfix`) : [Fail2ban](/01-fiches-simples/debian/13/vie-du-logiciel/fail2ban/fiche-simple-vm-debian-13-securite-fail2ban).
- Aucun mot de passe SMTP dans les fichiers de configuration ou l'historique shell.
- Ne pas exiger TLS sur le port 25 public sans accord avec les partenaires.

## Validation et retour arrière

- **Validation** : `openssl s_client -starttls smtp -connect MAIL.EXAMPLE.NET:587` montre un certificat valide et `postfix check` est propre.
- **Retour arrière** : restaurer `/etc/postfix` depuis la copie datée, recharger Postfix et retirer les règles ufw ajoutées (`sudo ufw delete allow 587/tcp`).

## Si le problème n'est pas résolu

- [Postfix — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-prerequis-limites)
- [Postfix — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-installer)
- [Certbot — TLS](/01-fiches-simples/debian/13/vie-du-logiciel/certbot/fiche-simple-vm-debian-13-securite-certbot-tls)
- [Fail2ban](/01-fiches-simples/debian/13/vie-du-logiciel/fail2ban/fiche-simple-vm-debian-13-securite-fail2ban)
- [Postfix — documentation officielle](https://www.postfix.org/documentation.html)
- [Debian — Postfix](https://wiki.debian.org/Postfix)