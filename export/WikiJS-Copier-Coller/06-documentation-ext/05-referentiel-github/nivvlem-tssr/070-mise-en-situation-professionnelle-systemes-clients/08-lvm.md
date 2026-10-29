# Mise en situation professionnelle : Systèmes clients

## Gestion avancée du stockage

## 🧱 Objectif

Mettre en œuvre une gestion avancée du stockage sous Debian avec **LVM** et des montages permanents spécifiques, tester le montage distant SMB vers Windows, et réaliser des exercices de bureautique avec Excel.

---

## 🐧 Debian 10 – Montage `/var/log` sur partition dédiée `LOGS`

### 📄 Objectif

Monter la partition `LOGS` (xfs) créée précédemment dans `/var/log` sans perte de données système.

### 🔧 Étapes

1. Monter temporairement la partition ailleurs :

```bash
sudo mount /dev/sdb3 /mnt/logs
```

2. Copier les fichiers actuels :

```bash
sudo rsync -av /var/log/ /mnt/logs/
```

3. Monter la partition en tant que `/var/log` :

- Modifier `/etc/fstab` :

```bash
LABEL=LOGS /var/log xfs defaults 0 2
```

4. Redémarrer et vérifier :

```bash
mount | grep /var/log
```

> 💡 Tu peux tester l’écriture d’un log avec `logger "test log"` et consulter `/var/log/syslog`

---

## 🐧 Debian 10 – LVM pour `/opt`

### 🎯 Objectif

Créer un **volume logique LVM** de 32 Go à partir de deux disques SCSI de 20 Go chacun, formaté en ext4 et monté en `/opt`

### 🔧 Étapes

1. Ajouter deux disques de 20 Go via VMware
2. Identifier les nouveaux disques :

```bash
lsblk
```

(Ici : `/dev/sdc` et `/dev/sdd`)

3. Initialiser LVM :

```bash
sudo pvcreate /dev/sdc /dev/sdd
sudo vgcreate vg_opt /dev/sdc /dev/sdd
sudo lvcreate -L 32G -n lv_opt vg_opt
```

4. Formater et monter :

```bash
sudo mkfs.ext4 /dev/vg_opt/lv_opt
sudo mkdir /opt
sudo mount /dev/vg_opt/lv_opt /opt
```

5. Ajout dans `/etc/fstab` :

```bash
/dev/vg_opt/lv_opt /opt ext4 defaults 0 2
```

> ⚠️ Les applications installées dans `/opt` ne doivent pas être écrasées → test requis post-montage.

---

## 🐧 Debian – Montage d’un partage SMB (Windows)

### 🎯 Objectif

Monter sur Debian le partage `Support_Info$` de ton Windows, à l’aide d’un compte autorisé.

### 🔧 Étapes

1. Installer les outils :

```bash
sudo apt install cifs-utils
```

2. Créer un point de montage + fichier credentials sécurisé :

```bash
sudo mkdir /mnt/support_info
sudo nano /etc/samba/cred_win.txt
```

Contenu du fichier :

```
username=md
password=mon_motdepasse
```

3. Modifier `/etc/fstab` :

```fstab
//10.107.200.72/Support_Info$ /mnt/support_info cifs credentials=/etc/samba/cred_win.txt,vers=3.0,uid=1000,gid=1000 0 0
```

4. Monter :

```bash
sudo mount -a
```

### ✅ Vérification

```bash
df -h | grep support_info
ls /mnt/support_info
```

---

## ✅ Résumé des validations

|Élément|Résultat attendu|
|---|---|
|`/var/log` monté sur LOGS|Montage persistant et logs fonctionnels|
|`/opt` monté via LVM|Volume de 32 Go ext4, montage permanent|
|Partage Windows monté sur Debian|`/mnt/support_info` accessible|
|Fichier Excel complété|Calculs, formules et conditions fonctionnelles|