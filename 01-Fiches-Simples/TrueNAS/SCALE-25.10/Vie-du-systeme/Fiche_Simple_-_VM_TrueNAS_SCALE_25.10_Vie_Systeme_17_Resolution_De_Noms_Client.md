# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_17_Resolution_De_Noms_Client

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 17 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-17`

---

## Problème précis à résoudre

Configurer les serveurs DNS.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Réseau > Paramètres globaux > Serveurs DNS 1 à 3.
   ```bash
   sudo midclt call network.configuration.update '{"nameserver1": "DNS1", "nameserver2": "DNS2"}'
   ```
   👉 Explication : DNS1 et DNS2 sont les serveurs internes.

2. Tester :
   ```bash
   getent hosts truenas.com
   cat /etc/resolv.conf
   ```
   👉 Explication : résolution réussie ; le fichier est géré par TrueNAS.

## 2. Production — Contrôles

Deux DNS internes, jamais un seul.

## 3. Production — Sécurité

Ne pas éditer `/etc/resolv.conf` à la main.

## Validation et retour arrière

- **Validation** : `getent hosts` renvoie une adresse.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./Sommaire_-_Vie_du_systeme_TrueNAS_SCALE_25.10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
