# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 16 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Fixer l'adresse IP du NAS.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Réseau > Interfaces > interface > Modifier > désactiver DHCP > Ajouter un alias IP (ADRESSE/24), puis Tester les modifications, puis Enregistrer.
   ```bash
   sudo midclt call interface.update INTERFACE '{"ipv4_dhcp": false, "aliases": [{"address": "ADRESSE", "netmask": 24}]}'
   sudo midclt call interface.commit
   sudo midclt call interface.checkin
   ```
   👉 Explication : INTERFACE est le nom (ex. `eno1`) ; ADRESSE l'IP fixe. TrueNAS annule le changement si on ne confirme pas (`checkin`).

2. Définir la passerelle : Réseau > Paramètres globaux > Passerelle IPv4.
   ```bash
   sudo midclt call network.configuration.update '{"ipv4gateway": "PASSERELLE"}'
   ```
   👉 Explication : route par défaut.

3. Vérifier :
   ```bash
   ip -br a
   ip route
   ```
   👉 Explication : adresse et route attendues.

## 2. Production — Contrôles

Réserver l'adresse dans l'IPAM ; prévoir une interface dédiée au stockage (iSCSI/NFS).

## 3. Production — Sécurité

Utiliser un VLAN de stockage non routé quand c'est possible.

## Validation et retour arrière

- **Validation** : Le NAS répond au ping sur l'IP fixe.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)