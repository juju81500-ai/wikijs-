# Fiche_Simple_-_VM_Rocky_9_ownCloud_Installer

- **Environnement** : VM Rocky Linux 9; ownCloud Infinite Scale (oCIS), binaire officiel
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Vie du logiciel / ownCloud — Installer

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

- [Prérequis et limites](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-prerequis-limites)
- [Configurer](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-configurer)
- [Sécuriser](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-securiser)
- [Valider (recette)](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-mise-a-jour-retour-arriere)
- [Documentation officielle](https://owncloud.dev/ocis/deployment/systemd/)