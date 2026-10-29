# Fiche_Simple_-_Hote_Multi-OS_NAS_SAN_Tester_Correction_Sure.md

- **Environnement** : Hôte Linux client ou serveur de stockage (Samba, NFSv4, iSCSI) et baie/NAS
- **OS / Version** : Multi-OS; clients et serveurs Linux, appliance de stockage
- **Catégorie** : diagnostic / stockage
- **Tags** : `nas`, `san`, `samba`, `nfs`, `iscsi`, `multipath`, `diagnostic`

---

## Problème précis à résoudre

Appliquer et valider une correction sans risque pour les données.

## 1. Hors-Production (Lab / Test / POC)

1. Capturer logs et états avant changement :
   ```bash
   sudo journalctl --since "1 hour ago" --no-pager > diag-avant.txt
   lsblk -f > lsblk-avant.txt
   ```
   👉 Explication : les fichiers sont créés dans le répertoire courant; ils servent de preuve avant/après.

2. Tester lecture/écriture uniquement dans un répertoire approuvé (CHEMIN_DU_MONTAGE et nom d'exemple à remplacer) :
   ```bash
   echo test > CHEMIN_DU_MONTAGE/controle-unique.txt
   cat CHEMIN_DU_MONTAGE/controle-unique.txt
   rm CHEMIN_DU_MONTAGE/controle-unique.txt
   ```
   👉 Explication : on supprime uniquement ce fichier de contrôle.

3. Valider permissions, latence, intégrité, reprise après reconnexion et comportement des autres clients.
   👉 Explication : la correction ne doit pas dégrader les autres clients.

4. Pour une erreur de capacité, vérifier l'espace du pool, les quotas, les réservations et les snapshots sur la baie.
   👉 Explication : un snapshot peut retenir des blocs même si le partage paraît vide.

## 2. Production — Contrôles

Utiliser un nom de fichier unique et approuvé.

## 3. Production — Sécurité

- Ne pas supprimer de données de production pour tester.

## Validation et retour arrière

- **Validation** : Lecture/écriture OK, autres clients inchangés.
- **Retour arrière** : Annuler la correction et revenir à l'état capturé.

## Si le problème n'est pas résolu

- [Samba — Documentation officielle](https://www.samba.org/samba/docs/)
- [Linux man-pages — exports(5)](https://man7.org/linux/man-pages/man5/exports.5.html)
- [open-iscsi — Documentation du projet](https://github.com/open-iscsi/open-iscsi)
- [Guide complet diagnostic NAS/SAN Samba NFS iSCSI](../../../../02-Fiches-Completes/Transverses/Multi-OS/Diagnostic/38_Diagnostic_NAS_SAN_Samba_NFS_iSCSI.md#6-tester-une-correction-de-maniere-sure)
