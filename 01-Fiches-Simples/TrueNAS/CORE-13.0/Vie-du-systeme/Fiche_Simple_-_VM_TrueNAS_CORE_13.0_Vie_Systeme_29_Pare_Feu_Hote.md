# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_29_Pare_Feu_Hote

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 29 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-29`

---

## Problème précis à résoudre

Limiter l'accès aux interfaces d'administration.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Général > Adresse IPv4 de l'interface web (liste d'écoute).
   ```sh
   midclt call system.general.update '{"ui_address": ["ADRESSE_NAS"]}'
   ```
   👉 Explication : limite l'écoute ; ne pas se couper l'accès.

2. Contrôler les ports ouverts :
   ```sh
   sockstat -4 -l
   ```
   👉 Explication : ports en écoute : 80/443, 22, 445, 2049, 3260.

## 2. Production — Contrôles

Filtrer sur le pare-feu réseau ; CORE n'a pas de pare-feu hôte configurable en GUI.

## 3. Production — Sécurité

Aucun port de stockage sur Internet.

## Validation et retour arrière

- **Validation** : Seuls les ports prévus sont ouverts.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
