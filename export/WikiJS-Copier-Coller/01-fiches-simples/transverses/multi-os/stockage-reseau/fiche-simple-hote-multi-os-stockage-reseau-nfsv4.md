# Fiche_Simple_-_Hote_Multi_OS_Stockage_Reseau_NFSv4.md

- **Environnement** : Serveur de stockage Linux dédié (Debian) pour Samba, NFSv4 et iSCSI
- **OS / Version** : Multi-OS (serveur Linux Debian); paquets de la distribution
- **Catégorie** : stockage réseau

---

## Problème précis à résoudre

Exporter un chemin dédié en NFSv4 vers des clients explicites.

## 1. Hors-Production (Lab / Test / POC)

1. Installer le serveur NFS :
   ```bash
   sudo apt install nfs-kernel-server
   ```
   👉 Explication : le paquet fournit `nfs-server`.

2. Dans `/etc/exports`, ajouter une ligne d'export avec clients ou réseau explicites, par exemple `/srv/partage 192.0.2.0/24(rw,sync,no_subtree_check)` (le réseau est un exemple à remplacer).
   👉 Explication : seuls les clients attendus peuvent monter; éviter `no_root_squash` sauf exigence documentée.

3. Appliquer et afficher les exports :
   ```bash
   sudo exportfs -rav
   sudo exportfs -v
   ```
   👉 Explication : la table d'export est rechargée puis contrôlée.

4. Activer le service :
   ```bash
   sudo systemctl enable --now nfs-server
   ```
   👉 Explication : le serveur démarre au boot.

5. Depuis un client représentatif, monter l'export et contrôler les UID/GID.
   👉 Explication : on valide le modèle d'identité en conditions réelles.

## 2. Production — Contrôles

N'autoriser que les clients et flux nécessaires à la version NFS choisie.

## 3. Production — Sécurité

- Éviter `no_root_squash` sauf exigence documentée et contrôlée.
- Ne jamais exporter à `*` (tout le monde).

## Validation et retour arrière

- **Validation** : `exportfs -v` montre l'export attendu; le montage client fonctionne.
- **Retour arrière** : Retirer la ligne de `/etc/exports` puis `sudo exportfs -rav`.

## Si le problème n'est pas résolu

- [Samba — documentation](https://www.samba.org/samba/docs/)
- [Linux NFS — exports(5)](https://man7.org/linux/man-pages/man5/exports.5.html)
- [Guide complet — déployer NFSv4](/02-fiches-completes/transverses/multi-os/installation-deploiement/07-stockage-reseau-nas-san-samba-nfsv4-iscsi#3-deployer-nfsv4)