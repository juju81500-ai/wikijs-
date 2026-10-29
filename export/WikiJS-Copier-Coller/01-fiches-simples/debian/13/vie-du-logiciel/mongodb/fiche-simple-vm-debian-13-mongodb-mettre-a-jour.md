# Fiche_Simple_-_VM_Debian_13_MongoDB_Mettre_A_Jour

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MongoDB Community (dépôt officiel)
- **Catégorie** : base de données / MongoDB / Mise à jour et retour arrière

---

## Problème précis à résoudre

Mettre à jour MongoDB avec retour arrière fondé sur sauvegarde et instantané.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder :
   ```bash
   mongodump --uri='mongodb://ADMIN_DB@NOM_SERVEUR:27017/?authSource=admin&tls=true&tlsCAFile=/chemin/CA.crt' --gzip --archive=/var/backups/mongodb/avant-maj-$(date +%F).archive.gz
   sudo tar -czpf /var/backups/mongodb/conf-$(date +%F).tar.gz /etc/mongod.conf /etc/mongodb
   ```
   👉 Explication : ajouter un instantané de VM.

2. Consulter la compatibilité :
   ```bash
   mongosh --eval 'db.adminCommand({getParameter:1, featureCompatibilityVersion:1})'
   ```
   👉 Explication : relever la `featureCompatibilityVersion` ; une montée majeure se fait une série à la fois et se teste sur copie.

3. Appliquer une mise à jour de correctif :
   ```bash
   sudo apt-mark unhold mongodb-org 2>/dev/null; echo 'mongodb-org install' | sudo dpkg --set-selections
   sudo apt update && sudo apt install --only-upgrade mongodb-org
   sudo systemctl restart mongod
   echo 'mongodb-org hold' | sudo dpkg --set-selections
   ```
   👉 Explication : lever puis remettre le blocage ; vérifier avec `mongod --version`.

4. Retour arrière :
   ```bash
   sudo systemctl stop mongod
   # restaurer l'instantané de VM, ou sur une VM saine :
   mongorestore --gzip --archive=/var/backups/mongodb/avant-maj-DATE.archive.gz
   ```
   👉 Explication : le retour de version en place n'est pas garanti après une montée de `featureCompatibilityVersion` : privilégier l'instantané. Remplacer `DATE` (à remplacer).

## 2. Production — Contrôles

Pilote d'abord, fenêtre approuvée, instantané préalable, surveillance du journal ensuite ; ne relever la FCV qu'après validation.

## 3. Production — Sécurité

- Ne pas relever la FCV avant la validation complète.
- Conserver les sauvegardes.
- Prévenir les applications.

## Validation et retour arrière

- **Validation** : `mongod --version` affiche la version cible et les applications fonctionnent.
- **Retour arrière** : restaurer l'instantané ou la sauvegarde.

## Si le problème n'est pas résolu

- [MongoDB — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-prerequis-limites)
- [MongoDB — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-installer)
- [MongoDB — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-configurer)
- [MongoDB — Sécuriser (authentification, TLS, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-securiser)
- [MongoDB — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-valider)
- [MongoDB — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-sauvegarder-restaurer)
- [MongoDB — installation sous Debian](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/)
- [MongoDB — sécurité](https://www.mongodb.com/docs/manual/security/)