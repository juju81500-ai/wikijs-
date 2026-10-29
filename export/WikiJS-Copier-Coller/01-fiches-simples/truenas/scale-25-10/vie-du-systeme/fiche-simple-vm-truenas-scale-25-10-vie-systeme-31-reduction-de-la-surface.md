# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_31_Reduction_De_La_Surface

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 31 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Arrêter les services inutiles.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Services : mettre sur arrêt et désactiver le démarrage automatique de ce qui n'est pas utilisé (FTP, Telnet, SNMP, etc.).
   ```bash
   sudo midclt call service.query | python3 -m json.tool | grep -B2 -A6 '"enable": true'
   ```
   👉 Explication : liste les services qui démarrent au boot.

2. Désactiver un service :
   ```bash
   sudo midclt call service.update SERVICE '{"enable": false}'
   sudo midclt call service.stop SERVICE
   ```
   👉 Explication : SERVICE est par exemple `ftp`, `snmp` ou `nfs`.

## 2. Production — Contrôles

Documenter chaque service actif.

## 3. Production — Sécurité

Préférer SMB3 chiffré, NFSv4 et iSCSI avec CHAP.

## Validation et retour arrière

- **Validation** : Seuls les services nécessaires tournent.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)