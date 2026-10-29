# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_02_Recuperation_De_L_Image

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 02 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-02`

---

## Problème précis à résoudre

Obtenir l'ISO officielle d'Alpine Linux 3.19.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'ISO « virt » (VM) ou « standard » (matériel) avec sa somme de contrôle et sa signature (remplacer `PATCH` par le numéro de correctif publié, par exemple celui affiché dans le répertoire du miroir) :
   ```sh
   curl -LO https://dl-cdn.alpinelinux.org/alpine/v3.19/releases/x86_64/alpine-virt-3.19.PATCH-x86_64.iso
   curl -LO https://dl-cdn.alpinelinux.org/alpine/v3.19/releases/x86_64/alpine-virt-3.19.PATCH-x86_64.iso.sha256
   curl -LO https://dl-cdn.alpinelinux.org/alpine/v3.19/releases/x86_64/alpine-virt-3.19.PATCH-x86_64.iso.asc
   ```
   👉 Explication : récupère l'image, son empreinte SHA-256 et sa signature GPG; `virt` embarque le noyau optimisé pour les machines virtuelles, `standard` convient au matériel.

2. Contrôler la taille et la date du fichier :
   ```sh
   ls -lh alpine-virt-3.19.*-x86_64.iso
   ```
   👉 Explication : l'ISO virt fait quelques dizaines de Mo; une taille anormalement petite indique un téléchargement interrompu.

3. Ranger l'ISO dans un dépôt interne avec sa version.
   👉 Explication : garantit que la même image sert à tous les déploiements.

## 2. Production — Contrôles

Utiliser un miroir interne ou un dépôt d'images contrôlé.

## 3. Production — Sécurité

Ne télécharger que depuis `alpinelinux.org` ou un miroir listé sur ce site, en HTTPS.

## Validation et retour arrière

- **Validation** : ISO, fichier `.sha256` et fichier `.asc` présents, taille cohérente.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
