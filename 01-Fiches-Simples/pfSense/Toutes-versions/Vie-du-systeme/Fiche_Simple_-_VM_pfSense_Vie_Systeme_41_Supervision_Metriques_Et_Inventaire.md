# Fiche_Simple_-_VM_pfSense_Vie_Systeme_41_Supervision_Metriques_Et_Inventaire

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 41 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-41`

---

## Problème précis à résoudre

Surveiller l'état et les performances.

## 1. Hors-Production (Lab / Test / POC)

1. Activer SNMP : Services > SNMP, renseigner la communauté et lier à l'interface LAN seulement.
   👉 Explication : permet à la supervision de lire les métriques.

2. Consulter Status > Monitoring et Status > Dashboard; ou installer `zabbix-agent` / `Telegraf` pour exporter les métriques.
   👉 Explication : affiche CPU, mémoire, trafic et état des passerelles.

3. Contrôler en shell :
   ```sh
   snmpwalk -v2c -c COMMUNAUTE IP_LAN system 2>/dev/null | head -3
   top -b -n1 | head -10
   ```
   👉 Explication : `COMMUNAUTE` est la chaîne de lecture SNMP; vérifie la réponse et la charge.

## 2. Production — Contrôles

Alerter sur la charge, l'espace disque, l'état des passerelles et des tunnels.

## 3. Production — Sécurité

Ne jamais laisser la communauté `public`; limiter à l'adresse de la supervision.

## Validation et retour arrière

- **Validation** : La supervision reçoit les métriques.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire pfSense CE](./Sommaire_-_Vie_du_systeme_pfSense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
