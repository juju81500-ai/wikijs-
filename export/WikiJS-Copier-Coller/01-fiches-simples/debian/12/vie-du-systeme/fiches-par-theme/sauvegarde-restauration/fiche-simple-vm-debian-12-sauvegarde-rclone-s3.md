# 📄 VM_Debian_12_Sauvegarde_Configuration-Rclone-S3.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Sauvegarde & Stockage Cloud

## 🎯 Problème précis à résoudre
Installer l'outil officiel Rclone, configurer un dépôt de stockage distant compatible S3 / Cloud, et automatiser une sauvegarde chiffrée avec rotation et journalisation.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation rapide depuis les dépôts standard :
   `apt-get update && apt-get install -y rclone`
   👉 Explication : Met à jour le catalogue et installe la version binaire de Rclone fournie par Debian.
2. Copie de test sans suppression des objets distants :
   `rclone copy /var/www/html remote-s3:bucket-lab-test --progress --dry-run`
   👉 Explication : `copy` n'efface pas les fichiers supplémentaires à destination. Retirer `--dry-run` uniquement après vérification de la liste des opérations.
3. Vérification du contenu distant :
   `rclone ls remote-s3:bucket-lab-test`
   👉 Explication : Liste les fichiers présents sur le bucket distant pour valider la transmission.

---

## ⚡ 2. Production — Façon Simplifiée
1. Installation du paquet binaire officiel :
   `apt-get install -y rclone ca-certificates`
   👉 Explication : Télécharge et installe les paquets stables et les certificats racine d'autorité de certification.
2. Configuration interactive du remote S3 :
   `rclone config`
   👉 Explication : Ouvre le menu interactif pour saisir la clé d'accès (Access Key), la clé secrète (Secret Key) et l'endpoint S3.
3. Créer une tâche planifiée sous un compte dédié après un essai manuel. Utiliser `rclone copy` par défaut. Si un miroir est explicitement requis, tester d'abord `rclone sync --dry-run`, valider les suppressions prévues et activer le versioning côté bucket.
   👉 Explication : `sync` supprime à destination les fichiers absents de la source ; une erreur de chemin ou de montage peut donc effacer la sauvegarde distante.

---

## 🔒 3. Production — Façon Sécurisée (Hardening Enterprise & Chiffrement Client-Side)
1. Isolation de l'utilisateur système dédié sans shell :
   `useradd -r -s /usr/sbin/nologin -d /var/lib/rclone rcloneuser`
   👉 Explication : Crée un compte système restreint sans possibilité de connexion interactive console.
2. Créer un remote `crypt` au-dessus du remote S3 via `rclone config`, conserver ses mots de passe dans un coffre et sauvegarder séparément les paramètres de déchiffrement.
   👉 Explication : Le remote chiffre côté client selon l'implémentation/documentation de la version Rclone ; ne pas annoncer un algorithme précis sans vérifier la version et les options configurées.
3. Protéger le fichier de configuration réellement utilisé par le compte de sauvegarde (souvent `~/.config/rclone/rclone.conf`) et vérifier les permissions avec `rclone config file`. Ne pas appliquer les droits à `/etc/rclone.conf` s'il n'est pas utilisé.
4. Première exécution de sauvegarde chiffrée en mode simulation, puis copie vérifiée :
   ```bash
   rclone copy /data/critical crypt-s3:secured-bucket --bwlimit 10M --log-level INFO --dry-run
   rclone check /data/critical crypt-s3:secured-bucket
   ```
   👉 Explication : Définir une rétention indépendante côté stockage et tester régulièrement une restauration ; un remote crypt n'est pas une sauvegarde si les secrets de déchiffrement sont perdus.