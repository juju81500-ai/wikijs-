# Fiche_Simple_-_VM_Ubuntu_24.04_Migration_26.04_Inventorier_Sauvegarder.md

- **Environnement** : VM ou serveur Ubuntu Server LTS
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble) vers 26.04 LTS (Resolute)
- **Catégorie** : migration de version
- **Tags** : `ubuntu24.04`, `ubuntu26.04`, `migration`, `inventaire`, `sauvegarde`

---

## Problème précis à résoudre

Inventorier l'état du système et sauvegarder avant l'intervention.

## 1. Hors-Production (Lab / Test / POC)

1. Relever l'état système :
   ```bash
   cat /etc/os-release
   apt list --upgradable
   apt-mark showhold
   sudo dpkg --audit
   systemctl --failed
   df -h / /boot /var
   ```
   👉 Explication : on détecte paquets retenus, incohérences dpkg, services en échec et manque d'espace.

2. Inventorier dépôts externes/PPAs, services, extensions, clés SSH, montages, tâches planifiées et fichiers de configuration.
   👉 Explication : on sait quoi vérifier après la migration.

3. Faire une sauvegarde complète vers une cible distincte (snapshot de VM ou sauvegarde système).
   👉 Explication : il n'y a pas de retour arrière APT pris en charge.

4. Restaurer une copie dans une VM isolée avant l'intervention réelle.
   👉 Explication : on prouve que la sauvegarde est exploitable.

## 2. Production — Contrôles

Vérifier l'espace libre et conserver une sauvegarde sur une cible distincte.

## 3. Production — Sécurité

- Chiffrer les sauvegardes et protéger l'inventaire.

## Validation et retour arrière

- **Validation** : Inventaire complet et sauvegarde restaurée en VM isolée.
- **Retour arrière** : Lecture seule : rien à annuler.

## Si le problème n'est pas résolu

- [Ubuntu 26.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/26.04/)
- [Ubuntu 24.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
- [Guide complet — inventorier et sauvegarder](../../../../../../02-Fiches-Completes/Ubuntu/24.04/Installation-Deploiement/22_Migration_Ubuntu_Server_24.04_vers_26.04_LTS.md#2-inventorier-et-sauvegarder)
