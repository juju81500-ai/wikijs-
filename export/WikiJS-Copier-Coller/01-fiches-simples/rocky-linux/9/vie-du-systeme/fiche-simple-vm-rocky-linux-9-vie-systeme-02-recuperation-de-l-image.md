# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_02_Recuperation_De_L_Image

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 02 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Obtenir l'ISO officielle de Rocky Linux 9.

## 1. Hors-Production (Lab / Test / POC)

1. Choisir le miroir officiel et télécharger l'ISO minimale :
   ```bash
   curl -LO https://download.rockylinux.org/pub/rocky/9/isos/x86_64/Rocky-9-latest-x86_64-minimal.iso
   curl -LO https://download.rockylinux.org/pub/rocky/9/isos/x86_64/CHECKSUM
   ```
   👉 Explication : récupère l'image et le fichier `CHECKSUM` du même répertoire (aucun abonnement n'est nécessaire).

2. Contrôler la taille et la date du fichier :
   ```bash
   ls -lh Rocky-9-latest-x86_64-minimal.iso
   ```
   👉 Explication : une taille anormalement petite indique un téléchargement interrompu.

3. Ranger l'ISO dans un dépôt interne avec sa version.
   👉 Explication : garantit que la même image sert à tous les déploiements.

## 2. Production — Contrôles

Utiliser un miroir interne ou un dépôt d'images contrôlé.

## 3. Production — Sécurité

Ne télécharger que depuis `rockylinux.org` ou un miroir listé sur ce site, en HTTPS.

## Validation et retour arrière

- **Validation** : ISO et fichier CHECKSUM présents, taille cohérente.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)