# 📄 Ansible

- **Environnement** : VM Debian 13 (nœud de contrôle Ansible) et hôtes cibles joignables en SSH
- **OS / Version** : Debian 13 (Trixie) - Famille Debian / Ansible (paquet Debian 13, version à relever avec `ansible --version`, à vérifier sur la version déployée)
- **Catégorie** : Automatisation, déploiement et IaC

## 🎯 Problème précis à résoudre
Installer Ansible sur un nœud de contrôle Debian 13, vérifier sa version, joindre des hôtes cibles en SSH, puis lancer un premier playbook en simulation (`--check`) avant toute modification. Le parcours sécurisé isole le compte d'automatisation, utilise une clé SSH dédiée et chiffre les secrets avec Ansible Vault.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation d'Ansible depuis les dépôts Debian 13 :
   ```bash
   sudo apt update && sudo apt install -y ansible
   ```
   👉 Explication : Installe le paquet Ansible officiel de Debian 13 et ses dépendances Python.

2. Relevé de la version installée :
   ```bash
   ansible --version
   ```
   👉 Explication : Affiche la version d'Ansible (à noter dans la documentation) et le fichier de configuration utilisé. Version à vérifier sur la version déployée.

3. Test du moteur sur la machine locale :
   ```bash
   ansible localhost -m ping
   ```
   👉 Explication : Valide le fonctionnement du moteur en utilisant la connexion locale. Aucun hôte distant n'est sollicité ; un avertissement sur l'absence d'inventaire est normal.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création d'un répertoire de projet dédié :
   ```bash
   mkdir -p ~/ansible-projet
   ```
   👉 Explication : Garde l'inventaire et les playbooks hors de `/etc/ansible/hosts`, pour que le projet soit versionnable et séparé du système.

2. Création de l'inventaire des hôtes cibles :
   ```bash
   nano ~/ansible-projet/inventaire.ini
   ```
   Contenu du fichier :
   ```ini
   [serveurs_linux]
   <nom_de_l_hote> ansible_host=<adresse_ip_serveur> ansible_user=<utilisateur_cible>
   ```
   👉 Explication : `<nom_de_l_hote>` est le nom logique du serveur dans Ansible, `<adresse_ip_serveur>` son adresse joignable et `<utilisateur_cible>` le compte SSH utilisé. Ajouter une ligne par serveur du groupe.

3. Test de joignabilité de l'inventaire :
   ```bash
   ansible serveurs_linux -i ~/ansible-projet/inventaire.ini -m ping
   ```
   👉 Explication : Vérifie que chaque hôte du groupe répond. Un échec indique un problème de clé SSH, d'adresse ou de nom d'utilisateur.

4. Playbook minimal en simulation. Créer le fichier `~/ansible-projet/ping.yml` contenant :
   ```yaml
   - name: Verification de la connexion
     hosts: serveurs_linux
     tasks:
       - name: Test ping Ansible
         ansible.builtin.ping:
   ```
   puis lancer :
   ```bash
   ansible-playbook -i ~/ansible-projet/inventaire.ini ~/ansible-projet/ping.yml --check
   ```
   👉 Explication : Exécute le playbook sans modifier les serveurs grâce à `--check`. Ce mode est le réflexe à garder avant tout playbook qui change l'état d'une machine.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Création d'un compte dédié et sans mot de passe utilisable sur le nœud de contrôle :
   ```bash
   sudo useradd -m -s /bin/bash ansible-admin && sudo passwd -l ansible-admin
   ```
   👉 Explication : Isole l'automatisation hors du compte `root`. Le mot de passe est verrouillé, l'accès se fait uniquement par clé SSH.

2. Préparation du dossier SSH du compte dédié et génération d'une clé ED25519 protégée par phrase secrète :
   ```bash
   sudo install -d -m 700 -o ansible-admin -g ansible-admin /home/ansible-admin/.ssh && sudo -iu ansible-admin ssh-keygen -t ed25519 -a 100 -C "ansible-controle-debian13" -f /home/ansible-admin/.ssh/id_ansible
   ```
   👉 Explication : Crée un dossier `.ssh` réservé au compte, puis génère la paire de clés. Saisir une phrase secrète forte ; pour les sessions interactives, utiliser `ssh-agent`. Les automatisations non interactives doivent suivre une gestion de secret documentée.

3. Déploiement de la clé publique sur chaque hôte cible :
   ```bash
   sudo -iu ansible-admin ssh-copy-id -i /home/ansible-admin/.ssh/id_ansible.pub <utilisateur_cible>@<adresse_ip_serveur>
   ```
   👉 Explication : Copie uniquement la clé publique dans le compte `<utilisateur_cible>` de l'hôte `<adresse_ip_serveur>`. Vérifier l'empreinte affichée de l'hôte avant de l'accepter.

4. Création du projet du compte dédié et chiffrement des secrets avec Ansible Vault :
   ```bash
   sudo -iu ansible-admin mkdir -p /home/ansible-admin/ansible-projet && sudo -iu ansible-admin ansible-vault create /home/ansible-admin/ansible-projet/secrets.yml
   ```
   👉 Explication : Crée le fichier `secrets.yml` chiffré en AES-256 pour les mots de passe et jetons. Le mot de passe Vault ne doit jamais être stocké dans le dépôt de code.

5. Restriction des permissions sur la clé privée et les secrets :
   ```bash
   sudo chmod 700 /home/ansible-admin/.ssh && sudo chmod 600 /home/ansible-admin/.ssh/id_ansible && sudo chmod 600 /home/ansible-admin/ansible-projet/secrets.yml
   ```
   👉 Explication : Seul le compte `ansible-admin` peut lire la clé privée et le fichier de secrets. Ne pas modifier le fichier `/etc/ansible/ansible.cfg` sans relecture de la politique de l'équipe.

6. Test final sous le compte dédié (inventaire copié dans le répertoire de `ansible-admin`) :
   ```bash
   sudo -iu ansible-admin ansible serveurs_linux -i /home/ansible-admin/ansible-projet/inventaire.ini -m ping
   ```
   👉 Explication : Valide que le compte dédié atteint les hôtes avec sa clé. Le contrôle de vérification des clés d'hôte doit rester actif (valeur par défaut d'Ansible, à vérifier sur la version déployée).