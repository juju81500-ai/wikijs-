# Fiche_Simple_-_VM_Debian_13_OpenMediaVault_Durcissement.md

- **Environnement** : OpenMediaVault 8 sur Debian 13 minimal
- **OS / Version** : Debian 13; OpenMediaVault 8.0 Synchrony
- **Catégorie** : stockage / durcissement

---

## Problème précis à résoudre

Durcir OMV, planifier les mises à jour et sauvegarder les données.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'écoute des services :
   ```bash
   sudo ss -tlnp
   ```
   👉 Explication : Seuls SSH, interface Web et SMB attendus, limités au réseau d'administration/clients prévus.

2. Désactiver le SSH direct root une fois le service contrôlé :
   ```bash
   sudo grep -E '^\s*PermitRootLogin' /etc/ssh/sshd_config /etc/ssh/sshd_config.d/*.conf
   ```
   👉 Explication : Doit valoir `no`; utiliser un compte non privilégié avec `sudo`.

3. Appliquer les mises à jour (**System > Update Management** ou en console) :
   ```bash
   sudo omv-upgrade
   ```
   👉 Explication : Mises à jour OMV sans mélanger Backports/Testing/Experimental.

4. Tester la restauration d'un dossier et d'un fichier avec leurs permissions.
   👉 Explication : Une sauvegarde non testée n'est pas une sauvegarde.

## 2. Production — Contrôles

Sauvegarder les données sur un autre système ou support hors ligne, avec copie séparée des clés; valider la compatibilité OMV 8 d'un plugin de sauvegarde de configuration sur VM de test.

## 3. Production — Sécurité

- Restreindre l'interface Web à un VLAN de gestion.
- Désactiver invité et anciens protocoles SMB.

## Validation et retour arrière

- **Validation** : mises à jour appliquées, restauration testée.
- **Retour arrière** : restaurer la VM ou les données depuis la sauvegarde.

## Si le problème n'est pas résolu

- [OpenMediaVault — installation sur Debian](https://docs.openmediavault.org/en/latest/installation/on_debian.html)
- [OpenMediaVault — prérequis](https://docs.openmediavault.org/en/latest/prerequisites.html)
- [Guide complet OpenMediaVault Debian 13](/02-fiches-completes/debian/13/installation-deploiement/66-deploiement-openmediavault-8-debian-13#7-durcissement-mises-a-jour-et-sauvegarde)