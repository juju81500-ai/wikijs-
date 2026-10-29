# Fiche_Simple_-_VM_Debian_13_NetBox_Migrations_Admin.md

- **Environnement** : NetBox 4.7.4 en pilote, PostgreSQL et Redis locaux
- **OS / Version** : Debian 13; NetBox 4.7.4
- **Catégorie** : IPAM / DCIM / initialisation

---

## Problème précis à résoudre

Exécuter les migrations NetBox puis créer un compte administrateur sans contourner les erreurs.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer le script de mise à niveau :
   ```bash
   sudo /opt/netbox/upgrade.sh
   ```
   👉 Explication : crée l'environnement virtuel, installe les dépendances, applique les migrations et collecte les fichiers statiques; ne pas poursuivre en cas d'erreur.

2. Vérifier l'état des migrations :
   ```bash
   sudo -u netbox /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py showmigrations | grep -c '\[ \]' || true
   ```
   👉 Explication : `0` signifie qu'aucune migration n'est en attente.

3. Créer le superutilisateur (mot de passe saisi à l'invite) :
   ```bash
   sudo -u netbox /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py createsuperuser
   ```
   👉 Explication : ne jamais passer le mot de passe comme argument; le stocker dans le coffre.

4. Contrôler la configuration :
   ```bash
   sudo -u netbox /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py check
   ```
   👉 Explication : la commande doit se terminer sans erreur.

## 2. Production — Contrôles

Faire approuver sauvegarde PostgreSQL, release, migration, fenêtre, compte de secours et tests fonctionnels avant le changement.

## 3. Production — Sécurité

- Ne pas copier le mot de passe admin dans un script ou un ticket.
- Ne pas relancer une migration interrompue sans consulter journaux et procédure de récupération.
- Limiter les comptes superutilisateurs et vérifier leurs propriétaires.
- Ne pas importer de données de production pendant la validation.

## Validation et retour arrière

- **Validation** : migration réussie, compte nominatif de test actif, base cohérente.
- **Retour arrière** : restaurer la base et la version compatibles depuis une sauvegarde testée; ne pas rétrograder le code seul après migration.

## Si le problème n'est pas résolu

- [NetBox — installation](https://netbox.readthedocs.io/en/stable/installation/)
- [NetBox — gestion des utilisateurs](https://netbox.readthedocs.io/en/stable/administration/users/)
- [Guide complet NetBox Debian 13](/02-fiches-completes/debian/13/installation-deploiement/73-deploiement-netbox-4-7-4-debian-13#5-executer-les-migrations-et-creer-le-compte-administrateur)