# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_30_Protection_Contre_Le_Brute

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 30 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Limiter les tentatives de connexion.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Services > SSH > Paramètres avancés > nombre de tentatives, ou Système > Sécurité > Verrouillage.
   ```bash
   sudo midclt call system.security.config
   ```
   👉 Explication : affiche la politique de sécurité (délais, expiration de session).

2. Surveiller les échecs :
   ```bash
   sudo grep -i 'failed' /var/log/auth.log | tail
   ```
   👉 Explication : repère les tentatives en échec.

## 2. Production — Contrôles

Envoyer les journaux d'authentification vers un syslog central.

## 3. Production — Sécurité

Activer la 2FA : Système > Sécurité > Authentification à deux facteurs.

## Validation et retour arrière

- **Validation** : Les échecs sont détectés et alertés.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)