# Fiche_Simple_-_VM_Debian_13_LEMP_Configurer_TLS_Filtrage.md

- **Environnement** : serveur Web Debian 13 avec DNS validé et gestionnaire de pare-feu identifié
- **OS / Version** : Debian 13 Trixie; Nginx, PHP-FPM, MariaDB
- **Catégorie** : pile Web LEMP / TLS et réseau

---

## Problème précis à résoudre

Publier l'application en HTTPS avec un filtrage cohérent sans perdre l'accès d'administration ni exposer MariaDB.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le DNS et l'accès HTTP avant de publier :
   ```bash
   getent hosts app.example.net
   curl -fsSI http://app.example.net/
   ```
   👉 Explication : le certificat ne s'obtient qu'avec un DNS correct.

2. Identifier le gestionnaire de pare-feu actif avant toute règle :
   ```bash
   systemctl is-active nftables ufw firewalld
   sudo nft list ruleset | head -30
   ```
   👉 Explication : ne pas ajouter de règle sans connaître le gestionnaire et sans accès de secours.

3. Autoriser 80/443 et limiter SSH au réseau d'administration (exemple nftables, à adapter à l'existant) :
   ```bash
   sudo nft add rule inet filter input tcp dport { 80, 443 } accept
   sudo nft add rule inet filter input ip saddr 192.0.2.0/24 tcp dport 22 accept
   ```
   👉 Explication : remplacer `192.0.2.0/24` par le réseau d'administration; table et chaîne `inet filter input` supposées existantes. Rendre persistant via `/etc/nftables.conf`.

4. Déployer le certificat avec l'outil ACME approuvé (exemple certbot) et vérifier le renouvellement :
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d app.example.net
   sudo certbot renew --dry-run
   ```
   👉 Explication : `--dry-run` prouve que le renouvellement automatique fonctionnera.

## 2. Production — Contrôles

Valider certificat, chaîne, nom DNS, renouvellement, règles persistantes, accès de secours, exposition publique et journalisation.

## 3. Production — Sécurité

- Ne pas ouvrir MariaDB à Internet; limiter le port 3306 au local sauf architecture expressément approuvée.
- Ne pas changer le pare-feu sans console ou accès de secours vérifié.
- Ne pas désactiver les vérifications TLS ou accepter un certificat expiré.
- Ne pas publier le site avant résolution DNS et contrôle HTTPS.

## Validation et retour arrière

- **Validation** : connexion HTTPS correcte, certificat valide, renouvellement testable et ports limités au besoin.
- **Retour arrière** : retirer uniquement les règles ajoutées selon le gestionnaire actif et restaurer la configuration précédente après validation.

## Si le problème n'est pas résolu

- [Nginx — configuration HTTPS](https://nginx.org/en/docs/http/configuring_https_servers.html)
- [Let's Encrypt — documentation](https://letsencrypt.org/docs/)
- [Guide complet LEMP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb#5-tls-et-filtrage-reseau)