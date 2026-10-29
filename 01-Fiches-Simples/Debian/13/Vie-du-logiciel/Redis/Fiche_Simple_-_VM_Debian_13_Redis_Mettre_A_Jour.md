# Fiche_Simple_-_VM_Debian_13_Redis_Mettre_A_Jour

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Redis des dépôts Debian
- **Catégorie** : base clé-valeur / Redis / Mise à jour et retour arrière
- **Tags** : `debian13`, `redis`, `mise-a-jour`

---

## Problème précis à résoudre

Mettre à jour Redis avec un retour arrière fondé sur sauvegarde et instantané.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder :
   ```bash
   redis-cli BGSAVE
   sleep 2
   sudo cp -a /var/lib/redis /var/backups/redis/avant-maj-$(date +%F)
   sudo cp -a /etc/redis /var/backups/redis/etc-avant-maj-$(date +%F)
   ```
   👉 Explication : données et configuration ; ajouter un instantané de VM.

2. Lister la mise à jour :
   ```bash
   sudo apt update
   apt list --upgradable 2>/dev/null | grep -i redis
   redis-server --version
   ```
   👉 Explication : lire les notes de version (changements de licence, d'ACL, de commandes).

3. Appliquer :
   ```bash
   sudo apt install --only-upgrade redis-server redis-tools
   redis-server --version
   redis-cli ping
   ```
   👉 Explication : vérifier que les clients se reconnectent.

4. Retour arrière :
   ```bash
   sudo systemctl stop redis-server
   sudo apt install redis-server=VERSION_PRECEDENTE redis-tools=VERSION_PRECEDENTE
   sudo cp -a /var/backups/redis/avant-maj-DATE/. /var/lib/redis/
   sudo chown -R redis:redis /var/lib/redis
   sudo systemctl start redis-server
   ```
   👉 Explication : remplacer `VERSION_PRECEDENTE` et `DATE` (à remplacer) ; un format de données plus récent peut ne pas être lu par une version plus ancienne : privilégier l'instantané de VM.

## 2. Production — Contrôles

Pilote d'abord, fenêtre approuvée, surveillance mémoire/latence ensuite.

## 3. Production — Sécurité

- Pas de mise à jour majeure sans test.
- Conserver les sauvegardes jusqu'à validation.
- Prévenir les applications des reconnexions.

## Validation et retour arrière

- **Validation** : `redis-server --version` affiche la version cible, `PONG` et `DBSIZE` cohérents.
- **Retour arrière** : restaurer l'instantané ou la sauvegarde.

## Si le problème n'est pas résolu

- [Redis — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_Redis_Prerequis_Limites.md)
- [Redis — Installer](Fiche_Simple_-_VM_Debian_13_Redis_Installer.md)
- [Redis — Configurer](Fiche_Simple_-_VM_Debian_13_Redis_Configurer.md)
- [Redis — Sécuriser (ACL, TLS, pare-feu)](Fiche_Simple_-_VM_Debian_13_Redis_Securiser.md)
- [Redis — Valider (recette)](Fiche_Simple_-_VM_Debian_13_Redis_Valider.md)
- [Redis — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_Redis_Sauvegarder_Restaurer.md)
- [Redis — documentation officielle](https://redis.io/docs/latest/)
- [Redis — sécurité](https://redis.io/docs/latest/operate/oss_and_stack/management/security/)
- [Installation Redis avec NetBox (fiche du pack)](../PostgreSQL/Fiche_Simple_-_VM_Debian_13_NetBox_Installer_PostgreSQL_Redis.md)
