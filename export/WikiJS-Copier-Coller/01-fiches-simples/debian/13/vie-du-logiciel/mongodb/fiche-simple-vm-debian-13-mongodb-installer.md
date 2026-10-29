# Fiche_Simple_-_VM_Debian_13_MongoDB_Installer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MongoDB Community (dépôt officiel)
- **Catégorie** : base de données / MongoDB / Installer

---

## Problème précis à résoudre

Installer MongoDB Community depuis le dépôt officiel avec clé signée.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les prérequis et la clé du dépôt :
   ```bash
   sudo apt install -y gnupg curl
   curl -fsSL https://www.mongodb.org/static/pgp/server-VERSION.asc | sudo gpg --dearmor -o /usr/share/keyrings/mongodb-server-VERSION.gpg
   ```
   👉 Explication : remplacer `VERSION` par la série visée (ex. 8.0, à vérifier) ; contrôler l'empreinte publiée par l'éditeur.

2. Déclarer le dépôt :
   ```bash
   echo 'deb [signed-by=/usr/share/keyrings/mongodb-server-VERSION.gpg] http://repo.mongodb.org/apt/debian CODENAME_SUPPORTE/mongodb-org/VERSION main' | sudo tee /etc/apt/sources.list.d/mongodb-org-VERSION.list
   ```
   👉 Explication : remplacer `CODENAME_SUPPORTE` par le nom de distribution indiqué dans la documentation officielle (à vérifier pour Debian 13).

3. Installer :
   ```bash
   sudo apt update
   apt-cache policy mongodb-org
   sudo apt install -y mongodb-org
   ```
   👉 Explication : le méta-paquet installe serveur, shell et outils de sauvegarde.

4. Activer et vérifier :
   ```bash
   sudo systemctl enable --now mongod
   systemctl status mongod --no-pager
   mongod --version
   ```
   👉 Explication : service actif ; écoute loopback par défaut.

5. Figer la version :
   ```bash
   echo 'mongodb-org hold' | sudo dpkg --set-selections
   ```
   👉 Explication : évite une mise à jour involontaire (recommandé par l'éditeur).

## 2. Production — Contrôles

Consigner version, origine, empreinte de la clé et politique de mise à jour.

## 3. Production — Sécurité

- Ne jamais installer sans vérifier la clé.
- Ne pas ouvrir le port 27017 avant la sécurisation.
- Désactiver Transparent Huge Pages selon les recommandations éditeur.

## Validation et retour arrière

- **Validation** : `mongod --version` et `systemctl is-active mongod` confirment l'installation.
- **Retour arrière** : `sudo apt purge mongodb-org*` après sauvegarde de `/var/lib/mongodb` ; supprimer la liste de dépôt.

## Si le problème n'est pas résolu

- [MongoDB — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-prerequis-limites)
- [MongoDB — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-configurer)
- [MongoDB — Sécuriser (authentification, TLS, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-securiser)
- [MongoDB — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-valider)
- [MongoDB — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-sauvegarder-restaurer)
- [MongoDB — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-mettre-a-jour)
- [MongoDB — installation sous Debian](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/)
- [MongoDB — sécurité](https://www.mongodb.com/docs/manual/security/)