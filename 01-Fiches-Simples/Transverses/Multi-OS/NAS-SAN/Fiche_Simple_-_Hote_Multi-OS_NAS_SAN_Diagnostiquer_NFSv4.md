# Fiche_Simple_-_Hote_Multi-OS_NAS_SAN_Diagnostiquer_NFSv4.md

- **Environnement** : Hôte Linux client ou serveur de stockage (Samba, NFSv4, iSCSI) et baie/NAS
- **OS / Version** : Multi-OS; clients et serveurs Linux, appliance de stockage
- **Catégorie** : diagnostic / stockage
- **Tags** : `nas`, `san`, `samba`, `nfs`, `iscsi`, `multipath`, `diagnostic`

---

## Problème précis à résoudre

Contrôler exports, service et montage NFSv4.

## 1. Hors-Production (Lab / Test / POC)

1. Sur le serveur, examiner exports, service et journaux :
   ```bash
   sudo exportfs -v
   sudo systemctl --no-pager status nfs-server
   sudo journalctl -u nfs-server --since "30 minutes ago" --no-pager
   ```
   👉 Explication : les exports actifs, l'état du service et les erreurs récentes.

2. Sur le client, vérifier version et options du montage (CHEMIN_DU_MONTAGE à remplacer) :
   ```bash
   nfsstat -m
   findmnt CHEMIN_DU_MONTAGE
   ```
   👉 Explication : vérifie la version NFS négociée et les options.

3. Contrôler le réseau autorisé dans l'export, la résolution du serveur, UID/GID, ACL et un éventuel problème de verrouillage.
   👉 Explication : causes fréquentes de refus d'accès.

## 2. Production — Contrôles

Corriger la cause réelle plutôt que d'élargir les droits.

## 3. Production — Sécurité

- Ne pas ajouter `no_root_squash` pour contourner un refus d'accès.

## Validation et retour arrière

- **Validation** : Export visible, service actif, montage avec la version attendue.
- **Retour arrière** : Restaurer `/etc/exports` depuis la copie et relancer `sudo exportfs -ra`.

## Si le problème n'est pas résolu

- [Samba — Documentation officielle](https://www.samba.org/samba/docs/)
- [Linux man-pages — exports(5)](https://man7.org/linux/man-pages/man5/exports.5.html)
- [open-iscsi — Documentation du projet](https://github.com/open-iscsi/open-iscsi)
- [Guide complet diagnostic NAS/SAN Samba NFS iSCSI](../../../../02-Fiches-Completes/Transverses/Multi-OS/Diagnostic/38_Diagnostic_NAS_SAN_Samba_NFS_iSCSI.md#4-diagnostiquer-nfsv4)
