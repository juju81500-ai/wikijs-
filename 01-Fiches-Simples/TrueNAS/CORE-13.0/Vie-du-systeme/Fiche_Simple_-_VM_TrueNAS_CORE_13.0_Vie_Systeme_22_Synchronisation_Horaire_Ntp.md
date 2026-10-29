# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_22_Synchronisation_Horaire_Ntp

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 22 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-22`

---

## Problème précis à résoudre

Garder l'heure exacte.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Serveurs NTP > Ajouter.
   ```sh
   midclt call system.ntpserver.create '{"address": "SERVEUR_NTP", "prefer": true}'
   ```
   👉 Explication : SERVEUR_NTP est le serveur interne.

2. Vérifier :
   ```sh
   ntpq -p
   ```
   👉 Explication : une source marquée `*`.

## 2. Production — Contrôles

Au moins deux sources.

## 3. Production — Sécurité

Limiter NTP au réseau interne.

## Validation et retour arrière

- **Validation** : `ntpq -p` montre une source choisie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
