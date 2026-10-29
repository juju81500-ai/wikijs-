# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_31_Reduction_De_La_Surface

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 31 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Désactiver les services inutiles.

## 1. Hors-Production (Lab / Test / POC)

1. Lister et désactiver (remplacer `SERVICE`) :
   ```bash
   systemctl list-unit-files --state=enabled
   sudo systemctl disable --now SERVICE
   sudo systemctl mask SERVICE
   ```
   👉 Explication : `mask` empêche aussi un démarrage indirect.

2. Lister les ports en écoute :
   ```bash
   sudo ss -tulpn
   ```
   👉 Explication : chaque port ouvert doit être justifié.

## 2. Production — Contrôles

Documenter chaque service conservé.

## 3. Production — Sécurité

Valider qu'aucune dépendance n'est cassée avant `mask`.

## Validation et retour arrière

- **Validation** : `ss -tulpn` ne montre que les ports prévus.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 13](/01-fiches-simples/debian/13/vie-du-systeme/sommaire-vie-du-systeme-debian-13)
- [Documentation officielle](https://www.debian.org/doc/)