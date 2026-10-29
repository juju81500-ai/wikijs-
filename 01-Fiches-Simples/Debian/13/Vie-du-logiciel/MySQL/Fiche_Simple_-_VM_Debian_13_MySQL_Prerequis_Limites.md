# Fiche_Simple_-_VM_Debian_13_MySQL_Prerequis_Limites

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MySQL Community (dépôt officiel Oracle)
- **Catégorie** : base de données / MySQL / Prérequis et limites
- **Tags** : `debian13`, `mysql`, `prerequis`

---

## Problème précis à résoudre

Vérifier qu'un MySQL Community peut être installé sur Debian 13 et connaître les limites avant de commencer.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'OS et l'espace disque :
   ```bash
   cat /etc/os-release | grep PRETTY_NAME
   df -h /var/lib /var/backups
   ```
   👉 Explication : prévoir de l'espace pour les données, journaux binaires et sauvegardes.

2. Détecter un MariaDB déjà installé :
   ```bash
   dpkg -l | grep -E 'mariadb|mysql' || echo 'aucun serveur installé'
   sudo ss -tlnp | grep -E ':3306\b' || echo 'port 3306 libre'
   ```
   👉 Explication : MariaDB et MySQL ne cohabitent pas sur les mêmes paquets ni le même port.

3. Vérifier la prise en charge de Debian 13 par le dépôt Oracle :
   👉 Explication : Debian 13 ne distribue pas MySQL : il faut le dépôt APT officiel MySQL (paquet `mysql-apt-config`). Vérifier sur la page de téléchargement que Debian 13 est prise en charge pour la version visée (8.4 LTS) ; sinon utiliser MariaDB, une VM Ubuntu LTS ou un conteneur officiel.

## 2. Production — Contrôles

Consigner la raison du choix MySQL (compatibilité applicative), la version LTS, la volumétrie, les clients, le responsable.

## 3. Production — Sécurité

- Ne pas mélanger paquets Debian MariaDB et paquets MySQL Oracle.
- Pas d'exposition réseau avant la fiche Sécuriser.
- Limites : serveur unique ; réplication, InnoDB Cluster hors périmètre.

## Validation et retour arrière

- **Validation** : OS confirmé, port libre, prise en charge de la version vérifiée.
- **Retour arrière** : aucune modification effectuée.

## Si le problème n'est pas résolu

- [MySQL — Installer](Fiche_Simple_-_VM_Debian_13_MySQL_Installer.md)
- [MySQL — Configurer](Fiche_Simple_-_VM_Debian_13_MySQL_Configurer.md)
- [MySQL — Sécuriser (TLS, comptes, pare-feu)](Fiche_Simple_-_VM_Debian_13_MySQL_Securiser.md)
- [MySQL — Valider (recette)](Fiche_Simple_-_VM_Debian_13_MySQL_Valider.md)
- [MySQL — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_MySQL_Sauvegarder_Restaurer.md)
- [MySQL — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_MySQL_Mettre_A_Jour.md)
- [MySQL — documentation officielle](https://dev.mysql.com/doc/)
- [Alternative MariaDB (fiches du pack)](../MariaDB/Fiche_Simple_-_VM_Debian_13_MariaDB_Prerequis_Limites.md)
