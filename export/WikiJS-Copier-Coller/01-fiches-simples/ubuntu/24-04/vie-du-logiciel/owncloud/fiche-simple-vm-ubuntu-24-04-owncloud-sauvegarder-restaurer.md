# Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Sauvegarder_Restaurer

- **Environnement** : VM Ubuntu Server 24.04; ownCloud Infinite Scale (oCIS), binaire officiel
- **OS / Version** : Ubuntu Server 24.04
- **Catégorie** : Vie du logiciel / ownCloud — Sauvegarder / restaurer

---

## Problème précis à résoudre

Sauvegarder ensemble configuration et données oCIS.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder / restaurer :
   ```bash
   sudo systemctl stop ocis
sudo tar --xattrs -czf /root/ocis-backup-DATE.tgz /etc/ocis /var/lib/ocis
sudo chmod 600 /root/ocis-backup-DATE.tgz
   ```
   👉 Explication : Remplacer DATE par la date; service arrêté pour cohérence, archiver chiffré hors hôte.

## 2. Production — Contrôles

Définir rétention, chiffrement, RPO/RTO et restauration isolée.

## 3. Production — Sécurité

Archives contiennent données utilisateur; limiter et chiffrer les accès.

## Validation et retour arrière

- **Validation** : Restauration test démarre et permet vérifier un fichier témoin.
- **Retour arrière** : Arrêter lab; restauration production seulement après contrôle de cohérence.

## Si le problème n'est pas résolu

- [Prérequis et limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-prerequis-limites)
- [Installer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-installer)
- [Configurer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-configurer)
- [Sécuriser](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-securiser)
- [Valider (recette)](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-valider)
- [Mise à jour et retour arrière](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-mise-a-jour-retour-arriere)
- [Documentation officielle](https://owncloud.dev/ocis/deployment/systemd/)