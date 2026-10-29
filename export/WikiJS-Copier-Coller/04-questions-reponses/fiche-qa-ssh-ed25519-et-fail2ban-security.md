# Sécuriser un accès OpenSSH avec clés ED25519 et Fail2ban

### ❓ Question
Comment réduire les tentatives de connexion SSH sans perdre l'accès d'administration ?

---

### 📋 Procédure Pas-à-Pas (1 Commande = 1 Explication Technique)

1. **Générer une paire de clés sur le poste client** :
   ```bash
   ssh-keygen -t ed25519 -C "admin@lab.local"
   ```
   👉 *Explication : La clé privée reste sur le poste client. La protéger par une phrase secrète et ne jamais la copier sur le serveur.*

2. **Copier la clé publique sur le serveur distant** :
   ```bash
   ssh-copy-id -i ~/.ssh/id_ed25519.pub user@192.168.1.50
   ```
   👉 *Explication : Tu injectes ta clé publique dans le fichier `~/.ssh/authorized_keys` du serveur cible.*

3. **Garder une session et une console de secours ouvertes**, sauvegarder la configuration et vérifier les valeurs effectives :
   ```bash
   sudo sshd -t
   sudo sshd -T | grep -E '^(port|permitrootlogin|passwordauthentication|pubkeyauthentication) '
   ```
   👉 *Explication : Les fichiers inclus peuvent rendre un fichier `99-...` inefficace. Ne pas changer le port sans règle réseau correspondante.*

4. **Désactiver le mot de passe seulement après validation d'une seconde connexion par clé**. Modifier un seul fichier géré, puis vérifier et recharger :
   ```bash
   sudo sshd -t && sudo systemctl reload ssh
   ```
   👉 *Explication : Le test détecte une erreur de syntaxe avant application. Garder la session de secours jusqu'à connexion réussie dans un nouveau terminal.*

5. **Installer et activer Fail2ban après vérification de la source de journaux** :
   ```bash
   sudo apt install fail2ban
   systemctl enable --now fail2ban
   ```
   👉 *Explication : Le backend de journaux dépend du système. Vérifier l'état et les journaux Fail2ban, puis tester depuis une adresse autorisée avant d'appliquer une politique de bannissement stricte.*

---

### ⚙️ Matrice des 3 Modes d'Exécution

| Mode | Authentification SSH | Protection Réseau |
| :--- | :--- | :--- |
| **🧪 Hors-Prod** | Tester d'abord la clé sans désactiver l'accès existant. | Règles réseau de laboratoire. |
| **⚡ Production** | Clé vérifiée, compte nominatif, accès root direct interdit selon la politique. | Fail2ban configuré et testé. |
| **🔒 Production renforcée** | Accès limité aux comptes/groupes et algorithmes supportés par OpenSSH local. | Filtrage persistant, supervision et console de secours. |