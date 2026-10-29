# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_18_Table_D_Hotes_Locale

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 18 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-18`

---

## Problème précis à résoudre

Ajouter des correspondances locales indispensables.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Réseau > Paramètres globaux > Hôtes supplémentaires (une ligne `IP nom`).
   ```bash
   sudo midclt call network.configuration.update '{"hosts": ["ADRESSE NOM_HOTE"]}'
   ```
   👉 Explication : ADRESSE et NOM_HOTE sont une paire à ajouter (ex. contrôleur de domaine).

2. Contrôler :
   ```bash
   grep NOM_HOTE /etc/hosts
   ```
   👉 Explication : la ligne est générée par TrueNAS.

## 2. Production — Contrôles

Limiter aux cas où le DNS peut être indisponible.

## 3. Production — Sécurité

Ne pas modifier `/etc/hosts` directement : la modification serait perdue.

## Validation et retour arrière

- **Validation** : `getent hosts NOM_HOTE` répond.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./Sommaire_-_Vie_du_systeme_TrueNAS_SCALE_25.10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
