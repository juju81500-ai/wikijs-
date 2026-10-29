# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_25_Validation_De_L_Etat

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 25 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-25`

---

## Problème précis à résoudre

Figer un état propre.

## 1. Hors-Production (Lab / Test / POC)

1. Nettoyer, réinitialiser cloud-init pour un futur modèle et arrêter proprement :
   ```bash
   sudo apt clean
   sudo journalctl --vacuum-time=1d
   sudo cloud-init clean --logs
   sudo poweroff
   ```
   👉 Explication : supprime les caches et l'état cloud-init (cloud-init rejouera au prochain démarrage; ne pas l'exécuter sur une machine à conserver telle quelle).

2. Créer le snapshot (Proxmox : **VM > Snapshots > Take Snapshot**, nom `01-CLEAN-INSTALL`) :
   ```bash
   qm snapshot VMID 01-CLEAN-INSTALL --description "Installation propre"
   ```
   👉 Explication : remplacer `VMID`; sert de point de retour.

## 2. Production — Contrôles

Convertir en modèle seulement après nettoyage (machine-id, clés SSH).

## 3. Production — Sécurité

Le modèle ne doit contenir ni secret ni clé privée.

## Validation et retour arrière

- **Validation** : `qm listsnapshot VMID` montre le snapshot.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Ubuntu 26.04](./Sommaire_-_Vie_du_systeme_Ubuntu_26.04.md)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
