# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_41_Supervision_Metriques_Et_Inventaire

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 41 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Surveiller l'état du NAS.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Tableau de bord, Rapports (graphiques CPU, ARC, réseau, disques) et Alertes.
   ```bash
   sudo zpool status -x
   sudo zpool list -o name,size,alloc,free,cap,health
   ```
   👉 Explication : état de santé et occupation.

2. Activer SNMP si utilisé : Système > Services > SNMP.
   ```bash
   sudo midclt call service.update snmp '{"enable": true}'
   snmpwalk -v2c -c COMMUNAUTE ADRESSE_NAS 1.3.6.1.2.1.1
   ```
   👉 Explication : COMMUNAUTE est la chaîne de lecture à générer.

3. Configurer les alertes e-mail : Système > Général > E-mail.
   ```bash
   sudo midclt call mail.config | python3 -m json.tool | head
   ```
   👉 Explication : serveur SMTP configuré.

## 2. Production — Contrôles

Alerter à 70 % d'occupation du pool et sur toute erreur disque.

## 3. Production — Sécurité

SNMPv3 de préférence ; pas de communauté `public`.

## Validation et retour arrière

- **Validation** : Les métriques remontent à la supervision.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : TrueNAS SCALE 25.10 Supervision Alertes Pool](</01-fiches-simples/truenas/scale-25-10/vie-du-logiciel/supervision/fiche-simple-truenas-scale-25-10-supervision-alertes-pool>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)