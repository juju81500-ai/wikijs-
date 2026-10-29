# Fiche_Simple_-_Hote_Multi-OS_NAS_SAN_Diagnostiquer_iSCSI_Multipath.md

- **Environnement** : Hôte Linux client ou serveur de stockage (Samba, NFSv4, iSCSI) et baie/NAS
- **OS / Version** : Multi-OS; clients et serveurs Linux, appliance de stockage
- **Catégorie** : diagnostic / stockage

---

## Problème précis à résoudre

Contrôler sessions iSCSI et chemins multipath.

## 1. Hors-Production (Lab / Test / POC)

1. Lister sessions, chemins et disques :
   ```bash
   sudo iscsiadm -m session
   sudo multipath -ll
   lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
   ```
   👉 Explication : on compare aux IQN, LUN, ACL, VLAN et contrôleurs attendus.

2. Chercher les erreurs dans le journal :
   ```bash
   sudo journalctl -b --no-pager | grep -Ei 'iscsi|multipath|scsi|I/O error'
   ```
   👉 Explication : repère pertes de chemins et erreurs I/O.

3. Vérifier multipath et réservations persistantes selon la conception.
   👉 Explication : un chemin manquant doit être traité selon la procédure constructeur.

## 2. Production — Contrôles

Capturer les sorties avant toute action.

## 3. Production — Sécurité

- Si un chemin est perdu, ne pas déconnecter les autres chemins ni forcer une bascule sans procédure constructeur et validation de l'application.

## Validation et retour arrière

- **Validation** : Sessions et chemins conformes à la conception.
- **Retour arrière** : Aucune modification; commandes en lecture seule.

## Si le problème n'est pas résolu

- [Samba — Documentation officielle](https://www.samba.org/samba/docs/)
- [Linux man-pages — exports(5)](https://man7.org/linux/man-pages/man5/exports.5.html)
- [open-iscsi — Documentation du projet](https://github.com/open-iscsi/open-iscsi)
- [Guide complet diagnostic NAS/SAN Samba NFS iSCSI](/02-fiches-completes/transverses/multi-os/diagnostic/38-diagnostic-nas-san-samba-nfs-iscsi#5-diagnostiquer-iscsi-et-multipath)