# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_29_Pare_Feu_Hote

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 29 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Limiter l'accès aux interfaces d'administration.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Réseau > Paramètres globaux > Accès à l'interface web (adresses IP d'écoute) et Système > Général > GUI SSL.
   ```bash
   sudo midclt call system.general.update '{"ui_address": ["ADRESSE_NAS"]}'
   ```
   👉 Explication : limite l'écoute de l'interface à l'adresse d'administration ; ne pas se couper l'accès.

2. Contrôler les ports ouverts :
   ```bash
   sudo ss -tulpn
   ```
   👉 Explication : ports en écoute : 80/443 (GUI), 22 (SSH), 445 (SMB), 2049 (NFS), 3260 (iSCSI).

## 2. Production — Contrôles

Filtrer par pare-feu réseau (VLAN, règles IP source) ; le NAS n'a pas de pare-feu hôte configurable en GUI.

## 3. Production — Sécurité

Ne jamais exposer les partages ou la GUI sur Internet.

## Validation et retour arrière

- **Validation** : Seuls les ports prévus sont ouverts.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)