# 📄 Fiche_Simple_-_Hote_Docker_Securite_Activer_Mode_Rootless.md

- **Environnement** : Hôte Docker Debian 12 ou Ubuntu 24.04
- **OS / Version** : Debian 12 / Ubuntu 24.04 LTS avec Docker Engine officiel déjà installé
- **Catégorie** : Sécurité / Conteneurs

## 🎯 Problème précis à résoudre
Exécuter le démon Docker sous un compte utilisateur non privilégié avec le mode rootless, sans donner à ce compte l'accès au socket système rootful.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Depuis un compte utilisateur dédié, vérifier les prérequis et les outils :
   ```bash
   sudo apt update
   sudo apt install uidmap dbus-user-session slirp4netns docker-ce-rootless-extras
   ```
2. Installer le démon utilisateur et lancer un conteneur de test :
   ```bash
   dockerd-rootless-setuptool.sh install
   systemctl --user enable --now docker
   docker run --rm hello-world
   ```
   👉 *Explication : Ces commandes doivent être exécutées dans la session du compte qui exploitera Docker, pas dans un shell root.*

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier qu'un moteur Docker compatible et les prérequis rootless sont installés :
   ```bash
   command -v dockerd-rootless-setuptool.sh
   systemctl --user is-active docker
   ```
2. Installer et activer le service utilisateur :
   ```bash
   dockerd-rootless-setuptool.sh install
   systemctl --user enable --now docker
   sudo loginctl enable-linger "$USER"
   ```
3. Valider que le client utilise bien le démon rootless :
   ```bash
   docker context ls
   docker info --format '{{json .SecurityOptions}}'
   ```
   👉 *Explication : Le contexte rootless doit être sélectionné et les options de sécurité doivent inclure `rootless`.*

## 🔒 3. Production — Façon Sécurisée
1. Utiliser un compte dédié à l'exploitation et éviter son ajout au groupe `docker` du démon système : ce groupe permet généralement un contrôle équivalent à root.
2. Ne pas exposer le socket rootless sur TCP sans authentification et filtrage adaptés. Limiter les montages hôte et les capacités des conteneurs selon leur besoin.
3. Rootless réduit les privilèges du démon, mais ne remplace ni les mises à jour, ni l'isolation d'une VM pour des charges non fiables. Vérifier les limites réseau et de stockage avant migration.

## ✅ Validation et retour arrière
- Confirmer le contexte avec `docker context ls`, l'état avec `systemctl --user status docker` et l'option `rootless` dans `docker info`.
- Pour revenir au démon système, arrêter le service utilisateur et exécuter `dockerd-rootless-setuptool.sh uninstall` depuis le compte concerné; vérifier ensuite le contexte Docker utilisé.
- Ne désactiver le mode linger qu'après avoir confirmé qu'aucun service utilisateur ne dépend du démon : `sudo loginctl disable-linger "$USER"`.

## 🔗 Si le problème n'est pas résolu
- Vérifier les prérequis de l'installation Docker et les journaux avec `journalctl --user -u docker`.