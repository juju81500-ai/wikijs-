# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 16 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-16`

---

## Problème précis à résoudre

Fixer l'IP de gestion et le commutateur standard.

## 1. Hors-Production (Lab / Test / POC)

1. Host Client : **Réseau > Cartes VMkernel > vmk0 > Modifier les paramètres > Paramètres IPv4 > Statique**. En ligne de commande (remplacer les placeholders) :
   ```sh
   esxcli network ip interface ipv4 set -i vmk0 -t static -I IP_HOTE -N 255.255.255.0
   esxcli network ip route ipv4 add -n default -g IP_GW
   esxcli network ip interface ipv4 get
   ```
   👉 Explication : `IP_HOTE` = IP de gestion; `IP_GW` = passerelle.

2. Ajouter une 2e carte physique au commutateur de gestion pour la redondance (Host Client : **Réseau > Commutateurs virtuels > vSwitch0 > Ajouter une liaison montante**) :
   ```sh
   esxcli network vswitch standard uplink add -v vSwitch0 -u vmnic1
   esxcli network vswitch standard list
   ```
   👉 Explication : deux `vmnic` actives évitent de perdre l'hôte sur la panne d'un câble.

3. Tester :
   ```sh
   vmkping -I vmk0 IP_GW
   ```
   👉 Explication : confirme la sortie réseau.

## 2. Production — Contrôles

Faire la modification avec un accès console hors bande.

## 3. Production — Sécurité

Documenter l'IP dans l'IPAM; VLAN de gestion séparé.

## Validation et retour arrière

- **Validation** : Le Host Client répond sur https://IP_HOTE/ui.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
