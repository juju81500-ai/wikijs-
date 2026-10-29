# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_03_Verification_D_Integrite_Et

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 03 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

S'assurer que l'ISO n'est ni corrompue ni modifiée.

## 1. Hors-Production (Lab / Test / POC)

1. Calculer l'empreinte SHA256 de l'ISO :
   ```bash
   sha256sum TrueNAS-SCALE-*.iso
   ```
   👉 Explication : affiche l'empreinte à comparer.

2. Comparer avec la valeur publiée sur la page de téléchargement (fichier `.sha256` ou valeur affichée) :
   ```bash
   sha256sum -c TrueNAS-SCALE-VERSION.iso.sha256
   ```
   👉 Explication : répond `OK` si l'empreinte correspond ; VERSION est la version téléchargée.

3. Consigner l'empreinte validée dans le dossier du projet.
   👉 Explication : preuve de l'image utilisée.

## 2. Production — Contrôles

Refuser toute ISO dont l'empreinte diffère, la télécharger à nouveau.

## 3. Production — Sécurité

La comparaison doit se faire avec une valeur lue sur le site officiel, pas avec celle d'un tiers.

## Validation et retour arrière

- **Validation** : `sha256sum -c` affiche OK.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)