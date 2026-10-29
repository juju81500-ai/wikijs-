# Fiche_Simple_-_VM_pfSense_Vie_Systeme_45_Analyse_Des_Journaux_D

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 45 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-45`

---

## Problème précis à résoudre

Repérer les erreurs et blocages anormaux.

## 1. Hors-Production (Lab / Test / POC)

1. Consulter Status > System Logs > Firewall (filtre `block`) et Status > System Logs > System > General.
   👉 Explication : montre les paquets bloqués et les erreurs système.

2. Rechercher en shell :
   ```sh
   clog /var/log/system.log | grep -iE 'error|fail|panic' | tail
   clog /var/log/filter.log | grep block | tail -5
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

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire pfSense CE](./Sommaire_-_Vie_du_systeme_pfSense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
