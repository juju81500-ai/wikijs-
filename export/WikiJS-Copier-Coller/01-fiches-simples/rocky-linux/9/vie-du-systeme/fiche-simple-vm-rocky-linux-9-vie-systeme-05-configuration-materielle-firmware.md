# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_05_Configuration_Materielle_Firmware

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 05 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Régler le firmware avant l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Choisir UEFI et activer Secure Boot (pris en charge par Rocky 9) :
   👉 Explication : mode moderne; Secure Boot protège la chaîne d'amorçage (shim signé).

2. Activer les extensions de virtualisation si la machine héberge des VM :
   👉 Explication : VT-x/AMD-V dans le firmware ou l'hyperviseur.

3. Après installation, contrôler le mode d'amorçage :
   ```bash
   [ -d /sys/firmware/efi ] && echo UEFI || echo BIOS
   mokutil --sb-state
   ```
   👉 Explication : confirme UEFI et l'état de Secure Boot.

## 2. Production — Contrôles

Documenter la version du firmware et l'ordre d'amorçage.

## 3. Production — Sécurité

Protéger l'accès au firmware par mot de passe sur du matériel physique.

## Validation et retour arrière

- **Validation** : Le mode attendu (UEFI/BIOS) est confirmé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)