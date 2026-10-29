# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_12_Fuseau_Horaire

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 12 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-12`

---

## Problème précis à résoudre

Aligner l'horodatage.

## 1. Hors-Production (Lab / Test / POC)

1. ESXi travaille en UTC : il n'y a pas de fuseau local à définir. Contrôler :
   ```sh
   date
   date -u
   esxcli hardware clock get
   ```
   👉 Explication : les deux premières sorties doivent être identiques (UTC).

2. Les journaux et le Host Client affichent l'heure en UTC; l'adapter dans l'interprétation (Paris = UTC+1 ou +2).
   👉 Explication : évite les erreurs lors de la corrélation avec d'autres journaux.

3. Régler l'heure matérielle si besoin (rare) :
   ```sh
   esxcli hardware clock set -y ANNEE -M MOIS -d JOUR -H HEURE -m MIN -s SEC
   ```
   👉 Explication : valeurs en UTC; à éviter si NTP est configuré.

## 2. Production — Contrôles

Documenter que l'hôte est en UTC.

## 3. Production — Sécurité

Heure fiable pour l'audit et les certificats.

## Validation et retour arrière

- **Validation** : `date` et `date -u` identiques.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
