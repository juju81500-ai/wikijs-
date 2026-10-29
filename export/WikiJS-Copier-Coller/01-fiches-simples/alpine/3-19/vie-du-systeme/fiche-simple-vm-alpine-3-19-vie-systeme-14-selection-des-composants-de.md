# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_14_Selection_Des_Composants_De

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 14 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Installer l'ensemble minimal utile, sans paquet inutile.

## 1. Hors-Production (Lab / Test / POC)

1. Installer le serveur SSH et l'enregistrer au démarrage :
   ```sh
   setup-sshd -c openssh
   ```
   👉 Explication : installe OpenSSH et l'active (`-c` choisit le serveur : `openssh`, `dropbear` ou `none`).

2. Installer la synchronisation de l'heure :
   ```sh
   setup-ntp chrony
   ```
   👉 Explication : installe `chrony` et l'active; détaillé à l'étape 22.

3. Lister les paquets installés :
   ```sh
   apk info | sort | head -50
   ```
   👉 Explication : permet de relever la liste de base et de repérer ce qui est inutile.

## 2. Production — Contrôles

Garder l'ensemble minimal; chaque paquet est une surface d'attaque et un correctif de plus.

## 3. Production — Sécurité

Ne pas installer de compilateur, de client FTP ou de telnet sans besoin.

## Validation et retour arrière

- **Validation** : SSH fonctionne, `apk info` ne contient que le nécessaire.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)