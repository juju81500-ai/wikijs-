# Fiche_Simple_-_VM_Debian_13_Nextcloud_Securiser

- **Environnement** : VM Debian 13; Nextcloud (archive officielle), Apache, PHP 8.4 et MariaDB
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Nextcloud — Sécuriser

---

## Problème précis à résoudre

Passer Nextcloud en HTTPS, durcir Apache et limiter les accès.

## 1. Hors-Production (Lab / Test / POC)

1. Obtenir un certificat (fiche Certbot du pack), par exemple avec le plugin Apache :
   ```bash
   sudo apt install -y certbot python3-certbot-apache
   sudo certbot --apache -d CLOUD.EXAMPLE.NET
   ```
   👉 Explication : Certbot ajoute le virtual host 443 et la redirection ; renouvellement automatique via timer systemd.

2. Activer HSTS et masquer les informations serveur :
   ```bash
   sudo a2enmod headers
   sudo tee /etc/apache2/conf-available/nextcloud-secu.conf >/dev/null <<'EOF'
   ServerTokens Prod
   ServerSignature Off
   Header always set Strict-Transport-Security "max-age=15552000; includeSubDomains"
   EOF
   sudo a2enconf nextcloud-secu
   sudo apache2ctl configtest && sudo systemctl reload apache2
   ```
   👉 Explication : HSTS impose HTTPS aux navigateurs ; ne l'activer qu'une fois HTTPS fonctionnel.

3. Filtrer le pare-feu :
   ```bash
   sudo ufw allow 80/tcp
   sudo ufw allow 443/tcp
   ```
   👉 Explication : n'exposer que HTTP/HTTPS ; MariaDB reste en écoute locale uniquement.

4. Activer l'authentification à deux facteurs :
   ```bash
   cd /var/www/nextcloud
   sudo -u www-data php occ app:enable twofactor_totp
   ```
   👉 Explication : puis imposer le 2FA aux administrateurs (Paramètres > Administration > Sécurité).

5. Contrôler les alertes de sécurité :
   ```bash
   sudo -u www-data php occ integrity:check-core
   ```
   👉 Explication : l'intégrité du code doit être confirmée ; consulter aussi la page Administration > Vue d'ensemble.

## 2. Production — Contrôles

Tester l'instance avec un scanner de configuration TLS reconnu sur votre propre domaine, vérifier le renouvellement du certificat et la protection contre le brute-force intégrée.

## 3. Production — Sécurité

- MariaDB écoute sur 127.0.0.1 uniquement.
- Fail2ban peut compléter la protection (journal `nextcloud.log`) : voir [Fail2ban](/01-fiches-simples/debian/13/vie-du-logiciel/fail2ban/fiche-simple-vm-debian-13-securite-fail2ban).
- Les sauvegardes et `config.php` ne doivent pas être lisibles par tous (0640 ou plus strict).
- Mots de passe administrateur uniques, stockés dans un gestionnaire.

## Validation et retour arrière

- **Validation** : accès HTTPS valide, redirection 80 vers 443, `integrity:check-core` sans erreur.
- **Retour arrière** : `sudo a2disconf nextcloud-secu` puis recharger Apache ; `sudo certbot delete --cert-name CLOUD.EXAMPLE.NET` si besoin ; retirer les règles ufw.

## Si le problème n'est pas résolu

- [Nextcloud — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-prerequis-limites)
- [Nextcloud — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-installer)
- [Certbot — TLS](/01-fiches-simples/debian/13/vie-du-logiciel/certbot/fiche-simple-vm-debian-13-securite-certbot-tls)
- [Fail2ban](/01-fiches-simples/debian/13/vie-du-logiciel/fail2ban/fiche-simple-vm-debian-13-securite-fail2ban)
- [Nextcloud — manuel d'administration](https://docs.nextcloud.com/server/latest/admin_manual/)
- [Nextcloud — prérequis système](https://docs.nextcloud.com/server/latest/admin_manual/installation/system_requirements.html)