# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 16 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Fixer l'adresse IP.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Réseau > Interfaces > interface > Modifier : désactiver DHCP, ajouter l'alias IPv4 ADRESSE/24 ; Tester les changements puis Enregistrer.
   ```sh
   midclt call interface.update INTERFACE '{"ipv4_dhcp": false, "aliases": [{"address": "ADRESSE", "netmask": 24}]}'
   midclt call interface.commit
   midclt call interface.checkin
   ```
   👉 Explication : INTERFACE est par exemple `igb0` ; ADRESSE l'IP fixe. Le changement est annulé s'il n'est pas confirmé.

2. GUI : Réseau > Configuration globale > Passerelle IPv4.
   ```sh
   midclt call network.configuration.update '{"ipv4gateway": "PASSERELLE"}'
   ```
   👉 Explication : route par défaut.

3. Vérifier :
   ```sh
   ifconfig INTERFACE
   netstat -rn
   ```
   👉 Explication : adresse et route attendues.

## 2. Production — Contrôles

Adresse réservée dans l'IPAM ; interface séparée pour le stockage.

## 3. Production — Sécurité

VLAN de stockage non routé.

## Validation et retour arrière

- **Validation** : Le NAS répond au ping.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)