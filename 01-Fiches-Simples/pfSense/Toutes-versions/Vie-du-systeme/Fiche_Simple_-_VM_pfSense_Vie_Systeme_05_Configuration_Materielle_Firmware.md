# Fiche_Simple_-_VM_pfSense_Vie_Systeme_05_Configuration_Materielle_Firmware

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 05 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-05`

---

## Problème précis à résoudre

Régler le firmware et les options de la VM avant l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Choisir UEFI (ou BIOS) et noter ce choix; sur Proxmox : VM > Matériel > BIOS = OVMF, désactiver Secure Boot (Disque EFI sans clés préenrôlées).
   👉 Explication : pfSense CE ne démarre pas avec Secure Boot activé.

2. Choisir un modèle de carte réseau `VirtIO` (ou Intel E1000 en secours) et activer les extensions de virtualisation.
   👉 Explication : VirtIO donne de meilleures performances; désactiver les offloads si des paquets sont perdus (System > Advanced > Networking).

3. Après installation, contrôler le mode d'amorçage en shell :
   ```sh
   sysctl machdep.bootmethod
   gpart show
   ```
   👉 Explication : indique `UEFI` ou `BIOS` et la table de partitions.

## 2. Production — Contrôles

Documenter la version du firmware et l'ordre d'amorçage.

## 3. Production — Sécurité

Protéger l'accès au firmware par mot de passe sur du matériel physique.

## Validation et retour arrière

- **Validation** : Le mode d'amorçage attendu est confirmé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire pfSense CE](./Sommaire_-_Vie_du_systeme_pfSense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
