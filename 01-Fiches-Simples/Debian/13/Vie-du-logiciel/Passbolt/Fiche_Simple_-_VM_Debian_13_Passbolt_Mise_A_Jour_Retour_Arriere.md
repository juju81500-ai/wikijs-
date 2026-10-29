# Fiche_Simple_-_VM_Debian_13_Passbolt_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13 dédiée avec domaine, base et SMTP définis
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : gestionnaire de secrets / serveur
- **Tags** : `debian13`, `passbolt`, `secrets`, `tls`, `sauvegarde`
---

## Problème précis à résoudre

Mettre à jour paquet CE et suivre migrations compatibles en protégeant clés/base.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier versions et origine APT
   ```bash
   dpkg-query -W passbolt-ce-server
   apt-cache policy passbolt-ce-server
   ```
   👉 Explication : comparer aux notes officielles.

2. Créer sauvegarde complète vérifiée
   ```text
   Navigateur > ouvrir la documentation officielle : https://www.passbolt.com/docs/hosting/install/ce/debian/
   ```
   👉 Explication : ne pas continuer sans restauration disponible. Détail à confirmer dans la documentation officielle avant application : Sauvegarder base, config, clés et pièces jointes selon fiche dédiée; confirmer checksum et accès.

3. Simuler mise à jour
   ```bash
   sudo apt update
   sudo apt-get -s upgrade passbolt-ce-server
   ```
   👉 Explication : vérifier scripts de migration, origine et dépendances.

4. Appliquer en fenêtre et exécuter contrôle officiel
   ```bash
   sudo apt install --only-upgrade passbolt-ce-server
   sudo systemctl --no-pager status nginx mariadb
   ```
   👉 Explication : terminer par healthcheck officiel de la version.

## 2. Production — Contrôles

Répéter en préproduction; prévoir que rollback rétablit ensemble paquet, base, config et clés d’une date cohérente.

## 3. Production — Sécurité

- Ne pas rétrograder paquet seul après migration de base.
- Ne pas faire migration sans backup vérifié.
- Contrôler accès utilisateurs et mail après mise à jour.

## Validation et retour arrière

- **Validation** : Version et healthcheck sont conformes et un utilisateur test ouvre secret factice.
- **Retour arrière** : Restaurer l’ensemble cohérent depuis la sauvegarde testée.

## Si le problème n'est pas résolu

- [Passbolt — installation Debian 13 CE](https://www.passbolt.com/docs/hosting/install/ce/debian/)
- [Passbolt — configuration serveur](https://www.passbolt.com/docs/hosting/configure/)
- [Passbolt — sauvegarde](https://www.passbolt.com/docs/hosting/backup/)
- [Fiche connexe](<Fiche_Simple_-_VM_Debian_13_Passbolt_Prerequis_Limites.md>)
