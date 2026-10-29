# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_32_Automatisation_Des_Correctifs_De

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 32 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Suivre les mises à jour sans les subir.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Mise à jour : surveiller les alertes de mise à jour disponible.
   ```bash
   sudo midclt call update.check_available
   ```
   👉 Explication : interroge le serveur de mises à jour.

2. Planifier une fenêtre : annoncer, sauvegarder la configuration, mettre à jour, valider.
   👉 Explication : les mises à jour automatiques sans validation ne sont pas conseillées sur un NAS.

## 2. Production — Contrôles

Mettre à jour d'abord un NAS de test, puis la production.

## 3. Production — Sécurité

Consulter les notes de version avant chaque mise à jour.

## Validation et retour arrière

- **Validation** : Procédure de patching documentée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)