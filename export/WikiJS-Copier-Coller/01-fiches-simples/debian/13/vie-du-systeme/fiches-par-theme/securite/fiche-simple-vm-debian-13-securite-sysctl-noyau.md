# 📄 Fiche_Simple_-_VM_Debian_13_Securite_Sysctl_Noyau

- **Environnement** : VM ou serveur Debian 13 (Kernel 6.12+)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Sécurité / Durcissement du noyau et de la pile réseau

## 🎯 Problème précis à résoudre
Durcir les paramètres du noyau Linux et de la pile réseau IPv4 / IPv6 sur Debian 13 (protection contre les redirections ICMP, le spoofing et l'usurpation de liens), via un fichier persistant dans `/etc/sysctl.d/`, sans casser les services qui dépendent du routage.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever les valeurs actuelles des paramètres ciblés :
   ```bash
   sysctl net.ipv4.tcp_syncookies net.ipv4.conf.all.rp_filter net.ipv4.conf.all.accept_redirects
   sysctl kernel.dmesg_restrict fs.protected_symlinks
   ```
   👉 Explication : Les valeurs affichées servent de référence pour le retour arrière. Une valeur `0` sur `rp_filter` ou `syncookies` est fréquente sur une installation par défaut.

2. Appliquer temporairement un paramètre pour tester son effet, sans fichier persistant :
   ```bash
   sudo sysctl -w net.ipv4.conf.all.accept_redirects=0
   sysctl net.ipv4.conf.all.accept_redirects
   ```
   👉 Explication : `sysctl -w` modifie le noyau en mémoire uniquement. Le redémarrage restaure la valeur d'origine.

3. Vérifier qu'aucune erreur n'apparaît dans les journaux du noyau :
   ```bash
   sudo dmesg --level=err,crit,alert,emerg | tail -n 20
   ```
   👉 Explication : Confirme que le changement ne provoque pas d'erreur ou d'avertissement dans le noyau.

---

## ⚡ 2. Production — Façon Simplifiée
1. Créer le fichier de durcissement persistant dans `/etc/sysctl.d/` :
   ```bash
   sudo tee /etc/sysctl.d/90-tssr-hardening.conf >/dev/null <<'EOF'
   net.ipv4.tcp_syncookies = 1
   net.ipv4.conf.all.rp_filter = 1
   net.ipv4.conf.default.rp_filter = 1
   net.ipv4.conf.all.accept_redirects = 0
   net.ipv4.conf.default.accept_redirects = 0
   net.ipv6.conf.all.accept_redirects = 0
   net.ipv4.conf.all.send_redirects = 0
   net.ipv4.conf.all.log_martians = 1
   fs.protected_hardlinks = 1
   fs.protected_symlinks = 1
   kernel.dmesg_restrict = 1
   EOF
   ```
   👉 Explication : `tcp_syncookies` protège contre le SYN flood, `rp_filter` contre le spoofing d'adresses source, et `accept_redirects` / `send_redirects` désactivent les messages ICMP de redirection. `fs.protected_*` limite la création de liens dangereux dans `/tmp`. Le préfixe `90-` garantit que le fichier est lu après les défauts Debian.

2. Charger tous les fichiers `sysctl.d` et vérifier les valeurs effectives :
   ```bash
   sudo sysctl --system
   sysctl net.ipv4.tcp_syncookies net.ipv4.conf.all.rp_filter fs.protected_symlinks
   ```
   👉 Explication : `sysctl --system` relit `/etc/sysctl.d/` et applique les valeurs sans redémarrage. Les paramètres sont persistés au boot de la machine.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Ne pas désactiver le routage sur une machine qui doit router (pare-feu, VPN, passerelle) ou héberger des conteneurs : `net.ipv4.ip_forward` doit rester à `1` dans ce cas. Vérifier la valeur actuelle avant toute modification :
   ```bash
   sysctl net.ipv4.ip_forward
   ```
   👉 Explication : Sur un serveur simple, `net.ipv4.ip_forward = 0` est un durcissement utile. Docker et Kubernetes activent eux-mêmes ce paramètre ; une valeur forcée à `0` casse alors le réseau des conteneurs.

2. Restreindre la lecture de la mémoire noyau et des pointeurs pour les utilisateurs non privilégiés, puis vérifier :
   ```bash
   echo "kernel.kptr_restrict = 2" | sudo tee -a /etc/sysctl.d/90-tssr-hardening.conf
   sudo sysctl --system
   sysctl kernel.kptr_restrict
   ```
   👉 Explication : Empêche la lecture des adresses du noyau par des comptes non privilégiés, ce qui gêne l'exploitation de vulnérabilités locales.

3. Conserver le fichier dans le dépôt de configuration du projet, et contrôler régulièrement l'écart avec les valeurs réelles :
   ```bash
   sudo sysctl --system 2>&1 | grep -i "error\|unknown"
   ```
   👉 Explication : Une clé inconnue (faute de frappe, paramètre retiré d'une version du noyau) est signalée à l'application du fichier.