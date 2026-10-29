# 📄 Fiche_Simple_-_VM_Rocky_9_Systeme_Timezone_Locale.md

- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9 avec systemd
- **Catégorie** : Système & Services / Fuseau horaire et locale

## 🎯 Problème précis à résoudre
Régler le fuseau horaire (Europe/Paris), conserver l'horloge matérielle en UTC et définir la locale système française `fr_FR.UTF-8` sur Rocky Linux 9.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Rechercher le nom IANA du fuseau voulu :
   ```bash
   timedatectl list-timezones | grep Paris
   ```
   👉 Explication : Liste les fuseaux présents dans la base tzdata installée. Le nom à utiliser est `Europe/Paris`.

2. Appliquer le fuseau et vérifier l'heure locale et l'heure UTC :
   ```bash
   sudo timedatectl set-timezone Europe/Paris
   timedatectl
   ```
   👉 Explication : Crée le lien `/etc/localtime` vers la zone demandée. `timedatectl` affiche les heures locale, UTC et RTC.

---

## ⚡ 2. Production — Façon Simplifiée
1. Garder l'horloge matérielle en UTC (valeur par défaut sous Linux) :
   ```bash
   sudo timedatectl set-local-rtc 0
   timedatectl show --property=LocalRTC
   ```
   👉 Explication : Une RTC en UTC évite les décalages lors des passages été/hiver. Le réglage `1` n'est utile qu'en double démarrage avec Windows.

2. Installer la locale française et la définir pour le système :
   ```bash
   sudo dnf install -y glibc-langpack-fr
   sudo localectl set-locale LANG=fr_FR.UTF-8
   localectl status
   ```
   👉 Explication : Le paquet `glibc-langpack-fr` fournit la locale `fr_FR.UTF-8` sur Rocky Linux 9. `localectl set-locale` écrit `/etc/locale.conf`; les nouvelles sessions utilisent alors la locale définie.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérifier le fuseau réellement appliqué et la synchronisation de l'horloge :
   ```bash
   timedatectl show --property=Timezone --value
   timedatectl show --property=NTPSynchronized --value
   ```
   👉 Explication : Un horodatage cohérent est indispensable aux journaux, à Kerberos et aux certificats. La valeur `yes` confirme qu'une source NTP est synchronisée (voir la fiche Chrony).

2. Contrôler les tâches planifiées avant un changement de fuseau :
   ```bash
   sudo crontab -l
   sudo ls -l /etc/cron.d/
   ```
   👉 Explication : `cron` interprète les horaires en heure locale. Un changement de fuseau décale donc les tâches; il faut le planifier en fenêtre de maintenance.