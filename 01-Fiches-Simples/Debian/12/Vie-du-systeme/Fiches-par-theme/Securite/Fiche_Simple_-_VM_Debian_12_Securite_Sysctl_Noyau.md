# 📄 VM_Debian_12_Securite_Sysctl-Noyau.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Sécurité & Noyau / Durcissement réseau et système
- **Tags** : `[debian12]`, `[debian-family]`, `[sysctl]`, `[kernel]`, `[tcp-syncookies]`, `[rp-filter]`, `[hardening]`

## 🎯 Problème précis à résoudre
Durcir les paramètres du noyau Linux de Debian 12 via `sysctl` : protection contre le spoofing et les redirections ICMP, SYN flood, fuite d'adresses noyau et abus de liens symboliques, en persistant la configuration dans `/etc/sysctl.d/`.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lecture des valeurs courantes :
   `sysctl net.ipv4.tcp_syncookies net.ipv4.conf.all.accept_redirects kernel.kptr_restrict`
   👉 Explication : Affiche l'état actuel de trois paramètres de durcissement avant modification.
2. Contrôle du filtrage de chemin inverse :
   `sysctl net.ipv4.conf.all.rp_filter`
   👉 Explication : Une valeur `1` active le filtrage anti-spoofing ; `0` le désactive.
3. Vérification du routage IP :
   `sysctl net.ipv4.ip_forward`
   👉 Explication : Doit valoir `0` sur un serveur qui n'est pas routeur, pour éviter qu'il relaie du trafic.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création du fichier de durcissement persistant :
   `sudoedit /etc/sysctl.d/90-durcissement.conf`
   👉 Explication : Y placer `net.ipv4.tcp_syncookies = 1`, `net.ipv4.conf.all.rp_filter = 1`, `net.ipv4.conf.all.accept_redirects = 0`, `net.ipv4.conf.all.send_redirects = 0`, `net.ipv4.conf.all.accept_source_route = 0`, `net.ipv4.icmp_echo_ignore_broadcasts = 1`.
2. Chargement de tous les fichiers sysctl :
   `sudo sysctl --system`
   👉 Explication : Applique immédiatement les paramètres de `/etc/sysctl.d/`, `/etc/sysctl.conf` et des autres emplacements de configuration.

---

## 🔒 3. Production — Façon Sécurisée (Protection noyau & Vérification)
1. Ajout des protections système complémentaires :
   `sudoedit /etc/sysctl.d/90-durcissement.conf`
   👉 Explication : Ajouter `kernel.kptr_restrict = 2`, `kernel.dmesg_restrict = 1`, `fs.protected_hardlinks = 1`, `fs.protected_symlinks = 1` et `net.ipv6.conf.all.accept_redirects = 0` (si IPv6 actif).
2. Rechargement du fichier et contrôle des valeurs appliquées :
   `sudo sysctl -p /etc/sysctl.d/90-durcissement.conf`
   👉 Explication : Recharge uniquement ce fichier et affiche chaque paramètre réellement pris en compte ; une erreur de nom de clé apparaît ici.
3. Contrôle des redirections et du routage après application :
   `sudo sysctl -a 2>/dev/null | grep -E 'accept_redirects|send_redirects|ip_forward'`
   👉 Explication : Vérifie que les redirections sont refusées et que le routage est désactivé, sauf sur un routeur documenté.
