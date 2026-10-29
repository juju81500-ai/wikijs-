# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_20_Mise_A_Jour_Initiale

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 20 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-20`

---

## Problème précis à résoudre

Appliquer les correctifs disponibles dès l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans Système > Micrologiciel > Mises à jour > Vérifier les mises à jour, lire les notes de version, puis Mettre à jour.
   👉 Explication : applique le système et les paquets; un redémarrage peut être demandé.

2. Ou en shell (console option 12 ou SSH) :
   ```sh
   opnsense-update -c
   opnsense-update -bkp
   ```
   👉 Explication : `-c` vérifie si une mise à jour existe; `-bkp` met à jour base, noyau et paquets (utiliser la console option 12 pour une mise à jour guidée).

3. Prendre un point de restauration avant (Système > Snapshots > Ajouter) puis contrôler :
   ```sh
   opnsense-version
   configctl firmware health
   ```
   👉 Explication : affiche la version et vérifie l'intégrité des paquets installés.

## 2. Production — Contrôles

Planifier une fenêtre de maintenance et sauvegarder config.xml avant la mise à jour.

## 3. Production — Sécurité

Lire les notes de version pour les changements incompatibles.

## Validation et retour arrière

- **Validation** : `opnsense-version` renvoie la version cible.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire OPNsense](./Sommaire_-_Vie_du_systeme_OPNsense.md)
- [Documentation officielle](https://docs.opnsense.org/)
