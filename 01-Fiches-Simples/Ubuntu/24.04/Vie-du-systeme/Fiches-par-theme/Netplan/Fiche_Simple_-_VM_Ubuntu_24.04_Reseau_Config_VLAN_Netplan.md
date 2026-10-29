# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Reseau_Config_VLAN_Netplan.md

- **Environnement** : VM Ubuntu Server raccordée à un port trunk autorisant le VLAN
- **OS / Version** : Ubuntu Server 24.04 LTS avec Netplan et `systemd-networkd`
- **Catégorie** : Réseau / VLAN
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[netplan]`, `[vlan]`, `[8021q]`, `[networkd]`

## 🎯 Problème précis à résoudre
Configurer une interface VLAN 802.1Q persistante avec Netplan sous Ubuntu Server, après validation du VLAN côté hyperviseur ou switch.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Identifier l'interface physique, le renderer réseau et l'état initial :
   ```bash
   ip -br link
   ip route
   ls -l /etc/netplan/
   ```
2. Dans un fichier Netplan dédié, créer une sous-interface VLAN en remplaçant les valeurs d'exemple :
   ```yaml
   network:
     version: 2
     renderer: networkd
     ethernets:
       enp1s0:
         dhcp4: false
     vlans:
       vlan20:
         id: 20
         link: enp1s0
         addresses: [192.0.2.20/24]
         routes:
           - to: default
             via: 192.0.2.1
         nameservers:
           addresses: [192.0.2.53]
   ```
3. Vérifier la syntaxe et appliquer avec retour automatique :
   ```bash
   sudo netplan generate
   sudo netplan try
   ip -d link show vlan20
   ```
   👉 *Explication : le VLAN doit être autorisé sur le port trunk; l'ID, le sous-réseau et le DNS sont des exemples documentaires.*

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier le VLAN ID, le réseau IP, le MTU et l'interface trunk côté switch/hyperviseur; sauvegarder les fichiers Netplan existants.
2. Déclarer le VLAN avec le renderer réellement utilisé par la machine. Ne pas attribuer simultanément la même adresse à l'interface physique et au VLAN.
3. Appliquer avec `netplan try`, confirmer uniquement si l'accès est conservé, puis vérifier :
   ```bash
   ip -br address
   ip route
   resolvectl status
   ping -c 3 <passerelle-vlan>
   ```

## 🔒 3. Production — Façon Sécurisée
1. Utiliser une console hyperviseur avant de modifier le réseau d'administration; une erreur de VLAN peut couper SSH.
2. Ne pas exposer les interfaces non nécessaires et maintenir le filtrage cohérent avec le nouveau sous-réseau.
3. Si cloud-init gère le réseau, modifier la source de configuration prévue au lieu d'éditer un fichier généré.

## ✅ Validation et retour arrière
- Tester passerelle, DNS et service attendu depuis le VLAN, ainsi que l'absence de connectivité depuis les segments non autorisés.
- Si l'accès est perdu, laisser `netplan try` annuler ou restaurer le fichier précédent depuis la console.
- Confirmer la persistance après un redémarrage planifié.