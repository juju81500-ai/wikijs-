# Fiche_Simple_-_VM_Debian_13_Dovecot_Prerequis_Limites

- **Environnement** : VM Debian 13; Dovecot depuis les dépôts de la distribution
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Dovecot — Prérequis et limites

---

## Problème précis à résoudre

Vérifier qu'une VM Debian 13 peut héberger Dovecot (IMAP/LMTP) et identifier la limite majeure : Debian 13 fournit la branche 2.4, dont la syntaxe diffère de la 2.3.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'OS et le nom d'hôte :
   ```bash
   cat /etc/os-release | head -3
   hostnamectl --static
   ```
   👉 Explication : FQDN attendu (`MAIL.EXAMPLE.NET`, à remplacer) pour le certificat TLS.

2. Relever la version proposée :
   ```bash
   apt-cache policy dovecot-core
   ```
   👉 Explication : Debian 13 propose Dovecot 2.4.x (à vérifier sur la version publiée). Les exemples 2.3 trouvés sur Internet (`ssl_cert`, `mail_location`, `disable_plaintext_auth`) ne sont plus valables tels quels.

3. Contrôler les ports 143/993/110/995 :
   ```bash
   sudo ss -tlnp | grep -E ':(143|993|110|995)\b' || echo "ports libres"
   ```
   👉 Explication : aucun autre serveur IMAP/POP3 ne doit écouter.

4. Décider du périmètre :
   👉 Explication : IMAP chiffré (993) seulement ; POP3 non utilisé ; boîtes Maildir de comptes système (cas simple) ou utilisateurs virtuels (hors périmètre de cette fiche). Le MTA est Postfix (voir la fiche Postfix du pack).

5. Si migration depuis Debian 12 (Dovecot 2.3) : conserver la configuration d'origine pour la convertir.
   ```bash
   sudo cp -a /etc/dovecot /root/dovecot-2.3-orig
   ```
   👉 Explication : la configuration 2.3 n'est pas lue telle quelle par la 2.4 : suivre le guide officiel de migration.

## 2. Production — Contrôles

Documenter version, FQDN, type d'authentification, emplacement des boîtes, volumétrie, politique de quotas et propriétaire du service.

## 3. Production — Sécurité

- Ne publier que IMAPS (993) ; ne pas exposer 143/110 sans nécessité.
- Snapshot de VM avant installation.

## Validation et retour arrière

- **Validation** : version cible connue, ports libres, décision de périmètre documentée.
- **Retour arrière** : aucune modification n'a été faite : rien à annuler.

## Si le problème n'est pas résolu

- [Dovecot — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-installer)
- [Dovecot — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-configurer)
- [Dovecot 2.4 — documentation officielle](https://doc.dovecot.org/main/)
- [Dovecot — migration 2.3 vers 2.4](https://doc.dovecot.org/main/installation/upgrade/2.3-to-2.4.html)