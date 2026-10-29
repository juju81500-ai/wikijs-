# Fiche_Simple_-_VM_Rocky_9_ownCloud_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Rocky Linux 9; ownCloud Infinite Scale (oCIS), binaire officiel
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Vie du logiciel / ownCloud — Mise à jour et retour arrière

---

## Problème précis à résoudre

Mettre à jour le binaire oCIS après sauvegarde cohérente.

## 1. Hors-Production (Lab / Test / POC)

1. Mise à jour et retour arrière :
   ```bash
   curl -fsSL https://download.owncloud.com/ocis/ocis/stable/
sudo cp -a /usr/local/bin/ocis /usr/local/bin/ocis.previous
OCIS_VERSION=VERSION_A_REMPLACER
curl -fL "https://download.owncloud.com/ocis/ocis/stable/${OCIS_VERSION}/ocis-${OCIS_VERSION}-linux-amd64" -o /tmp/ocis.new
sudo systemctl stop ocis
sudo install -o root -g root -m 0755 /tmp/ocis.new /usr/local/bin/ocis
sudo systemctl start ocis
systemctl is-active ocis
   ```
   👉 Explication : Remplacer le placeholder, lire les notes de version et contrôler le service en lab.

## 2. Production — Contrôles

Préparer snapshot, sauvegarde, fenêtre et tests applicatifs.

## 3. Production — Sécurité

Télécharger depuis le miroir officiel et vérifier sommes/signatures disponibles.

## Validation et retour arrière

- **Validation** : Version cible active, logs propres, scénario réussi.
- **Retour arrière** : Restaurer ensemble binaire, configuration et données si migration de données.

## Si le problème n'est pas résolu

- [Prérequis et limites](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-prerequis-limites)
- [Installer](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-installer)
- [Configurer](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-configurer)
- [Sécuriser](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-securiser)
- [Valider (recette)](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-sauvegarder-restaurer)
- [Documentation officielle](https://owncloud.dev/ocis/deployment/systemd/)