# Fiche_Simple_-_TrueNAS_SCALE_25.10_Deploiement_Dimensionner_Preparer.md

- **Environnement** : NAS autonome pilote (matériel x86-64 ou VM de laboratoire)
- **OS / Version** : TrueNAS SCALE 25.10 Community Edition
- **Catégorie** : stockage NAS / cadrage
- **Tags** : `truenas`, `scale2510`, `zfs`, `nas`, `smb`, `sauvegarde`

---

## Problème précis à résoudre

Valider matériel, disques et réseau avant l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer 8 Go de RAM minimum, au moins deux disques de même capacité pour un miroir, un support de boot dédié (20 Go recommandé) et un accès console/IPMI.
   👉 Explication : conditions de la documentation TrueNAS.

2. Sur un hôte Linux de préparation ou depuis le Shell TrueNAS, lister les disques vus :
   ```bash
   lsblk -o NAME,SIZE,MODEL,SERIAL
   ```
   👉 Explication : les disques de données doivent être visibles directement (HBA/JBOD), sans RAID matériel masquant SMART.

3. Définir VLANs, DNS, NTP, certificats TLS, administrateurs, partage prévu et stratégie de chiffrement des datasets.
   👉 Explication : évite de redécouvrir ces choix après création du pool.

## 2. Production — Contrôles

Utiliser de l'ECC si possible; ne pas héberger de données critiques sur disques virtuels.

## 3. Production — Sécurité

- Pas de contrôleur RAID matériel masquant les disques.

## Validation et retour arrière

- **Validation** : Inventaire des disques et choix de design écrits.
- **Retour arrière** : Aucune modification ici.

## Si le problème n'est pas résolu

- [TrueNAS SCALE 25.10 — installation](https://www.truenas.com/docs/scale/25.10/gettingstarted/install/installingscale/)
- [TrueNAS SCALE 25.10 — guide matériel](https://www.truenas.com/docs/scale/25.10/gettingstarted/scalehardwareguide/)
- [Guide complet — 1. Dimensionner et préparer](../../../../../../02-Fiches-Completes/TrueNAS/SCALE-25.10/Installation-Deploiement/60_Deploiement_TrueNAS_SCALE_25.10.md#1-dimensionner-et-preparer)
