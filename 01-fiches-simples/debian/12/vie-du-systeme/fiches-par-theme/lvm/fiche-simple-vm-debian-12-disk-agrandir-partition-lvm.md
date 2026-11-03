# Agrandir un volume logique LVM sur Debian 12

- **Environnement** : VM ou serveur Debian 12 utilisant LVM
- **Catégorie** : Stockage / LVM
- **Tags** : `debian12`, `lvm`, `disque`, `resize`, `ext4`, `xfs`

## 🎯 Objectif et précautions

Agrandir un système de fichiers après augmentation du disque virtuel. Une extension n'est pas une sauvegarde et ne peut pas être annulée en restaurant un snapshot LVM de 1 Gio. Faire une sauvegarde vérifiée avant modification et garder la console hyperviseur accessible.

## 🧪 1. Diagnostic sans modification

```bash
df -hT /
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS
sudo pvs
sudo vgs
sudo lvs -a -o +devices
```
   👉 Explication : identifie disque, partition PV, groupe, LV et type de système de fichiers; ne rien modifier ici.

Identifier précisément le disque, la partition PV, le groupe, le LV et le type de système de fichiers. Ne pas recopier `/dev/sda3` ou `/dev/debian-vg/root` sans vérifier les sorties.

## ⚡ 2. Étendre le disque et le PV

1. Agrandir le disque virtuel depuis l'hyperviseur, avec une sauvegarde et une fenêtre de maintenance adaptées.
2. Relire la taille observée par Linux. Le rescanning dépend du bus et du nom du disque ; si nécessaire, utiliser la procédure de l'hyperviseur ou redémarrer pendant la fenêtre prévue.
3. Si le PV est une partition, installer `cloud-guest-utils` puis agrandir uniquement la partition PV identifiée. Exemple à adapter après contrôle :
   ```bash
   sudo growpart /dev/sda 3
   sudo partprobe /dev/sda
   ```
   👉 Explication : agrandit la partition PV; remplacer `/dev/sda` et `3` par les valeurs relevées.
4. Agrandir le PV et contrôler l'espace libre :
   ```bash
   sudo pvresize /dev/sda3
   sudo pvs
   sudo vgs
   ```
   👉 Explication : fait voir au PV et au groupe l'espace ajouté; remplacer `/dev/sda3`.

Si le PV est un disque entier, ne pas lancer `growpart`. Si les nouvelles tailles ne sont pas visibles, arrêter ici et vérifier la configuration de la VM.

## 🔒 3. Étendre le LV prudemment

Calculer l'espace souhaité avec `vgs` et choisir une taille explicite. L'exemple ci-dessous ajoute 10 Gio ; remplacer le chemin après vérification :

```bash
sudo lvextend -L +10G -r /dev/debian-vg/root
```
   👉 Explication : ajoute 10 Gio au LV et agrandit le système de fichiers (`-r`); remplacer le chemin.

`-r` demande à LVM de redimensionner le système de fichiers pris en charge. N'utiliser `+100%FREE` que si l'allocation de tout l'espace libre est voulue et documentée.

## ✅ 4. Vérifications

```bash
sudo lvs -o +devices
df -hT /
dmesg --level=err,warn | tail -50
```
   👉 Explication : confirme tailles attendues et absence d'erreur noyau.

Confirmer que le LV et le système de fichiers ont la taille attendue et que les services restent sains. Les systèmes XFS se développent avec leurs outils propres ; `-r` est préférable à une commande `resize2fs` codée en dur.

## Retour arrière

Une extension réussie n'a pas de retour arrière simple : réduire un système de fichiers comporte un risque de perte de données et n'est pas pris en charge par tous les types. En cas d'anomalie, ne pas supprimer un snapshot avec `lvremove -f` ni réduire le LV ; préserver l'état et restaurer la sauvegarde vérifiée si nécessaire.