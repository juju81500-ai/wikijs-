# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_32_Automatisation_Des_Correctifs_De

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 32 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Appliquer les correctifs de sécurité.

## 1. Hors-Production (Lab / Test / POC)

1. Installer et activer :
   ```bash
   sudo apt install unattended-upgrades
   sudo dpkg-reconfigure -plow unattended-upgrades
   ```
   👉 Explication : active les mises à jour de sécurité automatiques.

2. Tester :
   ```bash
   sudo unattended-upgrade --dry-run --debug
   ```
   👉 Explication : simule sans rien installer.

## 2. Production — Contrôles

Redémarrage automatique seulement dans une fenêtre définie.

## 3. Production — Sécurité

Limiter l'automatisation aux dépôts de sécurité.

## Validation et retour arrière

- **Validation** : `/var/log/unattended-upgrades/` consultable.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 12](/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)