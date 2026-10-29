# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_32_Automatisation_Des_Correctifs_De

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 32 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Appliquer les correctifs automatiquement.

## 1. Hors-Production (Lab / Test / POC)

1. Installer dnf-automatic :
   ```bash
   sudo dnf install -y dnf-automatic
   ```
   👉 Explication : fournit les minuteurs d'application automatique.

2. Limiter aux correctifs de sécurité :
   ```bash
   sudo sed -i 's/^upgrade_type.*/upgrade_type = security/; s/^apply_updates.*/apply_updates = yes/' /etc/dnf/automatic.conf
   ```
   👉 Explication : modifie `upgrade_type` et `apply_updates`.

3. Activer le minuteur :
   ```bash
   sudo systemctl enable --now dnf-automatic.timer
   systemctl list-timers dnf-automatic.timer
   ```
   👉 Explication : planifie l'exécution quotidienne.

## 2. Production — Contrôles

Tester sur un environnement pilote avant la production.

## 3. Production — Sécurité

Superviser les échecs et les redémarrages nécessaires.

## Validation et retour arrière

- **Validation** : Le minuteur est actif.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)