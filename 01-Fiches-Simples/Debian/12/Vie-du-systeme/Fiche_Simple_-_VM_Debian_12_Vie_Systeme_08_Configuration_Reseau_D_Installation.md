# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_08_Configuration_Reseau_D_Installation

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 08 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-08`

---

## Problème précis à résoudre

Disposer d'un réseau pendant l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur Debian, laisser le DHCP ou saisir une IP statique temporaire (**Configurer le réseau**). Après démarrage, contrôler :
   ```bash
   ip -br address
   ip route
   ping -c 2 deb.debian.org
   ```
   👉 Explication : vérifie l'adresse, la passerelle et l'accès aux dépôts.

## 2. Production — Contrôles

Utiliser un VLAN d'installation si le réseau de production n'a pas de DHCP.

## 3. Production — Sécurité

Ne pas exposer une machine non durcie sur Internet.

## Validation et retour arrière

- **Validation** : `ping` vers `deb.debian.org` réussit.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Debian 12](./Sommaire_-_Vie_du_systeme_Debian_12.md)
- [Documentation officielle](https://www.debian.org/doc/)
