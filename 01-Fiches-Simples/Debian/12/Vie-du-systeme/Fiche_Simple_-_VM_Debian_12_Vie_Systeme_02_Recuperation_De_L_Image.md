# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_02_Recuperation_De_L_Image

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 02 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-02`

---

## Problème précis à résoudre

Obtenir l'image officielle de Debian 12.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'ISO netinst et les sommes de contrôle depuis le site officiel (version 12 « bookworm », remplacer `12.X.Y` par la version publiée) :
   ```bash
   mkdir -p ~/iso && cd ~/iso
   curl -fLO https://cdimage.debian.org/cdimage/archive/12.X.Y/amd64/iso-cd/debian-12.X.Y-amd64-netinst.iso
   curl -fLO https://cdimage.debian.org/cdimage/archive/12.X.Y/amd64/iso-cd/SHA256SUMS
   curl -fLO https://cdimage.debian.org/cdimage/archive/12.X.Y/amd64/iso-cd/SHA256SUMS.sign
   ```
   👉 Explication : récupère l'image, sa somme de contrôle et la signature; vérifier l'URL exacte sur https://www.debian.org/distrib/.

2. Ranger l'image dans le stockage ISO de l'hyperviseur (Proxmox : **Datacenter > Stockage > ISO Images > Upload**).
   👉 Explication : l'image devient sélectionnable à la création de la VM.

## 2. Production — Contrôles

Utiliser uniquement les sources officielles ou le miroir interne approuvé.

## 3. Production — Sécurité

Ne jamais utiliser une image tierce non vérifiée.

## Validation et retour arrière

- **Validation** : Fichier `.iso` présent et taille cohérente (`ls -lh`).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Debian 12](./Sommaire_-_Vie_du_systeme_Debian_12.md)
- [Documentation officielle](https://www.debian.org/doc/)
