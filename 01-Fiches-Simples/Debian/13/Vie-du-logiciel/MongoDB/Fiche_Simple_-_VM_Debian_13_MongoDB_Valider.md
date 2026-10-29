# Fiche_Simple_-_VM_Debian_13_MongoDB_Valider

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MongoDB Community (dépôt officiel)
- **Catégorie** : base de données / MongoDB / Valider (recette)
- **Tags** : `debian13`, `mongodb`, `recette`

---

## Problème précis à résoudre

Prouver que MongoDB est opérationnel, authentifié et chiffré.

## 1. Hors-Production (Lab / Test / POC)

1. État du service et écoute :
   ```bash
   systemctl is-active mongod
   sudo ss -tlnp | grep mongod
   ```
   👉 Explication : écoute sur les adresses prévues seulement.

2. Refus sans authentification :
   ```bash
   mongosh --eval 'db.getSiblingDB("admin").getUsers()'
   ```
   👉 Explication : la commande doit retourner `Unauthorized`.

3. Connexion authentifiée avec TLS :
   ```bash
   mongosh 'mongodb://ADMIN_DB@NOM_SERVEUR:27017/admin?tls=true&tlsCAFile=/chemin/CA.crt' --eval 'db.runCommand({ping:1})'
   ```
   👉 Explication : le mot de passe est demandé ; remplacer `ADMIN_DB`, `NOM_SERVEUR`, le chemin de l'AC (à remplacer).

4. Écriture de test :
   ```bash
   mongosh 'mongodb://APPUSER@NOM_SERVEUR:27017/APPDB?tls=true&tlsCAFile=/chemin/CA.crt' --eval 'db.recette.insertOne({ok:1}); db.recette.drop()'
   ```
   👉 Explication : valide droits et écriture ; collection supprimée.

## 2. Production — Contrôles

Consigner la recette ; superviser disponibilité, connexions, espace disque, journal.

## 3. Production — Sécurité

- Supprimer les données de test.
- Aucun compte de recette conservé.
- Surveiller `/var/log/mongodb/mongod.log`.

## Validation et retour arrière

- **Validation** : tous les contrôles réussis.
- **Retour arrière** : revenir à la configuration sauvegardée.

## Si le problème n'est pas résolu

- [MongoDB — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_MongoDB_Prerequis_Limites.md)
- [MongoDB — Installer](Fiche_Simple_-_VM_Debian_13_MongoDB_Installer.md)
- [MongoDB — Configurer](Fiche_Simple_-_VM_Debian_13_MongoDB_Configurer.md)
- [MongoDB — Sécuriser (authentification, TLS, pare-feu)](Fiche_Simple_-_VM_Debian_13_MongoDB_Securiser.md)
- [MongoDB — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_MongoDB_Sauvegarder_Restaurer.md)
- [MongoDB — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_MongoDB_Mettre_A_Jour.md)
- [MongoDB — installation sous Debian](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/)
- [MongoDB — sécurité](https://www.mongodb.com/docs/manual/security/)
