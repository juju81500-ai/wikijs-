# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_06_Langue_Et_Localisation_Locales

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 06 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Définir la langue du système.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les locales disponibles :
   ```bash
   localectl list-locales | grep -i fr_FR
   ```
   👉 Explication : vérifie que `fr_FR.UTF-8` existe (paquet `glibc-langpack-fr`).

2. Installer le paquet de langue puis définir la locale :
   ```bash
   sudo dnf install -y glibc-langpack-fr
   sudo localectl set-locale LANG=fr_FR.UTF-8
   ```
   👉 Explication : écrit `/etc/locale.conf`; dans l'installateur, c'est l'écran Langue.

3. Contrôler :
   ```bash
   localectl status
   ```
   👉 Explication : affiche `System Locale: LANG=fr_FR.UTF-8`.

## 2. Production — Contrôles

Garder l'anglais pour les journaux si les outils d'analyse l'exigent.

## 3. Production — Sécurité

Toujours UTF-8 pour éviter les problèmes d'encodage.

## Validation et retour arrière

- **Validation** : `localectl status` indique la locale choisie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)