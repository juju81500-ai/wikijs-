# Fiche_Simple_-_Hote_Multi-OS_NAS_SAN_Diagnostiquer_SMB_Samba.md

- **Environnement** : Hôte Linux client ou serveur de stockage (Samba, NFSv4, iSCSI) et baie/NAS
- **OS / Version** : Multi-OS; clients et serveurs Linux, appliance de stockage
- **Catégorie** : diagnostic / stockage
- **Tags** : `nas`, `san`, `samba`, `nfs`, `iscsi`, `multipath`, `diagnostic`

---

## Problème précis à résoudre

Contrôler la configuration, le service et l'accès Samba.

## 1. Hors-Production (Lab / Test / POC)

1. Sur le serveur Samba, contrôler configuration et service :
   ```bash
   sudo testparm -s
   sudo systemctl --no-pager status smbd
   sudo smbstatus
   sudo journalctl -u smbd --since "30 minutes ago" --no-pager
   ```
   👉 Explication : `testparm` valide `smb.conf`, `smbstatus` liste connexions et verrous.

2. Depuis un client autorisé, lister les partages (SERVEUR et UTILISATEUR sont des exemples à remplacer; le mot de passe est demandé de façon interactive) :
   ```bash
   smbclient -L //SERVEUR -U UTILISATEUR
   ```
   👉 Explication : vérifie découverte et authentification.

3. Contrôler le nom du partage, les ACL/permissions, la résolution DNS et le dialecte/signature SMB.
   👉 Explication : ce sont les causes courantes de refus.

## 2. Production — Contrôles

Ne pas assouplir la signature ou le chiffrement globalement pour rétablir un seul client incompatible.

## 3. Production — Sécurité

- Ne pas désactiver la signature SMB globalement.
- Ne pas ouvrir le partage à tous pour tester.

## Validation et retour arrière

- **Validation** : Service actif, configuration valide, client autorisé connecté.
- **Retour arrière** : Restaurer la copie de `/etc/samba/smb.conf` faite avant modification puis `sudo systemctl reload smbd`.

## Si le problème n'est pas résolu

- [Samba — Documentation officielle](https://www.samba.org/samba/docs/)
- [Linux man-pages — exports(5)](https://man7.org/linux/man-pages/man5/exports.5.html)
- [open-iscsi — Documentation du projet](https://github.com/open-iscsi/open-iscsi)
- [Guide complet diagnostic NAS/SAN Samba NFS iSCSI](../../../../02-Fiches-Completes/Transverses/Multi-OS/Diagnostic/38_Diagnostic_NAS_SAN_Samba_NFS_iSCSI.md#3-diagnostiquer-smbsamba)
