# 📄 Apache

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Apache 2.4.x (paquet des dépôts Debian 12, à vérifier sur la version déployée)
- **Catégorie** : Services Web et bases de données
- **Tags** : `[debian-12]`, `[apache]`, `[serveur-web]`, `[https]`, `[hardening]`

## 🎯 Objectif
Installer le serveur web Apache 2.4 sur Debian 12, vérifier sur ce même serveur qu'une page de test répond, puis le durcir (HTTPS obligatoire, masquage de la version, modules inutiles désactivés) avant de le publier. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation d'Apache :
```bash
sudo apt update
sudo apt install -y apache2
```
👉 Explication : Installe le serveur Apache et ses fichiers de configuration dans `/etc/apache2/`. Les paquets proviennent des dépôts Debian 12.

2. Vérification de la version et de la syntaxe :
```bash
apache2 -v
sudo apache2ctl configtest
```
👉 Explication : `apache2 -v` affiche la version installée. `apache2ctl configtest` relit toute la configuration et affiche `Syntax OK` si elle est valide.

3. Démarrage du service et contrôle de son état :
```bash
sudo systemctl enable apache2
sudo systemctl start apache2
systemctl status apache2 --no-pager
```
👉 Explication : Active le démarrage automatique, lance le service puis affiche son état. La ligne `Active: active (running)` est attendue.

4. Création d'une page de test et contrôle de la réponse :
```bash
echo "<h1>Test Apache lab</h1>" | sudo tee /var/www/html/index.html
curl -I http://127.0.0.1/
```
👉 Explication : Remplace la page d'accueil par défaut par une page de test. `curl -I` ne récupère que les en-têtes : la ligne `HTTP/1.1 200 OK` est attendue.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création d'un hôte virtuel dédié :
```bash
sudo nano /etc/apache2/sites-available/<nom_site>.conf
```
Ajouter ce bloc, en remplaçant les valeurs entre chevrons :
```
<VirtualHost *:80>
    ServerName <nom_site_fqdn>
    DocumentRoot /var/www/<nom_site>
    ErrorLog ${APACHE_LOG_DIR}/<nom_site>-error.log
    CustomLog ${APACHE_LOG_DIR}/<nom_site>-access.log combined
</VirtualHost>
```
👉 Explication : Définit un site servi pour le nom `<nom_site_fqdn>`, avec ses propres journaux. `<nom_site>` est un identifiant court, sans espaces.

2. Activation du site et désactivation du site par défaut :
```bash
sudo mkdir -p /var/www/<nom_site>
sudo a2ensite <nom_site>.conf
sudo a2dissite 000-default.conf
sudo apache2ctl configtest
sudo systemctl reload apache2
```
👉 Explication : `a2ensite` active le nouvel hôte virtuel, `a2dissite` retire le site par défaut. `configtest` valide la syntaxe avant le rechargement.

3. Ouverture du pare-feu pour HTTP, HTTPS et administration :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow 'Apache Full'
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Ouvre SSH seulement pour `<adresse_ip_admin>` avant d'activer le pare-feu. Le profil `Apache Full` ouvre les ports 80 et 443. Vérifier que le profil existe avec `sudo ufw app list`.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Masquage de la version et des signatures :
```bash
sudo nano /etc/apache2/conf-available/security.conf
```
Régler les lignes suivantes :
```
ServerTokens Prod
ServerSignature Off
```
👉 Explication : Évite de révéler la version d'Apache dans les en-têtes et les pages d'erreur. Puis `sudo a2enconf security` et `sudo systemctl reload apache2`.

2. Activation de HTTPS et redirection depuis HTTP :
```bash
sudo a2enmod ssl headers rewrite
sudo a2enmod http2
```
👉 Explication : Active le module TLS, la gestion des en-têtes de sécurité et la réécriture d'URL. Le certificat est référencé dans un hôte virtuel `*:443` avec `SSLEngine on`, `SSLCertificateFile` et `SSLCertificateKeyFile` ; les chemins sont à vérifier sur la version déployée.

3. Désactivation des modules non utilisés :
```bash
apache2ctl -M
sudo a2dismod -f autoindex status
sudo systemctl reload apache2
```
👉 Explication : `apache2ctl -M` liste les modules chargés. Désactiver `autoindex` (listing des dossiers) et `status` (page d'état) s'ils ne servent pas à l'application.

4. Contrôle des journaux et des erreurs :
```bash
sudo tail -n 50 /var/log/apache2/error.log
sudo grep " 403 \| 500 " /var/log/apache2/access.log | tail -n 20
```
👉 Explication : Affiche les erreurs récentes et les codes 403 ou 500. Une vague de 403 peut signaler un scan ; à remonter au responsable sécurité.

5. Sauvegarde de la configuration avant toute évolution :
```bash
sudo tar czf /root/apache-conf-$(date +%F).tgz /etc/apache2
sudo ls -l /root/apache-conf-*.tgz
```
👉 Explication : Crée une archive datée de toute la configuration Apache, à stocker hors du serveur et à protéger en lecture.

---
