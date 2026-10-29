# 📄 Fiche_Simple_-_VM_Rocky_9_Stockage_Fstab_Options.md

- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9 (util-linux, systemd)
- **Catégorie** : Stockage / Montages et options de sécurité
- **Tags** : `[rocky9]`, `[rhel9]`, `[fstab]`, `[mount]`, `[tmp]`, `[hardening]`

## 🎯 Problème précis à résoudre
Vérifier les options de montage de `/tmp`, `/var/tmp` et `/dev/shm`, puis ajouter `nodev`, `nosuid` et `noexec` dans `/etc/fstab` sans rendre le serveur non démarrable.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lire les options actives des points de montage concernés :
   ```bash
   findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS /tmp /var/tmp /dev/shm
   ```
   👉 Explication : Sur Rocky Linux 9, `/tmp` n'est pas un montage séparé par défaut; `findmnt` affiche alors le périphérique racine (par exemple `/dev/mapper/rl-root`).

2. Vérifier la syntaxe de `/etc/fstab` sans redémarrer :
   ```bash
   sudo findmnt --verify --verbose
   ```
   👉 Explication : Contrôle les entrées du fichier et signale les erreurs de syntaxe ou les points de montage absents.

---

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder `/etc/fstab` avant toute modification :
   ```bash
   sudo cp -p /etc/fstab /etc/fstab.bak-$(date +%F)
   ```
   👉 Explication : La copie datée permet de revenir en arrière en cas d'erreur au démarrage.

2. Ajouter une entrée `/var/tmp` en liaison (bind) avec les options de sécurité :
   ```text
   /var/tmp  /var/tmp  none  bind,nodev,nosuid,noexec  0 0
   ```
   👉 Explication : `/var/tmp` fait partie de `/` par défaut; une option ne peut donc pas être ajoutée directement. Le montage en bind expose le même répertoire avec les options restrictives.

3. Appliquer les nouvelles options sans redémarrer, puis vérifier :
   ```bash
   sudo systemctl daemon-reload
   sudo mount -o remount,bind,nodev,nosuid,noexec /var/tmp
   sudo mount -o remount,nodev,nosuid,noexec /dev/shm
   findmnt -o TARGET,OPTIONS /var/tmp /dev/shm
   ```
   👉 Explication : `daemon-reload` relit `/etc/fstab` côté systemd. Le `remount` applique les options au montage actif. Les options doivent afficher `nodev`, `nosuid` et `noexec`.

   Attention : `noexec` sur `/var/tmp` bloque l'exécution de scripts d'installation qui y sont lancés. Tester les mises à jour et les déploiements applicatifs avant de généraliser.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Ajouter `/dev/shm` de manière persistante dans `/etc/fstab` :
   ```text
   tmpfs  /dev/shm  tmpfs  defaults,nodev,nosuid,noexec  0 0
   ```
   👉 Explication : Sans cette entrée, `/dev/shm` retrouve ses options par défaut après un redémarrage. Le type `tmpfs` est déjà monté par systemd.

2. Vérifier les options des autres montages sensibles, notamment `/home` et les supports amovibles :
   ```bash
   findmnt -R -o TARGET,FSTYPE,OPTIONS /
   ```
   👉 Explication : Repérer les montages qui ne portent pas `nodev` ou `nosuid` alors qu'ils ne doivent contenir ni périphérique ni binaire SUID.

3. Ne pas appliquer `noexec` sur `/tmp` sans test, car de nombreux outils y compilent ou exécutent des fichiers temporaires.
   ```bash
   sudo grep -v '^#' /etc/fstab
   ```
   👉 Explication : Relire les entrées actives après modification. Les lignes commentées sont filtrées par `grep`.

---

## ✅ Contrôle
```bash
sudo findmnt --verify
```
👉 Explication : Aucune erreur ne doit apparaître. Le contrôle doit être refait après chaque modification de `/etc/fstab`.
