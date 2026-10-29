# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_41_Supervision_Metriques_Et_Inventaire

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 41 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-41`

---

## Problème précis à résoudre

Superviser l'hôte et les VM.

## 1. Hors-Production (Lab / Test / POC)

1. Host Client : **Hôte > Surveiller > Performances / Matériel / Événements**. Pour SNMP :
   ```sh
   esxcli system snmp set --communities COMMUNAUTE --enable true
   esxcli system snmp get
   ```
   👉 Explication : `COMMUNAUTE` = chaîne secrète à ne pas laisser par défaut (utiliser SNMPv3 si possible).

2. Surveiller au minimum : CPU, RAM, latence disque, occupation des datastores, état du matériel, alertes d'événements.
   ```sh
   esxtop -b -n 1 | head -5
   esxcli hardware ipmi sdr list 2>/dev/null | head
   ```
   👉 Explication : `esxtop -b` donne un instantané; IPMI donne températures et ventilateurs.

3. Configurer les alertes dans la supervision (vCenter : **Surveiller > Alarmes**).
   👉 Explication : prévient l'équipe en cas de panne ou de saturation.

## 2. Production — Contrôles

Seuils d'alerte documentés (datastore à 80 %).

## 3. Production — Sécurité

Accès SNMP limité aux IP de supervision.

## Validation et retour arrière

- **Validation** : Les métriques de l'hôte remontent dans l'outil de supervision.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
