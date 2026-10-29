# Fiche_Simple_-_VM_Debian_13_Dovecot_Securiser

- **Environnement** : VM Debian 13; Dovecot depuis les dépôts de la distribution
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Dovecot — Sécuriser
- **Tags** : `debian13`, `dovecot`, `imap`, `messagerie`, `securiser`

---

## Problème précis à résoudre

Imposer TLS, refuser l'authentification en clair et filtrer l'accès à Dovecot.

## 1. Hors-Production (Lab / Test / POC)

1. Obtenir un certificat pour le FQDN (fiche Certbot du pack) puis déclarer TLS (syntaxe 2.4, à vérifier sur la version publiée) :
   ```bash
   sudo tee /etc/dovecot/conf.d/92-tls.conf >/dev/null <<'EOF'
   ssl = required
   ssl_server_cert_file = /etc/letsencrypt/live/MAIL.EXAMPLE.NET/fullchain.pem
   ssl_server_key_file = /etc/letsencrypt/live/MAIL.EXAMPLE.NET/privkey.pem
   ssl_min_protocol = TLSv1.2
   EOF
   ```
   👉 Explication : en 2.3 ces réglages s'appelaient `ssl_cert`/`ssl_key` avec le préfixe `<` ; chemin à adapter à la gestion de certificats retenue.

2. Refuser les mots de passe en clair hors TLS :
   ```bash
   sudo tee /etc/dovecot/conf.d/93-auth.conf >/dev/null <<'EOF'
   auth_allow_cleartext = no
   EOF
   ```
   👉 Explication : équivalent 2.4 de `disable_plaintext_auth = yes`.

3. Contrôler et recharger :
   ```bash
   sudo doveconf -n | grep -E 'ssl|cleartext'
   sudo systemctl reload dovecot
   ```
   👉 Explication : vérifier que les valeurs effectives sont celles attendues.

4. Filtrer le pare-feu :
   ```bash
   sudo ufw allow 993/tcp
   sudo ufw status
   ```
   👉 Explication : n'ouvrir que IMAPS ; restreindre aux réseaux utilisateurs si possible. Ne pas ouvrir 143.

5. Protéger contre le brute-force : activer la jail `dovecot` de Fail2ban.
   ```bash
   sudo fail2ban-client status
   ```
   👉 Explication : voir la fiche Fail2ban du pack ; ajuster le `logpath`/backend à journald.

## 2. Production — Contrôles

Vérifier le renouvellement du certificat (rechargement de Dovecot après renouvellement), la politique de mots de passe PAM et les journaux d'échecs de connexion.

## 3. Production — Sécurité

- Clé privée en 0600 root, jamais copiée.
- Aucun mot de passe en clair dans les fichiers de configuration ou l'historique.
- Exposer uniquement 993 ; POP3 désactivé sauf besoin.

## Validation et retour arrière

- **Validation** : `openssl s_client -connect MAIL.EXAMPLE.NET:993 -brief </dev/null` affiche un certificat valide ; une connexion en clair sur 143 est refusée ou non exposée.
- **Retour arrière** : supprimer `92-tls.conf` et `93-auth.conf`, recharger Dovecot et retirer la règle ufw (`sudo ufw delete allow 993/tcp`).

## Si le problème n'est pas résolu

- [Dovecot — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_Dovecot_Prerequis_Limites.md)
- [Dovecot — Installer](Fiche_Simple_-_VM_Debian_13_Dovecot_Installer.md)
- [Certbot — TLS](../Certbot/Fiche_Simple_-_VM_Debian_13_Securite_Certbot_TLS.md)
- [Fail2ban](../Fail2ban/Fiche_Simple_-_VM_Debian_13_Securite_Fail2ban.md)
- [Dovecot 2.4 — documentation officielle](https://doc.dovecot.org/main/)
- [Dovecot — migration 2.3 vers 2.4](https://doc.dovecot.org/main/installation/upgrade/2.3-to-2.4.html)
