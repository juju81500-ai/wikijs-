# 📄 Fiche_Simple_-_VM_Rocky_9_Stockage_Etendre_LVM_XFS.md

- **Environnement** : VM Rocky Linux dont le disque virtuel a déjà été agrandi
- **OS / Version** : Rocky Linux 9 / RHEL 9 avec LVM et XFS ou ext4
- **Catégorie** : Stockage / Maintenance

## 🎯 Problème précis à résoudre
Étendre un système de fichiers existant après l'agrandissement du disque virtuel, en distinguant un PV sur disque entier d'un PV dans une partition.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever les tailles et la topologie avant changement :
   ```bash
   lsblk -f
   sudo pvs
   sudo vgs
   sudo lvs -a -o +devices
   df -hT
   ```
2. Si le PV est sur le disque entier, redimensionner ce PV, puis le volume logique et son système de fichiers :
   ```bash
   sudo pvresize /dev/<disque-pv>
   sudo lvextend -r -L +10G /dev/<vg>/<lv>
   ```
   👉 *Explication : `-r` demande l'extension du système de fichiers avec le volume logique; confirmer le nom du PV, du VG et du LV avant exécution.*

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder les données, confirmer que l'hyperviseur a agrandi le bon disque et vérifier la capacité non allouée avec `lsblk`.
2. Si le PV utilise une partition, installer l'outil et agrandir la partition concernée :
   ```bash
   sudo dnf install cloud-utils-growpart
   sudo growpart /dev/<disque> <numero-partition>
   sudo pvresize /dev/<partition-pv>
   ```
   Si le PV occupe directement le disque, ne pas lancer `growpart`; exécuter seulement `pvresize /dev/<disque-pv>`.
3. Étendre le LV et vérifier le système de fichiers :
   ```bash
   sudo lvextend -r -L +10G /dev/<vg>/<lv>
   lsblk -f
   df -hT <point-de-montage>
   ```
   👉 *Explication : XFS s'agrandit, mais ne se réduit pas. Adapter la taille au VG disponible et au besoin réel.*

## 🔒 3. Production — Façon Sécurisée
1. Ne jamais utiliser `mkfs` pour agrandir un système de fichiers existant; cela le reformate et détruit les données.
2. Comparer les tailles avant/après et conserver un accès console. Éviter de modifier une partition montée sans comprendre la table et l'ordre des partitions.
3. En cas de disque partagé ou multipath, suivre la procédure du stockage concerné avant `pvresize`.

## ✅ Validation et retour arrière
- Confirmer `pvs`, `lvs`, `lsblk -f` et `df -hT` après l'opération; réaliser un test applicatif.
- L'extension ne possède pas de retour arrière simple; restaurer depuis une sauvegarde si le système de fichiers est endommagé.
- Ne pas supprimer le disque ni le LV avant d'avoir validé les données.