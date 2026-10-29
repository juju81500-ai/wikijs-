# 📄 VM_Debian_13_Securite_Configuration-Sudo-Chroot-Restreint.md

- **Environnement** : VM / LXC (Debian 13)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Sécurité & Privilèges / Sudoers
- **Tags** : `[debian13]`, `[sudo]`, `[security]`, `[privileges]`, `[hardening]`

## 🎯 Problème précis à résoudre
Administrer les règles de privilèges `sudo` sous Debian 13, autoriser des commandes ciblées pour les techniciens d'exploitation et bloquer l'évasion de shell.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du paquet sudo :
   `apt-get update && apt-get install -y sudo`
   👉 Explication : Télécharge et installe le gestionnaire de privilèges sudo.

2. Ajout rapide d'un utilisateur au groupe sudo :
   `usermod -aG sudo user_test`
   👉 Explication : Accorde l'élévation administrative globale à l'utilisateur de test.

3. Test de validation des privilèges :
   `sudo -u user_test sudo whoami`
   👉 Explication : Confirme que l'utilisateur peut exécuter des commandes en tant que root.

---

## ⚡ 2. Production — Façon Simplifiée
1. Éditer le fichier avec `visudo`, sans écraser d'autres règles :
   `sudo visudo -f /etc/sudoers.d/tssr-operators`
2. N'autoriser que les actions nécessaires sur le service précis :
   ```sudoers
   %tssr-ops ALL=(root) /usr/bin/systemctl restart nginx, /usr/bin/systemctl status nginx
   ```
   👉 Explication : Éviter les jokers d'unités et arguments. Une règle sudoers ne doit pas être considérée comme un bac à sable pour commandes complexes.
3. Contrôler la syntaxe globale et tester avec un compte non privilégié :
   ```bash
   sudo visudo -c
   sudo -l -U user_test
   ```

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Ajouter les options globales avec `visudo -f /etc/sudoers.d/00-global-hardening` sans remplacer un fichier existant :
   ```sudoers
   Defaults use_pty
   Defaults logfile="/var/log/sudo.log"
   ```
   👉 Explication : Force l'exécution des commandes dans un PTY dédié et journalise toutes les actions sudoers.

2. Ne pas s'appuyer sur `NOEXEC` comme barrière universelle contre l'évasion de shell. Pour consulter les journaux, préférer des droits de lecture dédiés et éviter de donner un shell privilégié à `less` ou à un outil interactif.

3. Consulter les événements sudo disponibles dans le journal système :
   `sudo journalctl _COMM=sudo --since today`
   👉 Explication : Le nom d'unité `sudo.service` n'existe pas nécessairement ; vérifier l'intégration syslog/journald de la distribution.