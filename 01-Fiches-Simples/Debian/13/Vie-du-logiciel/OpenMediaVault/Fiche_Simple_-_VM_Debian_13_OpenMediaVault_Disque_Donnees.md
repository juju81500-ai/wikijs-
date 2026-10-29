# Fiche_Simple_-_VM_Debian_13_OpenMediaVault_Disque_Donnees.md

- **Environnement** : OpenMediaVault 8 sur Debian 13 minimal
- **OS / Version** : Debian 13; OpenMediaVault 8.0 Synchrony
- **Catégorie** : stockage / disques
- **Tags** : `debian13`, `openmediavault`, `disque`, `raid`, `filesystem`

---

## Problème précis à résoudre

Ajouter un disque de données sans toucher au disque système.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier le disque par son numéro de série :
   ```bash
   lsblk -o NAME,SIZE,MODEL,SERIAL,FSTYPE,MOUNTPOINTS
   sudo smartctl --scan-open
   ```
   👉 Explication : Évite d'effacer le mauvais périphérique.

2. Contrôler les disques dans **Storage > Disks**; n'utiliser l'action de nettoyage qu'après vérification du numéro de série et sauvegarde.
   👉 Explication : L'effacement supprime signatures de partitions et de systèmes de fichiers.

3. Créer puis monter le système de fichiers : **Storage > File Systems**.
   👉 Explication : OMV garde ses volumes dans sa base; ne pas éditer à la main les zones OMV de `/etc/fstab`.

4. Pour un RAID logiciel : **Storage > RAID**.
   👉 Explication : Choisir le niveau selon capacité et tolérance de panne; un RAID n'est pas une sauvegarde.

## 2. Production — Contrôles

Sauvegarde vérifiée et plan de remplacement des disques avant toute création ou suppression de RAID.

## 3. Production — Sécurité

- Ne jamais effacer un disque sans avoir confirmé son numéro de série.

## Validation et retour arrière

- **Validation** : le système de fichiers est monté et visible dans OMV.
- **Retour arrière** : démonter le volume dans OMV; ne restaurer les données que depuis la sauvegarde.

## Si le problème n'est pas résolu

- [OpenMediaVault — installation sur Debian](https://docs.openmediavault.org/en/latest/installation/on_debian.html)
- [OpenMediaVault — prérequis](https://docs.openmediavault.org/en/latest/prerequisites.html)
- [Guide complet OpenMediaVault Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/66_Deploiement_OpenMediaVault_8_Debian_13.md#5-integrer-un-disque-de-donnees)
