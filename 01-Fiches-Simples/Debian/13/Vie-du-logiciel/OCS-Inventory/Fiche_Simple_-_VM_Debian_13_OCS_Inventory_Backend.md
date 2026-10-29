# Fiche_Simple_-_VM_Debian_13_OCS_Inventory_Backend.md

- **Environnement** : VM Debian 13 dédiée, OCS Inventory 3.0 (Nginx, uWSGI, PostgreSQL local)
- **OS / Version** : Debian 13 Trixie; OCS Inventory 3.0; PostgreSQL 17
- **Catégorie** : inventaire de parc / ITSM
- **Tags** : `debian13`, `ocs-inventory`, `ocs3`, `postgresql`, `nginx`, `backend`

---

## Problème précis à résoudre

Raccorder le backend OCS à PostgreSQL et appliquer les migrations.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer le script officiel de configuration :
   ```bash
   sudo /usr/share/ocsinventory-backend/tools/configure-ocsinventory-backend.sh
   ```
   👉 Explication : le script pose les questions de connexion et applique les migrations.

2. Répondre aux invites : choisir PostgreSQL, hôte `127.0.0.1`, port `5432`, base `ocsdb`, rôle `ocsuser`, saisir son mot de passe à l'invite et l'URL de console `https://ocs.example.net/` (valeurs d'exemple à remplacer).
   👉 Explication : le mot de passe se saisit dans l'invite du script, jamais en argument.

3. Contrôler le journal du backend :
   ```bash
   sudo tail -n 50 /var/log/ocsinventory-backend/ocsinventory-backend.log
   ```
   👉 Explication : les migrations doivent se terminer sans erreur.

## 2. Production — Contrôles

Documenter la base, le rôle et l'URL de console retenus; sauvegarder la configuration générée.

## 3. Production — Sécurité

- Ne pas laisser de mot de passe dans l'historique ni dans un script.
- Protéger les fichiers de configuration du backend (droits restreints).

## Validation et retour arrière

- **Validation** : Migrations appliquées sans erreur et service uWSGI démarré.
- **Retour arrière** : Restaurer la configuration sauvegardée avant la modification puis relancer le script.

## Si le problème n'est pas résolu

- [OCS Inventory — Installation essentielle](https://documentation.ocsinventory-ng.org/quickstart-guides/for-administrators/installation-essentials.md)
- [OCS Inventory — Prérequis](https://documentation.ocsinventory-ng.org/administrator-docs/system-requirements.md)
- [Guide complet OCS Inventory 3 Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/41_Deploiement_OCS_Inventory_3_Debian_13.md#4-configurer-le-backend)
