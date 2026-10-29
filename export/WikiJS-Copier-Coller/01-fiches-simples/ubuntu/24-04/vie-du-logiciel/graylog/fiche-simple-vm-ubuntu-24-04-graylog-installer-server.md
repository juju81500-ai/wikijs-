# Fiche_Simple_-_VM_Ubuntu_24.04_Graylog_Installer_Server.md

- **Environnement** : Ubuntu Server 24.04: nœud Graylog + MongoDB et Data Node (laboratoire)
- **OS / Version** : Ubuntu Server 24.04 LTS; Graylog 7.2; MongoDB 8.0
- **Catégorie** : journaux / installation

---

## Problème précis à résoudre

Installer et configurer Graylog Server.

## 1. Hors-Production (Lab / Test / POC)

1. Installer le dépôt Graylog 7.2 puis le paquet :
   ```bash
   sudo apt update
   sudo apt install graylog-server
   ```
   👉 Explication : installe le serveur.

2. Calculer le hash SHA-256 du secret administrateur sans l'écrire en clair dans l'historique :
   ```bash
   read -r -s -p 'Mot de passe admin : ' PW; echo; printf '%s' "$PW" | sha256sum | cut -d' ' -f1; unset PW
   ```
   👉 Explication : `read -s` masque la saisie; le résultat va dans `root_password_sha2`.

3. Éditer `/etc/graylog/server/server.conf` :
   ```bash
   sudoedit /etc/graylog/server/server.conf
   ```
   👉 Explication : renseigner `password_secret`, `root_password_sha2`, l'URI MongoDB authentifiée et l'adresse d'écoute limitée à l'interface interne.

4. Activer le service et lire l'état et le journal :
   ```bash
   sudo systemctl enable --now graylog-server
   sudo systemctl --no-pager status graylog-server
   sudo journalctl -u graylog-server -b --no-pager
   ```
   👉 Explication : la JVM vaut environ la moitié de la RAM, jusqu'à 16 Go.

## 2. Production — Contrôles

Dimensionner le journal d'entrée et la JVM.

## 3. Production — Sécurité

- Ne jamais passer le mot de passe en argument de commande.

## Validation et retour arrière

- **Validation** : `graylog-server` actif sans erreur dans le journal.
- **Retour arrière** : `sudo systemctl disable --now graylog-server`; restaurer l'ancien `server.conf`.

## Si le problème n'est pas résolu

- [Graylog 7.2 — installation Ubuntu](https://go2docs.graylog.org/current/downloading_and_installing_graylog/ubuntu_installation.htm)
- [Graylog — sécuriser l'environnement](https://go2docs.graylog.org/current/planning_your_deployment/secure_your_graylog_environment.htm)
- [Guide complet Graylog Ubuntu 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/49-deploiement-graylog-7-2-ubuntu-24-04#5-installer-graylog-server)