# Fiche_Simple_-_VM_Debian_13_MongoDB_Configurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MongoDB Community (dépôt officiel)
- **Catégorie** : base de données / MongoDB / Configurer
- **Tags** : `debian13`, `mongodb`, `configuration`

---

## Problème précis à résoudre

Configurer `/etc/mongod.conf` (écoute, stockage, journalisation) et vérifier le démarrage.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration :
   ```bash
   sudo cp -a /etc/mongod.conf /etc/mongod.conf.orig
   ```
   👉 Explication : point de retour.

2. Contrôler les sections principales :
   ```bash
   sudo grep -nE 'dbPath|bindIp|port|path|authorization' /etc/mongod.conf
   ```
   👉 Explication : vérifier `storage.dbPath`, `net.bindIp: 127.0.0.1`, `systemLog.path`.

3. Appliquer un changement et redémarrer :
   ```bash
   sudo systemctl restart mongod
   sudo journalctl -u mongod -n 20 --no-pager
   ```
   👉 Explication : aucune erreur au démarrage.

4. Tester la connexion locale :
   ```bash
   mongosh --eval 'db.runCommand({ ping: 1 })'
   ```
   👉 Explication : `ok: 1` attendu.

## 2. Production — Contrôles

Configuration versionnée et relue ; limites système (`ulimit`) et THP contrôlés.

## 3. Production — Sécurité

- `bindIp` limité à loopback tant que la sécurité n'est pas appliquée.
- Droits `mongodb:mongodb` sur `dbPath`.
- Aucun secret dans `mongod.conf`.

## Validation et retour arrière

- **Validation** : `ping` renvoie `ok: 1`.
- **Retour arrière** : restaurer `/etc/mongod.conf.orig` et redémarrer.

## Si le problème n'est pas résolu

- [MongoDB — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_MongoDB_Prerequis_Limites.md)
- [MongoDB — Installer](Fiche_Simple_-_VM_Debian_13_MongoDB_Installer.md)
- [MongoDB — Sécuriser (authentification, TLS, pare-feu)](Fiche_Simple_-_VM_Debian_13_MongoDB_Securiser.md)
- [MongoDB — Valider (recette)](Fiche_Simple_-_VM_Debian_13_MongoDB_Valider.md)
- [MongoDB — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_MongoDB_Sauvegarder_Restaurer.md)
- [MongoDB — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_MongoDB_Mettre_A_Jour.md)
- [MongoDB — installation sous Debian](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/)
- [MongoDB — sécurité](https://www.mongodb.com/docs/manual/security/)
