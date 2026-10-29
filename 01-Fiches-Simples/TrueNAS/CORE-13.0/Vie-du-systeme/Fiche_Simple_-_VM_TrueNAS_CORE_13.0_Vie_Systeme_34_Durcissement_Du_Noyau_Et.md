# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_34_Durcissement_Du_Noyau_Et

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 34 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-34`

---

## Problème précis à résoudre

Appliquer des réglages sûrs.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Tunables > Ajouter (variable, valeur, type sysctl).
   ```sh
   sysctl net.inet.tcp.blackhole
   midclt call tunable.create '{"type": "SYSCTL", "var": "net.inet.tcp.blackhole", "value": "2"}'
   ```
   👉 Explication : ajoute un réglage persistant ; `sysctl` seul serait perdu au redémarrage.

2. Vérifier :
   ```sh
   sysctl net.inet.tcp.blackhole
   ```
   👉 Explication : valeur active.

## 2. Production — Contrôles

Ne régler que les paramètres documentés.

## 3. Production — Sécurité

Éviter les modifications non supportées.

## Validation et retour arrière

- **Validation** : Valeurs conformes.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
