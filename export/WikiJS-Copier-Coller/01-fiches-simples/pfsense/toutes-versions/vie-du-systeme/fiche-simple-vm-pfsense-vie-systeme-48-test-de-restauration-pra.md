# Fiche_Simple_-_VM_pfSense_Vie_Systeme_48_Test_De_Restauration_Pra

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 48 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Prouver que la sauvegarde est restaurable.

## 1. Hors-Production (Lab / Test / POC)

1. Installer un pfSense de test, puis Diagnostics > Backup & Restore > Restore Backup : choisir le fichier, saisir `MOT_DE_PASSE_SAUVEGARDE`, Restore Configuration, redémarrer.
   👉 Explication : recrée la configuration sur une machine propre.

2. En console, option 15 (« Restore recent configuration ») pour une copie de `/cf/conf/backup`, ou en shell :
   ```sh
   ls -lt /cf/conf/backup | head
   cp /root/config-DATE.xml /cf/conf/config.xml
   rm -f /tmp/config.cache
   /etc/rc.reload_all
   ```
   👉 Explication : `DATE` est la date de la copie; recharge toute la configuration.

3. Vérifier les interfaces, règles et VPN après restauration.
   👉 Explication : confirme que la sauvegarde est complète.

## 2. Production — Contrôles

Faire ce test au moins annuellement et noter la durée.

## 3. Production — Sécurité

Détruire la machine de test et ses copies de configuration après l'exercice.

## Validation et retour arrière

- **Validation** : Le pare-feu restauré a les mêmes règles et interfaces.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)