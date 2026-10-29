# 📄 Fiche_Simple_-_VM_Debian_13_Services_Creer_Service_Systemd_Durci.md

- **Environnement** : VM ou serveur Debian 13
- **OS / Version** : Debian 13 (Trixie) avec systemd
- **Catégorie** : Services / Administration

## 🎯 Problème précis à résoudre
Créer une unité systemd pour une application déjà installée, l'exécuter sous un compte dédié non privilégié et limiter ses accès en écriture.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Créer un compte système et un répertoire de données pour l'application :
   ```bash
   sudo useradd --system --no-create-home --shell /usr/sbin/nologin monapp
   sudo install -d -o monapp -g monapp -m 0750 /var/lib/monapp
   ```
2. Créer `/etc/systemd/system/monapp.service` en adaptant les chemins à une application réellement installée :
   ```ini
   [Unit]
   Description=Application monapp
   After=network.target

   [Service]
   Type=simple
   User=monapp
   Group=monapp
   ExecStart=/usr/local/bin/monapp --config /etc/monapp/config.yml
   Restart=on-failure
   NoNewPrivileges=true
   PrivateTmp=true
   ProtectSystem=strict
   ProtectHome=true
   ReadWritePaths=/var/lib/monapp

   [Install]
   WantedBy=multi-user.target
   ```
3. Vérifier puis lancer le service :
   ```bash
   sudo systemd-analyze verify /etc/systemd/system/monapp.service
   sudo systemctl daemon-reload
   sudo systemctl start monapp
   sudo systemctl status monapp --no-pager
   ```
   👉 *Explication : `ExecStart` doit viser le vrai exécutable. Adapter les chemins modifiables avant d'activer l'unité au démarrage.*

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier le propriétaire du binaire, les fichiers de configuration et les répertoires dont l'application a besoin.
2. Installer le fichier d'unité avec les protections compatibles avec l'application, puis valider et activer :
   ```bash
   sudo systemd-analyze verify /etc/systemd/system/monapp.service
   sudo systemctl daemon-reload
   sudo systemctl enable --now monapp
   sudo journalctl -u monapp -n 50 --no-pager
   ```
3. Confirmer le compte d'exécution et le résultat fonctionnel du service :
   ```bash
   systemctl show monapp -p User -p Group -p ActiveState -p SubState
   ```

## 🔒 3. Production — Façon Sécurisée
1. Remplacer les noms d'exemple par un compte et des répertoires dédiés à l'application; ne pas lancer un service métier en root par défaut.
2. N'ajouter `ReadWritePaths` que pour les répertoires nécessaires. Tester chaque directive de durcissement, car une application peut dépendre de chemins spécifiques.
3. Ne pas utiliser `chmod 777` pour résoudre un refus; examiner `journalctl` et les permissions effectives.

## ✅ Validation et retour arrière
- Vérifier le statut, les journaux, le compte de processus et un test fonctionnel de l'application.
- Pour revenir en arrière, arrêter et désactiver l'unité, sauvegarder puis retirer son fichier, exécuter `systemctl daemon-reload` et redémarrer l'ancien mécanisme si nécessaire.
- Conserver l'ancien mode de lancement jusqu'à validation du nouveau service.