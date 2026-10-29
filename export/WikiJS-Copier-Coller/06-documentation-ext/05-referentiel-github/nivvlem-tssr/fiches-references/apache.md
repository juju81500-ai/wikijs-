# Apache (serveur HTTP)

## 📌 Présentation

Apache HTTP Server (ou Apache2) est l’un des serveurs web les plus utilisés au monde. Il permet d’héberger des sites web statiques ou dynamiques et d’en gérer la configuration via des fichiers `.conf`. Il est modulaire, extensible et compatible avec PHP, SSL, le reverse proxy, etc.

---

## 🧰 Commandes essentielles (Debian/Ubuntu)

| Commande                   | Description                        | Exemple                         |
| -------------------------- | ---------------------------------- | ------------------------------- |
| `apt install apache2`      | Installe Apache                    | `sudo apt install apache2`      |
| `systemctl start apache2`  | Démarre le service                 | `sudo systemctl start apache2`  |
| `systemctl enable apache2` | Active le démarrage auto           | `sudo systemctl enable apache2` |
| `systemctl status apache2` | Vérifie le statut                  | `sudo systemctl status apache2` |
| `apache2ctl configtest`    | Vérifie la validité de la config   | `sudo apache2ctl configtest`    |
| `a2enmod` / `a2dismod`     | Active / désactive un module       | `sudo a2enmod rewrite`          |
| `a2ensite` / `a2dissite`   | Active / désactive un site virtuel | `sudo a2ensite monsite.conf`    |
| `service apache2 reload`   | Recharge la configuration          | `sudo systemctl reload apache2` |

---

## 📁 Emplacements courants

- `/etc/apache2/` : dossier principal
- `/etc/apache2/sites-available/` : fichiers de configuration des hôtes virtuels (non activés)
- `/etc/apache2/sites-enabled/` : liens symboliques vers les sites activés
- `/var/www/html/` : répertoire web par défaut

---

## ⚙️ Fichiers de configuration (.conf)

Un fichier `.conf` dans `sites-available` contient typiquement :

```apache
<VirtualHost *:80>
    ServerName monsite.local
    DocumentRoot /var/www/monsite

    <Directory /var/www/monsite>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/monsite_error.log
    CustomLog ${APACHE_LOG_DIR}/monsite_access.log combined
</VirtualHost>
```

---

## 🔎 Cas d’usage courant

- Mise en place d’un site local (ex: `monsite.local`)
- Hébergement de plusieurs sites via VirtualHost
- Test de modules comme `mod_rewrite` ou `mod_ssl`
- Redirections HTTP/HTTPS
- Utilisation de `.htaccess` pour contrôler l’accès ou les réécritures d’URL

---

## ⚠️ Erreurs fréquentes

- Ne pas activer le bon site avec `a2ensite`
- Fichier `.conf` mal nommé (doit se terminer par `.conf`)
- Oublier `AllowOverride All` pour permettre l’utilisation des `.htaccess`
- Permissions insuffisantes sur `/var/www`
- Ne pas redémarrer ou recharger Apache après une modification

---

## ✅ Bonnes pratiques

- Toujours valider la config avec `apache2ctl configtest`
- Utiliser des noms explicites pour les VirtualHosts
- Centraliser les logs personnalisés pour chaque site
- Restreindre les accès aux dossiers sensibles avec des directives `<Directory>` adaptées
- Ne pas mettre le `DocumentRoot` à la racine `/`

---

## 📚 Ressources complémentaires

- [Documentation officielle Apache HTTP Server](https://httpd.apache.org/docs/)
- [Ubuntu - Apache2 Guide](https://ubuntu.com/server/docs/web-servers-apache)
- `man apache2`, `man a2enmod`, etc.