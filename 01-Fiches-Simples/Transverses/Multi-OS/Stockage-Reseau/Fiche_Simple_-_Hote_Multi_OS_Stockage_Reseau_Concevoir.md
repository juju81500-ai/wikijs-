# Fiche_Simple_-_Hote_Multi_OS_Stockage_Reseau_Concevoir.md

- **Environnement** : Serveur de stockage Linux dédié (Debian) pour Samba, NFSv4 et iSCSI
- **OS / Version** : Multi-OS (serveur Linux Debian); paquets de la distribution
- **Catégorie** : stockage réseau
- **Tags** : `stockage`, `conception`

---

## Problème précis à résoudre

Définir clients, droits, protocole et protection avant de créer le moindre partage.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les clients, droits, plan d'adressage, protocole, capacité, snapshots, sauvegarde et scénario de restauration.
   👉 Explication : on choisit Samba (clients SMB), NFSv4 (clients Unix) ou iSCSI (blocs) selon le besoin.

2. Ne pas présenter un même système de fichiers en NFS/SMB et en LUN iSCSI simultanément.
   👉 Explication : un montage concurrent incompatible peut corrompre les données.

3. Contrôler les volumes disponibles :
   ```bash
   lsblk -f
   df -h
   ```
   👉 Explication : on repère les disques et l'espace pour les volumes dédiés.

4. Créer un point de montage dédié par usage (exemple `/srv/partage`, à adapter) :
   ```bash
   sudo mkdir -p /srv/partage
   ```
   👉 Explication : un volume séparé évite qu'un partage plein sature le système.

## 2. Production — Contrôles

Mettre en place supervision d'espace et protection contre la saturation; chiffrer les flux sur réseaux non fiables.

## 3. Production — Sécurité

- Chiffrer les flux sur les réseaux non fiables.
- Séparer le réseau de stockage du réseau utilisateur.

## Validation et retour arrière

- **Validation** : Plan documenté : clients, droits, protocole, capacité et sauvegarde.
- **Retour arrière** : `sudo rmdir /srv/partage` si le dossier est inutilisé.

## Si le problème n'est pas résolu

- [Samba — documentation](https://www.samba.org/samba/docs/)
- [Linux NFS — exports(5)](https://man7.org/linux/man-pages/man5/exports.5.html)
- [Guide complet — concevoir avant d'installer](../../../../02-Fiches-Completes/Transverses/Multi-OS/Installation-Deploiement/07_Stockage_Reseau_NAS_SAN_Samba_NFSv4_iSCSI.md#1-concevoir-avant-dinstaller)
