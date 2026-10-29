# Fiche_Simple_-_VM_Debian_13_ownCloud_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13; ownCloud Infinite Scale (oCIS), binaire officiel, Nginx
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / ownCloud — Mise à jour et retour arrière
- **Tags** : `debian13`, `owncloud`, `ocis`, `cloud`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour le binaire ownCloud Infinite Scale avec retour arrière par sauvegarde.

## 1. Hors-Production (Lab / Test / POC)

1. Lire les notes de version et vérifier les chemins de migration autorisés, puis sauvegarder (fiche Sauvegarder / restaurer) et prendre un snapshot.
   👉 Explication : les changements de données entre versions peuvent ne pas être réversibles : la sauvegarde est le seul retour arrière sûr.

2. Conserver l'ancien binaire et arrêter le service :
   ```bash
   sudo cp -a /usr/local/bin/ocis /usr/local/bin/ocis.OLD
   sudo systemctl stop ocis
   ```
   👉 Explication : permet de revenir à la version précédente si aucune migration n'a modifié les données.

3. Installer la nouvelle version :
   ```bash
   OCIS_VERSION=X.Y.Z
   curl -fL -o /tmp/ocis https://download.owncloud.com/ocis/ocis/stable/${OCIS_VERSION}/ocis-${OCIS_VERSION}-linux-amd64
   sudo install -m 0755 /tmp/ocis /usr/local/bin/ocis
   sudo systemctl start ocis
   ocis version
   ```
   👉 Explication : `X.Y.Z` est à remplacer par la version cible.

4. Rejouer la recette (fiche Valider).
   ```bash
   sudo journalctl -u ocis -n 30 --no-pager
   ```
   👉 Explication : contrôler l'absence d'erreur de migration.

## 2. Production — Contrôles

Fenêtre de maintenance, sauvegarde testée, version cible compatible, surveillance 24 h.

## 3. Production — Sécurité

- Télécharger uniquement depuis le domaine officiel de l'éditeur.
- Conserver le binaire précédent jusqu'à validation.

## Validation et retour arrière

- **Validation** : `ocis version` affiche la version cible et la recette est OK.
- **Retour arrière** : arrêter le service, remettre `/usr/local/bin/ocis.OLD` si les données n'ont pas migré, sinon restaurer l'archive et le binaire précédents, ou le snapshot.

## Si le problème n'est pas résolu

- [ownCloud — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_ownCloud_Prerequis_Limites.md)
- [ownCloud — Installer](Fiche_Simple_-_VM_Debian_13_ownCloud_Installer.md)
- [ownCloud Infinite Scale — documentation officielle](https://doc.owncloud.com/ocis/next/)
- [ownCloud — téléchargements](https://owncloud.com/download-server/)
