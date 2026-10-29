# Fiche_Simple_-_VM_Debian_12_Borg_Cadrer_Besoin.md

- **Environnement** : serveur Debian 12 Bookworm, dépôt Borg local dédié ou distant
- **OS / Version** : Debian 12; BorgBackup depuis les dépôts Debian approuvés
- **Catégorie** : sauvegarde / cadrage Borg

---

## Problème précis à résoudre

Définir les données, la cohérence applicative et la protection des clés avant de créer un dépôt Borg.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les données à protéger et l'espace occupé :
   ```bash
   sudo du -sh /etc /home /var/www
   df -h
   ```
   👉 Explication : détermine volume, fréquence et capacité de la destination.

2. Pour une base active, prévoir un dump à inclure dans l'archive :
   ```bash
   sudo mkdir -p /var/backups/dumps
   sudo mariadb-dump --single-transaction --all-databases | gzip | sudo tee /var/backups/dumps/mariadb.sql.gz >/dev/null
   ```
   👉 Explication : une copie de fichiers d'une base en fonctionnement peut être incohérente (adapter au moteur utilisé).

3. Consigner : fréquence, rétention, RPO/RTO, destination indépendante, qui détient la clé.
   👉 Explication : la déduplication n'est pas une réplication; prévoir une copie hors site.

## 2. Production — Contrôles

Faire approuver périmètre, fréquence, capacité, rétention, stockage, chiffrement, responsables et procédure de récupération.

## 3. Production — Sécurité

- Une déduplication n'est ni une réplication ni une copie indépendante.
- Ne pas placer le seul dépôt sur le serveur qu'il protège.
- Ne pas copier directement des fichiers de base en cours d'écriture sans cohérence.
- Ne pas laisser l'unique clé ou phrase de passe sur la machine sauvegardée.

## Validation et retour arrière

- **Validation** : périmètre, destination indépendante et accès aux clés sont documentés et testables.
- **Arrêt** : ne pas initialiser de dépôt de production si la perte de clé ou l'absence de restauration n'est pas couverte.

## Si le problème n'est pas résolu

- [BorgBackup — documentation](https://borgbackup.readthedocs.io/en/stable/)
- [Guide complet BorgBackup Debian 12](/02-fiches-completes/debian/12/autres/19-sauvegarde-restauration-borgbackup-debian-12)