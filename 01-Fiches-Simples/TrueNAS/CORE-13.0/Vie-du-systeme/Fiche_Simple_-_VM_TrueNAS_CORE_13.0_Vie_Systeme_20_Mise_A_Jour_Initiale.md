# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_20_Mise_A_Jour_Initiale

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 20 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-20`

---

## Problème précis à résoudre

Mettre le NAS à jour dès l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Mises à jour > Rechercher > Appliquer la mise à jour.
   ```sh
   midclt call update.check_available
   ```
   👉 Explication : indique si une version est disponible.

2. Appliquer en CLI :
   ```sh
   midclt call update.update '{"reboot": true}'
   ```
   👉 Explication : installe et redémarre ; fenêtre de maintenance.

3. Vérifier la version :
   ```sh
   cat /etc/version
   ```
   👉 Explication : version installée.

## 2. Production — Contrôles

Sauvegarder la configuration avant.

## 3. Production — Sécurité

Ne jamais couper l'alimentation pendant la mise à jour.

## Validation et retour arrière

- **Validation** : Version cible affichée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
