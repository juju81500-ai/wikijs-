# Fiche_Simple_-_VM_Debian_13_OCS_Inventory_Recette.md

- **Environnement** : VM Debian 13 dédiée, OCS Inventory 3.0 (Nginx, uWSGI, PostgreSQL local)
- **OS / Version** : Debian 13 Trixie; OCS Inventory 3.0; PostgreSQL 17
- **Catégorie** : inventaire de parc / ITSM
- **Tags** : `debian13`, `ocs-inventory`, `ocs3`, `postgresql`, `nginx`, `recette`

---

## Problème précis à résoudre

Vérifier que les services, la console, l'API et un agent de test fonctionnent.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les services :
   ```bash
   sudo systemctl --no-pager status nginx ocsinventory-backend-uwsgi
   ```
   👉 Explication : les deux services doivent être `active (running)`.

2. Lire les journaux récents :
   ```bash
   sudo journalctl -u ocsinventory-backend-uwsgi -n 50 --no-pager
   sudo tail -n 50 /var/log/ocsinventory-backend/ocsinventory-backend.log
   ```
   👉 Explication : repère les erreurs de démarrage ou de base de données.

3. Vérifier l'accès TLS à la console puis tester l'API avec un compte habilité.
   👉 Explication : une réponse `401 Unauthorized` à la racine de l'API peut être attendue et confirme sa disponibilité.

4. Installer un agent de test depuis la fiche simple « Installer Agent OCS Inventory » et vérifier qu'un inventaire apparaît.
   👉 Explication : valide la chaîne complète agent, API, base, console.

## 2. Production — Contrôles

Consigner le résultat de recette, la version installée et les exceptions acceptées.

## 3. Production — Sécurité

- Utiliser un agent pilote avant tout déploiement sur le parc.
- Ne pas exposer l'API à des réseaux non autorisés pendant les tests.

## Validation et retour arrière

- **Validation** : Services actifs, console accessible en HTTPS, inventaire de l'agent de test visible.
- **Retour arrière** : Désinstaller l'agent de test et supprimer sa machine de la console.

## Si le problème n'est pas résolu

- [OCS Inventory — Installation essentielle](https://documentation.ocsinventory-ng.org/quickstart-guides/for-administrators/installation-essentials.md)
- [Guide complet OCS Inventory 3 Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/41_Deploiement_OCS_Inventory_3_Debian_13.md#7-recette)
