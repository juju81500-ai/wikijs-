# 📘 Synthèse – Administration d'une distribution GNU/Linux (Debian)

## 🧱 Fondamentaux

### ✅ À connaître absolument

- Debian repose sur une architecture solide : **noyau Linux** + **philosophie GNU**
- Arborescence conforme au **FHS** : `/etc`, `/home`, `/srv`, `/var`, `/opt`, etc.
- Chaque élément système est un **fichier** (périphérique, configuration, log…)
- L’administration se fait en grande majorité **en ligne de commande (CLI)**

---

## 🖥️ Installation & démarrage

### 📥 Moyens d’installation

- ISO Netinstall (léger, à jour), ISO DVD (complet, hors-ligne), Live CD, PXE
- Mode serveur : sans interface graphique / Mode client : avec environnement GNOME/KDE

### ⚙️ GRUB & démarrage

- GRUB est le **chargeur d’amorçage** (via `/etc/default/grub`, `/boot/grub/grub.cfg`)
- SystemD gère le démarrage, les cibles (`multi-user.target`, `graphical.target`…)
- `journalctl`, `systemctl`, `hostnamectl`, `timedatectl` : les outils clés

### 🛠️ Mode maintenance

- `init=/bin/bash` (accès root sans mot de passe)
- `single` ou `rescue.target` pour maintenance authentifiée

---

## 🌐 Réseau

### 🧠 Outils principaux

```bash
ip a            # adresses
ip r            # routes
cat /etc/resolv.conf
systemctl restart networking
nmtui            # configuration semi-graphique (NetworkManager)
```

### 📁 Configuration

- Fichier : `/etc/network/interfaces`
- DNS : `/etc/resolv.conf`
- Nom de machine : `/etc/hostname`, `/etc/hosts`

---

## 📦 Gestion des paquets

### 📁 Dépôts : `/etc/apt/sources.list`

```bash
apt update && apt upgrade
apt install / remove / purge / show
apt search mot-clé
```

### 📦 dpkg (bas niveau)

```bash
dpkg -L nom-paquet       # fichiers installés
dpkg -S /chemin/fichier  # paquet d’origine
```

### ⚙️ Compilation manuelle (rare, à documenter)

```bash
./configure && make && sudo make install
```

---

## 💾 Stockage & LVM

### 🧱 Partitionnement

- MBR (hérité) / GPT (moderne)
- Commandes : `fdisk`, `parted`, `lsblk`, `blkid`

### 🔄 LVM (volumes logiques)

```bash
pvcreate /dev/sdb1
vgcreate vgdata /dev/sdb1
lvcreate -n lvhome -L 20G vgdata
lvextend -r -L +10G /dev/vgdata/lvhome
```

---

## 🗃️ Systèmes de fichiers

### Création, montage, maintenance

```bash
mkfs.ext4 /dev/sdXn
mount /dev/sdXn /mnt
umount /mnt
resize2fs /dev/mapper/vg-lv
```

### Automatisation avec `/etc/fstab`

```fstab
UUID=xxxx-xxxx /data ext4 defaults 0 2
```

---

## 👥 Utilisateurs & groupes

### 📁 Fichiers système

- `/etc/passwd`, `/etc/shadow`, `/etc/group`, `/etc/gshadow`

### 🔧 Commandes

```bash
useradd, usermod, userdel
passwd, chage
groupadd, gpasswd, groupdel
id, su, sudo
```

### 🔐 Politiques

- Verrouillage : `usermod -L user`
- Forcer un changement : `passwd -e user`
- Ajouter à sudo : `usermod -aG sudo user`

---

## 🔐 Permissions & droits

### Notation

- Symbolique : `rwxr-x---`
- Octale : `chmod 750 fichier`

### 🧩 Droits spéciaux

```bash
chmod u+s fichier   # SetUID
chmod g+s dossier   # SetGID
chmod +t /dossier   # Sticky Bit
```

### 🌐 umask

- Détermine les droits par défaut : `umask 027` → fichiers 640, dossiers 750

---

## 🔍 Maintenance, logs et planification

### 🗂️ Journalisation

```bash
journalctl -xe / -u service
logger -p daemon.warning "test"
```

- Config : `/etc/systemd/journald.conf`, `/etc/rsyslog.conf`
- Rotation : `logrotate`

### 📅 Tâches planifiées

```bash
crontab -e
/etc/crontab  # version système
```

- `anacron` permet d’exécuter les tâches même après redémarrage

---

## ✅ À retenir pour les révisions

- **Systemctl, apt, useradd, mount, journalctl, crontab, rsyslog, lvm, chown, chmod** sont vos alliés quotidiens
- Savoir lire un log, une table de partition, une ligne fstab ou un cron est indispensable
- La **documentation (man, wiki, `--help`) est votre meilleure arme**

---

## 📌 Bonnes pratiques professionnelles

- Séparer `/home`, `/var`, `/srv` dans leur propre partition ou volume logique
- Toujours documenter : comptes, accès, scripts, tâches planifiées, logs personnalisés
- Tester les configurations critiques sur VM avant production
- Éviter les commandes destructrices non documentées (`rm -rf /`, `chmod 777 -R`, etc.)
- Conserver des sauvegardes, y compris des fichiers de config avant modification

---

## 🔗 Ressources complémentaires

- [Debian Wiki](https://wiki.debian.org/)
- [Cheat.sh](https://cheat.sh/)
- [Explainshell](https://explainshell.com/)