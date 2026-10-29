# 📄 RHEL

- **Environnement** : VM (RHEL 9)
- **OS / Version** : Red Hat Enterprise Linux 9.x
- **Version** : RHEL 9 (abonnement Red Hat requis, à vérifier sur la version déployée)
- **Catégorie** : Systèmes, annuaires et services

## 🎯 Problème précis à résoudre
Gérer les paquets d'un serveur RHEL 9 déjà installé : vérifier l'abonnement et les dépôts, appliquer les mises à jour, ouvrir un port de service dans firewalld et l'autoriser dans SELinux, puis durcir la gestion des paquets et du pare-feu. L'installation du système n'est pas reprise ici. Sans abonnement valide, les dépôts RHEL ne fournissent pas de mises à jour.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Identification de la version et de l'état de l'abonnement :
```bash
cat /etc/os-release
rpm -q redhat-release
sudo subscription-manager status
```
👉 Explication : Confirme RHEL 9. `subscription-manager status` doit afficher `Overall Status: Current`. Un autre état signifie que les dépôts ne sont pas accessibles.

2. Enregistrement du système si nécessaire (saisie interactive des identifiants Red Hat) :
```bash
sudo subscription-manager register
sudo subscription-manager attach --auto
sudo subscription-manager repos --list-enabled
```
👉 Explication : `register` demande l'identifiant et le mot de passe du compte Red Hat à l'invite, ils ne doivent pas figurer dans la commande. `attach --auto` rattache un abonnement disponible. `repos --list-enabled` liste les dépôts actifs, par exemple `rhel-9-for-x86_64-baseos-rpms` et `rhel-9-for-x86_64-appstream-rpms`.

3. Mise à jour des index et des paquets :
```bash
sudo dnf clean all
sudo dnf makecache
sudo dnf upgrade -y
sudo reboot
```
👉 Explication : Rafraîchit les métadonnées puis applique les mises à jour. Vérifier la version du noyau après redémarrage avec `uname -r`.

4. Installation des outils de contrôle SELinux :
```bash
sudo dnf install -y policycoreutils-python-utils setroubleshoot-server
rpm -q policycoreutils-python-utils setroubleshoot-server
```
👉 Explication : `semanage` (dans `policycoreutils-python-utils`) déclare les ports SELinux. `setroubleshoot-server` aide à interpréter les refus.

5. Contrôle de firewalld et de SELinux :
```bash
sudo systemctl status firewalld --no-pager
sudo firewall-cmd --list-all
sestatus
```
👉 Explication : `firewalld` doit être actif. `sestatus` doit afficher `Current mode: enforcing`.

6. Ouverture d'un port de test (exemple : 8443/tcp) dans firewalld et SELinux :
```bash
sudo semanage port -a -t http_port_t -p tcp 8443
sudo firewall-cmd --permanent --add-port=8443/tcp
sudo firewall-cmd --reload
sudo firewall-cmd --list-ports
```
👉 Explication : Déclare le port 8443 pour SELinux puis l'ouvre dans firewalld. Les deux étapes sont nécessaires. Si le port est déjà déclaré, utiliser `semanage port -m`.

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
👉 Explication : Applique les correctifs de sécurité automatiquement. Valider la politique avec l'exploitation, car un correctif noyau impose un redémarrage.

2. Ouverture de HTTPS pour le réseau interne uniquement :
```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.10.0/24" service name="https" accept'
sudo firewall-cmd --reload
sudo firewall-cmd --list-all
```
👉 Explication : N'ouvre HTTPS que pour `192.168.10.0/24`. Adapter le réseau à l'entreprise.

3. Historique des transactions dnf :
```bash
sudo dnf history list --reverse | tail -n 10
sudo dnf history info last
```
👉 Explication : Liste les dernières modifications de paquets, utile pour retrouver ce qu'il faut annuler après un incident.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérification de la signature des paquets dans chaque dépôt :
```bash
sudo grep -rH "gpgcheck" /etc/yum.repos.d/
sudo grep -rH "^enabled" /etc/yum.repos.d/redhat.repo
```
👉 Explication : Tous les dépôts actifs doivent avoir `gpgcheck=1`. Le fichier `redhat.repo` est géré par `subscription-manager` : ne pas le modifier à la main.

2. Limitation de SSH au réseau d'administration :
```bash
sudo firewall-cmd --list-services
sudo firewall-cmd --permanent --remove-service=ssh
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.10.0/24" service name="ssh" accept'
sudo firewall-cmd --reload
sudo firewall-cmd --list-all
```
👉 Explication : Retire SSH de la zone et ne l'accepte que depuis le réseau d'administration. Tester depuis un poste autorisé avant de fermer la session courante.

3. Contrôle des refus SELinux et des erreurs système :
```bash
sudo ausearch -m AVC,USER_AVC -ts today
sudo journalctl -p err -b --no-pager
```
👉 Explication : Liste les refus SELinux du jour et les erreurs du démarrage courant. Un refus se traite par une règle ciblée, jamais par `setenforce 0`.

4. Sauvegarde de la configuration du pare-feu :
```bash
sudo cp -a /etc/firewalld /root/firewalld-$(date +%F)
sudo ls -l /root/firewalld-*
```
👉 Explication : Copie la configuration firewalld avant chaque modification.

5. Point à vérifier : les identifiants des dépôts optionnels (par exemple `codeready-builder-for-rhel-9-x86_64-rpms`) dépendent de l'abonnement et de la version mineure. Vérifier avec `sudo subscription-manager repos --available` avant activation.

---