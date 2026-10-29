---
title: "Maintenance d’un système en production (Debian GNU/Linux)"
description: "cat /etc/debianversion   # version Debian"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Maintenance d’un système en production (Debian GNU/Linux)

## 📊 Analyse et diagnostic du système

### 🧠 Commandes utiles

```bash
cat /etc/debian_version   # version Debian
uname -a                  # noyau et architecture
lscpu                     # CPU
lspci, lsusb              # périphériques PCI/USB
lsblk, df -h, du -sh      # disques, partitions, taille
file /bin/bash            # type de fichier
```

### 🔍 Suivi en temps réel

```bash
top                      # processus actifs
htop                     # version améliorée (à installer)
glances                  # synthèse système (à installer)
```

---

## 📋 Gestion des journaux avec systemd-journald

### 🔍 Consulter les logs

```bash
systemctl status sshd.service
journalctl               # tout
journalctl -f            # temps réel
journalctl -u sshd       # service spécifique
journalctl -p err        # par priorité
journalctl _PID=1        # par PID
journalctl /usr/bin/sshd # par binaire
```

### 🛠️ Configuration journald

- Fichier : `/etc/systemd/journald.conf`
- Rendre les logs persistants :

```bash
mkdir -p /var/log/journal
```

- Contrôler l’espace disque :

```ini
SystemMaxUse=500M
SystemMaxFileSize=50M
```

---

## 📁 Complément avec rsyslog

### 🔧 Fichier : `/etc/rsyslog.conf`

Exemple de configuration :

```ini
auth,authpriv.*        /var/log/auth.log
*.*;auth,authpriv.none -/var/log/syslog
cron.*                 /var/log/cron.log
daemon.*               /var/log/daemon.log
```

### 🧪 Tester avec `logger`

```bash
logger -p cron.info "Message de test"
```

### 💡 Rsyslog peut envoyer des logs vers un serveur distant.

---

## 🔁 Gestion de la taille des logs : `logrotate`

### 📂 Fichier principal : `/etc/logrotate.conf`

- Les configurations spécifiques : `/etc/logrotate.d/*`

### Exemple de rotation

```ini
/var/log/squid/access.log {
  daily
  compress
  delaycompress
  rotate 30
  create 640
}
```

---

## ⏱️ Planification de tâches avec cron et anacron

### 🛠️ Crontab utilisateur

```bash
crontab -e
```

Syntaxe :

```
* * * * * commande
│ │ │ │ │
│ │ │ │ └── jour de la semaine (0 = dimanche)
│ │ │ └──── mois
│ │ └────── jour du mois
│ └──────── heure
└────────── minute
```

### Exemple

```bash
0 5 * * 1 /opt/bin/backup.sh   # tous les lundis à 5h
```

### 🧠 Astuces syntaxe

- `1,3,5` = lundi, mercredi, vendredi
- `10-20` = du 10 au 20
- `*/2` = toutes les 2 unités

### 📂 Crontab système : `/etc/crontab`

- Permet de spécifier l’utilisateur exécutant la tâche

---

## 🔄 Lancement de tâches différées : `anacron`

- Permet d’exécuter des tâches régulières même si le PC n’est pas allumé au moment prévu
- Fichier principal : `/etc/anacrontab`
- Exécute ce qui est prévu dans `/etc/cron.daily`, `/etc/cron.weekly`, etc.

---

## ✅ À retenir pour les révisions

- `journalctl`, `systemctl`, `logger`, `logrotate`, `crontab`, `anacron`, `top`, `df`, `du`, `lsof` sont essentiels
- La journalisation est assurée par **journald** et **rsyslog**, en parallèle
- `logrotate` évite que les fichiers de logs saturent le disque
- `cron` planifie à heure fixe, `anacron` rattrape les tâches manquées

---

## 📌 Bonnes pratiques professionnelles

- Configurer la **persistance des logs journald**
- Vérifier la rotation des logs (taille, conservation, compression)
- Préférer des scripts appelés par `cron` plutôt que des commandes longues
- Séparer les logs systèmes et applicatifs
- Surveiller régulièrement l’espace disque et l’état des services

---

## 🔗 Commandes utiles

```bash
journalctl -u sshd -f
systemctl status sshd.service
logger -p daemon.warning "Attention"
crontab -e
logrotate -d /etc/logrotate.conf
```

## Ressources complémentaires

- [Debian Logging Wiki](https://wiki.debian.org/Logging)