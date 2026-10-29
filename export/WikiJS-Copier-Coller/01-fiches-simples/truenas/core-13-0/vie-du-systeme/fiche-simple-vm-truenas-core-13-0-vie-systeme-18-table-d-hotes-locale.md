# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_18_Table_D_Hotes_Locale

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 18 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Ajouter des correspondances locales.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Réseau > Configuration globale > Hosts (une ligne `IP nom`).
   ```sh
   midclt call network.configuration.update '{"hosts": ["ADRESSE NOM_HOTE"]}'
   ```
   👉 Explication : paire ADRESSE / NOM_HOTE à ajouter.

2. Contrôler :
   ```sh
   grep NOM_HOTE /etc/hosts
   ```
   👉 Explication : ligne générée par TrueNAS.

## 2. Production — Contrôles

Limiter aux cas indispensables.

## 3. Production — Sécurité

Ne pas modifier `/etc/hosts` directement.

## Validation et retour arrière

- **Validation** : `ping NOM_HOTE` résout.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)