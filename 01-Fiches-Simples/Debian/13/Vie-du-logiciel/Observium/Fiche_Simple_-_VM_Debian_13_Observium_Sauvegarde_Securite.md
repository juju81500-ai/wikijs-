# Fiche_Simple_-_VM_Debian_13_Observium_Sauvegarde_Securite.md

- **Environnement** : Observium Community sur Debian 13 (Apache/PHP, MariaDB, SNMPv3)
- **OS / Version** : Debian 13 Trixie x86-64; Observium Community
- **Catégorie** : supervision réseau / sauvegarde sécurité
- **Tags** : `debian13`, `observium`, `sauvegarde`, `securite`, `rrd`

---

## Problème précis à résoudre

Sauvegarder base, configuration et RRD et appliquer les contrôles de sécurité Community.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un dump cohérent de la base (identifiants lus dans la configuration d'accès administrateur local) :
   ```bash
   sudo install -d -m 0700 /var/backups/observium
   sudo mariadb-dump --single-transaction observium | sudo tee /var/backups/observium/observium-$(date +%F).sql >/dev/null
   ```
   👉 Explication : `--single-transaction` donne une copie cohérente sans bloquer; le dossier est réservé à root.

2. Sauvegarder configuration, Apache et données RRD :
   ```bash
   sudo tar -czf /var/backups/observium/fichiers-$(date +%F).tar.gz /opt/observium/config.php /opt/observium/rrd /etc/apache2/sites-available/observium.conf /etc/cron.d/observium
   ```
   👉 Explication : ces éléments permettent de reconstruire le service avec le dump.

3. Contrôler les droits sur le code et les secrets :
   ```bash
   ls -l /opt/observium/config.php
   find /opt/observium -maxdepth 1 -writable -user www-data
   ```
   👉 Explication : `config.php` doit être en 0640 et le serveur web ne doit pas écrire dans le code ni dans les scripts CLI.

## 2. Production — Contrôles

Copie hors hôte, restauration testée en environnement isolé, surveillance disque/RRD, mises à niveau Community uniquement (pas de commandes SVN Subscription).

## 3. Production — Sécurité

- Chiffrer les sauvegardes (elles contiennent les secrets SNMPv3).
- Vérifier le droit d'usage des fonctions alertes/syslog avant conception.

## Validation et retour arrière

- **Validation** : le dump et l'archive existent et une restauration de test aboutit.
- **Retour arrière** : supprimer les sauvegardes de test; la restauration se fait dans un environnement isolé.

## Si le problème n'est pas résolu

- [Observium — installation Debian/Ubuntu](https://docs.observium.org/install_debian/)
- [Observium — prérequis logiciels](https://docs.observium.org/software_requirements/)
- [Observium — ajouter un équipement](https://docs.observium.org/add_device/)
- [Guide complet — étape 8](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/69_Deploiement_Observium_Community_Debian_13.md#8-sauvegardes-securite-et-limites-community)
