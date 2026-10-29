# 📄 Fiche_Simple_-_Proxmox_VE_8_Diagnostic_Journaux_Taches.md

- **Environnement** : Hyperviseur Proxmox VE 8 (nœud autonome ou membre de cluster)
- **OS / Version** : Proxmox VE 8.x - Debian 12 Bookworm
- **Catégorie** : Diagnostic / Journaux et tâches
- **Tags** : `[proxmox-ve-8]`, `[debian-bookworm]`, `[journalctl]`, `[logs]`, `[taches]`, `[hardening]`

---

## 🎯 Problème précis à résoudre
Identifier les erreurs de l'hôte Proxmox VE 8 (services en échec, erreurs noyau, tâches échouées des VM et conteneurs), puis centraliser et limiter les journaux pour l'exploitation.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lister les services en échec et les erreurs du démarrage courant :
```bash
systemctl --failed
journalctl -p err -b --no-pager | tail -n 50
```
👉 Explication : `systemctl --failed` liste les unités systemd en échec ; `journalctl -p err -b` affiche les messages de niveau erreur depuis le dernier démarrage.

2. Consulter les journaux des démons Proxmox :
```bash
journalctl -u pvedaemon -u pveproxy -u pvestatd --since "1 hour ago" --no-pager
```
👉 Explication : affiche l'activité de l'API (`pvedaemon`), de l'interface web (`pveproxy`) et de la collecte des statistiques (`pvestatd`) sur l'heure écoulée.

3. Lister les tâches récentes du nœud, en ne gardant que les erreurs :
```bash
pvesh get /nodes/<nom_de_l_hote>/tasks --errors 1 --limit 20
```
👉 Explication : interroge l'API Proxmox et affiche les 20 dernières tâches en erreur (sauvegardes, migrations, démarrages de VM) avec leur identifiant UPID.

4. Consulter les tâches en cours et l'index des tâches :
```bash
cat /var/log/pve/tasks/active
head -n 20 /var/log/pve/tasks/index
```
👉 Explication : `active` liste les tâches encore en cours ; `index` contient l'historique récent des tâches avec leur statut final.

---

## ⚡ 2. Production — Façon Simplifiée
1. Analyser les erreurs du noyau par niveau de gravité :
```bash
dmesg -T --level=err,crit,alert,emerg | tail -n 50
```
👉 Explication : affiche les messages noyau d'erreur ou critiques avec horodatage lisible, utiles pour diagnostiquer disques, RAM ou cartes réseau.

2. Examiner les journaux du cluster Corosync et du système de fichiers de cluster :
```bash
journalctl -u corosync -u pve-cluster --since today --no-pager
```
👉 Explication : détecte les pertes de quorum, les changements de membres et les erreurs de `/etc/pve` ; sans cluster, les unités sont inactives et la commande ne renvoie rien d'utile.

3. Contrôler la taille du journal systemd :
```bash
journalctl --disk-usage
```
👉 Explication : indique l'espace occupé par les journaux persistants ou volatils, pour prévenir un remplissage de la partition système.

4. Vérifier la rotation des journaux :
```bash
logrotate -d /etc/logrotate.conf 2>&1 | head -n 30
```
👉 Explication : exécute `logrotate` en mode simulation (`-d`) pour vérifier que les fichiers de `/var/log` sont bien pris en charge sans rien modifier.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Activer le journal systemd persistant :
```bash
mkdir -p /var/log/journal
systemd-tmpfiles --create --prefix /var/log/journal
systemctl restart systemd-journald
```
👉 Explication : crée le répertoire `/var/log/journal` pour conserver les journaux après redémarrage, indispensable pour analyser une panne survenue avant le reboot.

2. Limiter la taille du journal persistant :
```bash
mkdir -p /etc/systemd/journald.conf.d
printf '[Journal]\nSystemMaxUse=2G\n' > /etc/systemd/journald.conf.d/90-limites.conf
systemctl restart systemd-journald
```
👉 Explication : plafonne l'espace occupé par les journaux à 2 Go pour éviter qu'ils ne saturent `/var` ; adapter la valeur à la taille de la partition.

3. Transmettre les journaux à un collecteur SIEM distant :
```bash
apt install -y rsyslog
echo '*.* @@<ip_siem>:514' > /etc/rsyslog.d/90-siem.conf
systemctl restart rsyslog
logger -p user.warning "Test de transmission SIEM depuis <nom_de_l_hote>"
```
👉 Explication : `@@` transmet les messages en TCP vers le collecteur ; le message de test doit apparaître côté SIEM, ce qui valide la chaîne complète.

4. Vérifier qu'aucune erreur critique n'est restée sans traitement :
```bash
journalctl -p crit -b --no-pager
```
👉 Explication : liste les événements de niveau critique depuis le dernier démarrage ; chaque entrée doit être documentée, corrigée ou justifiée dans le dossier d'exploitation.
