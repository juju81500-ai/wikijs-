# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_04_Preparation_Du_Support_D

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 04 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-04`

---

## Problème précis à résoudre

Rendre l'ISO amorçable sur la machine ou l'hyperviseur.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier la clé USB avec précaution :
   ```bash
   lsblk -o NAME,SIZE,MODEL,TRAN
   ```
   👉 Explication : repère le disque `/dev/sdX` de la clé; une erreur effacerait un autre disque.

2. Écrire l'ISO sur la clé (remplacer `/dev/sdX`) :
   ```bash
   sudo dd if=Rocky-9-latest-x86_64-minimal.iso of=/dev/sdX bs=4M status=progress oflag=sync
   ```
   👉 Explication : copie bloc à bloc l'image hybride; `/dev/sdX` est le périphérique entier, sans numéro de partition.

3. Sur un hyperviseur, attacher l'ISO comme lecteur CD-ROM de la VM.
   👉 Explication : évite de créer une clé physique.

## 2. Production — Contrôles

Utiliser le virtuel (ISO sur datastore) ou PXE pour les déploiements en série.

## 3. Production — Sécurité

Vérifier deux fois le périphérique cible avant `dd`.

## Validation et retour arrière

- **Validation** : La clé ou l'ISO apparaît dans le menu de démarrage.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
