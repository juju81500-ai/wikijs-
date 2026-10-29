# 📄 Git

- **Environnement** : VM (Debian 12) client et serveur de sauvegarde
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Git 2.39.x (paquet des dépôts Debian 12, à vérifier sur la version déployée)
- **Catégorie** : Automatisation, déploiement et IaC

## 🎯 Problème précis à résoudre
Configurer Git sur un poste d'administration Debian 12 (identité, clé SSH, branches), puis héberger un dépôt nu de sauvegarde sur un serveur Linux accessible en SSH. La procédure ne couvre pas GitHub (SaaS).

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de Git et vérification de la version :
```bash
sudo apt update
sudo apt install -y git openssh-client
git --version
```
👉 Explication : Installe Git et le client SSH. `git --version` confirme la version installée.

2. Identité et paramètres locaux :
```bash
git config --global user.name "<prenom_nom>"
git config --global user.email "<adresse_courriel>"
git config --global init.defaultBranch main
git config --global --list
```
👉 Explication : L'identité est enregistrée dans chaque commit. `init.defaultBranch main` crée la branche `main` par défaut. `git config --global --list` affiche le résultat.

3. Création d'un dépôt de test et premier commit :
```bash
mkdir -p ~/lab-git && cd ~/lab-git
git init
echo "Fiche de test" > README.md
git add README.md
git commit -m "Premier commit de test"
git log --oneline
```
👉 Explication : Crée un dépôt local, ajoute un fichier, valide un commit et affiche l'historique.

4. Branche de travail, puis fusion dans `main` :
```bash
git switch -c correctif-lab
echo "Ligne ajoutée" >> README.md
git commit -am "Ajout d'une ligne"
git switch main
git merge correctif-lab
git branch
```
👉 Explication : Crée la branche `correctif-lab`, y valide une modification, revient sur `main` et fusionne. `git branch` affiche la branche active marquée d'un `*`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Génération d'une clé SSH dédiée à l'administrateur :
```bash
ssh-keygen -t ed25519 -C "<adresse_courriel>" -f ~/.ssh/id_ed25519_git
ssh-add ~/.ssh/id_ed25519_git
cat ~/.ssh/id_ed25519_git.pub
```
👉 Explication : Crée une paire de clés Ed25519. La clé publique (`.pub`) est déposée sur le serveur de dépôt, la clé privée ne quitte jamais le poste. Une passphrase est recommandée.

2. Création du dépôt nu de sauvegarde sur le serveur (Debian 12) :
```bash
sudo adduser --disabled-password --gecos "" gitbackup
sudo mkdir -p /srv/git/<nom_depot>.git
sudo chown -R gitbackup:gitbackup /srv/git
sudo -u gitbackup git init --bare /srv/git/<nom_depot>.git
```
👉 Explication : Crée un utilisateur dédié sans mot de passe, puis un dépôt nu (`--bare`) qui ne contient que l'historique, sans copie de travail. Le chemin `/srv/git` est un choix de cette fiche.

3. Autorisation de la clé publique pour cet utilisateur :
```bash
sudo install -d -m 700 -o gitbackup -g gitbackup /home/gitbackup/.ssh
echo "<ligne_cle_publique>" | sudo tee -a /home/gitbackup/.ssh/authorized_keys
sudo chown gitbackup:gitbackup /home/gitbackup/.ssh/authorized_keys
sudo chmod 600 /home/gitbackup/.ssh/authorized_keys
```
👉 Explication : Ajoute la clé publique du poste dans `authorized_keys`. Remplacer `<ligne_cle_publique>` par le contenu de `id_ed25519_git.pub`. Droits stricts exigés par SSH.

4. Ajout du dépôt distant et envoi de la branche `main` :
```bash
cd ~/lab-git
git remote add sauvegarde gitbackup@<adresse_serveur>:/srv/git/<nom_depot>.git
git push -u sauvegarde main
```
👉 Explication : Déclare le serveur comme dépôt distant nommé `sauvegarde`, puis pousse `main`. `-u` mémorise la branche de suivi.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Accès SSH réservé au compte de sauvegarde, sans mot de passe :
```bash
sudo nano /etc/ssh/sshd_config.d/gitbackup.conf
```
Contenu, à adapter :
```
Match User gitbackup
    PasswordAuthentication no
    AllowTcpForwarding no
    X11Forwarding no
    PermitTTY no
```
```bash
sudo sshd -t
sudo systemctl restart ssh
```
👉 Explication : Pour `gitbackup`, bloque mot de passe, redirections et terminal interactif. Git ne demande qu'un transfert de dépôt. `sshd -t` valide la syntaxe avant de relancer le service. Le nom du service SSH est `ssh` sur Debian 12.

2. Restriction du compte à la commande Git uniquement :
```bash
sudo nano /home/gitbackup/.ssh/authorized_keys
```
Préfixer la ligne de clé par :
```
command="git-shell",no-port-forwarding,no-agent-forwarding,no-pty <ligne_cle_publique>
```
👉 Explication : `git-shell` limite la session aux commandes Git (pousser et tirer), sans shell interactif. Les options `no-*` coupent les tunnels. Cette restriction est à tester sur un clone avant mise en service.

3. Protection des branches de référence sur le dépôt de sauvegarde :
```bash
sudo -u gitbackup git -C /srv/git/<nom_depot>.git config receive.denyNonFastForwards true
sudo -u gitbackup git -C /srv/git/<nom_depot>.git config receive.denyDeletes true
```
👉 Explication : Refuse les réécritures d'historique (`push --force`) et la suppression de branches sur le dépôt de sauvegarde. Les sauvegardes restent ainsi intactes.

4. Vérification de l'intégrité du dépôt de sauvegarde :
```bash
sudo -u gitbackup git -C /srv/git/<nom_depot>.git fsck --full
```
👉 Explication : Contrôle les objets du dépôt. Une sortie vide ou sans erreur est attendue. Toute erreur est à remonter immédiatement.

---