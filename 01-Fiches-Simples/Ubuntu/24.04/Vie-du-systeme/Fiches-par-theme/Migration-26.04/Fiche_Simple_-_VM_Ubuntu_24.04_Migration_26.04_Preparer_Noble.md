# Fiche_Simple_-_VM_Ubuntu_24.04_Migration_26.04_Preparer_Noble.md

- **Environnement** : VM ou serveur Ubuntu Server LTS
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble) vers 26.04 LTS (Resolute)
- **Catégorie** : migration de version
- **Tags** : `ubuntu24.04`, `ubuntu26.04`, `migration`, `preparation`, `noble`

---

## Problème précis à résoudre

Mettre Noble à jour et corriger les blocages avant l'upgrade.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les mises à jour de Noble :
   ```bash
   sudo apt update
   sudo apt full-upgrade
   ```
   👉 Explication : le système part d'un état à jour.

2. Redémarrer si nécessaire :
   ```bash
   sudo reboot
   ```
   👉 Explication : les nouveaux noyau et bibliothèques sont chargés.

3. Corriger les incohérences dpkg, dépôts externes non compatibles, paquets retenus et espace insuffisant :
   ```bash
   sudo dpkg --audit
   apt-mark showhold
   ```
   👉 Explication : la commande liste ce qu'il faut corriger.

4. Vérifier cloud-init/Netplan, DNS, accès console et session SSH de secours.
   👉 Explication : on garde un accès si le réseau change.

5. Pour une base MariaDB ou PostgreSQL, confirmer la sauvegarde cohérente et la procédure de mise à niveau du moteur.
   👉 Explication : la mise à niveau du moteur est une opération séparée.

## 2. Production — Contrôles

Vérifier la présence de la console ou de l'accès hors bande.

## 3. Production — Sécurité

- Garder une session SSH de secours ouverte.

## Validation et retour arrière

- **Validation** : `dpkg --audit` sans sortie et aucun paquet retenu inattendu.
- **Retour arrière** : Restaurer le snapshot si la préparation a cassé le système.

## Si le problème n'est pas résolu

- [Ubuntu 26.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/26.04/)
- [Ubuntu 24.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
- [Guide complet — préparer Noble](../../../../../../02-Fiches-Completes/Ubuntu/24.04/Installation-Deploiement/22_Migration_Ubuntu_Server_24.04_vers_26.04_LTS.md#4-preparer-noble)
