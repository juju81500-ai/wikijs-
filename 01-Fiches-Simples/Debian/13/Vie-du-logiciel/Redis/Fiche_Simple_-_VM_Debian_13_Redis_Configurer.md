# Fiche_Simple_-_VM_Debian_13_Redis_Configurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Redis des dépôts Debian
- **Catégorie** : base clé-valeur / Redis / Configurer
- **Tags** : `debian13`, `redis`, `configuration`

---

## Problème précis à résoudre

Configurer l'écoute, la mémoire et la persistance de Redis dans un fichier local inclus.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration :
   ```bash
   sudo cp -a /etc/redis/redis.conf /etc/redis/redis.conf.orig
   ```
   👉 Explication : point de retour.

2. Créer un fichier de réglages local :
   ```bash
   sudo tee /etc/redis/redis-local.conf >/dev/null <<'EOF'
   bind 127.0.0.1 -::1
   protected-mode yes
   maxmemory TAILLE_MAXMEMORY
   maxmemory-policy allkeys-lru
   appendonly yes
   EOF
   sudo chown redis:redis /etc/redis/redis-local.conf && sudo chmod 0640 /etc/redis/redis-local.conf
   echo 'include /etc/redis/redis-local.conf' | sudo tee -a /etc/redis/redis.conf
   ```
   👉 Explication : remplacer `TAILLE_MAXMEMORY` par une valeur comme `512mb` (à remplacer) ; l'`include` placé en fin de fichier prime sur les valeurs précédentes ; adapter la politique d'éviction à l'usage (`noeviction` pour des données à conserver).

3. Redémarrer et contrôler :
   ```bash
   sudo systemctl restart redis-server
   redis-cli CONFIG GET maxmemory
   redis-cli CONFIG GET appendonly
   ```
   👉 Explication : les valeurs doivent correspondre au fichier.

4. Contrôler les journaux :
   ```bash
   sudo journalctl -u redis-server -n 20 --no-pager
   ```
   👉 Explication : aucune erreur au démarrage.

## 2. Production — Contrôles

Configuration versionnée, mémoire et politique d'éviction documentées, persistance adaptée à l'usage.

## 3. Production — Sécurité

- `bind` limité à loopback tant que la sécurisation n'est pas faite.
- Fichier de configuration en `0640 redis`.
- Ne pas désactiver `protected-mode`.

## Validation et retour arrière

- **Validation** : `redis-cli ping` répond et les paramètres sont appliqués.
- **Retour arrière** : restaurer `redis.conf.orig`, supprimer `redis-local.conf`, redémarrer.

## Si le problème n'est pas résolu

- [Redis — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_Redis_Prerequis_Limites.md)
- [Redis — Installer](Fiche_Simple_-_VM_Debian_13_Redis_Installer.md)
- [Redis — Sécuriser (ACL, TLS, pare-feu)](Fiche_Simple_-_VM_Debian_13_Redis_Securiser.md)
- [Redis — Valider (recette)](Fiche_Simple_-_VM_Debian_13_Redis_Valider.md)
- [Redis — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_Redis_Sauvegarder_Restaurer.md)
- [Redis — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_Redis_Mettre_A_Jour.md)
- [Redis — documentation officielle](https://redis.io/docs/latest/)
- [Redis — sécurité](https://redis.io/docs/latest/operate/oss_and_stack/management/security/)
- [Installation Redis avec NetBox (fiche du pack)](../PostgreSQL/Fiche_Simple_-_VM_Debian_13_NetBox_Installer_PostgreSQL_Redis.md)
