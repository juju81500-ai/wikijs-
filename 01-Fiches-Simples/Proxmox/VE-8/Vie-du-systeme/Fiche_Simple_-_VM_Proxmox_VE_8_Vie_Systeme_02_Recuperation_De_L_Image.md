# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_02_Recuperation_De_L_Image

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 02 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-02`

---

## Problème précis à résoudre

Obtenir l'ISO officielle de Proxmox VE 8.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'ISO depuis le site officiel (GUI : navigateur, https://www.proxmox.com/en/downloads > Proxmox Virtual Environment > ISO Images) ou en ligne de commande (remplacer `X.Y-Z` par la version choisie) :
   ```bash
   curl -LO https://enterprise.proxmox.com/iso/proxmox-ve_X.Y-Z.iso
   curl -LO https://enterprise.proxmox.com/iso/SHA256SUMS
   ```
   👉 Explication : récupère l'image et le fichier des empreintes depuis le serveur officiel Proxmox.

2. Contrôler la taille du fichier :
   ```bash
   ls -lh proxmox-ve_*.iso
   ```
   👉 Explication : une taille anormalement petite indique un téléchargement interrompu.

3. Ranger l'ISO dans un dépôt interne avec sa version.
   👉 Explication : garantit que tous les nœuds du cluster sont installés avec la même version.

## 2. Production — Contrôles

Utiliser un dépôt d'images interne; installer tous les nœuds d'un cluster avec la même version majeure.

## 3. Production — Sécurité

Télécharger uniquement depuis proxmox.com, en HTTPS.

## Validation et retour arrière

- **Validation** : ISO et fichier SHA256SUMS présents, taille cohérente.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Proxmox VE 8](./Sommaire_-_Vie_du_systeme_Proxmox_VE_8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
