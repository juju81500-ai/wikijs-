---
title: "Fiche Simple - VM Debian 12 Vie Systeme 16 Adressage Ip Fixe Definitif"
description: "Configurer une adresse IPv4 statique avec le gestionnaire réseau réellement utilisé par le serveur, sans perdre l'accès d'administration."
published: true
date: 2026-11-03T09:36:13Z
tags: ["debian12", "vie-du-systeme", "cycle-de-vie", "etape-16"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 16 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-16`

---

## Problème précis à résoudre

Configurer une adresse IPv4 statique avec le gestionnaire réseau réellement utilisé par le serveur, sans perdre l'accès d'administration.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier l'interface et vérifier quel gestionnaire la configure :
   ```bash
   ip -br link
   ```
   👉 Explication : utiliser une seule méthode réseau. Ne pas modifier ifupdown si l'interface est gérée par Netplan, NetworkManager ou un autre outil.

2. Pour une interface gérée par ifupdown, modifier `/etc/network/interfaces` :
   ```bash
   sudoedit /etc/network/interfaces
   ```
   👉 Explication : exemple de paramètres à adapter après réservation IPAM : `iface ens18 inet static`, `address 192.0.2.10/24`, `gateway 192.0.2.1`.

3. Pour une interface gérée par Netplan, modifier le fichier Netplan qui configure effectivement l'interface et remplacer sa configuration DHCP :
   ```bash
   sudoedit /etc/netplan/90-default.yaml
   ```
   👉 Explication : ne pas ajouter un second fichier concurrent qui configure la même interface. Exemple YAML à adapter :
   ```yaml
   network:
     version: 2
     ethernets:
       ens18:
         dhcp4: false
         dhcp6: false
         addresses:
           - 192.0.2.10/24
         routes:
           - to: default
             via: 192.0.2.1
         nameservers:
           addresses:
             - 192.0.2.53
   ```
   👉 Explication : remplacer le nom de l'interface, l'adresse, la passerelle et le DNS par les valeurs réservées dans l'IPAM.

4. Appliquer la configuration ifupdown uniquement si cette méthode gère l'interface :
   ```bash
   sudo systemctl restart networking
   ```
   👉 Explication : garder une console hyperviseur ouverte ; cette action peut interrompre SSH.

5. Valider et appliquer Netplan uniquement si cette méthode gère l'interface :
   ```bash
   sudo netplan generate
   ```
   👉 Explication : vérifie la syntaxe et génère la configuration sans changer le réseau actif.
   ```bash
   sudo netplan try --timeout 120
   ```
   👉 Explication : applique temporairement les changements et revient à l'ancienne configuration si elle n'est pas confirmée avant le délai.

6. Vérifier l'adresse et la route après application :
   ```bash
   ip -br address
   ip route
   ```
   👉 Explication : l'interface doit afficher l'adresse réservée et la route par défaut doit passer par la passerelle approuvée.

## 2. Production — Contrôles

Réserver l'adresse dans l'IPAM (étape 49).

## 3. Production — Sécurité

Valider depuis la console : une erreur coupe l'accès SSH.

## Validation et retour arrière

- **Validation** : Le serveur répond sur la nouvelle IP.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire Debian 12](/fr/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)