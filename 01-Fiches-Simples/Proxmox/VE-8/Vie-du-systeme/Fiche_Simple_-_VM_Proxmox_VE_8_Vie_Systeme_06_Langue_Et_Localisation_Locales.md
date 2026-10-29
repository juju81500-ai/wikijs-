# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_06_Langue_Et_Localisation_Locales

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 06 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-06`

---

## Problème précis à résoudre

Choisir la langue et le pays de l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur : écran **Country / Time zone / Keyboard Layout** : pays = France.
   👉 Explication : renseigne langue, fuseau et clavier de l'hôte en une étape.

2. Après installation, vérifier les locales :
   ```bash
   locale
   locale -a | head
   ```
   👉 Explication : affiche la langue active et les locales générées.

3. Générer au besoin `fr_FR.UTF-8` :
   ```bash
   dpkg-reconfigure locales
   localectl set-locale LANG=fr_FR.UTF-8
   ```
   👉 Explication : génère la locale puis la définit comme défaut.

## 2. Production — Contrôles

Garder l'hôte en `en_US.UTF-8` ou `fr_FR.UTF-8` de façon homogène sur tout le cluster.

## 3. Production — Sécurité

Une locale UTF-8 évite les erreurs d'encodage dans les journaux.

## Validation et retour arrière

- **Validation** : `locale` affiche la valeur choisie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Proxmox VE 8](./Sommaire_-_Vie_du_systeme_Proxmox_VE_8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
