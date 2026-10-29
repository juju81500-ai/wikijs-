---
title: "Déployer Cacti 1.2.31 sur Debian 12"
description: "Fiche simple : [cadrer et préparer le déploiement](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Cacti/FicheSimple-VMDebian12CactiCadrer.md)."
published: true
date: 2026-10-29T19:55:10Z
tags: ["cacti", "debian12", "snmp", "rrdtool", "supervision", "mariadb"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# Déployer Cacti 1.2.31 sur Debian 12

- **OS / Version** : Debian 12 Bookworm; Cacti 1.2.31
- **Type de fiche** : Installation/Déploiement
- **Architecture** : serveur web, PHP, MariaDB et poller local
- **Catégorie** : Supervision réseau et graphes historiques
- **Tags** : `cacti`, `debian12`, `snmp`, `rrdtool`, `supervision`, `mariadb`

## 1. Cadrage et prérequis

Fiche simple : [cadrer et préparer le déploiement](/01-fiches-simples/debian/12/vie-du-logiciel/cacti/fiche-simple-vm-debian-12-cacti-cadrer).

Installer sur une VM dédiée et dimensionner CPU, RAM, stockage RRD et base selon le nombre de périphériques, de graphes et la fréquence d'interrogation. Préparer DNS, NTP, certificat TLS, stratégie de sauvegarde et compte de service SNMP lecture seule. La collecte par polling implique une connectivité réseau explicite entre le poller et les équipements autorisés.

La version actuelle documentée par Cacti est 1.2.31; vérifier les exigences PHP, extensions, MariaDB, RRDtool et Composer avant de figer les paquets. Ne pas utiliser un dépôt de branche mobile en production : choisir une archive/release identifiée, vérifier sa provenance et appliquer les correctifs de sécurité.

## 2. Installer les dépendances

Fiche simple : [installer les dépendances](/01-fiches-simples/debian/12/vie-du-logiciel/cacti/fiche-simple-vm-debian-12-cacti-installer-dependances).

```bash
sudo apt update
sudo apt install apache2 mariadb-server rrdtool snmp snmpd php php-mysql php-snmp php-xml php-mbstring php-gd php-gmp php-zip php-ldap php-intl php-cli composer
```

Vérifier la version PHP réellement fournie par Debian et les extensions requises par Cacti 1.2.31. Configurer MariaDB selon les recommandations compatibles avec la version installée; ne pas reprendre d'anciens réglages de blog tels que `innodb_doublewrite=OFF` ou des valeurs arbitraires de threads.

## 3. Installer Cacti

Fiche simple : [installer Cacti depuis la release officielle](/01-fiches-simples/debian/12/vie-du-logiciel/cacti/fiche-simple-vm-debian-12-cacti-installer-cacti).

Télécharger la release stable Cacti 1.2.31 depuis le projet officiel ou cloner explicitement le tag correspondant, puis contrôler le checksum/signature publié avant déploiement. Installer les fichiers dans un chemin dédié document root (par exemple `/var/www/html/cacti`), appliquer le propriétaire web attendu et lancer Composer selon le guide officiel.

Ne pas utiliser les commandes d'exemple anciennes qui déplacent arbitrairement le répertoire ou modifient AppArmor/SELinux. Conserver le confinement de Debian et les profils du serveur web; si un accès est refusé, diagnostiquer l'événement et définir une règle minimale.

## 4. Créer la base et la credential applicative

Fiche simple : [créer la base et la credential applicative](/01-fiches-simples/debian/12/vie-du-logiciel/cacti/fiche-simple-vm-debian-12-cacti-base-et-credential).

Créer une base `cacti` en `utf8mb4` et un compte dédié à localhost avec un secret aléatoire du coffre. Accorder uniquement les privilèges requis par la documentation de Cacti sur sa base et les accès nécessaires à la table timezone; ne jamais conserver le mot de passe d'exemple `cactiuser`.

Importer le schéma `cacti.sql` fourni par la même release que le code, puis renseigner les identifiants dans `include/config.php`. Restreindre les permissions du fichier de configuration et ne pas le placer dans un dossier publiquement servi autre que le chemin protégé/documenté.

## 5. Finaliser l'interface et la collecte

Fiche simple : [finaliser l'interface et la collecte](/01-fiches-simples/debian/12/vie-du-logiciel/cacti/fiche-simple-vm-debian-12-cacti-finaliser-collecte).

Redémarrer Apache/PHP-FPM après configuration si utilisé. Ouvrir l'interface derrière HTTPS et terminer l'assistant avec un compte administrateur unique; changer les valeurs initiales et supprimer tout accès de démonstration.

Configurer le poller sous un compte dédié et le cron ou service systemd recommandé par la release. Ajouter d'abord un équipement pilote autorisé, utiliser SNMPv3 authPriv en lecture seule et attacher uniquement les templates utiles. Le poller doit recevoir les réponses depuis les équipements; limiter UDP/161 aux sources nécessaires.

## 6. Vérifier

Fiche simple : [vérifier le déploiement](/01-fiches-simples/debian/12/vie-du-logiciel/cacti/fiche-simple-vm-debian-12-cacti-verifier).

```bash
sudo systemctl --no-pager status apache2 mariadb
sudo journalctl -u apache2 -b --no-pager
sudo mariadb -e 'SHOW DATABASES LIKE "cacti";'
```

Dans Cacti, confirmer l'état du poller, les logs de collecte, l'historique de l'hôte pilote et la création des graphes. Comparer les compteurs d'interfaces et les dates de dernière collecte avec l'équipement source.

## 7. Sécuriser et exploiter

Fiche simple : [sécuriser et exploiter](/01-fiches-simples/debian/12/vie-du-logiciel/cacti/fiche-simple-vm-debian-12-cacti-securiser-exploiter).

- Forcer HTTPS et restreindre le VirtualHost aux réseaux d'administration.
- Restreindre MariaDB à localhost, appliquer les mises à jour et limiter les comptes web.
- Chiffrer/contrôler l'accès au stockage de configuration et aux sauvegardes.
- Sauvegarder la base, `config.php`, templates personnalisés et données RRD; tester la restauration.
- Surveiller cron/poller, erreurs SNMP, saturation disque, croissance RRD et connexions MariaDB.
- Revoir les recommandations de tuning sur la version exacte, les mesures réelles et la charge; une modification de performance n'est pas une valeur universelle.

## Sources

- [Cacti — Documentation officielle](https://docs.cacti.net/)
- [Cacti — Installation Ubuntu/Debian](https://docs.cacti.net/Installing-Under-Ubuntu-Debian.md)
- [Cacti — Prérequis](https://docs.cacti.net/Requirements.md)
- [Cacti — Release 1.2.31](https://www.cacti.net/info/changelog)
- [Cacti — Gestion des appareils](https://docs.cacti.net/Devices.md)
- [Cacti — Configuration SNMP](https://docs.cacti.net/SNMP-Options.md)