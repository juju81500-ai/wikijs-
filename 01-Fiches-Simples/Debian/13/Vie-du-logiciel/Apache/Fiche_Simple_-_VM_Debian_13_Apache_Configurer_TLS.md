# Fiche_Simple_-_VM_Debian_13_Apache_Configurer_TLS.md

- **Environnement** : VM Debian 13 Trixie, certificat existant fourni par l'organisation
- **OS / Version** : Debian 13 Trixie; Apache HTTP Server 2.4.x
- **Catégorie** : serveur Web / TLS
- **Tags** : `debian13`, `apache`, `tls`, `certificat`, `https`

---

## Problème précis à résoudre

Servir le site pilote en HTTPS avec un certificat correspondant au FQDN et sans exposer sa clé privée.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler certificat, clé et permissions :
   ```bash
   sudo ls -l /etc/ssl/certs/www.example.net.crt /etc/ssl/private/www.example.net.key
   ```
   👉 Explication : la clé privée doit être restreinte (0600/0640 root:ssl-cert) et le nom DNS correspondre au certificat.

2. Activer le module TLS :
   ```bash
   sudo a2enmod ssl
   ```
   👉 Explication : charge `mod_ssl`.

3. Créer l'hôte virtuel HTTPS (adapter nom et chemins) :
   ```bash
   sudo tee /etc/apache2/sites-available/pilote-ssl.conf >/dev/null <<'EOF'
   <VirtualHost *:443>
       ServerName www.example.net
       DocumentRoot /var/www/pilote
       <Directory /var/www/pilote>
           Options -Indexes
           AllowOverride None
           Require all granted
       </Directory>
       SSLEngine on
       SSLCertificateFile /etc/ssl/certs/www.example.net.crt
       SSLCertificateKeyFile /etc/ssl/private/www.example.net.key
       ErrorLog ${APACHE_LOG_DIR}/pilote-ssl-error.log
       CustomLog ${APACHE_LOG_DIR}/pilote-ssl-access.log combined
   </VirtualHost>
   EOF
   sudo apache2ctl configtest
   sudo apache2ctl -M | grep ssl
   ```
   👉 Explication : valider la syntaxe et la présence du module avant activation.

4. Activer et recharger :
   ```bash
   sudo a2ensite pilote-ssl.conf
   sudo apache2ctl configtest
   sudo systemctl reload apache2
   ```
   👉 Explication : tester depuis un client approuvé (chaîne, nom, expiration); ne configurer de redirection HTTP vers HTTPS qu'après validation.

## 2. Production — Contrôles

Consigner le propriétaire du certificat, le processus de renouvellement, les notifications d'expiration, le FQDN et les clients autorisés. Tester le renouvellement et la configuration dans un environnement pilote avant toute modification de production.

## 3. Production — Sécurité

- Ne pas générer ou partager de clé privée dans le cadre de cette fiche.
- N'accepter que des certificats provisionnés par un mécanisme approuvé.
- Ne pas ouvrir TCP/443 avant validation du certificat, du nom et des règles réseau.
- Ne rediriger HTTP vers HTTPS qu'après validation de toutes les dépendances du site TLS.

## Validation et retour arrière

- **Validation** : TLS présente le certificat attendu, les clients approuvés valident la chaîne et les journaux n'affichent pas d'erreur de clé/module.
- **Retour arrière** : désactiver le nouvel hôte HTTPS et restaurer la configuration précédente après validation syntaxique; ne pas supprimer un certificat partagé.

## Si le problème n'est pas résolu

- [Apache HTTP Server — guide TLS](https://httpd.apache.org/docs/2.4/ssl/ssl_howto.html)
- [Apache HTTP Server — module mod_ssl](https://httpd.apache.org/docs/2.4/mod/mod_ssl.html)
- [Guide complet Apache Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/124_Deploiement_Apache_HTTP_Server_Debian_13.md#4-configurer-tls)
