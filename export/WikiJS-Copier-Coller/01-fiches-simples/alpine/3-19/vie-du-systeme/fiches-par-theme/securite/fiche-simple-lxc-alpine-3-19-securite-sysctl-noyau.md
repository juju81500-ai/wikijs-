# 📄 Fiche_Simple_-_LXC_Alpine_3.19_Securite_Sysctl_Noyau.md

- **Environnement** : LXC (Proxmox VE)
- **OS / Version** : Alpine Linux 3.19 - Famille Alpine (OpenRC, apk)
- **Catégorie** : Sécurité / Durcissement noyau et pile réseau

## 🎯 Problème précis à résoudre
Lire, tester et rendre persistants des paramètres `sysctl` de durcissement réseau sur un conteneur Alpine Linux, en distinguant les paramètres propres au conteneur de ceux qui relèvent du noyau de l'hôte Proxmox.

> Alpine 3.19 est en fin de support : valider cette procédure sur une branche maintenue avant tout usage en production.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lire les valeurs actuelles des paramètres ciblés :
   ```sh
   sysctl net.ipv4.tcp_syncookies
   sysctl net.ipv4.conf.all.accept_redirects
   sysctl net.ipv4.conf.all.rp_filter
   sysctl kernel.dmesg_restrict
   ```
   👉 Explication : La lecture ne modifie rien. Elle sert de référence avant toute écriture.

2. Tester une valeur à chaud :
   ```sh
   sysctl -w net.ipv4.conf.all.accept_redirects=0
   sysctl net.ipv4.conf.all.accept_redirects
   ```
   👉 Explication : La modification est immédiate mais disparaît au redémarrage. Si la commande échoue avec `Read-only file system` ou `permission denied`, le paramètre relève du noyau de l'hôte et doit être réglé sur Proxmox.

---

## ⚡ 2. Production — Façon Simplifiée
1. Créer un fichier dédié dans `/etc/sysctl.d/` :
   ```sh
   cat > /etc/sysctl.d/99-durcissement.conf <<'EOF'
   net.ipv4.conf.all.accept_redirects = 0
   net.ipv4.conf.all.send_redirects = 0
   net.ipv4.conf.all.accept_source_route = 0
   net.ipv4.conf.all.rp_filter = 1
   net.ipv4.tcp_syncookies = 1
   EOF
   ```
   👉 Explication : Ces paramètres refusent les redirections ICMP et le routage par la source, activent les SYN cookies et le filtrage de chemin inverse. Ne pas placer `kernel.*` dans ce fichier pour un LXC : ces clés sont celles de l'hôte.

2. Appliquer le fichier et le rendre persistant au démarrage avec OpenRC :
   ```sh
   sysctl -p /etc/sysctl.d/99-durcissement.conf
   rc-update add sysctl boot
   rc-service sysctl status
   ```
   👉 Explication : `sysctl -p` charge le fichier immédiatement; le service `sysctl` du runlevel `boot` le rejoue à chaque démarrage du conteneur.

---

## 🔒 3. Production — Façon Sécurisée
1. Régler les paramètres `kernel.*` sur l'hôte Proxmox, par exemple `kernel.dmesg_restrict`, dans `/etc/sysctl.d/` de l'hôte, puis appliquer :
   ```sh
   sysctl --system
   ```
   👉 Explication : À exécuter sur l'hôte. Un conteneur partage le noyau de l'hôte : un durcissement global se valide au niveau de l'hôte, pas dans le CT.

2. Contrôler la valeur effective dans le conteneur :
   ```sh
   sysctl net.ipv4.tcp_syncookies net.ipv4.conf.all.rp_filter
   ```
   👉 Explication : Les valeurs attendues sont `1`. Un écart indique que la configuration n'a pas été rechargée ou qu'un autre fichier `sysctl.d` la contredit.