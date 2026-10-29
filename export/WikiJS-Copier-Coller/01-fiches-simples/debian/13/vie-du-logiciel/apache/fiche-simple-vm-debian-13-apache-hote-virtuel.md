# Fiche_Simple_-_VM_Debian_13_Apache_Hote_Virtuel.md

- **Environnement** : VM Debian 13 Trixie, hôte virtuel statique de test
- **OS / Version** : Debian 13 Trixie; Apache HTTP Server 2.4.x du dépôt Debian
- **Catégorie** : serveur Web / hôte virtuel

---

## Problème précis à résoudre

Servir une page statique de test depuis un hôte virtuel dédié avec un répertoire non inscriptible par le serveur Web.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le répertoire et la page pilote :
   ```bash
   sudo install -d -o root -g root -m 0755 /var/www/pilote
   printf '%s\n' '<!doctype html><title>Apache pilote</title><h1>Site pilote</h1>' | sudo tee /var/www/pilote/index.html >/dev/null
   sudo chmod 0644 /var/www/pilote/index.html
   ```
   👉 Explication : contenu non sensible, propriété root, non modifiable par Apache.

2. Créer l'hôte virtuel (remplacer `www.example.net` par le FQDN validé) :
   ```bash
   sudo tee /etc/apache2/sites-available/pilote.conf >/dev/null <<'EOF'
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
   EOF
   ```
   👉 Explication : `Options -Indexes` interdit le listage; `AllowOverride None` ignore les `.htaccess`.

3. Activer, tester, recharger :
   ```bash
   sudo a2ensite pilote.conf
   sudo apache2ctl configtest
   sudo apache2ctl -S
   sudo systemctl reload apache2
   ```
   👉 Explication : ne pas recharger si `configtest` échoue; examiner les hôtes virtuels existants avant sur un serveur déjà utilisé.

## 2. Production — Contrôles

Pour un site métier, valider le contenu, le propriétaire, le FQDN, les bindings, les chemins, les règles d'accès, les destinations de journaux et la procédure de changement avec l'équipe applicative.

## 3. Production — Sécurité

- Ne pas mettre de secret, sauvegarde ou fichier de configuration dans le document root.
- Laisser Apache en lecture seule sur le contenu, sauf répertoire d'écriture applicative explicitement requis et isolé.
- Garder `AllowOverride None` et ne pas activer de listing de répertoire sans exception validée.
- Ne pas remplacer un site existant ou recharger une configuration non validée.

## Validation et retour arrière

- **Validation** : `configtest` retourne `Syntax OK`, l'hôte virtuel attendu apparaît, la page de test répond et les journaux sont créés.
- **Retour arrière** : désactiver uniquement le nouvel hôte virtuel, restaurer le fichier précédent, valider puis recharger.

## Si le problème n'est pas résolu

- [Apache HTTP Server — hôtes virtuels](https://httpd.apache.org/docs/2.4/vhosts/)
- [Guide complet Apache Debian 13](/02-fiches-completes/debian/13/installation-deploiement/124-deploiement-apache-http-server-debian-13#3-preparer-un-site-statique-pilote)