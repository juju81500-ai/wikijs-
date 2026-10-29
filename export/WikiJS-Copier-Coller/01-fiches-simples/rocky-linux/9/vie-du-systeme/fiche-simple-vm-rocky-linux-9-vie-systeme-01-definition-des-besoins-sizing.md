# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_01_Definition_Des_Besoins_Sizing

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 01 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Dimensionner la machine avant de la créer.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les ressources actuelles ou cibles :
   ```bash
   nproc
   free -h
   lsblk -o NAME,SIZE,TYPE
   uname -m
   ```
   👉 Explication : nombre de vCPU, RAM, disques et architecture (`x86_64` ou `aarch64`) pour comparer au besoin.

2. Mesurer les entrées/sorties d'une machine comparable :
   ```bash
   sudo dnf install -y sysstat
   iostat -x 1 5
   ```
   👉 Explication : `%util` et `await` élevés indiquent un stockage à surdimensionner.

3. Noter vCPU, RAM, disque, IOPS, réseau et architecture dans le dossier du projet.
   👉 Explication : ce tableau sert de référence pour l'hyperviseur et pour la recette (Rocky 9 exige un CPU x86-64-v2 au minimum).

## 2. Production — Contrôles

Ajouter 20 à 30 % de marge, valider le dimensionnement avec le propriétaire du service.

## 3. Production — Sécurité

Prévoir un volume séparé pour `/var` ou les données si le service écrit beaucoup.

## Validation et retour arrière

- **Validation** : Tableau de sizing signé et conservé avec le dossier.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)