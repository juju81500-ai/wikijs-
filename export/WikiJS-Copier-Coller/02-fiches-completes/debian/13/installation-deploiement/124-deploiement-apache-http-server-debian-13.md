# Déployer Apache HTTP Server sur Debian 13

- **OS / Version** : Debian 13 Trixie; paquet `apache2` des dépôts Debian configurés
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : installation, site statique pilote en hôte virtuel, validation, TLS avec certificat déjà géré par l'organisation
- **Catégorie** : serveur Web

## 1. Périmètre et prérequis

Fiche simple : [cadrer le pilote Apache](/01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-cadrer-pilote).

Cette procédure installe Apache sur un serveur Debian 13 et publie un site statique pilote. Elle ne déploie pas de runtime applicatif, de base de données, de reverse proxy, de certificat ACME, de WAF ni d'architecture haute disponibilité.

Prérequis : VM dédiée et approuvée, accès administrateur, nom DNS choisi, certificat TLS valide et sa clé privée provisionnés par le mécanisme de l'organisation, règles de pare-feu planifiées, sauvegarde de la VM et fenêtre de changement. Pour une production, définir le propriétaire applicatif, les critères de disponibilité, la journalisation, la supervision, les mises à jour et le retour arrière.

## 2. Installer le paquet Debian

Fiche simple : [installer le paquet Apache](/01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-installer-paquet).

Examiner les dépôts actifs et leur politique avant toute installation :

```bash
sudo apt update
apt-cache policy apache2
sudo apt install apache2
apache2 -v
systemctl status apache2 --no-pager
```

Installer depuis les dépôts Debian approuvés; ne pas ajouter un dépôt tiers ni figer une version sans processus de maintenance. Vérifier la version réellement livrée par le miroir utilisé.

## 3. Préparer un site statique pilote

Fiche simple : [configurer l'hôte virtuel pilote](/01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-hote-virtuel).

Créer un répertoire dédié, contrôlé par root et lisible par le serveur Web, puis un contenu non sensible :

```bash
sudo install -d -o root -g root -m 0755 /var/www/pilote
printf '%s\n' '<!doctype html><title>Apache pilote</title><h1>Site pilote</h1>' \
  | sudo tee /var/www/pilote/index.html >/dev/null
sudo chmod 0644 /var/www/pilote/index.html
```

Créer `/etc/apache2/sites-available/pilote.conf` et remplacer `www.example.net` par le FQDN validé :

```apache
<VirtualHost *:80>
    ServerName www.example.net
    DocumentRoot /var/www/pilote

    <Directory /var/www/pilote>
        Options -Indexes
        AllowOverride None
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/pilote-error.log
    CustomLog ${APACHE_LOG_DIR}/pilote-access.log combined
</VirtualHost>
```

Ne pas placer de secrets dans le document root. Garder les fichiers et sous-répertoires non accessibles en écriture au processus Apache, sauf besoin applicatif documenté et limité.

Activer le site pilote. Désactiver le site par défaut uniquement si le serveur lui est dédié et si aucun autre service ne l'utilise :

```bash
sudo a2ensite pilote.conf
sudo apache2ctl configtest
sudo apache2ctl -S
sudo systemctl reload apache2
```

Ne pas recharger si la validation échoue. Si le serveur héberge déjà des sites, examiner d'abord les hôtes virtuels existants et intégrer le nouveau site selon le processus de changement.

## 4. Configurer TLS

Fiche simple : [configurer TLS](/01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-configurer-tls).

S'assurer que le certificat et la clé sont fournis par un mécanisme approuvé, que les permissions de la clé privée sont restreintes et que le nom DNS correspond au certificat. Activer `mod_ssl`, puis ajouter un hôte virtuel dédié :

```bash
sudo a2enmod ssl
```

Créer `/etc/apache2/sites-available/pilote-ssl.conf` en remplaçant les chemins ci-dessous par ceux du certificat déjà provisionné :

```apache
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
```

Valider la syntaxe et la présence des modules avant activation/rechargement :

```bash
sudo apache2ctl configtest
sudo apache2ctl -M
sudo apache2ctl -S
```

Après vérification des chemins, du DNS et du certificat, activer le fichier HTTPS, tester à nouveau, puis recharger :

```bash
sudo a2ensite pilote-ssl.conf
sudo apache2ctl configtest
sudo systemctl reload apache2
```

Tester HTTPS depuis un client approuvé et confirmer la chaîne, le nom et la date d'expiration du certificat. Ne configurer une redirection HTTP vers HTTPS qu'après validation complète de l'hôte HTTPS et de ses dépendances.

## 5. Contrôles de sécurité et exploitation

Fiche simple : [sécuriser et exploiter Apache](/01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-exploiter-securiser).

- Limiter les règles entrantes aux ports et réseaux clients nécessaires via le pare-feu approuvé; vérifier qu'aucune règle large n'est activée par défaut.
- Garder les modules activés au minimum requis. Vérifier les directives de sécurité livrées par Debian et les exigences de l'application avant tout changement global.
- Ne pas utiliser `AllowOverride All` ou accorder des permissions d'écriture générales sans besoin démontré.
- Surveiller `systemctl status apache2`, les journaux du site et l'espace disque; appliquer les correctifs Debian après validation dans un pilote.
- Sauvegarder `/etc/apache2`, le contenu du site et les certificats séparément. La configuration ne contient pas les données métier ni nécessairement les clés privées.

Vérifier le service localement et depuis un client autorisé :

```bash
curl -fsSI -H 'Host: www.example.net' http://127.0.0.1/
curl -fsSI --resolve www.example.net:443:127.0.0.1 https://www.example.net/
sudo journalctl -u apache2 --since '15 minutes ago' --no-pager
```

Le deuxième test vérifie la confiance TLS locale du client; ne pas utiliser `-k` pour masquer un certificat invalide. Les commandes HTTP ne valident pas la sécurité fonctionnelle de l'application.

## 6. Retour arrière

Fiche simple : [préparer le retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-retour-arriere).

Avant le changement, sauvegarder les fichiers modifiés et la sortie de `apache2ctl -S`. Si le nouveau site cause une anomalie, désactiver son hôte virtuel, restaurer les fichiers sauvegardés, valider la configuration puis recharger :

```bash
sudo a2dissite pilote-ssl.conf
sudo a2dissite pilote.conf
sudo apache2ctl configtest
sudo systemctl reload apache2
```

Ne pas désactiver un site ou module partagé sans avoir vérifié ses dépendances. Si le service ne revient pas, arrêter la publication via le mécanisme réseau approuvé et restaurer l'état sauvegardé plutôt que d'improviser des règles de pare-feu.

## Sources

- [Apache HTTP Server 2.4 — hôtes virtuels](https://httpd.apache.org/docs/2.4/vhosts/)
- [Apache HTTP Server 2.4 — configuration TLS](https://httpd.apache.org/docs/2.4/ssl/ssl_howto.html)
- [Apache HTTP Server 2.4 — apachectl](https://httpd.apache.org/docs/2.4/programs/apachectl.html)
- [Debian — documentation de la version 13 (Trixie)](https://www.debian.org/releases/trixie/)
- [Debian — paquet apache2](https://packages.debian.org/trixie/apache2)

Le certificat, le FQDN, les règles réseau et les dépendances doivent être validés sur un système pilote avant toute publication en production.