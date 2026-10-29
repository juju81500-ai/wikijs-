# 📄 Fiche_Simple_-_VM_Debian_13_Systeme_Locale_Timezone

- **Environnement** : VM ou LXC Debian 13
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Système & Services / Locale et fuseau horaire

## 🎯 Problème précis à résoudre
Définir une locale UTF-8 française et le fuseau `Europe/Paris` sur Debian 13 (Trixie), avec l'horloge matérielle en UTC, afin que les journaux, les sauvegardes et la supervision utilisent des horodatages cohérents et comparables.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Consulter la locale et le fuseau actuellement configurés :
   ```bash
   localectl status
   timedatectl status
   ```
   👉 Explication : `localectl` affiche la locale système et la disposition clavier ; `timedatectl` affiche le fuseau, l'état de la synchronisation NTP et le mode de l'horloge matérielle (RTC).

2. Installer le support des locales et générer la locale `fr_FR.UTF-8` :
   ```bash
   sudo apt-get update
   sudo apt-get install -y locales
   sudo sed -i 's/^# *fr_FR.UTF-8 UTF-8/fr_FR.UTF-8 UTF-8/' /etc/locale.gen
   sudo locale-gen
   ```
   👉 Explication : Le paquet `locales` fournit les fichiers de traduction. La ligne `fr_FR.UTF-8` est décommentée dans `/etc/locale.gen`, puis compilée par `locale-gen`. Sous Debian 13, ce mécanisme est identique à Debian 12.

3. Définir la locale par défaut et vérifier qu'elle est disponible :
   ```bash
   sudo localectl set-locale LANG=fr_FR.UTF-8
   localectl status
   locale -a | grep -i fr_fr
   ```
   👉 Explication : `localectl set-locale` écrit `LANG` dans `/etc/default/locale`. La nouvelle valeur n'apparaît qu'à la prochaine ouverture de session.

4. Choisir le fuseau horaire et le valider :
   ```bash
   timedatectl list-timezones | grep -i paris
   sudo timedatectl set-timezone Europe/Paris
   timedatectl status
   ```
   👉 Explication : Le nom `Europe/Paris` provient de la base IANA fournie par le paquet `tzdata` ; il gère automatiquement l'heure d'été et d'hiver.

---

## ⚡ 2. Production — Façon Simplifiée
1. Appliquer la locale, le fuseau et le mode RTC attendus pour le rôle du serveur :
   ```bash
   sudo localectl set-locale LANG=fr_FR.UTF-8
   sudo timedatectl set-timezone Europe/Paris
   sudo timedatectl set-local-rtc 0
   ```
   👉 Explication : `set-local-rtc 0` conserve l'horloge matérielle en UTC. Les journaux restent lisibles en heure locale, et les changements d'heure ne décalent plus le système au redémarrage.

2. Vérifier le résultat effectif :
   ```bash
   timedatectl
   localectl status
   date
   ```
   👉 Explication : Confirmer les lignes `Time zone: Europe/Paris`, `RTC in local TZ: no`, `System clock synchronized: yes` et `LANG=fr_FR.UTF-8`.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérifier que l'horloge est réellement synchronisée avant de considérer les horodatages fiables :
   ```bash
   timedatectl show -p NTPSynchronized --value
   ```
   👉 Explication : La valeur `yes` confirme la synchronisation NTP. Une dérive de plus de quelques minutes casse l'authentification Kerberos (Active Directory) et la validité des certificats TLS. La configuration du client NTP est décrite dans la fiche Chrony de Debian 13.

2. Documenter la locale réellement appliquée et vérifier que le fuseau pointe vers la bonne zone :
   ```bash
   cat /etc/default/locale
   ls -l /etc/localtime
   ```
   👉 Explication : `/etc/localtime` doit être un lien symbolique vers `/usr/share/zoneinfo/Europe/Paris`. Un fichier de configuration par service qui force `TZ=` peut contredire ce réglage ; le contrôle suivant le détecte :
   ```bash
   sudo grep -rs "^TZ=" /etc/environment /etc/default /etc/systemd/system 2>/dev/null
   ```