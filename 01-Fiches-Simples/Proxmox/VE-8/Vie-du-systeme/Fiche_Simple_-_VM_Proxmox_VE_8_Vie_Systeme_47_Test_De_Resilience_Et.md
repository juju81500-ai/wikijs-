# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_47_Test_De_Resilience_Et

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 47 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-47`

---

## Problème précis à résoudre

Vérifier que la panne est détectée et que l'alerte part.

## 1. Hors-Production (Lab / Test / POC)

1. Provoquer une alerte contrôlée (par exemple arrêter une VM de test ou un service non critique) :
   ```bash
   qm stop 9000
   systemctl stop pvestatd
   ```
   👉 Explication : `9000` = VM de test; remettre ensuite en route (`qm start 9000`, `systemctl start pvestatd`).

2. En cluster avec HA, tester la bascule sur une VM de test (GUI : **Datacenter > HA > Add**, puis éteindre le nœud de test).
   ```bash
   ha-manager status
   ```
   👉 Explication : la VM doit redémarrer sur un autre nœud.

3. Contrôler la réception de l'alerte et noter le délai.
   👉 Explication : mesure la réactivité de la supervision.

## 2. Production — Contrôles

Test réalisé hors heures pour un nœud réel.

## 3. Production — Sécurité

Prévenir l'équipe avant le test.

## Validation et retour arrière

- **Validation** : L'alerte est reçue dans le délai prévu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : Hote Proxmox VE 8 Cluster Valider](<../Vie-du-logiciel/Cluster-Corosync/Fiche_Simple_-_Hote_Proxmox_VE_8_Cluster_Valider.md>)
- [Fiche détaillée : Proxmox VE 8 Supervision Zabbix Snmp](<../Vie-du-logiciel/Zabbix/Fiche_Simple_-_Proxmox_VE_8_Supervision_Zabbix_Snmp.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Proxmox VE 8](./Sommaire_-_Vie_du_systeme_Proxmox_VE_8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
