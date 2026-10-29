# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_03_Verification_D_Integrite_Et

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 03 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-03`

---

## Problème précis à résoudre

S'assurer que l'ISO n'est pas corrompue.

## 1. Hors-Production (Lab / Test / POC)

1. Calculer l'empreinte SHA256 :
   ```sh
   sha256 TrueNAS-13.0*.iso
   ```
   👉 Explication : sous FreeBSD, `sha256` ; sous Linux, `sha256sum`.

2. Comparer avec la valeur publiée sur la page officielle :
   ```sh
   cat TrueNAS-13.0*.iso.sha256
   ```
   👉 Explication : les deux valeurs doivent être identiques.

3. Consigner l'empreinte validée.
   👉 Explication : preuve de l'image utilisée.

## 2. Production — Contrôles

Refuser toute ISO dont l'empreinte diffère.

## 3. Production — Sécurité

Lire l'empreinte sur le site officiel, pas chez un tiers.

## Validation et retour arrière

- **Validation** : Empreintes identiques.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
