# Déployer Observium Community sur Debian 13

- **OS / Version** : Debian 13 Trixie x86-64; édition Observium Community, archive publiée par le projet
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : serveur web Apache/PHP, MariaDB, poller et un équipement pilote SNMPv3
- **Catégorie** : Supervision réseau et inventaire
- **Tags** : `observium`, `community`, `debian13`, `snmpv3`, `supervision`, `mariadb`

## 1. Définir le périmètre et dimensionner

Fiche simple : [cadrer et dimensionner Observium](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Observium/Fiche_Simple_-_VM_Debian_13_Observium_Cadrer.md).

Observium Community est l'édition libre, distribuée en archives majeures deux fois par an. L'édition Subscription suit des canaux SVN distincts, reçoit des mises à jour plus fréquentes et comporte des fonctions supplémentaires. Cette fiche ne décrit que Community; les fonctions avancées d'alerting mentionnées dans la documentation peuvent être réservées à l'édition Subscription.

La documentation Observium indique Debian 13 parmi les distributions compatibles, PHP supérieur à 8.2, MariaDB supérieur à 10.3, Apache supérieur à 2.4, Net-SNMP supérieur à 5.8, fping supérieur à 3.8 et RRDtool supérieur à 1.7.2. Pour un petit laboratoire, les repères publiés sont 2 cœurs, 4 Go de RAM et 20 Go SSD jusqu'à environ 50 appareils/1 000 ports. Dimensionner le stockage des RRD, les E/S et les ressources au volume réel.

Utiliser une VM dédiée, une adresse de gestion stable, une résolution DNS fiable et une synchronisation NTP. Prévoir un certificat HTTPS, des sauvegardes de la base MariaDB, de `config.php` et du répertoire `rrd`, ainsi qu'une restauration testée.

## 2. Installer les dépendances Debian

Fiche simple : [installer les dépendances Observium](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Observium/Fiche_Simple_-_VM_Debian_13_Observium_Dependances.md).

Installer les paquets depuis les dépôts Debian 13. `apt` choisit la version PHP supportée par Trixie; vérifier les dépendances effectives après installation.

```bash
sudo apt update
sudo apt install -y apache2 libapache2-mod-php php-cli php-mysql php-gd php-bcmath php-mbstring php-curl php-apcu php-pear mariadb-server mariadb-client snmp fping rrdtool whois mtr-tiny ipmitool libvirt-clients python3-mysqldb python3-pymysql python-is-python3 graphviz imagemagick
php --version
php -m
fping --version
rrdtool --version
```

Confirmer en particulier les extensions PHP requises par la documentation et les versions effectives d'Apache, PHP, MariaDB, Net-SNMP, fping et RRDtool. Si un prérequis n'est pas satisfait, arrêter avant de récupérer l'application.

## 3. Récupérer l'archive Community

Fiche simple : [récupérer l'archive Observium Community](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Observium/Fiche_Simple_-_VM_Debian_13_Observium_Archive.md).

Créer le répertoire d'installation et télécharger l'archive Community officielle via HTTPS. La ressource `community-latest` est mobile; consigner la date, la version affichée par l'application et l'empreinte locale pour rendre le déploiement reproductible. Ne pas traiter une empreinte calculée localement comme une signature upstream.

```bash
cd /opt
sudo install -d -o root -g root -m 0755 /opt/observium-stage
cd /opt/observium-stage
sudo curl --fail --location --proto '=https' --tlsv1.2 -o observium-community-latest.tar.gz https://www.observium.org/observium-community-latest.tar.gz
sha256sum observium-community-latest.tar.gz
tar -tzf observium-community-latest.tar.gz | head
sudo tar -xzf observium-community-latest.tar.gz -C /opt
sudo chown -R root:root /opt/observium
```

Examiner le contenu listé avant l'extraction et confirmer que l'archive crée `/opt/observium`. Si le répertoire existe déjà, arrêter et suivre la procédure de mise à niveau; ne pas écraser une installation. Ne pas exécuter de script d'installation téléchargé directement avec `sudo bash`; installer les dépendances explicitement et contrôler chaque étape.

## 4. Préparer MariaDB et la configuration

Fiche simple : [préparer MariaDB et config.php Observium](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Observium/Fiche_Simple_-_VM_Debian_13_Observium_MariaDB_Config.md).

Activer MariaDB et entrer dans son client local via l'authentification système :

```bash
sudo systemctl enable --now mariadb
sudo mariadb
```

Dans la console MariaDB, créer le schéma et un compte limité à cette base; remplacer immédiatement le mot de passe d'exemple par un secret aléatoire unique :

```sql
CREATE DATABASE observium DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'observium'@'localhost' IDENTIFIED BY 'SECRET_A_REMPLACER';
GRANT ALL ON observium.* TO 'observium'@'localhost';
EXIT;
```

Dans `/opt/observium`, copier `config.php.default` vers `config.php`, puis renseigner l'utilisateur et le secret MariaDB. Protéger ce fichier, qui contient des identifiants :

```bash
cd /opt/observium
sudo cp config.php.default config.php
sudo chown root:www-data config.php
sudo chmod 0640 config.php
sudo install -d -o www-data -g www-data -m 0750 rrd logs
sudo ./discovery.php -u
```

La commande `discovery.php -u` initialise ou met à jour le schéma selon l'archive. Contrôler sa sortie; ne pas ignorer les erreurs de base en production. Sous Debian, configurer Net-SNMP pour employer les MIB livrés avec Observium si le fichier `/etc/snmp/snmp.conf` contient la directive Debian `mibs :` qui désactive leur chargement; sauvegarder le fichier initial avant modification.

## 5. Configurer Apache en HTTPS

Fiche simple : [configurer Apache HTTPS pour Observium](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Observium/Fiche_Simple_-_VM_Debian_13_Observium_Apache_HTTPS.md).

Employer un certificat délivré par l'autorité de confiance de l'organisation. Remplacer le nom DNS, le réseau d'administration et les chemins de certificat. Le réseau `192.0.2.0/24` ci-dessous est réservé à la documentation et doit être remplacé par le véritable réseau d'administration.

Créer un VirtualHost Apache dédié au port 443 :

```apache
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

Sur Debian 13, identifier le module PHP installé (habituellement `php8.4`), puis activer le MPM et modules nécessaires. Ne pas laisser un MPM incompatible activé avec mod_php.

```bash
sudo a2dismod mpm_event
sudo a2enmod mpm_prefork ssl rewrite php8.4
sudo a2ensite observium.conf
sudo apache2ctl configtest
sudo systemctl reload apache2
```

Limiter le pare-feu au port TCP 443 depuis le réseau d'administration. L'accès SNMP sortant du serveur doit être limité aux équipements explicitement autorisés (UDP 161); ICMP n'est à autoriser que si la politique de supervision l'utilise. Ne pas publier l'interface d'administration sur Internet.

## 6. Créer l'utilisateur et ajouter un équipement pilote

Fiche simple : [créer l'utilisateur et ajouter un équipement Observium](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Observium/Fiche_Simple_-_VM_Debian_13_Observium_Utilisateur_Equipement.md).

Créer le premier compte administrateur avec l'outil fourni par la version Community. Le niveau `10` correspond à l'administrateur :

```bash
cd /opt/observium
sudo ./adduser.php observium-admin 'MOT_DE_PASSE_TEMPORAIRE_A_REMPLACER' 10
```

Remplacer immédiatement la valeur d'exemple par un secret aléatoire et temporaire. Le mot de passe est transmis en argument et peut être visible dans l'historique du shell ou dans la liste des processus; effectuer l'opération depuis une session d'administration contrôlée, ne pas l'inscrire dans un script ou un ticket, puis le changer dans l'interface après la première connexion. Attribuer le niveau administrateur uniquement au compte d'exploitation nominatif.

Avant l'ajout, vérifier depuis le serveur que le nom de l'équipement résout et que SNMP répond. Sur l'équipement pilote, configurer un utilisateur SNMPv3 `authPriv`, en lecture seule, autorisé uniquement depuis l'adresse de supervision. Préférer SHA-2 et AES lorsque l'équipement et Net-SNMP les prennent en charge; sinon choisir le meilleur algorithme commun validé par la politique locale. Ne pas utiliser la communauté `public` ni SNMPv1/v2c pour ce pilote.

Ajouter l'appareil via l'interface HTTPS d'Observium en saisissant les identifiants SNMPv3, ou employer `add_device.php` depuis une session contrôlée en tenant compte du fait que les secrets fournis en arguments peuvent être visibles dans la liste des processus. Vérifier le nom canonique, le modèle, le sysObjectID, les interfaces et la date de dernière interrogation. N'activer aucune découverte automatique de voisins au-delà des sous-réseaux autorisés.

## 7. Configurer découverte, interrogation et vérification

Fiche simple : [configurer découverte, poller et cron Observium](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Observium/Fiche_Simple_-_VM_Debian_13_Observium_Decouverte_Cron.md).

Lancer manuellement une découverte et une interrogation initiales :

```bash
cd /opt/observium
sudo ./discovery.php -h <nom-ou-id-du-pilote>
sudo ./poller.php -h <nom-ou-id-du-pilote>
```

Remplacer la valeur entre chevrons par l'identifiant attendu par la version installée. Confirmer l'absence d'erreurs SNMP, la création des données RRD et la mise à jour des graphiques avant d'ajouter d'autres appareils.

Créer `/etc/cron.d/observium` avec les tâches de la documentation officielle. Le poller doit impérativement tourner toutes les cinq minutes :

```cron
*/5 * * * * root /opt/observium/observium-wrapper poller >> /dev/null 2>&1
*/5 * * * * root /opt/observium/observium-wrapper discovery --host new >> /dev/null 2>&1
33 */6 * * * root /opt/observium/observium-wrapper discovery >> /dev/null 2>&1
```

Le champ utilisateur `root` convient au format `/etc/cron.d`; ne pas recopier ces lignes telles quelles dans `crontab -e`. Vérifier le journal cron, la dernière exécution du poller et les erreurs PHP/Apache/MariaDB après un cycle de cinq minutes.

## 8. Sauvegardes, sécurité et limites Community

Fiche simple : [sauvegarder et sécuriser Observium](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Observium/Fiche_Simple_-_VM_Debian_13_Observium_Sauvegarde_Securite.md).

- Sauvegarder MariaDB par dump cohérent, `config.php`, certificats, règles Apache et données RRD; conserver une copie hors de l'hôte et tester une restauration dans un environnement isolé.
- Restreindre les droits d'écriture du serveur web; en particulier, ne pas donner à Apache un accès général en écriture au code, aux scripts CLI ou à `rrd` sans exigence confirmée par la version installée.
- Protéger le compte MariaDB, l'accès web et les secrets SNMPv3; limiter l'accès web à HTTPS et au réseau d'administration.
- Surveiller la croissance MariaDB/RRD, l'espace disque, la fraîcheur des interrogations, les erreurs SNMP et l'état des tâches cron.
- En Community, les archives majeures sont publiées deux fois par an et les mises à niveau se font selon la procédure Community. Ne pas appliquer les commandes SVN réservées à Subscription Edition.
- Ne pas considérer les alertes, le syslog ou les intégrations comme disponibles au même niveau entre Community et Subscription; vérifier le droit d'usage et la fonctionnalité exacte avant conception.

## Sources

- [Observium — distributions Debian/Ubuntu compatibles et installation](https://docs.observium.org/install_debian/)
- [Observium — prérequis logiciels](https://docs.observium.org/software_requirements/)
- [Observium — options SNMP et configuration](https://docs.observium.org/config_options/)
- [Observium — ajouter un équipement](https://docs.observium.org/add_device/)
- [Observium — configuration Linux/Net-SNMP](https://docs.observium.org/device_linux/)
- [Observium — mises à jour Community et Subscription](https://docs.observium.org/updating/)
- [Observium — dimensionnement](https://docs.observium.org/hardware_scaling/)

Les archives Community et les instructions évoluent; relever et valider la version exacte avant mise en production. Aucun déploiement, ajout d'équipement ou essai de charge n'est consigné par cette fiche.