# Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Ubuntu Server 24.04; ownCloud Infinite Scale (oCIS), binaire officiel
- **OS / Version** : Ubuntu Server 24.04
- **Catégorie** : Vie du logiciel / ownCloud — Mise à jour et retour arrière
- **Tags** : `owncloud`, `serveur`, `vie-du-logiciel`, `mise_a_jour_retour_arriere`

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

- [Prérequis et limites](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Prerequis_Limites.md)
- [Installer](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Installer.md)
- [Configurer](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Configurer.md)
- [Sécuriser](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Securiser.md)
- [Valider (recette)](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Valider.md)
- [Sauvegarder / restaurer](Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Sauvegarder_Restaurer.md)
- [Documentation officielle](https://owncloud.dev/ocis/deployment/systemd/)
