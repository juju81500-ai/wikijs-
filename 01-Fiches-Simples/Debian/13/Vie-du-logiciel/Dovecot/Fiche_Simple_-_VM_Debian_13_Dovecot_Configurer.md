# Fiche_Simple_-_VM_Debian_13_Dovecot_Configurer

- **Environnement** : VM Debian 13; Dovecot depuis les dépôts de la distribution
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Dovecot — Configurer
- **Tags** : `debian13`, `dovecot`, `imap`, `messagerie`, `configurer`

---

## Problème précis à résoudre

Configurer les boîtes Maildir et la remise LMTP de Dovecot 2.4 via un fichier local séparé.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration :
   ```bash
   sudo cp -a /etc/dovecot /etc/dovecot.orig-$(date +%F)
   ```
   👉 Explication : retour arrière rapide.

2. Créer un fichier de réglages locaux (les noms ci-dessous suivent la syntaxe 2.4 ; vérifier avec la doc de la version installée) :
   ```bash
   sudo tee /etc/dovecot/conf.d/90-local.conf >/dev/null <<'EOF'
   protocols = imap lmtp
   mail_driver = maildir
   mail_path = ~/Maildir
   EOF
   ```
   👉 Explication : `mail_driver` et `mail_path` remplacent `mail_location` de la 2.3. Les fichiers de `conf.d/` sont inclus par la configuration Debian.

3. Exposer le canal d'authentification à Postfix (SASL) et la remise LMTP :
   ```bash
   sudo tee /etc/dovecot/conf.d/91-postfix.conf >/dev/null <<'EOF'
   service auth {
     unix_listener /var/spool/postfix/private/auth {
       mode = 0660
       user = postfix
       group = postfix
     }
   }
   service lmtp {
     unix_listener /var/spool/postfix/private/dovecot-lmtp {
       mode = 0600
       user = postfix
       group = postfix
     }
   }
   EOF
   ```
   👉 Explication : Postfix communique par sockets dans son chroot : `smtpd_sasl_path = private/auth` et `mailbox_transport = lmtp:unix:private/dovecot-lmtp` (voir la fiche Postfix Configurer du pack).

4. Créer un compte de test sans mot de passe écrit dans la commande :
   ```bash
   sudo adduser --gecos '' UTILISATEUR_TEST
   ```
   👉 Explication : `UTILISATEUR_TEST` est à remplacer ; `adduser` demande le mot de passe en saisie interactive.

5. Contrôler et recharger :
   ```bash
   sudo doveconf -n >/dev/null && echo syntaxe-ok
   sudo systemctl reload dovecot
   ```
   👉 Explication : `doveconf` signale toute erreur de syntaxe/paramètre inconnu (typique en cas de réglage 2.3 sur 2.4).

## 2. Production — Contrôles

Relire `doveconf -n` : `protocols`, `mail_path` et les listeners doivent correspondre au design ; droits des sockets limités à l'utilisateur postfix.

## 3. Production — Sécurité

- Ne pas modifier les fichiers fournis par le paquet : utiliser des fichiers locaux dédiés.
- Sockets en 0600/0660, jamais en 0666.

## Validation et retour arrière

- **Validation** : `doveconf -n` sans erreur et service rechargé.
- **Retour arrière** : `sudo rm /etc/dovecot/conf.d/90-local.conf /etc/dovecot/conf.d/91-postfix.conf` puis `sudo systemctl reload dovecot`.

## Si le problème n'est pas résolu

- [Dovecot — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_Dovecot_Prerequis_Limites.md)
- [Dovecot — Installer](Fiche_Simple_-_VM_Debian_13_Dovecot_Installer.md)
- [Postfix — Configurer](../Postfix/Fiche_Simple_-_VM_Debian_13_Postfix_Configurer.md)
- [Dovecot 2.4 — documentation officielle](https://doc.dovecot.org/main/)
- [Dovecot — migration 2.3 vers 2.4](https://doc.dovecot.org/main/installation/upgrade/2.3-to-2.4.html)
