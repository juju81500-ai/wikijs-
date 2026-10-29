# Fiche_Simple_-_VM_Ubuntu_Restic_Definir_Donnees_Depot.md

- **Environnement** : VM Ubuntu Server avec destination de sauvegarde indépendante
- **OS / Version** : Ubuntu Server (toutes versions supportées); paquet restic des dépôts Ubuntu
- **Catégorie** : sauvegarde / restauration

---

## Problème précis à résoudre

Décider quoi sauvegarder et où, avant toute commande.

## 1. Hors-Production (Lab / Test / POC)

1. Repérer l'espace occupé par les chemins candidats :
   ```bash
   sudo du -sh /etc /home /srv /var/backups
   ```
   👉 Explication : on dimensionne la destination.

2. Lister chemins, bases de données, données applicatives et règles de rétention; choisir une destination indépendante du serveur (SFTP, stockage objet ou volume distant protégé).
   👉 Explication : un autre répertoire du même disque n'est pas une sauvegarde.

3. Pour PostgreSQL/MariaDB, produire d'abord un dump cohérent avec les outils de la base; pour les applications qui écrivent dans des fichiers, utiliser leur méthode de sauvegarde ou arrêter proprement le service.
   👉 Explication : on évite une sauvegarde incohérente.

## 2. Production — Contrôles

Consigner dépôt, backend, exclusions et rétention.

## 3. Production — Sécurité

- Ne pas sauvegarder sur le même disque que les données.

## Validation et retour arrière

- **Validation** : Liste des chemins, destination et rétention décidées.
- **Retour arrière** : Aucune modification; rien à annuler.

## Si le problème n'est pas résolu

- [Restic — Documentation officielle](https://restic.readthedocs.io/en/stable/)
- [Ubuntu — Documentation serveur](https://documentation.ubuntu.com/server/)
- [Guide complet sauvegarde Ubuntu Server Restic](/02-fiches-completes/ubuntu/toutes-versions/autres/29-sauvegarde-restauration-ubuntu-server-restic#1-definir-les-donnees-et-le-depot)