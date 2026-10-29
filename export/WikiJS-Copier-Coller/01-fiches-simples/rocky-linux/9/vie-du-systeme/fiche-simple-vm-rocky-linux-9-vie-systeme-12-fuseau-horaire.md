# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_12_Fuseau_Horaire

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 12 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Régler le fuseau horaire.

## 1. Hors-Production (Lab / Test / POC)

1. Rechercher et appliquer le fuseau :
   ```bash
   timedatectl list-timezones | grep Paris
   sudo timedatectl set-timezone Europe/Paris
   ```
   👉 Explication : crée le lien `/etc/localtime`.

2. Contrôler :
   ```bash
   timedatectl
   ```
   👉 Explication : affiche `Time zone: Europe/Paris`.

3. Conserver l'heure matérielle en UTC :
   ```bash
   sudo timedatectl set-local-rtc 0
   ```
   👉 Explication : évite les décalages lors des changements d'heure.

## 2. Production — Contrôles

Un seul fuseau cohérent sur tous les serveurs.

## 3. Production — Sécurité

Des horloges décalées faussent les journaux et les certificats.

## Validation et retour arrière

- **Validation** : `timedatectl` indique le fuseau attendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)