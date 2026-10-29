# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_04_Preparation_Du_Support_D

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 04 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Créer la clé USB ou le média virtuel d'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier la clé USB avec précaution :
   ```bash
   lsblk -o NAME,SIZE,MODEL,TRAN
   ```
   👉 Explication : repérer le disque `/dev/sdX` de la clé (jamais un disque de données).

2. Écrire l'ISO sur la clé (remplacer /dev/sdX par la clé identifiée) :
   ```bash
   sudo dd if=TrueNAS-SCALE-VERSION.iso of=/dev/sdX bs=4M status=progress conv=fsync
   ```
   👉 Explication : copie brute de l'image ; efface tout le contenu de la clé.

3. Pour une VM ou un BMC (IPMI/iDRAC), monter l'ISO comme lecteur optique virtuel.
   👉 Explication : évite la clé physique.

## 2. Production — Contrôles

Utiliser le média virtuel du BMC pour les serveurs distants.

## 3. Production — Sécurité

Ne jamais laisser la clé d'installation branchée après installation.

## Validation et retour arrière

- **Validation** : La machine démarre sur le menu d'installation.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)