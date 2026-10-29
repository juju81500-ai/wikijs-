# Fiche_Simple_-_VM_Debian_13_Postfix_Configurer

- **Environnement** : VM Debian 13; Postfix depuis les dépôts de la distribution
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Postfix — Configurer

---

## Problème précis à résoudre

Configurer les paramètres essentiels de Postfix (identité, réseaux autorisés, Maildir) sans créer de relais ouvert.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration d'origine :
   ```bash
   sudo cp -a /etc/postfix /etc/postfix.orig-$(date +%F)
   ```
   👉 Explication : permet un retour arrière immédiat.

2. Définir l'identité et l'écoute :
   ```bash
   sudo postconf -e 'myhostname = MAIL.EXAMPLE.NET'
   sudo postconf -e 'mydomain = EXAMPLE.NET'
   sudo postconf -e 'myorigin = $mydomain'
   sudo postconf -e 'inet_interfaces = all'
   sudo postconf -e 'inet_protocols = ipv4'
   ```
   👉 Explication : `MAIL.EXAMPLE.NET` et `EXAMPLE.NET` sont à remplacer ; `inet_protocols = ipv4` à adapter si l'IPv6 est exploité.

3. Restreindre aux réseaux de confiance :
   ```bash
   sudo postconf -e 'mynetworks = 127.0.0.0/8 [::1]/128'
   sudo postconf -e 'mydestination = $myhostname, localhost.$mydomain, localhost, $mydomain'
   ```
   👉 Explication : seul le local peut relayer sans authentification ; ajouter un réseau (ex. `RESEAU_INTERNE/24`, à remplacer) uniquement si nécessaire.

4. Stocker les messages en Maildir :
   ```bash
   sudo postconf -e 'home_mailbox = Maildir/'
   ```
   👉 Explication : format compatible avec Dovecot (voir la fiche Dovecot du pack).

5. Contrôler et recharger :
   ```bash
   sudo postfix check
   sudo postconf -n
   sudo systemctl reload postfix
   ```
   👉 Explication : `postfix check` détecte les erreurs de droits/syntaxe ; `postconf -n` n'affiche que les valeurs modifiées.

## 2. Production — Contrôles

Relire `postconf -n` : `mynetworks` ne doit jamais contenir `0.0.0.0/0`, `smtpd_relay_restrictions` doit rester celui de Debian (permit_mynetworks, permit_sasl_authenticated, defer_unauth_destination).

## 3. Production — Sécurité

- Ne jamais élargir `mynetworks` à un réseau non maîtrisé.
- Conserver `defer_unauth_destination` : il évite le relais ouvert.
- Journaliser tout changement de `main.cf`.

## Validation et retour arrière

- **Validation** : `postfix check` sans message et `postconf -n` conforme au design.
- **Retour arrière** : `sudo rsync -a --delete /etc/postfix.orig-DATE/ /etc/postfix/` (remplacer `DATE`) puis `sudo systemctl reload postfix`.

## Si le problème n'est pas résolu

- [Postfix — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-prerequis-limites)
- [Postfix — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-installer)
- [Postfix — documentation officielle](https://www.postfix.org/documentation.html)
- [Debian — Postfix](https://wiki.debian.org/Postfix)