# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_12_Fuseau_Horaire

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 12 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Régler le fuseau horaire de l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur : champ **Time zone** = Europe/Paris. Après installation (GUI : **Nœud > System > Time > Edit**) :
   ```bash
   timedatectl set-timezone Europe/Paris
   timedatectl
   ```
   👉 Explication : définit et affiche le fuseau actif.

2. Vérifier l'heure locale et UTC :
   ```bash
   date
   date -u
   ```
   👉 Explication : l'écart avec UTC doit correspondre à l'heure d'été ou d'hiver.

3. Appliquer le même fuseau sur tous les nœuds du cluster.
   👉 Explication : un fuseau différent complique la lecture des journaux croisés.

## 2. Production — Contrôles

Fuseau homogène sur tous les hôtes.

## 3. Production — Sécurité

Des horodatages cohérents sont indispensables à l'analyse d'incident.

## Validation et retour arrière

- **Validation** : `timedatectl` indique `Europe/Paris`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)