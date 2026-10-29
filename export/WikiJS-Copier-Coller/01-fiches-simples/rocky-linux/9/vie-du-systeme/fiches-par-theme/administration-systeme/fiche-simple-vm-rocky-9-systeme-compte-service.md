# 📄 Fiche_Simple_-_VM_Rocky_9_Systeme_Compte_Service.md

- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9 avec systemd et SELinux
- **Catégorie** : Système & Services / Isolation des comptes de service

## 🎯 Problème précis à résoudre
Créer un compte système sans shell interactif pour exécuter un service sous Rocky Linux 9, avec un répertoire de données dédié et des droits limités, puis lancer ce service avec systemd sous ce compte.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Créer le compte système :
   ```bash
   sudo useradd -r -M -d /var/lib/<service_user> -s /usr/sbin/nologin <service_user>
   ```
   👉 Explication : `-r` attribue un UID de compte système (inférieur à 1000), `-M` ne crée pas de répertoire personnel, `-s /usr/sbin/nologin` interdit toute ouverture de session interactive.

2. Vérifier le compte créé :
   ```bash
   id <service_user>
   getent passwd <service_user>
   ```
   👉 Explication : Le shell affiché doit être `/usr/sbin/nologin` et l'UID doit être inférieur à 1000.

---

## ⚡ 2. Production — Façon Simplifiée
1. Créer le répertoire de données appartenant au compte de service :
   ```bash
   sudo install -d -o <service_user> -g <service_user> -m 0750 /var/lib/<service_user>
   ```
   👉 Explication : `install -d` crée le répertoire avec propriétaire, groupe et droits explicites. Le mode `0750` ferme l'accès aux autres utilisateurs.

2. Déclarer le service systemd avec ce compte. Créer `/etc/systemd/system/<nom_du_service>.service` :
   ```ini
   [Unit]
   Description=<description_du_service>
   After=network-online.target
   Wants=network-online.target

   [Service]
   User=<service_user>
   Group=<service_user>
   ExecStart=<chemin_executable> <arguments>
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
   ```
   👉 Explication : Les directives `User=` et `Group=` font tourner le processus sous le compte de service. `Restart=on-failure` relance le service en cas d'arrêt anormal.

3. Recharger systemd, activer le service et vérifier le compte d'exécution :
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable --now <nom_du_service>
   ps -o user,pid,comm -u <service_user>
   ```
   👉 Explication : `ps` doit lister le processus du service avec l'utilisateur `<service_user>`, et non `root`.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Ajouter un durcissement dans la section `[Service]` de l'unité :
   ```ini
   NoNewPrivileges=yes
   PrivateTmp=yes
   ProtectSystem=strict
   ProtectHome=yes
   ReadWritePaths=/var/lib/<service_user>
   ```
   👉 Explication : `NoNewPrivileges` interdit l'élévation de privilèges, `ProtectSystem=strict` rend le système de fichiers en lecture seule sauf les chemins listés dans `ReadWritePaths`.

2. Vérifier le score de sécurité de l'unité après modification :
   ```bash
   sudo systemctl daemon-reload
   systemd-analyze security <nom_du_service>
   ```
   👉 Explication : Affiche les protections appliquées et celles qui manquent. Un score bas indique des directives de durcissement à ajouter.

3. Contrôler que le compte n'a aucun droit sudo ni appartenance au groupe `wheel` :
   ```bash
   sudo -l -U <service_user>
   id -nG <service_user>
   ```
   👉 Explication : `sudo -l -U` doit afficher que l'utilisateur ne peut exécuter aucune commande. Les groupes ne doivent pas contenir `wheel`.

---

## ✅ Contrôle
```bash
ls -ld /var/lib/<service_user>
```
👉 Explication : Le propriétaire et le groupe doivent être `<service_user>` et le mode `drwxr-x---`.