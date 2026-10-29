# Fiche_Simple_-_VM_Debian_13_Passbolt_Valider_Recette

- **Environnement** : VM Debian 13 dédiée avec domaine, base et SMTP définis
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : gestionnaire de secrets / serveur

---

## Problème précis à résoudre

Tester healthcheck, invitation, partage et révocation avec comptes/valeurs factices.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter healthcheck officiel après confirmation syntaxe
   ```text
   Navigateur > ouvrir la documentation officielle : https://www.passbolt.com/docs/hosting/install/ce/debian/
   ```
   👉 Explication : option/chemin peuvent dépendre de version; utiliser la documentation paquet. Détail à confirmer dans la documentation officielle avant application : Lancer le healthcheck indiqué pour le paquet Passbolt CE installé et traiter les alertes bloquantes.

2. Créer comptes d’essai
   ```text
   Navigateur > ouvrir la documentation officielle : https://www.passbolt.com/docs/hosting/install/ce/debian/
   ```
   👉 Explication : remplacer les adresses à remplacer; aucune donnée réelle. Détail à confirmer dans la documentation officielle avant application : Inviter deux comptes de test et accepter invitations depuis postes isolés.

3. Partager puis révoquer un secret factice
   ```text
   Navigateur > ouvrir la documentation officielle : https://www.passbolt.com/docs/hosting/install/ce/debian/
   ```
   👉 Explication : tester autorisation positive et négative. Détail à confirmer dans la documentation officielle avant application : Partager une valeur fictive avec le second compte, retirer son accès et vérifier la révocation.

4. Consulter journaux sans exporter de secrets
   ```bash
   sudo journalctl -u nginx --since "30 minutes ago" --no-pager
   ```
   👉 Explication : adapter au service; éviter de joindre logs bruts à un ticket.

## 2. Production — Contrôles

Faire valider parcours utilisateur, extensions, recovery et journaux par les propriétaires de service.

## 3. Production — Sécurité

- Données factices uniquement.
- Ne pas exporter clés privées ou coffre réel pendant recette.
- Retirer comptes et secrets temporaires.

## Validation et retour arrière

- **Validation** : Invitation et partage fonctionnent et la révocation bloque bien le second compte.
- **Retour arrière** : Désactiver comptes de test et restaurer état de pilote.

## Si le problème n'est pas résolu

- [Passbolt — installation Debian 13 CE](https://www.passbolt.com/docs/hosting/install/ce/debian/)
- [Passbolt — configuration serveur](https://www.passbolt.com/docs/hosting/configure/)
- [Passbolt — sauvegarde](https://www.passbolt.com/docs/hosting/backup/)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/passbolt/fiche-simple-vm-debian-13-passbolt-prerequis-limites>)