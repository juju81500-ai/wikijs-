# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_08_Configuration_Reseau_D_Installation

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 08 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-08`

---

## Problème précis à résoudre

Donner une adresse au NAS pour pouvoir accéder à l'interface web.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur, ne pas configurer le réseau ; au premier démarrage, le menu console propose `1) Configure network interfaces`.
   👉 Explication : choisir l'interface et saisir l'adresse IP, le masque et la passerelle.

2. Contrôler l'adresse reçue :
   ```bash
   ip -br a
   ip route
   ```
   👉 Explication : interface UP avec son adresse et la route par défaut.

3. Tester la sortie réseau :
   ```bash
   ping -c 3 PASSERELLE
   ping -c 3 truenas.com
   ```
   👉 Explication : PASSERELLE est l'adresse du routeur local.

## 2. Production — Contrôles

Utiliser une adresse fixe réservée dans l'IPAM dès l'installation.

## 3. Production — Sécurité

Réseau d'administration séparé des réseaux de données.

## Validation et retour arrière

- **Validation** : L'interface web répond sur http://IP_NAS.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./Sommaire_-_Vie_du_systeme_TrueNAS_SCALE_25.10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
