# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_12_Fuseau_Horaire

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 12 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Régler le fuseau pour des journaux cohérents.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les données de fuseau et régler `Europe/Paris` :
   ```sh
   apk add tzdata
   setup-timezone -z Europe/Paris
   ```
   👉 Explication : écrit le lien `/etc/localtime` et `/etc/TZ`.

2. Contrôler l'heure locale :
   ```sh
   date
   ls -l /etc/localtime
   ```
   👉 Explication : affiche l'heure en CET/CEST et la cible du lien.

3. Conserver l'horloge matérielle en UTC (valeur par défaut d'Alpine) :
   ```sh
   hwclock -r
   ```
   👉 Explication : affiche l'heure matérielle; elle doit rester en UTC, la conversion étant faite par le système.

## 2. Production — Contrôles

Un seul fuseau pour tous les serveurs, validé par l'exploitation.

## 3. Production — Sécurité

Un fuseau erroné fausse la corrélation des journaux de sécurité.

## Validation et retour arrière

- **Validation** : `date` affiche l'heure locale attendue.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)