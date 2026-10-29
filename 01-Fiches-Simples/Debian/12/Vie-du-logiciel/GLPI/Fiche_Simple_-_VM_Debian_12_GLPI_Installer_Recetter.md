# Fiche_Simple_-_VM_Debian_12_GLPI_Installer_Recetter.md

- **Environnement** : GLPI déployé en HTTPS, accès depuis un poste d'administration
- **OS / Version** : Debian 12 ou 13; version GLPI maintenue
- **Catégorie** : GLPI / installation et recette
- **Tags** : `debian12`, `glpi`, `itsm`, `https`, `validation`

---

## Problème précis à résoudre

Terminer l'installation GLPI et valider les fonctions essentielles sans laisser l'installateur ou les comptes initiaux accessibles.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir l'URL HTTPS depuis un poste d'administration : **https://glpi.example.net** puis suivre l'assistant (langue, licence, **Installer**, informations de base : serveur `localhost`, utilisateur `glpi`, base `glpi`).
   👉 Explication : utiliser le compte SQL dédié.

2. Sécuriser après installation : supprimer l'installateur et remplacer les comptes par défaut : **Configuration > Utilisateurs** (changer `glpi`, `tech`, `normal`, `post-only`).
   ```bash
   sudo rm -f /var/www/glpi/current/install/install.php
   ```
   👉 Explication : selon la version, l'installateur est déjà désactivé; suivre la documentation officielle.

3. Vérifier les services :
   ```bash
   sudo nginx -t
   sudo systemctl --no-pager status nginx mariadb
   sudo journalctl -u nginx --since '-15 minutes' --no-pager
   ```
   👉 Explication : aucun service en échec ni erreur 5xx.

4. Recette fonctionnelle : **Assistance > Créer un ticket**, vérifier **Configuration > Notifications** et **Configuration > Actions automatiques** (cron).
   👉 Explication : tester l'envoi de courriel, puis supprimer les données de test.

## 2. Production — Contrôles

Faire valider comptes, rôles, tâches planifiées, notifications, courriels, journaux et procédure de support avant ouverture aux utilisateurs.

## 3. Production — Sécurité

- Ne pas laisser l'installateur accessible après le déploiement.
- Changer les identifiants initiaux et ne jamais conserver les secrets de démonstration.
- N'ouvrir l'application qu'en HTTPS sur les réseaux prévus.
- Ne pas laisser des tickets de test ou données fictives visibles aux utilisateurs.

## Validation et retour arrière

- **Validation** : ticket de test créé et retiré, notifications testées, tâches actives, comptes initiaux sécurisés.
- **Retour arrière** : fermer l'accès utilisateur, conserver logs et base, puis revenir à la version précédente selon la procédure approuvée.

## Si le problème n'est pas résolu

- [GLPI — documentation](https://glpi-install.readthedocs.io/en/latest/)
- [GLPI — prérequis](https://glpi-install.readthedocs.io/en/latest/prerequisites.html)
- [Guide complet GLPI Debian](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/03_Helpdesk_ITSM_GLPI_11_12_Debian_12_13.md)
