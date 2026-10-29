# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_04_Preparation_Du_Support_D

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 04 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Rendre l'image amorçable sur le matériel ou l'hyperviseur.

## 1. Hors-Production (Lab / Test / POC)

1. Sur un matériel physique, identifier la clé USB puis y écrire l'image `vga` (remplacer `/dev/sdX`) :
   ```sh
   lsblk -o NAME,SIZE,MODEL,TRAN
   sudo dd if=OPNsense-VERSION-vga-amd64.img of=/dev/sdX bs=4M status=progress oflag=sync
   ```
   👉 Explication : `/dev/sdX` est le disque entier de la clé (sans numéro de partition); une erreur effacerait un autre disque.

2. Sur un hyperviseur, attacher l'ISO comme lecteur CD-ROM de la VM (Proxmox : VM > Matériel > Lecteur CD/DVD > Utiliser un fichier ISO).
   👉 Explication : évite de créer une clé physique.

3. Pour un équipement sans écran, choisir l'image `serial` et noter la vitesse de la console (115200 bauds).
   👉 Explication : l'installateur s'affiche alors sur le port série.

## 2. Production — Contrôles

Utiliser le virtuel ou une image préparée pour les déploiements en série.

## 3. Production — Sécurité

Vérifier deux fois le périphérique cible avant `dd`.

## Validation et retour arrière

- **Validation** : L'écran de démarrage OPNsense (menu de boot) apparaît.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)