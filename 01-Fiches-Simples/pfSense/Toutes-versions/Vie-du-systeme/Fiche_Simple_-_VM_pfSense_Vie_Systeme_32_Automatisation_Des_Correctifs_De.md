# Fiche_Simple_-_VM_pfSense_Vie_Systeme_32_Automatisation_Des_Correctifs_De

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 32 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-32`

---

## Problème précis à résoudre

Être alerté des mises à jour et vulnérabilités.

## 1. Hors-Production (Lab / Test / POC)

1. Surveiller System > Update (le Dashboard signale la disponibilité d'une version via le widget Netgate Services And Support).
   👉 Explication : pfSense CE ne s'applique pas seul; la mise à jour reste une action contrôlée.

2. Rechercher les paquets vulnérables en shell :
   ```sh
   pkg-static audit -F
   pfSense-upgrade -c
   ```
   👉 Explication : télécharge la base de vulnérabilités et vérifie les mises à jour disponibles.

3. Programmer le contrôle avec le paquet Cron (Services > Cron) si une tâche de vérification est utile.
   👉 Explication : automatise l'alerte sans appliquer automatiquement.

## 2. Production — Contrôles

Appliquer les correctifs de sécurité dans une fenêtre de maintenance avec point de restauration.

## 3. Production — Sécurité

Appliquer sans délai les correctifs critiques exposant le WAN.

## Validation et retour arrière

- **Validation** : `pkg-static audit` ne signale aucune vulnérabilité ouverte.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire pfSense CE](./Sommaire_-_Vie_du_systeme_pfSense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
