# Fiche_Simple_-_VM_Debian_13_OpenMediaVault_Installer_OMV.md

- **Environnement** : OpenMediaVault 8 sur Debian 13 minimal
- **OS / Version** : Debian 13; OpenMediaVault 8.0 Synchrony
- **Catégorie** : stockage / installation
- **Tags** : `debian13`, `openmediavault`, `apt`, `gpg`, `omv8`

---

## Problème précis à résoudre

Installer le paquet openmediavault depuis le dépôt officiel signé.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les prérequis et activer systemd-resolved :
   ```bash
   sudo apt install --yes systemd-resolved psmisc gnupg
   sudo systemctl enable --now systemd-resolved.service
   ```
   👉 Explication : La méthode Debian exige systemd-resolved actif.

2. Définir un DNS accessible (remplacer `ens18` par votre interface et `192.0.2.53` par votre résolveur) :
   ```bash
   sudo resolvectl dns ens18 192.0.2.53
   resolvectl status
   ```
   👉 Explication : Utiliser de préférence le résolveur approuvé par le site.

3. Installer la clé officielle dans le trousseau APT :
   ```bash
   wget --quiet --output-document=- https://packages.openmediavault.io/archive.key \
     | sudo gpg --dearmor --yes --output /usr/share/keyrings/openmediavault-archive-keyring.gpg
   ```
   👉 Explication : La clé sert uniquement au dépôt OMV via `signed-by`.

4. Déclarer le dépôt stable Debian 13 « synchrony » :
   ```bash
   echo 'deb [signed-by=/usr/share/keyrings/openmediavault-archive-keyring.gpg] http://packages.openmediavault.org/public/ synchrony main' | sudo tee /etc/apt/sources.list.d/openmediavault.list
   ```
   👉 Explication : Crée la source APT documentée par OMV.

5. Installer OMV avec les options prescrites :
   ```bash
   export LANG=C.UTF-8
   export DEBIAN_FRONTEND=noninteractive
   export APT_LISTCHANGES_FRONTEND=none
   sudo apt-get update
   sudo apt-get --yes --auto-remove --show-upgraded \
     --allow-downgrades --allow-change-held-packages --no-install-recommends \
     --option DPkg::Options::="--force-confdef" \
     --option DPkg::Options::="--force-confold" \
     install openmediavault
   ```
   👉 Explication : Ne pas interrompre dpkg ni couper l'alimentation pendant la transaction.

6. Initialiser la base de configuration puis ouvrir la console de reprise si le réseau doit être repris :
   ```bash
   sudo omv-confdbadm populate
   sudo omv-firstaid
   ```
   👉 Explication : `populate` reprend certaines configurations existantes; l'IP peut changer à l'application.

## 2. Production — Contrôles

Prévoir accès console hyperviseur et fenêtre de maintenance : la configuration réseau existante peut être réécrite.

## 3. Production — Sécurité

- Vérifier l'empreinte de la clé avant de l'installer.
- Ne pas mélanger Debian Backports, Testing ou Experimental.

## Validation et retour arrière

- **Validation** : `dpkg -l openmediavault` indique le paquet installé et l'interface Web répond.
- **Retour arrière** : restaurer la sauvegarde ou l'instantané de la VM; OMV ne se désinstalle pas proprement.

## Si le problème n'est pas résolu

- [OpenMediaVault — installation sur Debian](https://docs.openmediavault.org/en/latest/installation/on_debian.html)
- [OpenMediaVault — prérequis](https://docs.openmediavault.org/en/latest/prerequisites.html)
- [Guide complet OpenMediaVault Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/66_Deploiement_OpenMediaVault_8_Debian_13.md#3-installer-openmediavault-depuis-le-depot-signe)
