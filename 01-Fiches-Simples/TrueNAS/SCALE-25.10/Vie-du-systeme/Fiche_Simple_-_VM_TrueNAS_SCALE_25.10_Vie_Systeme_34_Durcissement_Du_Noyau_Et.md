# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_34_Durcissement_Du_Noyau_Et

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 34 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-34`

---

## Problème précis à résoudre

Appliquer les réglages réseau sûrs.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Avancé > Sysctl > Ajouter (variable, valeur).
   ```bash
   sudo sysctl net.ipv4.conf.all.rp_filter
   sudo midclt call tunable.create '{"type": "SYSCTL", "var": "net.ipv4.conf.all.rp_filter", "value": "1"}'
   ```
   👉 Explication : ajoute un réglage persistant par l'interface de TrueNAS.

2. Vérifier :
   ```bash
   sudo sysctl net.ipv4.conf.all.rp_filter
   ```
   👉 Explication : valeur active.

## 2. Production — Contrôles

Ne régler que les paramètres documentés par iXsystems.

## 3. Production — Sécurité

Éviter toute modification non supportée.

## Validation et retour arrière

- **Validation** : Valeurs conformes à la politique.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./Sommaire_-_Vie_du_systeme_TrueNAS_SCALE_25.10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
