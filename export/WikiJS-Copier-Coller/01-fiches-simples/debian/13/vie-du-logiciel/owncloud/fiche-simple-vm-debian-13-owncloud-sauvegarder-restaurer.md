# Fiche_Simple_-_VM_Debian_13_ownCloud_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13; ownCloud Infinite Scale (oCIS), binaire officiel, Nginx
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / ownCloud — Sauvegarder / restaurer

---

## Problème précis à résoudre

Sauvegarder et restaurer la configuration et les données d'ownCloud Infinite Scale de façon cohérente.

## 1. Hors-Production (Lab / Test / POC)

1. Arrêter le service pour une sauvegarde cohérente :
   ```bash
   sudo systemctl stop ocis
   ```
   👉 Explication : les métadonnées et blobs doivent être copiés au même instant ; sinon utiliser un snapshot de volume atomique.

2. Archiver configuration et données :
   ```bash
   sudo tar -czpf /var/backups/ocis-$(date +%F).tar.gz /etc/ocis /var/lib/ocis
   ```
   👉 Explication : contient secrets et fichiers utilisateurs : droits 0600 et chiffrement si copie hors serveur (voir la fiche Restic du pack). Sur gros volume, préférer rsync/snapshot.

3. Redémarrer :
   ```bash
   sudo systemctl start ocis
   systemctl is-active ocis
   ```
   👉 Explication : retour au service.

4. Restaurer :
   ```bash
   sudo systemctl stop ocis
   sudo tar -xzpf /var/backups/ocis-DATE.tar.gz -C /
   sudo systemctl start ocis
   ```
   👉 Explication : `DATE` est à remplacer ; tester d'abord sur une VM de lab avec même version d'oCIS.

5. Vérifier après restauration :
   ```bash
   curl -fsS https://OCIS.EXAMPLE.NET/.well-known/openid-configuration >/dev/null && echo ok
   ```
   👉 Explication : puis ouvrir l'interface et contrôler les fichiers.

## 2. Production — Contrôles

Planifier la sauvegarde, externaliser (3-2-1), chiffrer, tester régulièrement la restauration, restaurer avec la même version du binaire.

## 3. Production — Sécurité

- Archives en droits restreints.
- Conserver les secrets (`ocis.yaml`) : sans eux les données ne sont plus lisibles.

## Validation et retour arrière

- **Validation** : restauration testée en lab, fichiers lisibles.
- **Retour arrière** : remettre l'archive précédente ou restaurer le snapshot.

## Si le problème n'est pas résolu

- [ownCloud — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-prerequis-limites)
- [ownCloud — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-installer)
- [Restic — dépôt de sauvegarde](/01-fiches-simples/debian/13/vie-du-logiciel/restic/fiche-simple-vm-debian-13-sauvegarde-restic-depot)
- [ownCloud Infinite Scale — documentation officielle](https://doc.owncloud.com/ocis/next/)
- [ownCloud — téléchargements](https://owncloud.com/download-server/)