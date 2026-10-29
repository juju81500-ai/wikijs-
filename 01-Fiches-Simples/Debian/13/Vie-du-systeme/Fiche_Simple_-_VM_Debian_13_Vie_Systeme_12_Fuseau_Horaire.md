# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_12_Fuseau_Horaire

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 12 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian13`, `vie-du-systeme`, `cycle-de-vie`, `etape-12`

---

## Problème précis à résoudre

Régler le fuseau.

## 1. Hors-Production (Lab / Test / POC)

1. Lister puis fixer le fuseau :
   ```bash
   timedatectl list-timezones | grep Europe/Paris
   sudo timedatectl set-timezone Europe/Paris
   timedatectl
   ```
   👉 Explication : règle le fuseau; l'horloge matérielle doit rester en UTC (`RTC in local TZ: no`).

## 2. Production — Contrôles

Utiliser UTC pour les serveurs d'une zone multi-site.

## 3. Production — Sécurité

Une heure fausse invalide certificats et journaux.

## Validation et retour arrière

- **Validation** : `timedatectl` affiche le bon fuseau.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Debian 13](./Sommaire_-_Vie_du_systeme_Debian_13.md)
- [Documentation officielle](https://www.debian.org/doc/)
