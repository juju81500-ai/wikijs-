# Fiche_Simple_-_VM_pfSense_Vie_Systeme_42_Journaux_Rotation_Et_Centralisation

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 42 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-42`

---

## Problème précis à résoudre

Centraliser et conserver les journaux.

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans Status > System Logs > Settings > Enable Remote Logging, renseigner `IP_SYSLOG:514` et cocher les catégories.
   👉 Explication : `IP_SYSLOG` est le serveur de journaux; les événements sont envoyés en temps réel.

2. Régler la rétention locale (Log Rotation Size, nombre de fichiers) dans la même page.
   👉 Explication : évite de remplir le disque.

3. Contrôler en shell :
   ```sh
   ls -lh /var/log | head
   clog /var/log/filter.log | tail -5
   ```
   👉 Explication : liste les journaux et affiche les dernières lignes du pare-feu.

## 2. Production — Contrôles

Conserver les journaux selon la politique de rétention (12 mois pour la traçabilité).

## 3. Production — Sécurité

Journaliser les règles de blocage et protéger le serveur de journaux.

## Validation et retour arrière

- **Validation** : Les événements arrivent sur le serveur `IP_SYSLOG`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire pfSense CE](./Sommaire_-_Vie_du_systeme_pfSense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
