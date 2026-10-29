# Fiche_Simple_-_VM_Debian_13_Redis_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Redis des dépôts Debian
- **Catégorie** : base clé-valeur / Redis / Sauvegarder et restaurer
- **Tags** : `debian13`, `redis`, `sauvegarde`

---

## Problème précis à résoudre

Sauvegarder et restaurer les données Redis (RDB et AOF).

## 1. Hors-Production (Lab / Test / POC)

1. Forcer un instantané RDB et attendre sa fin :
   ```bash
   redis-cli BGSAVE
   sleep 2; redis-cli INFO persistence | grep rdb_bgsave_in_progress
   ```
   👉 Explication : la valeur doit repasser à `0` avant la copie.

2. Copier les fichiers de données :
   ```bash
   sudo install -d -m 0700 /var/backups/redis
   sudo cp -a /var/lib/redis/dump.rdb /var/backups/redis/dump-$(date +%F).rdb
   sudo cp -a /etc/redis /var/backups/redis/etc-$(date +%F)
   ```
   👉 Explication : avec `appendonly yes`, sauvegarder aussi le dossier `appendonlydir` de `/var/lib/redis`.

3. Restaurer sur un serveur de test :
   ```bash
   sudo systemctl stop redis-server
   sudo cp -a /var/backups/redis/dump-DATE.rdb /var/lib/redis/dump.rdb
   sudo chown redis:redis /var/lib/redis/dump.rdb
   sudo systemctl start redis-server
   ```
   👉 Explication : remplacer `DATE` (à remplacer) ; si `appendonly yes`, Redis charge l'AOF en priorité : le déplacer ou le supprimer avant le test.

4. Vérifier :
   ```bash
   redis-cli DBSIZE
   ```
   👉 Explication : le nombre de clés doit correspondre à la sauvegarde.

## 2. Production — Contrôles

Sauvegarde planifiée et chiffrée, copie hors site, test de restauration ; pour un simple cache, la sauvegarde peut être inutile (à décider).

## 3. Production — Sécurité

- Chiffrer les copies : elles contiennent toutes les données en clair.
- Dossier en `0700`.
- Ne pas restaurer sur la production sans copie préalable.

## Validation et retour arrière

- **Validation** : `DBSIZE` conforme après restauration.
- **Retour arrière** : reprendre la sauvegarde précédente.

## Si le problème n'est pas résolu

- [Redis — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_Redis_Prerequis_Limites.md)
- [Redis — Installer](Fiche_Simple_-_VM_Debian_13_Redis_Installer.md)
- [Redis — Configurer](Fiche_Simple_-_VM_Debian_13_Redis_Configurer.md)
- [Redis — Sécuriser (ACL, TLS, pare-feu)](Fiche_Simple_-_VM_Debian_13_Redis_Securiser.md)
- [Redis — Valider (recette)](Fiche_Simple_-_VM_Debian_13_Redis_Valider.md)
- [Redis — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_Redis_Mettre_A_Jour.md)
- [Redis — documentation officielle](https://redis.io/docs/latest/)
- [Redis — sécurité](https://redis.io/docs/latest/operate/oss_and_stack/management/security/)
- [Installation Redis avec NetBox (fiche du pack)](../PostgreSQL/Fiche_Simple_-_VM_Debian_13_NetBox_Installer_PostgreSQL_Redis.md)
