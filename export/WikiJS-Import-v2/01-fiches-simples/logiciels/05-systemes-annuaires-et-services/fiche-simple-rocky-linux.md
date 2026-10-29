---
title: "Rocky Linux"
description: "Gérer les paquets d'un serveur Rocky Linux 9 déjà installé : vérifier la version et les dépôts, appliquer les mises à jour, ouvrir un port de service dans firewalld et l'autoriser dans SELinux, puis durcir la gestion des paquets et du pare-feu. L'installation du système n'est pas reprise ici (voir l"
published: true
date: 2026-10-29T12:25:38Z
tags: ["[rocky-linux-9]", "[dnf]", "[firewalld]", "[selinux]", "[paquets]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:25:38Z
dateModified: 2026-10-29T12:25:38Z
---

# 📄 Rocky Linux

- **Environnement** : VM (Rocky Linux 9)
- **OS / Version** : Rocky Linux 9.x
- **Version** : Rocky Linux 9 (dépôts `rocky` et `rocky-extras`, à vérifier sur la version déployée)
- **Catégorie** : Systèmes, annuaires et services
- **Tags** : `[rocky-linux-9]`, `[dnf]`, `[firewalld]`, `[selinux]`, `[paquets]`, `[hardening]`

## 🎯 Problème précis à résoudre
Gérer les paquets d'un serveur Rocky Linux 9 déjà installé : vérifier la version et les dépôts, appliquer les mises à jour, ouvrir un port de service dans firewalld et l'autoriser dans SELinux, puis durcir la gestion des paquets et du pare-feu. L'installation du système n'est pas reprise ici (voir les fiches d'installation Rocky 9 du pack).

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Identification de la version et des dépôts actifs :
```bash
cat /etc/os-release
rpm -q rocky-release
dnf repolist
```
👉 Explication : Confirme la version Rocky 9 et liste les dépôts actifs (`rocky`, `rocky-extras`, `epel` si présent). Les paquets proviennent de ces dépôts.

2. Mise à jour des index et des paquets :
```bash
sudo dnf clean all
sudo dnf makecache
sudo dnf check-update
sudo dnf upgrade -y
sudo reboot
```
👉 Explication : Rafraîchit les métadonnées des dépôts, puis applique les mises à jour. Un redémarrage est nécessaire si le noyau a été mis à jour : vérifier avec `uname -r` après le redémarrage.

3. Installation des outils de contrôle SELinux :
```bash
sudo dnf install -y policycoreutils-python-utils setroubleshoot-server
rpm -q policycoreutils-python-utils setroubleshoot-server
```
👉 Explication : `policycoreutils-python-utils` fournit `semanage`, utilisé plus loin pour déclarer des ports. `setroubleshoot-server` aide à interpréter les refus SELinux.

4. Contrôle de firewalld et de SELinux :
```bash
sudo systemctl status firewalld --no-pager
sudo firewall-cmd --get-default-zone
sudo firewall-cmd --list-all
sestatus
```
👉 Explication : `firewalld` doit être actif. La zone par défaut est généralement `public`. `sestatus` doit afficher `SELinux status: enabled` et `Current mode: enforcing`.

5. Ouverture d'un port de test (exemple : serveur web sur 8443/tcp) dans firewalld et SELinux :
```bash
sudo semanage port -a -t http_port_t -p tcp 8443
sudo firewall-cmd --permanent --add-port=8443/tcp
sudo firewall-cmd --reload
sudo firewall-cmd --list-ports
```
👉 Explication : `semanage port -a` déclare le port 8443 comme port HTTP pour SELinux (sinon le service est refusé même si le pare-feu est ouvert). `firewall-cmd --add-port` ouvre le port dans firewalld. Si le port est déjà déclaré, `semanage` renvoie une erreur `ValueError` : utiliser `semanage port -m` pour modifier. Le port 8443 est un exemple à adapter.

---

## ⚡ 2. Production — Façon Simplifiée
1. Mises à jour de sécurité automatiques :
```bash
sudo dnf install -y dnf-automatic
sudo nano /etc/dnf/automatic.conf
```
Dans la section `[commands]`, régler :
```
upgrade_type = security
apply_updates = yes
```
```bash
sudo systemctl enable --now dnf-automatic-install.timer
systemctl list-timers dnf-automatic-install.timer --no-pager
```
👉 Explication : Limite les mises à jour automatiques aux correctifs de sécurité et les applique. Le minuteur est à valider avec la politique de changement de l'entreprise, car une mise à jour peut nécessiter un redémarrage.

2. Ouverture d'un service standard uniquement pour le réseau interne :
```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.10.0/24" service name="https" accept'
sudo firewall-cmd --reload
sudo firewall-cmd --list-all
```
👉 Explication : N'ouvre HTTPS (443/tcp) que pour le réseau interne, sans l'exposer à toute la zone. Adapter le réseau `192.168.10.0/24` à celui de l'entreprise.

3. Contrôle de l'historique des paquets :
```bash
sudo dnf history list --reverse | tail -n 10
sudo dnf history info last
```
👉 Explication : Liste les dernières transactions `dnf` (installations, mises à jour, suppressions). Permet de retrouver la modification à annuler en cas d'incident.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérification de la signature des paquets dans chaque dépôt :
```bash
sudo grep -rH "gpgcheck" /etc/yum.repos.d/
grep -rH "^enabled" /etc/yum.repos.d/
```
👉 Explication : Tous les dépôts actifs doivent avoir `gpgcheck=1`. Un dépôt en `gpgcheck=0` doit être désactivé ou justifié par écrit.

2. Limitation de l'accès SSH au réseau d'administration :
```bash
sudo firewall-cmd --list-services
sudo firewall-cmd --permanent --remove-service=ssh
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.10.0/24" service name="ssh" accept'
sudo firewall-cmd --reload
sudo firewall-cmd --list-all
```
👉 Explication : Retire SSH de la zone par défaut puis n'accepte SSH que depuis le réseau d'administration. Vérifier depuis un poste autorisé avant de fermer la session courante, sinon l'accès est perdu.

3. Contrôle des refus SELinux et des erreurs système :
```bash
sudo ausearch -m AVC,USER_AVC -ts today
sudo journalctl -p err -b --no-pager
```
👉 Explication : `ausearch` liste les refus SELinux du jour. `journalctl -p err -b` affiche les erreurs du démarrage courant. Un refus SELinux se corrige par une règle ciblée (`audit2allow` ou `semanage`), jamais par `setenforce 0`.

4. Sauvegarde de la configuration du pare-feu :
```bash
sudo cp -a /etc/firewalld /root/firewalld-$(date +%F)
sudo ls -l /root/firewalld-*
```
👉 Explication : Copie la configuration firewalld avant une modification. Pour restaurer, arrêter `firewalld`, remettre le dossier en place puis redémarrer le service.

5. Point à vérifier : le nom exact des dépôts optionnels (`crb`, `epel`) peut varier selon la version mineure de Rocky Linux 9. Vérifier avec `dnf repolist --all` avant d'activer un dépôt.

---