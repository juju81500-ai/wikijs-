# 📄 Redis

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Redis 7.0.x (paquet des dépôts Debian 12, à vérifier sur la version déployée)
- **Catégorie** : Services Web et bases de données
- **Tags** : `[debian-12]`, `[redis]`, `[cache]`, `[sauvegarde]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer Redis sur Debian 12, vérifier qu'il répond et qu'il enregistre une valeur, puis le préparer pour la production : écoute limitée, authentification obligatoire, utilisateur applicatif restreint, sauvegarde testée. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du serveur et du client :
```bash
sudo apt update
sudo apt install -y redis-server redis-tools
redis-server --version
systemctl status redis-server --no-pager
```
👉 Explication : Installe Redis 7.0 depuis les dépôts Debian 12. Le service `redis-server` doit être `active (running)`.

2. Test de réponse et d'écriture :
```bash
redis-cli ping
redis-cli SET essai_lab "ok"
redis-cli GET essai_lab
```
👉 Explication : `ping` doit répondre `PONG`. `SET` puis `GET` doivent renvoyer la valeur `ok`. En lab, Redis n'écoute que sur `127.0.0.1` par défaut et ne demande pas de mot de passe.

---

## ⚡ 2. Production — Façon Simplifiée
1. Écoute réseau limitée et mode protégé actif :
```bash
sudo nano /etc/redis/redis.conf
sudo systemctl restart redis-server
sudo ss -ltnp | grep 6379
```
Dans le fichier, régler `bind 127.0.0.1 192.168.10.40` (adresse du serveur Redis, à adapter) et vérifier que `protected-mode yes` est présent.
👉 Explication : `bind` limite l'écoute aux interfaces indiquées. `protected-mode yes` refuse les connexions externes tant qu'aucun mot de passe n'est défini. `ss` confirme le port 6379 et l'adresse d'écoute.

2. Définition d'un mot de passe généré et stocké hors du fichier de configuration partagé :
```bash
REDIS_PASS=$(openssl rand -base64 32)
echo "requirepass $REDIS_PASS" | sudo tee -a /etc/redis/redis.conf > /dev/null
sudo systemctl restart redis-server
REDISCLI_AUTH="$REDIS_PASS" redis-cli ping
echo "$REDIS_PASS"
```
👉 Explication : Le mot de passe est ajouté à la configuration, puis le test `ping` avec authentification doit renvoyer `PONG`. Le mot de passe s'affiche une seule fois : le copier dans le coffre-fort du pack. La variable `REDISCLI_AUTH` évite de l'écrire dans la ligne de commande.

3. Ouverture du pare-feu pour l'application et l'administration SSH :
```bash
sudo apt install -y ufw
sudo ufw allow from 192.168.10.0/24 to any port 22 proto tcp
sudo ufw allow from 192.168.10.21 to any port 6379 proto tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Le port 6379 n'est accessible qu'au serveur applicatif `192.168.10.21` (à adapter). SSH est ouvert avant l'activation du pare-feu.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Création d'un utilisateur applicatif limité, au lieu du compte `default` :
```bash
APP_PASS=$(openssl rand -base64 32)
REDISCLI_AUTH="$REDIS_PASS" redis-cli ACL SETUSER appli on ">$APP_PASS" "~cache:*" +get +set +del +expire -@dangerous
REDISCLI_AUTH="$REDIS_PASS" redis-cli ACL LIST
echo "$APP_PASS"
```
👉 Explication : L'utilisateur `appli` ne peut lire et écrire que les clés préfixées `cache:` et ne peut exécuter aucune commande dangereuse (`FLUSHALL`, `CONFIG`, etc.). `ACL LIST` affiche les règles appliquées. La variable `$REDIS_PASS` est celle de la section 2, étape 2 : si la session a changé, la reprendre depuis le coffre-fort. Tester la connexion avec `REDISCLI_AUTH="$APP_PASS" redis-cli --user appli ping` avant de désactiver le compte `default`.

2. Restriction des droits sur la configuration :
```bash
sudo chown root:redis /etc/redis/redis.conf
sudo chmod 640 /etc/redis/redis.conf
ls -l /etc/redis/redis.conf
```
👉 Explication : Seul `root` peut modifier le fichier. Le groupe `redis` peut le lire. Le fichier contient le mot de passe de service.

3. Sauvegarde de la base sur disque :
```bash
redis-cli CONFIG GET dir
redis-cli BGSAVE
sudo install -d -m 700 /root/sauvegardes
sudo cp /var/lib/redis/dump.rdb /root/sauvegardes/redis-$(date +%F).rdb
sudo ls -l /root/sauvegardes
```
👉 Explication : `CONFIG GET dir` indique le dossier de sauvegarde (par défaut `/var/lib/redis`). `BGSAVE` produit un instantané de la base sans bloquer le service. Le fichier `dump.rdb` doit être copié hors du serveur. Un cache n'a pas forcément besoin de sauvegarde : le choix doit être validé par l'équipe applicative.

4. Contrôle des journaux de service :
```bash
sudo journalctl -u redis-server -n 50 --no-pager
```
👉 Explication : Affiche les 50 dernières lignes du journal. Les messages `WRONGPASS` et les tentatives refusées par les ACL doivent être remontés au responsable sécurité.

---
