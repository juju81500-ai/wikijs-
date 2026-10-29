# Fiche_Simple_-_Hote_Multi-OS_NAS_SAN_Escalade_Cloture.md

- **Environnement** : Hôte Linux client ou serveur de stockage (Samba, NFSv4, iSCSI) et baie/NAS
- **OS / Version** : Multi-OS; clients et serveurs Linux, appliance de stockage
- **Catégorie** : diagnostic / stockage
- **Tags** : `nas`, `san`, `samba`, `nfs`, `iscsi`, `multipath`, `diagnostic`

---

## Problème précis à résoudre

Escalader correctement ou clôturer l'incident.

## 1. Hors-Production (Lab / Test / POC)

1. En cas d'erreurs matérielles, corruption, chemins multiples incohérents ou cluster non propriétaire, arrêter les écritures selon le runbook.
   👉 Explication : on évite l'aggravation.

2. Contacter l'équipe stockage/constructeur avec les sorties non sensibles, la topologie, les versions, les volumes impactés et la dernière sauvegarde vérifiée.
   👉 Explication : un dossier complet accélère le traitement.

3. Consigner la cause, la correction et la validation, puis clôturer.
   👉 Explication : on garde une trace pour la suite.

## 2. Production — Contrôles

Ne partager que des sorties expurgées.

## 3. Production — Sécurité

- Ne pas inclure de mots de passe ni de clés dans le ticket.

## Validation et retour arrière

- **Validation** : Escalade documentée ou incident clôturé avec preuves.
- **Retour arrière** : Reprendre les écritures suspendues uniquement après accord de l'équipe stockage.

## Si le problème n'est pas résolu

- [Samba — Documentation officielle](https://www.samba.org/samba/docs/)
- [Linux man-pages — exports(5)](https://man7.org/linux/man-pages/man5/exports.5.html)
- [open-iscsi — Documentation du projet](https://github.com/open-iscsi/open-iscsi)
- [Guide complet diagnostic NAS/SAN Samba NFS iSCSI](../../../../02-Fiches-Completes/Transverses/Multi-OS/Diagnostic/38_Diagnostic_NAS_SAN_Samba_NFS_iSCSI.md#7-escalade-et-cloture)
