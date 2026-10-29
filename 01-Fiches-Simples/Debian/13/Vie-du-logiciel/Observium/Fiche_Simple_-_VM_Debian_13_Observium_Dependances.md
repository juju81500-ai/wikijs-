# Fiche_Simple_-_VM_Debian_13_Observium_Dependances.md

- **Environnement** : Observium Community sur Debian 13 (Apache/PHP, MariaDB, SNMPv3)
- **OS / Version** : Debian 13 Trixie x86-64; Observium Community
- **Catégorie** : supervision réseau / paquets
- **Tags** : `debian13`, `observium`, `apache`, `php`, `mariadb`, `apt`

---

## Problème précis à résoudre

Installer depuis Debian 13 la pile Apache, PHP, MariaDB et les outils SNMP nécessaires.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les paquets requis :
   ```bash
   sudo apt update
   sudo apt install -y apache2 libapache2-mod-php php-cli php-mysql php-gd php-bcmath php-mbstring php-curl php-apcu php-pear mariadb-server mariadb-client snmp fping rrdtool whois mtr-tiny ipmitool libvirt-clients python3-mysqldb python3-pymysql python-is-python3 graphviz imagemagick
   ```
   👉 Explication : APT choisit la version PHP supportée par Trixie.

2. Contrôler les versions effectives :
   ```bash
   php --version
   php -m | grep -Ei 'mysql|gd|bcmath|mbstring|curl'
   fping --version
   rrdtool --version
   ```
   👉 Explication : on confirme PHP supérieur à 8.2, les extensions requises, fping et RRDtool conformes à la documentation.

## 2. Production — Contrôles

Si un prérequis n'est pas satisfait, arrêter avant de récupérer l'application; consigner les versions installées.

## 3. Production — Sécurité

- Installer uniquement depuis les dépôts Debian approuvés.
- Ne pas exécuter de script d'installation téléchargé avec `sudo bash`.

## Validation et retour arrière

- **Validation** : toutes les commandes de version répondent et les extensions PHP sont listées.
- **Retour arrière** : `sudo apt remove` des paquets installés pour le lab (hors MariaDB si elle contient d'autres bases).

## Si le problème n'est pas résolu

- [Observium — installation Debian/Ubuntu](https://docs.observium.org/install_debian/)
- [Observium — prérequis logiciels](https://docs.observium.org/software_requirements/)
- [Observium — ajouter un équipement](https://docs.observium.org/add_device/)
- [Guide complet — étape 2](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/69_Deploiement_Observium_Community_Debian_13.md#2-installer-les-dependances-debian)
