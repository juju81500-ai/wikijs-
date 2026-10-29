# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_04_Preparation_Du_Support_D

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 04 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-04`

---

## Problème précis à résoudre

Rendre l'ISO démarrable sur un serveur physique.

## 1. Hors-Production (Lab / Test / POC)

1. Clé USB depuis Linux (remplacer `sdX` par la clé; **efface tout**) :
   ```sh
   lsblk -o NAME,SIZE,MODEL,TRAN
   sudo dd if=VMware-VMvisor-Installer-8.0.iso of=/dev/sdX bs=1M conv=fsync status=progress
   ```
   👉 Explication : écrit l'ISO en mode bloc; sous Windows, utiliser Rufus en mode DD.

2. Alternative : média virtuel dans la console de gestion (iDRAC : **Console virtuelle > Connecter le média virtuel > Mapper CD/DVD**; iLO : **Remote Console > Virtual Media**).
   👉 Explication : évite le déplacement sur site; l'ISO doit rester accessible durant l'installation.

3. Pour un hôte de test en VM (Workstation/Proxmox), monter l'ISO dans le lecteur CD de la VM (VM imbriquée : activer la virtualisation matérielle exposée).
   👉 Explication : ESXi en VM sert uniquement aux tests.

## 2. Production — Contrôles

Média virtuel pour les serveurs distants.

## 3. Production — Sécurité

Protéger l'accès à la console de gestion; effacer la clé après usage.

## Validation et retour arrière

- **Validation** : Le serveur démarre sur l'installateur ESXi.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
