# Fiche_Simple_-_VM_Debian_13_MySQL_Valider

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MySQL Community (dépôt officiel Oracle)
- **Catégorie** : base de données / MySQL / Valider (recette)
- **Tags** : `debian13`, `mysql`, `recette`

---

## Problème précis à résoudre

Prouver que MySQL est opérationnel, chiffré et supervisable.

## 1. Hors-Production (Lab / Test / POC)

1. État du service :
   ```bash
   systemctl is-active mysql
   mysql -u root -p -e 'SELECT VERSION(); SHOW DATABASES;'
   ```
   👉 Explication : service actif, version attendue.

2. Comptes et écoute :
   ```bash
   mysql -u root -p -e "SELECT user,host FROM mysql.user;"
   sudo ss -tlnp | grep mysqld
   ```
   👉 Explication : pas de compte anonyme ni `root@%` ; écoute sur l'adresse prévue seulement.

3. Test applicatif chiffré :
   ```bash
   mysql -h IP_SERVEUR -u APPUSER -p -e "SHOW STATUS LIKE 'Ssl_cipher';"
   ```
   👉 Explication : chiffrement actif.

4. Lecture/écriture de test :
   ```bash
   mysql -u APPUSER -p APPDB -e 'CREATE TABLE recette(id INT); INSERT INTO recette VALUES (1); SELECT * FROM recette; DROP TABLE recette;'
   ```
   👉 Explication : valide droits et écriture ; table supprimée.

## 2. Production — Contrôles

Consigner la recette ; superviser disponibilité, connexions, espace disque, requêtes lentes.

## 3. Production — Sécurité

- Supprimer toute donnée de test.
- Aucun compte de recette conservé.
- Surveiller le journal d'erreurs.

## Validation et retour arrière

- **Validation** : tous les contrôles réussis.
- **Retour arrière** : revenir à la configuration précédente.

## Si le problème n'est pas résolu

- [MySQL — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_MySQL_Prerequis_Limites.md)
- [MySQL — Installer](Fiche_Simple_-_VM_Debian_13_MySQL_Installer.md)
- [MySQL — Configurer](Fiche_Simple_-_VM_Debian_13_MySQL_Configurer.md)
- [MySQL — Sécuriser (TLS, comptes, pare-feu)](Fiche_Simple_-_VM_Debian_13_MySQL_Securiser.md)
- [MySQL — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_MySQL_Sauvegarder_Restaurer.md)
- [MySQL — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_MySQL_Mettre_A_Jour.md)
- [MySQL — documentation officielle](https://dev.mysql.com/doc/)
- [Alternative MariaDB (fiches du pack)](../MariaDB/Fiche_Simple_-_VM_Debian_13_MariaDB_Prerequis_Limites.md)
