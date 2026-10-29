# Fiche_Simple_-_TrueNAS_CORE_13.0_Deploiement_Prerequis.md

- **Environnement** : Appliance TrueNAS CORE (FreeBSD) en VM de laboratoire ou NAS existant
- **OS / Version** : TrueNAS CORE, branche 13.0 (build exact à relever sur l'ISO)
- **Catégorie** : stockage NAS / prérequis

---

## Problème précis à résoudre

Réunir matériel ou VM conforme et une ISO vérifiée.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier : x86-64 2 cœurs, 8 Go de RAM, disque de boot SSD 16 Go, au moins deux disques de données de même taille (pas de SMR, pas de clé USB en boot, pas de pool sur un seul disque).
   👉 Explication : conditions de la documentation matérielle CORE 13.0.

2. En VM de test : 8 Go de RAM, disque système de 20 Go, au moins un disque de données de 4 Go, réseau en bridge, OS invité FreeBSD 64 bits, démarrage BIOS sous VMware.
   👉 Explication : paramètres de VM recommandés par la documentation.

3. Télécharger l'ISO depuis la source officielle iXsystems puis calculer son empreinte (Linux) :
   ```bash
   sha256sum TrueNAS-13.0.iso
   ```
   👉 Explication : (nom de fichier d'exemple à remplacer) à comparer avec l'empreinte publiée au même endroit.

4. Équivalent Windows :
   ```powershell
   Get-FileHash .\TrueNAS-13.0.iso -Algorithm SHA256
   ```
   👉 Explication : même contrôle; si aucune empreinte n'est publiée, arrêter et escalader.

## 2. Production — Contrôles

Présenter les disques bruts à ZFS (pas de RAID matériel).

## 3. Production — Sécurité

- Ne pas utiliser une ISO dont l'empreinte ne correspond pas.

## Validation et retour arrière

- **Validation** : L'empreinte correspond à celle publiée.
- **Retour arrière** : Supprimer l'ISO douteuse et la retélécharger.

## Si le problème n'est pas résolu

- [TrueNAS — documentation CORE 13.0](https://www.truenas.com/docs/core/13.0/)
- [TrueNAS — Software Status](https://www.truenas.com/docs/softwarestatus/)
- [Guide complet — 2. Prérequis](/02-fiches-completes/truenas/core-13-0/installation-deploiement/89-deploiement-truenas-core-13-0#2-prerequis)