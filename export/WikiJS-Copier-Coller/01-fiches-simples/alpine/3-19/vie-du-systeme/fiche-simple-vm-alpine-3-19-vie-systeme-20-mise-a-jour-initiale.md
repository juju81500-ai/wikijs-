# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_20_Mise_A_Jour_Initiale

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 20 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Appliquer tous les correctifs disponibles.

## 1. Hors-Production (Lab / Test / POC)

1. Mettre à jour l'index et lister les mises à jour :
   ```sh
   doas apk update
   apk version -l '<'
   ```
   👉 Explication : `apk version -l '<'` liste les paquets installés dont une version plus récente existe.

2. Appliquer les mises à jour :
   ```sh
   doas apk upgrade
   ```
   👉 Explication : met à jour tous les paquets vers la dernière version de 3.19.

3. Redémarrer si le noyau a changé, puis comparer :
   ```sh
   uname -r
   ls /lib/modules
   doas reboot
   ```
   👉 Explication : si `uname -r` diffère du dossier de `/lib/modules`, un redémarrage est nécessaire.

4. Pour un système en mode diskless ou data, enregistrer l'état :
   ```sh
   doas lbu commit
   ```
   👉 Explication : écrit la configuration modifiée dans l'archive `.apkovl`; inutile en mode `sys`.

## 2. Production — Contrôles

Programmer une fenêtre de maintenance et sauvegarder avant.

## 3. Production — Sécurité

Lire la liste des paquets avant d'accepter les mises à jour de noyau.

## Validation et retour arrière

- **Validation** : `apk version -l '<'` ne retourne plus rien.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)