# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Systeme_Compte_Service

- **Environnement** : VM Ubuntu Server
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat)
- **Catégorie** : Système / Comptes de service et isolation
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[useradd]`, `[nologin]`, `[systemd]`, `[service-account]`, `[hardening]`

## 🎯 Problème précis à résoudre
Créer un compte système sans session interactive pour exécuter un service sur Ubuntu Server 24.04 LTS, limiter ses droits sur ses répertoires et le faire tourner depuis une unité systemd dédiée.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier qu'un compte portant le même nom n'existe pas déjà :
   ```bash
   getent passwd <compte_service>
   ```
   👉 *Explication : Si la commande ne renvoie rien, le compte peut être créé. Un résultat existant impose de choisir un autre nom.*
2. Créer le compte système sans shell de connexion :
   ```bash
   sudo useradd --system --no-create-home --shell /usr/sbin/nologin <compte_service>
   getent passwd <compte_service>
   ```
   👉 *Explication : `--system` attribue un UID inférieur à 1000 ; `/usr/sbin/nologin` refuse toute connexion interactive, même avec un mot de passe valide.*

## ⚡ 2. Production — Façon Simplifiée
1. Créer le répertoire de données propre au service et limiter les droits :
   ```bash
   sudo install -d -o <compte_service> -g <compte_service> -m 0750 /var/lib/<service>
   ls -ld /var/lib/<service>
   ```
   👉 *Explication : Le compte de service est le seul propriétaire ; les autres comptes n'ont aucun accès.*
2. Vérifier qu'aucun mot de passe n'est défini pour le compte :
   ```bash
   sudo passwd -S <compte_service>
   ```
   👉 *Explication : Le statut `L` indique un compte verrouillé ; c'est l'état attendu pour un compte de service.*

## 🔒 3. Production — Façon Sécurisée
1. Déclarer le service avec son propre utilisateur et des restrictions systemd :
   ```bash
   sudo install -o root -g root -m 0644 /dev/null /etc/systemd/system/<service>.service
   sudo tee /etc/systemd/system/<service>.service >/dev/null <<'EOF'
   [Unit]
   Description=<description_du_service>
   After=network-online.target
   Wants=network-online.target

   [Service]
   User=<compte_service>
   Group=<compte_service>
   ExecStart=<chemin_du_binaire> <arguments>
   Restart=on-failure
   NoNewPrivileges=yes
   ProtectSystem=strict
   ProtectHome=yes
   PrivateTmp=yes
   ReadWritePaths=/var/lib/<service>

   [Install]
   WantedBy=multi-user.target
   EOF
   sudo systemctl daemon-reload
   sudo systemd-analyze verify /etc/systemd/system/<service>.service
   ```
   👉 *Explication : `ProtectSystem=strict` rend le système de fichiers en lecture seule sauf les chemins listés ; `systemd-analyze verify` signale les erreurs de syntaxe avant tout démarrage.*
2. Démarrer le service et contrôler le compte réellement utilisé :
   ```bash
   sudo systemctl enable --now <service>
   ps -o user,pid,cmd -C <nom_du_binaire>
   ```
   👉 *Explication : La première colonne doit afficher `<compte_service>`, et non `root`.*

## ✅ Validation et retour arrière
- Tenter une session avec `sudo -u <compte_service> -i` ; le shell `nologin` doit refuser la session et afficher « This account is currently not available. ».
- Retour arrière : `sudo systemctl disable --now <service>`, `sudo rm /etc/systemd/system/<service>.service`, `sudo systemctl daemon-reload`, puis `sudo userdel <compte_service>`.
