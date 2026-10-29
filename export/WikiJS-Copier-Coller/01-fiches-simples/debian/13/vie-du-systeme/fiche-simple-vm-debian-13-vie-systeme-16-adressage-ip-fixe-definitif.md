# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 16 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Fixer l'IP du serveur.

## 1. Hors-Production (Lab / Test / POC)

1. Éditer `/etc/network/interfaces` (ifupdown, par défaut sous Debian 13 ; l'alternative `systemd-networkd` est décrite dans la fiche détaillée ; remplacer interface et valeurs) :
   ```bash
   sudoedit /etc/network/interfaces
   ```
   👉 Explication : exemple : `iface ens18 inet static`, `address 192.0.2.10/24`, `gateway 192.0.2.1`.

2. Appliquer en gardant la console ouverte, puis tester :
   ```bash
   sudo systemctl restart networking
   ip -br address
   ip route
   ping -c 2 192.0.2.1
   ```
   👉 Explication : recharge le réseau; l'IP et la route par défaut doivent apparaître.

## 2. Production — Contrôles

Réserver l'adresse dans l'IPAM (étape 49).

## 3. Production — Sécurité

Valider depuis la console : une erreur coupe l'accès SSH.

## Validation et retour arrière

- **Validation** : Le serveur répond sur la nouvelle IP.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 13](/01-fiches-simples/debian/13/vie-du-systeme/sommaire-vie-du-systeme-debian-13)
- [Documentation officielle](https://www.debian.org/doc/)