# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_47_Test_De_Resilience_Et

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 47 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-47`

---

## Problème précis à résoudre

Vérifier que la panne est détectée et que l'alerte part.

## 1. Hors-Production (Lab / Test / POC)

1. Provoquer une alerte contrôlée (par exemple débrancher une liaison montante en redondance ou arrêter un service non critique) :
   ```sh
   esxcli network vswitch standard uplink remove -v vSwitch0 -u vmnic1
   esxcli network vswitch standard uplink add -v vSwitch0 -u vmnic1
   ```
   👉 Explication : la 1re commande simule la panne, la 2e rétablit; le trafic de gestion doit rester joignable.

2. Avec vCenter, tester HA sur une VM de test (vSphere Client : **Cluster > Configurer > Disponibilité vSphere**) puis couper l'hôte de test.
   👉 Explication : la VM doit redémarrer sur un autre hôte.

3. Contrôler la réception de l'alerte et noter le délai.
   👉 Explication : mesure la réactivité de la supervision.

## 2. Production — Contrôles

Test réalisé hors heures pour un hôte réel.

## 3. Production — Sécurité

Prévenir l'équipe avant le test.

## Validation et retour arrière

- **Validation** : L'alerte est reçue dans le délai prévu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
