# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_45_Analyse_Des_Journaux_D

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 45 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Repérer les erreurs et blocages anormaux.

## 1. Hors-Production (Lab / Test / POC)

1. Consulter Pare-feu > Journaux > Vue en direct (filtrer `action = block`) et Système > Journaux > Fichiers > Général.
   👉 Explication : montre les paquets bloqués et les erreurs système.

2. Rechercher en shell :
   ```sh
   clog /var/log/system/latest.log | grep -iE 'error|fail|panic' | tail
   clog /var/log/filter/latest.log | grep block | tail -5
   ```
   👉 Explication : extrait les erreurs et les derniers blocages.

## 2. Production — Contrôles

Revue des journaux à fréquence définie et traitement des anomalies.

## 3. Production — Sécurité

Corréler les blocages avec les tentatives d'intrusion.

## Validation et retour arrière

- **Validation** : Aucune erreur critique non expliquée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)