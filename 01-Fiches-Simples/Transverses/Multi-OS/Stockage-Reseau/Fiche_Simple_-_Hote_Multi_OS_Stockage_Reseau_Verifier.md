# Fiche_Simple_-_Hote_Multi_OS_Stockage_Reseau_Verifier.md

- **Environnement** : Serveur de stockage Linux dédié (Debian) pour Samba, NFSv4 et iSCSI
- **OS / Version** : Multi-OS (serveur Linux Debian); paquets de la distribution
- **Catégorie** : stockage réseau
- **Tags** : `stockage`, `validation`, `sauvegarde`

---

## Problème précis à résoudre

Tester accès, refus, supervision et restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Tester lecture et écriture depuis un client autorisé.
   👉 Explication : on valide l'accès nominal.

2. Tester le refus d'accès depuis un client non autorisé.
   👉 Explication : on valide la restriction.

3. Surveiller capacité et état disque :
   ```bash
   df -h /srv/partage
   sudo journalctl -p err -b --no-pager
   ```
   👉 Explication : on repère saturation et erreurs disque.

4. Sauvegarder les données indépendamment du serveur et tester la restauration.
   👉 Explication : un partage sans sauvegarde testée est un risque.

5. Planifier toute modification d'export ou de LUN.
   👉 Explication : les clients peuvent perdre des écritures ou se bloquer.

## 2. Production — Contrôles

Surveiller latence, erreurs disque, capacité, permissions et disponibilité.

## 3. Production — Sécurité

- Ne pas modifier d'export ou de LUN hors fenêtre de maintenance.

## Validation et retour arrière

- **Validation** : Accès autorisé OK, accès non autorisé refusé, restauration testée.
- **Retour arrière** : Rétablir la configuration précédente sauvegardée de `smb.conf`, `/etc/exports` ou `targetcli`.

## Si le problème n'est pas résolu

- [Samba — documentation](https://www.samba.org/samba/docs/)
- [Linux NFS — exports(5)](https://man7.org/linux/man-pages/man5/exports.5.html)
- [Guide complet — vérifier et protéger](../../../../02-Fiches-Completes/Transverses/Multi-OS/Installation-Deploiement/07_Stockage_Reseau_NAS_SAN_Samba_NFSv4_iSCSI.md#5-verifier-et-proteger)
