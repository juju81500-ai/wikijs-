# Fiche_Simple_-_VM_Rocky_9_ownCloud_Installer

- **Environnement** : VM Rocky Linux 9; ownCloud Infinite Scale (oCIS), binaire officiel
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Vie du logiciel / ownCloud — Installer
- **Tags** : `owncloud`, `serveur`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer le binaire officiel sous un compte dédié.

## 1. Hors-Production (Lab / Test / POC)

1. Installer :
   ```bash
   sudo dnf install -y curl ca-certificates
OCIS_VERSION=VERSION_A_REMPLACER
curl -fL "https://download.owncloud.com/ocis/ocis/stable/${OCIS_VERSION}/ocis-${OCIS_VERSION}-linux-amd64" -o /tmp/ocis
sudo install -o root -g root -m 0755 /tmp/ocis /usr/local/bin/ocis
/usr/local/bin/ocis version
sudo useradd --system --home-dir /var/lib/ocis --create-home --shell /usr/sbin/nologin ocis
sudo install -d -o ocis -g ocis -m 0750 /var/lib/ocis
sudo install -d -o root -g ocis -m 0750 /etc/ocis
   ```
   👉 Explication : `VERSION_A_REMPLACER` est un placeholder; choisir version stable et architecture correspondantes, vérifier les artefacts d’intégrité publiés.


## 2. Production — Contrôles

Utiliser un binaire stable officiel, vérifier provenance et archiver version.

## 3. Production — Sécurité

Ne pas exécuter en root; garder SELinux actif sur Rocky.

## Validation et retour arrière

- **Validation** : Binaire affiche la version et compte dédié non interactif.
- **Retour arrière** : Arrêter le service avant retrait; préserver données/configuration.

## Si le problème n'est pas résolu

- [Prérequis et limites](Fiche_Simple_-_VM_Rocky_9_ownCloud_Prerequis_Limites.md)
- [Configurer](Fiche_Simple_-_VM_Rocky_9_ownCloud_Configurer.md)
- [Sécuriser](Fiche_Simple_-_VM_Rocky_9_ownCloud_Securiser.md)
- [Valider (recette)](Fiche_Simple_-_VM_Rocky_9_ownCloud_Valider.md)
- [Sauvegarder / restaurer](Fiche_Simple_-_VM_Rocky_9_ownCloud_Sauvegarder_Restaurer.md)
- [Mise à jour et retour arrière](Fiche_Simple_-_VM_Rocky_9_ownCloud_Mise_A_Jour_Retour_Arriere.md)
- [Documentation officielle](https://owncloud.dev/ocis/deployment/systemd/)
