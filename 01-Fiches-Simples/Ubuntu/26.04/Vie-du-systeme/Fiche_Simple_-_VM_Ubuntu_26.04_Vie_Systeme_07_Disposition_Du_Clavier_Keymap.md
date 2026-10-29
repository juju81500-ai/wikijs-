# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_07_Disposition_Du_Clavier_Keymap

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 07 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-07`

---

## Problème précis à résoudre

Régler le clavier de la console.

## 1. Hors-Production (Lab / Test / POC)

1. Choisir la disposition :
   ```bash
   sudo dpkg-reconfigure keyboard-configuration
   sudo localectl set-keymap fr
   localectl status
   ```
   👉 Explication : sélection du clavier (par exemple `fr`) et affichage de la configuration.

2. Appliquer sans redémarrer :
   ```bash
   sudo setupcon
   ```
   👉 Explication : recharge la disposition sur la console.

## 2. Production — Contrôles

Documenter la disposition pour l'accès console de secours.

## 3. Production — Sécurité

Vérifier le clavier avant de saisir un mot de passe fort.

## Validation et retour arrière

- **Validation** : Les caractères spéciaux sont corrects en console.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Ubuntu 26.04](./Sommaire_-_Vie_du_systeme_Ubuntu_26.04.md)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
