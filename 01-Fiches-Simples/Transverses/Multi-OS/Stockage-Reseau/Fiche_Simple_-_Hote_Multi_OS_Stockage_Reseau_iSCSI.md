# Fiche_Simple_-_Hote_Multi_OS_Stockage_Reseau_iSCSI.md

- **Environnement** : Serveur de stockage Linux dédié (Debian) pour Samba, NFSv4 et iSCSI
- **OS / Version** : Multi-OS (serveur Linux Debian); paquets de la distribution
- **Catégorie** : stockage réseau
- **Tags** : `stockage`, `iscsi`, `targetcli`

---

## Problème précis à résoudre

Exporter un LUN vers un initiateur autorisé.

## 1. Hors-Production (Lab / Test / POC)

1. Réserver une adresse sur un réseau de stockage isolé.
   👉 Explication : le trafic iSCSI n'est pas chiffré par défaut.

2. Installer l'outil maintenu par la distribution :
   ```bash
   sudo apt install targetcli-fb
   ```
   👉 Explication : `targetcli` configure la cible LIO du noyau.

3. Ouvrir la console de configuration :
   ```bash
   sudo targetcli
   ```
   👉 Explication : on y crée le backstore, la cible, le LUN et les ACL (commande `ls` pour naviguer).

4. Autoriser uniquement l'IQN de l'initiateur prévu, puis vérifier chaque identifiant avant d'exporter.
   👉 Explication : une ACL stricte empêche d'autres hôtes de voir le volume.

5. Pour un multi-accès, utiliser un système de fichiers en cluster et un mécanisme de réservation compatibles.
   👉 Explication : un système de fichiers classique monté par plusieurs hôtes sera corrompu.

## 2. Production — Contrôles

Définir un initiateur propriétaire clair pour chaque LUN brute.

## 3. Production — Sécurité

- Ne pas monter le même système de fichiers classique en écriture depuis plusieurs hôtes.
- Isoler le réseau iSCSI.

## Validation et retour arrière

- **Validation** : `sudo targetcli ls` montre le LUN et l'ACL attendue.
- **Retour arrière** : Dans `targetcli`, supprimer l'ACL ou le LUN après déconnexion de l'initiateur.

## Si le problème n'est pas résolu

- [Samba — documentation](https://www.samba.org/samba/docs/)
- [Linux NFS — exports(5)](https://man7.org/linux/man-pages/man5/exports.5.html)
- [Guide complet — présenter une cible iSCSI](../../../../02-Fiches-Completes/Transverses/Multi-OS/Installation-Deploiement/07_Stockage_Reseau_NAS_SAN_Samba_NFSv4_iSCSI.md#4-presenter-une-cible-iscsi)
