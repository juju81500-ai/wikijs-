# Fiche_Simple_-_VM_Debian_13_NetBox_Installer_Release.md

- **Environnement** : Debian 13, archive officielle NetBox 4.7.4
- **OS / Version** : Debian 13; NetBox 4.7.4
- **Catégorie** : IPAM / DCIM / installation
- **Tags** : `debian13`, `netbox`, `release`, `archive`, `permissions`

---

## Problème précis à résoudre

Installer la release NetBox versionnée sans écraser une instance existante ni donner au serveur Web l'écriture sur le code.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'archive de version fixe et calculer son empreinte :
   ```bash
   cd /tmp
   curl --fail --location --proto '=https' --tlsv1.2 -o netbox-v4.7.4.tar.gz https://github.com/netbox-community/netbox/archive/refs/tags/v4.7.4.tar.gz
   sha256sum netbox-v4.7.4.tar.gz
   ```
   👉 Explication : consigner l'empreinte; elle ne remplace pas une signature publiée mais permet de retrouver l'archive.

2. Contrôler le contenu avant extraction :
   ```bash
   tar -tzf netbox-v4.7.4.tar.gz | head
   ls -d /opt/netbox /opt/netbox-4.7.4 2>/dev/null || echo "aucune instance existante"
   ```
   👉 Explication : si une instance existe, arrêter et suivre la mise à niveau; ne pas l'écraser.

3. Extraire et créer le lien :
   ```bash
   sudo tar -xzf netbox-v4.7.4.tar.gz -C /opt
   sudo ln -s /opt/netbox-4.7.4 /opt/netbox
   ```
   👉 Explication : le lien `/opt/netbox` facilite les futures mises à niveau.

4. Créer le compte de service et limiter les écritures :
   ```bash
   sudo adduser --system --group netbox
   sudo chown -R netbox:netbox /opt/netbox/netbox/media /opt/netbox/netbox/reports /opt/netbox/netbox/scripts
   ```
   👉 Explication : seuls les dossiers de données sont inscriptibles; ne pas donner `www-data` l'écriture sur le code.

## 2. Production — Contrôles

Enregistrer le tag, l'empreinte, la source, le propriétaire du service et les fichiers locaux; utiliser un répertoire versionné distinct pour chaque release.

## 3. Production — Sécurité

- Une empreinte calculée localement identifie une archive mais ne prouve pas sa signature éditeur.
- Ne pas extraire par-dessus une installation existante.
- Ne pas donner des droits d'écriture larges à `www-data`.
- Ne pas servir une archive téléchargée d'une source non officielle.

## Validation et retour arrière

- **Validation** : release et chemin versionnés, compte dédié, permissions minimales.
- **Retour arrière** : garder l'ancienne version intacte et ne basculer le lien qu'après validation complète.

## Si le problème n'est pas résolu

- [NetBox — archive de release](https://netbox.readthedocs.io/en/stable/installation/3-netbox/)
- [NetBox — releases](https://github.com/netbox-community/netbox/releases)
- [Guide complet NetBox Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/73_Deploiement_NetBox_4.7.4_Debian_13.md#3-telecharger-et-installer-netbox-4-7-4)
