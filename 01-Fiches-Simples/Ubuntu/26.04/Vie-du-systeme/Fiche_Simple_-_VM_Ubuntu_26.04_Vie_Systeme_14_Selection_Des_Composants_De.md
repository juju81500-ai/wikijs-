# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_14_Selection_Des_Composants_De

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 14 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-14`

---

## Problème précis à résoudre

Installer le strict nécessaire.

## 1. Hors-Production (Lab / Test / POC)

1. À l'installation, choisir **Ubuntu Server** (ou **Ubuntu Server (minimized)**) et cocher **Install OpenSSH server**; ne cocher aucun snap serveur inutile. Après installation, contrôler :
   ```bash
   systemctl list-units --type=service --state=running
   apt list --installed 2>/dev/null | wc -l
   snap list
   ```
   👉 Explication : liste les services actifs, le nombre de paquets et les snaps installés.

2. Conserver la configuration d'installation pour automatiser les prochaines VM (autoinstall) :
   ```bash
   sudo ls -l /var/log/installer/autoinstall-user-data
   ```
   👉 Explication : ce fichier YAML décrit l'installation et sert de base à un autoinstall; il contient un condensé de mot de passe : ne pas le diffuser tel quel.

## 2. Production — Contrôles

Ne pas installer d'environnement de bureau sur un serveur.

## 3. Production — Sécurité

Moins de paquets = moins de surface d'attaque.

## Validation et retour arrière

- **Validation** : Seuls SSH et les services de base tournent.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Ubuntu 26.04](./Sommaire_-_Vie_du_systeme_Ubuntu_26.04.md)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
