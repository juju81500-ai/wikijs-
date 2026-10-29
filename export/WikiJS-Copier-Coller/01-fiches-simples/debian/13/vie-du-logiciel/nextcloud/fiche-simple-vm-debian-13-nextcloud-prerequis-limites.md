# Fiche_Simple_-_VM_Debian_13_Nextcloud_Prerequis_Limites

- **Environnement** : VM Debian 13; Nextcloud (archive officielle), Apache, PHP 8.4 et MariaDB
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Nextcloud — Prérequis et limites

---

## Problème précis à résoudre

Vérifier la compatibilité d'une VM Debian 13 avec Nextcloud installé depuis l'archive officielle (le paquet n'est pas fourni par Debian 13).

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'OS, la RAM et l'espace disque :
   ```bash
   cat /etc/os-release | head -3
   free -h
   df -h /var /srv
   ```
   👉 Explication : dimensionner selon la doc officielle (RAM, volume de données) ; prévoir un volume séparé pour les données.

2. Relever la version PHP proposée par Debian 13 :
   ```bash
   apt-cache policy php | head -4
   ```
   👉 Explication : Debian 13 fournit PHP 8.4 ; vérifier dans les prérequis officiels que la version de Nextcloud visée prend en charge PHP 8.4, sinon choisir une autre version de Nextcloud.

3. Relever MariaDB et Apache :
   ```bash
   apt-cache policy mariadb-server apache2 | grep -E 'Candidate|^[a-z]'
   ```
   👉 Explication : MariaDB (ou PostgreSQL) et Apache/Nginx sont requis ; versions à comparer à la matrice officielle.

4. Définir le nom DNS et le répertoire de données :
   ```bash
   hostnamectl --static
   sudo install -d -m 0750 /srv/nextcloud-data
   ```
   👉 Explication : `/srv/nextcloud-data` doit être hors de la racine web (`/var/www`) ; nom DNS (`CLOUD.EXAMPLE.NET`) à remplacer.

## 2. Production — Contrôles

Documenter version cible, FQDN, volumétrie, authentification, politique de sauvegarde, besoin de Redis/antivirus. Pour une approche conteneurisée voir le guide Docker du pack.

## 3. Production — Sécurité

- Ne jamais placer le dossier de données dans la racine web.
- Snapshot de VM avant installation.

## Validation et retour arrière

- **Validation** : compatibilité PHP/BDD confirmée avec la documentation officielle de la version visée.
- **Retour arrière** : aucune modification applicative à ce stade ; supprimer `/srv/nextcloud-data` si créé et inutile.

## Si le problème n'est pas résolu

- [Nextcloud — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-installer)
- [Nextcloud — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-configurer)
- [Guide complet Docker Nextcloud 29 (alternative conteneurisée)](/02-fiches-completes/transverses/docker/installation-deploiement/05-cloud-prive-nextcloud-29-docker-mariadb-redis)
- [Nextcloud — manuel d'administration](https://docs.nextcloud.com/server/latest/admin_manual/)
- [Nextcloud — prérequis système](https://docs.nextcloud.com/server/latest/admin_manual/installation/system_requirements.html)