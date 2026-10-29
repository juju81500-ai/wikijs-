# Fiche_Simple_-_VM_Debian_13_Observium_Apache_HTTPS.md

- **Environnement** : Observium Community sur Debian 13 (Apache/PHP, MariaDB, SNMPv3)
- **OS / Version** : Debian 13 Trixie x86-64; Observium Community
- **Catégorie** : supervision réseau / web

---

## Problème précis à résoudre

Publier l'interface Observium en HTTPS, limitée au réseau d'administration.

## 1. Hors-Production (Lab / Test / POC)

1. Créer `/etc/apache2/sites-available/observium.conf` (nom, réseau et chemins d'exemple à remplacer; 192.0.2.0/24 est un réseau de documentation) :
   ```bash
   sudoedit /etc/apache2/sites-available/observium.conf
   ```
   👉 Explication : le fichier est créé avec le contenu suivant.

2. Y placer ce VirtualHost :
   ```bash
   <VirtualHost *:443>
       ServerName observium.mgmt.example
       DocumentRoot /opt/observium/html
       SSLEngine on
       SSLCertificateFile /etc/ssl/certs/observium-fullchain.pem
       SSLCertificateKeyFile /etc/ssl/private/observium.key
       <Directory /opt/observium/html>
           DirectoryIndex index.php
           Options FollowSymLinks
           AllowOverride All
           Require ip 192.0.2.0/24
       </Directory>
   </VirtualHost>
   ```
   👉 Explication : ce bloc (à enregistrer dans le fichier) sert l'interface en HTTPS pour le seul réseau d'administration.

3. Activer MPM prefork, modules et site, puis tester :
   ```bash
   sudo a2dismod mpm_event
   sudo a2enmod mpm_prefork ssl rewrite php8.4
   sudo a2ensite observium.conf
   sudo apache2ctl configtest
   sudo systemctl reload apache2
   ```
   👉 Explication : mod_php exige prefork; `php8.4` est le module habituel de Debian 13, à adapter si `ls /etc/apache2/mods-available | grep php` indique autre chose.

4. Limiter le pare-feu au TCP 443 depuis le réseau d'administration (exemple nftables/ufw selon l'outil en place).
   👉 Explication : aucun accès depuis Internet; SNMP sortant UDP 161 vers les seuls équipements autorisés.

## 2. Production — Contrôles

Certificat de l'autorité de confiance, renouvellement planifié, règles pare-feu revues.

## 3. Production — Sécurité

- Ne pas publier l'interface sur Internet.
- Clé privée en lecture root uniquement.

## Validation et retour arrière

- **Validation** : `sudo apache2ctl configtest` répond `Syntax OK` et `curl -I https://observium.mgmt.example/` répond depuis le réseau autorisé.
- **Retour arrière** : `sudo a2dissite observium.conf && sudo systemctl reload apache2`.

## Si le problème n'est pas résolu

- [Observium — installation Debian/Ubuntu](https://docs.observium.org/install_debian/)
- [Observium — prérequis logiciels](https://docs.observium.org/software_requirements/)
- [Observium — ajouter un équipement](https://docs.observium.org/add_device/)
- [Guide complet — étape 5](/02-fiches-completes/debian/13/installation-deploiement/69-deploiement-observium-community-debian-13#5-configurer-apache-en-https)