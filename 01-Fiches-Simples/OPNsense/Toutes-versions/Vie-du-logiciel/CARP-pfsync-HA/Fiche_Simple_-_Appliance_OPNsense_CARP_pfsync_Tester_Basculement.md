# Fiche_Simple_-_Appliance_OPNsense_CARP_pfsync_Tester_Basculement.md

- **Environnement** : Deux appliances OPNsense en haute disponibilité (CARP et pfsync)
- **OS / Version** : OPNsense (toutes versions compatibles entre les deux nœuds)
- **Catégorie** : pare-feu / haute disponibilité
- **Tags** : `opnsense`, `carp`, `pfsync`, `ha`, `firewall`

---

## Problème précis à résoudre

Vérifier que le basculement fonctionne et que les services restent disponibles.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l'état CARP des deux nœuds : **Interfaces > Virtual IPs > Status**.
   👉 Explication : un nœud MASTER et un BACKUP attendus.

2. Confirmer que les états de sessions sont synchronisés.
   👉 Explication : permet de conserver les connexions existantes au basculement.

3. Depuis un client, lancer un ping continu vers la VIP (remplacer 192.0.2.1 par la VIP réelle) :
   ```bash
   ping 192.0.2.1
   ```
   👉 Explication : sert à mesurer l'interruption pendant l'essai.

4. Couper proprement le nœud actif (**Interfaces > Virtual IPs > Status > Enter Persistent CARP Maintenance Mode**) et mesurer le basculement.
   👉 Explication : simule la panne sans débrancher.

5. Restaurer le nœud et observer la préemption.
   👉 Explication : vérifie le comportement de retour.

6. Vérifier DHCP, DNS, VPN, NAT et règles nécessaires.
   👉 Explication : les services doivent rester fonctionnels.

## 2. Production — Contrôles

Réaliser l'essai en fenêtre de maintenance avec accès console.

## 3. Production — Sécurité

- Ne pas tester sur un réseau de production sans fenêtre approuvée.

## Validation et retour arrière

- **Validation** : le basculement est rapide, sans perte de service et le retour est conforme.
- **Retour arrière** : quitter le mode maintenance CARP et rétablir la configuration sauvegardée si nécessaire.

## Si le problème n'est pas résolu

- [OPNsense — haute disponibilité](https://docs.opnsense.org/manual/hacarp.html)
- [OPNsense — haute disponibilité](https://docs.opnsense.org/manual/hacarp.html)
- [Guide complet](../../../../../02-Fiches-Completes/OPNsense/Toutes-versions/Autres/10_Pare_Feu_Appliance_OPNsense_CARP_pfSync_HA.md#4-tester)
