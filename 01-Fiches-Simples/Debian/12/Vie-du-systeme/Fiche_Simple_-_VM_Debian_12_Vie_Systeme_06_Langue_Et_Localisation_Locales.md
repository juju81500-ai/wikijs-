# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_06_Langue_Et_Localisation_Locales

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 06 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-06`

---

## Problème précis à résoudre

Définir la langue du système.

## 1. Hors-Production (Lab / Test / POC)

1. Générer et choisir la locale (le choix se fait à l'installateur, ou après coup) :
   ```bash
   sudo dpkg-reconfigure locales
   localectl status
   ```
   👉 Explication : `fr_FR.UTF-8` ou `en_US.UTF-8` selon la politique; `localectl` affiche la locale active.

2. Fixer la locale par défaut :
   ```bash
   sudo localectl set-locale LANG=fr_FR.UTF-8
   ```
   👉 Explication : écrit `LANG` dans `/etc/default/locale`.

## 2. Production — Contrôles

Utiliser la même locale sur tout le parc pour des journaux homogènes.

## 3. Production — Sécurité

Préférer UTF-8 partout.

## Validation et retour arrière

- **Validation** : `localectl status` montre la locale choisie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Debian 12](./Sommaire_-_Vie_du_systeme_Debian_12.md)
- [Documentation officielle](https://www.debian.org/doc/)
