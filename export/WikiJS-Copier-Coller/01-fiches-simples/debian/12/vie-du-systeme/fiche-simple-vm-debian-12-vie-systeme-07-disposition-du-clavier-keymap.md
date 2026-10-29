# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_07_Disposition_Du_Clavier_Keymap

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 07 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Régler le clavier de la console.

## 1. Hors-Production (Lab / Test / POC)

1. Choisir la disposition :
   ```bash
   sudo dpkg-reconfigure keyboard-configuration
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

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 12](/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)