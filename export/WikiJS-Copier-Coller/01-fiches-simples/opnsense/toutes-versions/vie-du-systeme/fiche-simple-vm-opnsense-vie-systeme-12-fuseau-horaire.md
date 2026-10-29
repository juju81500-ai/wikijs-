# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_12_Fuseau_Horaire

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 12 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Régler le fuseau pour des journaux datés correctement.

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans Système > Paramètres > Général > Fuseau horaire et choisir `Europe/Paris`, puis Enregistrer.
   👉 Explication : tous les journaux et tâches planifiées utilisent ce fuseau.

2. Contrôler en shell :
   ```sh
   date
   grep '<timezone>' /conf/config.xml
   ```
   👉 Explication : doit afficher l'heure locale et `Europe/Paris`.

## 2. Production — Contrôles

Utiliser le même fuseau (ou UTC) sur tous les équipements pour la corrélation.

## 3. Production — Sécurité

Un fuseau erroné fausse les journaux utilisés comme preuve.

## Validation et retour arrière

- **Validation** : `date` affiche l'heure locale correcte.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)