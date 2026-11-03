# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_23_Outils_D_Administration_Fondamentaux

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 23 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-23`

---

## Problème précis à résoudre

Connaître les outils intégrés au [[Glossary:NAS]].

## 1. Hors-Production (Lab / Test / POC)

1. Utiliser la console de l'interface : Système > Shell (ou [[Glossary:SSH]]) pour les commandes [[Glossary:ZFS]] :
   ```bash
   sudo zpool list
   sudo zfs list
   sudo smartctl --scan
   ```
   👉 Explication : pools, jeux de données et disques.

2. Utiliser le [[Glossary:CLI]] TrueNAS :
   ```bash
   cli -c 'storage pool query name,status'
   ```
   👉 Explication : interroge l'[[Glossary:API]] en mode texte.

3. Utiliser l'API en ligne de commande :
   ```bash
   sudo midclt call system.info | python3 -m json.tool | head
   ```
   👉 Explication : informations système.

## 2. Production — Contrôles

Documenter les commandes autorisées en exploitation.

## 3. Production — Sécurité

Réserver les modifications à la [[Glossary:GUI]] ou à `midclt`, éviter les modifications manuelles ZFS sur un pool géré.

## Validation et retour arrière

- **Validation** : Les commandes de consultation répondent.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-administration/01-gouvernance-architecture/vie-du-systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./sommaire-vie-du-systeme-truenas-scale-25-10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
