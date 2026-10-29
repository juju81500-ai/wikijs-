# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_08_Configuration_Reseau_D_Installation

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 08 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-08`

---

## Problème précis à résoudre

Disposer d'un réseau pendant l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Dans le programme d'installation (Subiquity), écran **Network connections** : laisser le DHCP ou choisir **Edit IPv4 > Manual** pour une IP statique temporaire. Après démarrage, contrôler :
   ```bash
   ip -br address
   ip route
   ping -c 2 archive.ubuntu.com
   ```
   👉 Explication : vérifie l'adresse, la passerelle et l'accès aux dépôts; l'installateur génère un fichier Netplan dans `/etc/netplan/`.

## 2. Production — Contrôles

Utiliser un VLAN d'installation si le réseau de production n'a pas de DHCP.

## 3. Production — Sécurité

Ne pas exposer une machine non durcie sur Internet.

## Validation et retour arrière

- **Validation** : `ping` vers `archive.ubuntu.com` réussit.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Ubuntu 26.04](./Sommaire_-_Vie_du_systeme_Ubuntu_26.04.md)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
