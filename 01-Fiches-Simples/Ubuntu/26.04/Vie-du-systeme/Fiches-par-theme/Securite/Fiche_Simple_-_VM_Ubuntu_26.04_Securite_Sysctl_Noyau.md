# 📄 Fiche_Simple_-_VM_Ubuntu_26.04_Securite_Sysctl_Noyau

- **Environnement** : VM ou serveur Ubuntu exposé au réseau (hors routeur ou hôte de conteneurs)
- **OS / Version** : Ubuntu Server 26.04 LTS (noyau 7.0)
- **Catégorie** : Sécurité / Durcissement du noyau et de la pile réseau
- **Tags** : `ubuntu2604`, `sysctl`, `noyau`, `tcp-syncookies`, `rp-filter`, `hardening`

---

## 🎯 Problème précis à résoudre

Appliquer un jeu de paramètres `sysctl` de durcissement (redirections ICMP, SYN cookies, filtrage de source, protections des liens symboliques et des pointeurs noyau) de façon persistante, sans casser le routage ni Docker.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Relever les valeurs actuelles :
```bash
sysctl net.ipv4.tcp_syncookies net.ipv4.conf.all.accept_redirects net.ipv4.conf.all.rp_filter kernel.kptr_restrict
```
👉 Explication : Affiche la valeur active de chaque paramètre avant modification, pour pouvoir revenir en arrière.

2. Créer un fichier de configuration dédié :
```bash
sudo nano /etc/sysctl.d/99-hardening.conf
```
Contenu :
```text
net.ipv4.tcp_syncookies = 1
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.all.log_martians = 1
net.ipv4.icmp_echo_ignore_broadcasts = 1
fs.protected_hardlinks = 1
fs.protected_symlinks = 1
kernel.kptr_restrict = 2
kernel.dmesg_restrict = 1
```
👉 Explication : Le préfixe `99-` place le fichier après les fichiers par défaut. Chaque ligne désactive un vecteur d'attaque courant : redirections ICMP falsifiées, usurpation d'adresse source, adresses noyau exposées dans les journaux.

3. Appliquer tous les fichiers `sysctl.d` :
```bash
sudo sysctl --system
```
👉 Explication : Recharge la configuration sans redémarrage. Les lignes en erreur sont affichées ; une ligne inconnue signale un nom de paramètre incorrect.

## ⚡ 2. Production — Façon Simplifiée

1. Contrôler les paramètres réellement actifs :
```bash
sysctl net.ipv4.tcp_syncookies net.ipv4.conf.all.rp_filter fs.protected_symlinks kernel.dmesg_restrict
```
👉 Explication : Chaque valeur doit correspondre au fichier `99-hardening.conf`. Une valeur différente signale un autre fichier `sysctl.d` ou un fichier `/etc/sysctl.conf` plus récent qui écrase la valeur.

2. Identifier les fichiers qui surchargent les paramètres :
```bash
grep -r "rp_filter\|accept_redirects" /etc/sysctl.conf /etc/sysctl.d/ /usr/lib/sysctl.d/ 2>/dev/null
```
👉 Explication : Sur Ubuntu, `/etc/sysctl.conf` et `/etc/sysctl.d/` sont lus après `/usr/lib/sysctl.d/`. Le dernier fichier lu gagne.

## 🔒 3. Production — Façon Sécurisée

1. Ne pas désactiver le routage sur un hôte qui en a besoin (routeur, Docker, Kubernetes, WireGuard en relais) : ne pas ajouter `net.ipv4.ip_forward = 0` dans ce cas.
👉 Explication : Docker et les réseaux de conteneurs exigent `ip_forward = 1`. Le désactiver coupe le trafic des conteneurs sans message d'erreur évident.

2. Vérifier l'absence de régression réseau après application :
```bash
ip -br address
ip route
```
👉 Explication : Confirme que les interfaces et la route par défaut restent identiques après le rechargement des paramètres.

3. Consigner la configuration appliquée et la date dans le dépôt de configuration (Git ou Ansible) :
```bash
sudo sysctl --system > /tmp/sysctl-appliquee-$(date +%F).log
```
👉 Explication : Garde une trace horodatée pour la preuve de conformité et pour comparer les dérives futures.

## ✅ Validation et retour arrière

- **Précontrôles** : valeurs initiales relevées, console de secours, confirmation que la machine n'est pas un routeur ou un hôte Docker.
- **Validation** : `sysctl net.ipv4.tcp_syncookies` renvoie `1` ; `sudo sysctl --system` s'exécute sans erreur ; les services réseau répondent.
- **Retour arrière** : `sudo rm /etc/sysctl.d/99-hardening.conf` puis `sudo sysctl --system` ; les valeurs par défaut du noyau reviennent.
