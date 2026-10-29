# 📄 Fiche_Simple_-_VM_Rocky_9_Securite_Sysctl_Noyau.md

- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9 (noyau 5.14 et supérieur)
- **Catégorie** : Sécurité / Durcissement du noyau et de la pile réseau
- **Tags** : `[rocky9]`, `[rhel9]`, `[sysctl]`, `[kernel]`, `[reseau]`, `[hardening]`

## 🎯 Problème précis à résoudre
Appliquer un durcissement sysctl persistant (redirections ICMP, SYN cookies, filtrage anti-spoofing, ASLR, accès aux logs noyau) via `/etc/sysctl.d/` sur Rocky Linux 9, sans casser le routage ou les conteneurs.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lire les valeurs actives :
   ```bash
   sysctl net.ipv4.tcp_syncookies kernel.randomize_va_space kernel.dmesg_restrict
   ```
   👉 Explication : `sysctl` lit les valeurs dans `/proc/sys`. Ces valeurs sont celles appliquées à l'instant, pas forcément celles du fichier de configuration.

2. Tester une valeur sans la rendre persistante :
   ```bash
   sudo sysctl -w kernel.dmesg_restrict=1
   ```
   👉 Explication : La modification disparaît au redémarrage. Elle permet de vérifier l'effet avant d'écrire le fichier définitif.

---

## ⚡ 2. Production — Façon Simplifiée
1. Créer le fichier de durcissement persistant :
   ```bash
   sudo tee /etc/sysctl.d/90-durcissement.conf >/dev/null <<'EOF'
   net.ipv4.tcp_syncookies = 1
   net.ipv4.conf.all.accept_redirects = 0
   net.ipv4.conf.all.send_redirects = 0
   net.ipv4.conf.all.accept_source_route = 0
   net.ipv4.conf.all.rp_filter = 1
   net.ipv4.conf.all.log_martians = 1
   net.ipv4.icmp_echo_ignore_broadcasts = 1
   net.ipv6.conf.all.accept_redirects = 0
   kernel.randomize_va_space = 2
   kernel.kptr_restrict = 2
   kernel.dmesg_restrict = 1
   fs.protected_hardlinks = 1
   fs.protected_symlinks = 1
   EOF
   ```
   👉 Explication : Ces clés refusent les redirections ICMP et le routage par la source, activent les SYN cookies contre le flood SYN et le filtrage anti-spoofing `rp_filter`. `randomize_va_space = 2` active l'ASLR complet.

2. Charger tous les fichiers et vérifier les valeurs :
   ```bash
   sudo sysctl --system
   sudo sysctl net.ipv4.conf.all.accept_redirects kernel.randomize_va_space
   ```
   👉 Explication : `sysctl --system` relit `/usr/lib/sysctl.d/`, `/run/sysctl.d/` et `/etc/sysctl.d/` par ordre alphabétique. Le fichier `90-` est donc appliqué en dernier.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérifier avant application les hôtes qui routent du trafic (passerelle, hyperviseur, hôte de conteneurs) :
   ```bash
   sysctl net.ipv4.ip_forward
   ```
   👉 Explication : `ip_forward` doit rester à `1` sur un routeur ou un hôte Podman avec réseau bridge. Ne pas forcer `0` dans le fichier de durcissement sur ces hôtes.

2. Contrôler le filtrage de chemin inverse sur les serveurs multi-interfaces ou VPN :
   ```bash
   sysctl net.ipv4.conf.all.rp_filter
   ```
   👉 Explication : Avec `rp_filter = 1`, un trafic arrivant par une interface qui n'est pas la route de retour est rejeté. Passer en mode `2` (lâche) si le routage asymétrique est volontaire.

3. Conserver une procédure de retour arrière :
   ```bash
   sudo rm /etc/sysctl.d/90-durcissement.conf
   sudo sysctl --system
   ```
   👉 Explication : Supprimer le fichier et recharger; les valeurs par défaut de Rocky Linux reprennent immédiatement. Vérifier le chemin avant la suppression.

---

## ✅ Contrôle
```bash
sysctl -a 2>/dev/null | grep -E '^(net.ipv4.tcp_syncookies|kernel.dmesg_restrict) '
```
👉 Explication : Les valeurs affichées doivent être `1`. La commande `sysctl -a` liste toutes les clés du noyau.
