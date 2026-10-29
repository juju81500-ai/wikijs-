# 📄 Fiche_Simple_-_VM_Ubuntu_26.04_Securite_Fail2ban

- **Environnement** : VM ou serveur Ubuntu exposant SSH ou un service web
- **OS / Version** : Ubuntu Server 26.04 LTS
- **Catégorie** : Sécurité / Protection contre le brute-force

---

## 🎯 Problème précis à résoudre

Bloquer automatiquement, pendant une durée limitée, les adresses IP qui échouent répétitivement à s'authentifier sur SSH, sans bloquer les administrateurs légitimes.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Installer Fail2ban :
```bash
sudo apt update
sudo apt install -y fail2ban
```
👉 Explication : Installe le démon qui lit les journaux et ajoute des règles de blocage. Le paquet est disponible dans les dépôts `main` d'Ubuntu 26.04.

2. Vérifier que SSH journalise dans journald :
```bash
sudo journalctl -u ssh -n 5 --no-pager
```
👉 Explication : Sur Ubuntu 26.04, le service SSH écrit dans le journal systemd. Fail2ban doit donc utiliser le backend `systemd`, sinon il ne voit aucun échec.

3. Créer un fichier de configuration local (ne jamais modifier `jail.conf`) :
```bash
sudo nano /etc/fail2ban/jail.local
```
Contenu :
```text
[DEFAULT]
bantime  = 1h
findtime = 10m
maxretry = 5
backend  = systemd

[sshd]
enabled = true
port    = ssh
```
👉 Explication : Cinq échecs en dix minutes déclenchent un bannissement d'une heure. `jail.local` est lu après `jail.conf`, ce qui permet aux mises à jour du paquet de remplacer le fichier de référence sans effacer votre configuration.

4. Activer le service et vérifier la configuration :
```bash
sudo fail2ban-client -t
sudo systemctl enable --now fail2ban
sudo fail2ban-client status sshd
```
👉 Explication : `-t` valide la syntaxe avant le démarrage. `status sshd` affiche le nombre d'échecs et d'adresses bannies.

## ⚡ 2. Production — Façon Simplifiée

1. Ajouter les adresses d'administration à la liste blanche dans `/etc/fail2ban/jail.local`, sous `[DEFAULT]` :
```text
ignoreip = 127.0.0.1/8 ::1 <IP_ADMINISTRATION>
```
👉 Explication : Empêche le bannissement d'un poste d'administration qui se trompe de mot de passe. Il faut lister l'IP fixe du bastion ou du VPN d'administration.

2. Recharger la configuration :
```bash
sudo systemctl restart fail2ban
sudo fail2ban-client status
```
👉 Explication : Le second appel liste les prisons actives. Une prison absente signale une erreur de configuration à corriger dans les journaux.

## 🔒 3. Production — Façon Sécurisée

1. Allonger la durée de bannissement pour les récidivistes avec le filtre `recidive` :
```text
[recidive]
enabled  = true
bantime  = 1w
findtime = 1d
maxretry = 3
```
👉 Explication : Une adresse bannie plusieurs fois par le filtre SSH est bloquée une semaine. Cela ralentit fortement les attaques distribuées lentes.

2. Faire passer les bannissements par UFW plutôt que par des règles iptables directes, dans `/etc/fail2ban/jail.local`, sous `[DEFAULT]` :
```text
banaction = ufw
```
Puis vérifier que le pare-feu est actif :
```bash
sudo ufw status verbose
```
👉 Explication : L'action par défaut de Fail2ban (`iptables-multiport`) insère ses règles hors de UFW, ce qui rend leur gestion opaque. Avec `banaction = ufw`, les bannissements apparaissent dans `ufw status`. Si UFW est inactif, le bannissement reste inscrit dans les journaux mais n'empêche pas la connexion.

3. Surveiller les bannissements :
```bash
sudo fail2ban-client status sshd
sudo journalctl -u fail2ban -n 50 --no-pager
```
👉 Explication : Fournit la liste des IP bannies et les événements récents, à intégrer dans la supervision.

## ✅ Validation et retour arrière

- **Précontrôles** : IP d'administration connue, session SSH ouverte de secours, `sudo fail2ban-client -t` sans erreur.
- **Validation** : `sudo fail2ban-client status sshd` affiche la prison active ; un test volontaire avec mauvais mot de passe depuis une autre machine apparaît après le seuil.
- **Retour arrière** : `sudo fail2ban-client unban <IP>` pour débloquer une adresse ; `sudo systemctl disable --now fail2ban` pour désactiver le service.