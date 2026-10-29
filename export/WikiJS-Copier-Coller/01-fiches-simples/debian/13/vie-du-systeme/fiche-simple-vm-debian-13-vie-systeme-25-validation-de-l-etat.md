# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_25_Validation_De_L_Etat

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 25 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Figer un état propre.

## 1. Hors-Production (Lab / Test / POC)

1. Nettoyer et arrêter proprement :
   ```bash
   sudo apt clean
   sudo journalctl --vacuum-time=1d
   sudo poweroff
   ```
   👉 Explication : supprime les caches puis arrête la VM.

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

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 13](/01-fiches-simples/debian/13/vie-du-systeme/sommaire-vie-du-systeme-debian-13)
- [Documentation officielle](https://www.debian.org/doc/)