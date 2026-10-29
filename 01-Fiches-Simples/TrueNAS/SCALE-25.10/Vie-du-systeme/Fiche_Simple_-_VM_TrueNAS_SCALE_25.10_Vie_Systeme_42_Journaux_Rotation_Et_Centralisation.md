# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_42_Journaux_Rotation_Et_Centralisation

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 42 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-42`

---

## Problème précis à résoudre

Conserver les journaux et les envoyer ailleurs.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Avancé > Syslog > Serveur syslog distant.
   ```bash
   sudo midclt call system.advanced.update '{"syslogserver": "SERVEUR_LOG", "syslog_transport": "TLS"}'
   ```
   👉 Explication : SERVEUR_LOG est le collecteur central.

2. Consulter les journaux :
   ```bash
   sudo journalctl -p err -b | tail
   sudo tail -n 50 /var/log/middlewared.log
   ```
   👉 Explication : erreurs récentes du système et du middleware.

## 2. Production — Contrôles

Conserver 90 jours minimum selon la politique.

## 3. Production — Sécurité

Chiffrer le transport (TLS) et restreindre l'accès aux journaux.

## Validation et retour arrière

- **Validation** : Les événements arrivent sur le collecteur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : TrueNAS SCALE 25.10 Supervision Alertes Pool](<../Vie-du-logiciel/Supervision/Fiche_Simple_-_TrueNAS_SCALE_25.10_Supervision_Alertes_Pool.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./Sommaire_-_Vie_du_systeme_TrueNAS_SCALE_25.10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
