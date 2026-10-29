# Fiche_Simple_-_VM_Debian_12_Cacti_Installer_Dependances.md

- **Environnement** : VM Debian 12 dédiée (Apache, PHP, MariaDB, poller local)
- **OS / Version** : Debian 12 Bookworm; Cacti 1.2.31
- **Catégorie** : supervision / paquets
- **Tags** : `debian12`, `cacti`, `snmp`, `rrdtool`, `mariadb`

---

## Problème précis à résoudre

Installer Apache, MariaDB, RRDtool, SNMP, PHP et ses extensions.

## 1. Hors-Production (Lab / Test / POC)

1. Mettre à jour l'index puis installer les paquets :
   ```bash
   sudo apt update
   sudo apt install apache2 mariadb-server rrdtool snmp snmpd php php-mysql php-snmp php-xml php-mbstring php-gd php-gmp php-zip php-ldap php-intl php-cli composer
   ```
   👉 Explication : installe la pile web, la base, RRDtool, SNMP et les extensions PHP demandées par le guide.

2. Vérifier la version PHP fournie et les extensions :
   ```bash
   php -v
   php -m | grep -Ei 'snmp|mysql|gd|gmp|intl|mbstring|xml|zip|ldap'
   ```
   👉 Explication : confirme que les extensions requises par Cacti sont chargées.

## 2. Production — Contrôles

Configurer MariaDB selon les recommandations compatibles avec la version installée.

## 3. Production — Sécurité

- Ne pas reprendre d'anciens réglages de blog comme `innodb_doublewrite=OFF`.

## Validation et retour arrière

- **Validation** : Paquets installés, PHP et extensions présents.
- **Retour arrière** : Retirer les paquets avec `sudo apt remove` uniquement sur une VM de test non utilisée par d'autres services.

## Si le problème n'est pas résolu

- [Cacti — documentation officielle](https://docs.cacti.net/)
- [Cacti — installation Ubuntu/Debian](https://docs.cacti.net/Installing-Under-Ubuntu-Debian.md)
- [Guide complet — 2. Installer les dépendances](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/51_Deploiement_Cacti_1.2.31_Debian_12.md#2-installer-les-dependances)
