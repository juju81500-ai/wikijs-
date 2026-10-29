# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_05_Configuration_Materielle_Firmware

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 05 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Régler le firmware avant l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Choisir UEFI (ou BIOS) et désactiver Secure Boot :
   👉 Explication : l'ISO Alpine n'est pas signée pour Secure Boot : s'il est actif, la machine refuse de démarrer l'image (menu du firmware, rubrique Boot / Security, ou option de la VM).

2. Pour une VM, choisir un contrôleur disque et une carte réseau `virtio` :
   👉 Explication : ils sont reconnus par le noyau Alpine `virt` et donnent de meilleures performances; ajouter l'ISO comme premier périphérique d'amorçage.

3. Vérifier la virtualisation matérielle depuis un Linux existant :
   ```sh
   grep -Ec 'vmx|svm' /proc/cpuinfo
   ```
   👉 Explication : un résultat supérieur à 0 confirme que le processeur expose la virtualisation (utile pour un hôte, pas pour une VM simple).

## 2. Production — Contrôles

Documenter le mode de firmware choisi (UEFI ou BIOS) : il détermine le chargeur d'amorçage installé.

## 3. Production — Sécurité

Protéger le firmware par un mot de passe sur le matériel physique.

## Validation et retour arrière

- **Validation** : La machine démarre sur l'invite `localhost login:` de l'ISO Alpine (connexion `root` sans mot de passe).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)