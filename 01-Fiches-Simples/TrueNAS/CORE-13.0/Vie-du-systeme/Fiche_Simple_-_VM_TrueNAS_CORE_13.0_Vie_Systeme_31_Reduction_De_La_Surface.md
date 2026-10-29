# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_31_Reduction_De_La_Surface

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 31 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-31`

---

## Problème précis à résoudre

Arrêter les services inutiles.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Services : désactiver et mettre à Off FTP, Telnet, SNMP, UPS si inutiles.
   ```sh
   midclt call service.query | grep -B3 -A3 '"enable": true'
   ```
   👉 Explication : liste les services démarrés au boot.

2. Désactiver un service :
   ```sh
   midclt call service.update SERVICE '{"enable": false}'
   midclt call service.stop SERVICE
   ```
   👉 Explication : SERVICE est par exemple `ftp` ou `snmp`.

## 2. Production — Contrôles

Documenter chaque service actif.

## 3. Production — Sécurité

Préférer SMB3 chiffré, NFSv4 et iSCSI avec CHAP.

## Validation et retour arrière

- **Validation** : Seuls les services nécessaires tournent.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
