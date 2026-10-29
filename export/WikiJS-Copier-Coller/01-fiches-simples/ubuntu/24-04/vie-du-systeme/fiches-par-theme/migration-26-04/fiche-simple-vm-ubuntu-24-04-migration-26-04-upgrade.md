# Fiche_Simple_-_VM_Ubuntu_24.04_Migration_26.04_Upgrade.md

- **Environnement** : VM ou serveur Ubuntu Server LTS
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble) vers 26.04 LTS (Resolute)
- **Catégorie** : migration de version

---

## Problème précis à résoudre

Lancer la mise à niveau majeure avec l'outil officiel en fenêtre de maintenance.

## 1. Hors-Production (Lab / Test / POC)

1. Avec console ou accès hors bande, mettre à jour une dernière fois :
   ```bash
   sudo apt update
   sudo apt full-upgrade
   ```
   👉 Explication : on part d'un système à jour.

2. Vérifier la disponibilité de la nouvelle LTS :
   ```bash
   sudo do-release-upgrade -c
   ```
   👉 Explication : la commande indique si la version LTS cible est proposée.

3. Lancer la mise à niveau :
   ```bash
   sudo do-release-upgrade
   ```
   👉 Explication : l'outil officiel gère les dépôts, les paquets et les redémarrages.

4. Lire chaque proposition de suppression, de remplacement de configuration et de redémarrage de service.
   👉 Explication : on évite de perdre une configuration locale.

## 2. Production — Contrôles

Exécuter uniquement en fenêtre de maintenance avec console disponible.

## 3. Production — Sécurité

- Ne pas forcer une suite APT `resolute` dans les sources pendant qu'un upgrade est interrompu.

## Validation et retour arrière

- **Validation** : L'outil termine sans erreur et propose le redémarrage.
- **Retour arrière** : Pas de downgrade APT : restaurer le snapshot ou la sauvegarde validée.

## Si le problème n'est pas résolu

- [Ubuntu 26.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/26.04/)
- [Ubuntu 24.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
- [Guide complet — exécuter l'upgrade](/02-fiches-completes/ubuntu/24-04/installation-deploiement/22-migration-ubuntu-server-24-04-vers-26-04-lts#5-executer-lupgrade)