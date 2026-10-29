# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_06_Langue_Et_Localisation_Locales

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 06 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Définir la langue du système.

## 1. Hors-Production (Lab / Test / POC)

1. Générer la locale puis la choisir (la langue se règle aussi à l'installateur) :
   ```bash
   sudo locale-gen fr_FR.UTF-8
   sudo update-locale LANG=fr_FR.UTF-8
   localectl status
   ```
   👉 Explication : génère `fr_FR.UTF-8`, l'écrit dans `/etc/default/locale` et affiche la locale active (effective à la prochaine connexion).

2. Ou fixer la locale avec systemd :
   ```bash
   sudo localectl set-locale LANG=fr_FR.UTF-8
   ```
   👉 Explication : écrit `LANG` dans `/etc/locale.conf` / `/etc/default/locale`; la locale doit d'abord être générée.

## 2. Production — Contrôles

Utiliser la même locale sur tout le parc pour des journaux homogènes.

## 3. Production — Sécurité

Préférer UTF-8 partout.

## Validation et retour arrière

- **Validation** : `localectl status` montre la locale choisie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 26.04](/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)