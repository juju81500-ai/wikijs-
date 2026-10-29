# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_40_Configuration_Des_Sauvegardes

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 40 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-40`

---

## Problème précis à résoudre

Mettre en place une sauvegarde chiffrée.

## 1. Hors-Production (Lab / Test / POC)

1. Installer restic (EPEL) :
   ```bash
   sudo dnf install -y epel-release
   sudo dnf install -y restic
   ```
   👉 Explication : outil de sauvegarde chiffré et dédupliqué.

2. Initialiser le dépôt (adapter `/srv/sauvegardes/restic`) :
   ```bash
   export RESTIC_PASSWORD_FILE=/root/.restic-pass
   sudo -E restic init -r /srv/sauvegardes/restic
   ```
   👉 Explication : le mot de passe est dans un fichier `600` du coffre-fort, jamais sur la ligne de commande.

3. Lancer une sauvegarde :
   ```bash
   sudo -E restic -r /srv/sauvegardes/restic backup /etc /var/lib /home
   ```
   👉 Explication : sauvegarde configuration et données.

## 2. Production — Contrôles

Règle 3-2-1 et sauvegarde hors site.

## 3. Production — Sécurité

Chiffrer et protéger la clé; sauvegarder aussi les contextes SELinux (`--xattr` ou `tar --selinux`).

## Validation et retour arrière

- **Validation** : `restic snapshots` liste le snapshot.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Rocky 9 Sauvegarde Restic Depot](<../Vie-du-logiciel/Restic/Fiche_Simple_-_VM_Rocky_9_Sauvegarde_Restic_Depot.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
