# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_21_Pilotes_Et_Agents_De

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 21 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Optimiser le NAS lorsqu'il est une VM ou ajouter des pilotes matériels.

## 1. Hors-Production (Lab / Test / POC)

1. Sur une VM, présenter les disques par passthrough du contrôleur (PCI passthrough HBA) plutôt que des disques virtuels.
   ```bash
   lspci | grep -i -E 'sas|sata|nvme'
   ```
   👉 Explication : ZFS accède directement aux disques physiques.

2. Activer l'agent invité si disponible : Applications ou service QEMU guest agent selon l'hyperviseur.
   ```bash
   systemctl status qemu-guest-agent
   ```
   👉 Explication : peut être absent sur l'appliance.

3. Contrôler le matériel détecté :
   ```bash
   lsblk -d -o NAME,MODEL,SIZE
   sudo dmesg | grep -i -E 'error|fail' | tail
   ```
   👉 Explication : disques et erreurs de pilotes.

## 2. Production — Contrôles

Préférer un NAS sur matériel dédié ; en VM, passthrough HBA obligatoire.

## 3. Production — Sécurité

Ne pas installer de pilotes tiers sur l'appliance.

## Validation et retour arrière

- **Validation** : Tous les disques sont visibles.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)