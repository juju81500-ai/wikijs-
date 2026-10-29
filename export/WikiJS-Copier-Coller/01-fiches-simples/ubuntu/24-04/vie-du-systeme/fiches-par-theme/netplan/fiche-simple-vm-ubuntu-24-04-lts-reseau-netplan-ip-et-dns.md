# 📄 VM_Ubuntu_24.04_Reseau_Fixer-IP-Et-DNS.md

- **Environnement** : VM (Proxmox VE / KVM / VMware)
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat) - Famille Debian
- **Catégorie** : Réseau / Netplan

---

## 🎯 Problème précis à résoudre
Fixer une adresse IP statique, la passerelle et les serveurs DNS sous Ubuntu Server 24.04 LTS avec l'outil Netplan et le backend `systemd-networkd`.

---

## ⚡ Méthode Étape par Étape

1. **Repérer le nom de la carte réseau** :
   ```bash
   ip a
   ```
   👉 *Explication : Tu identifies le nom exact de l'interface réseau (ex: `eth0` ou `enp0s3`).*

2. **Identifier le fichier Netplan et son gestionnaire** :
  ```bash
  ls -l /etc/netplan/
  cloud-init status --long
  ```
  👉 *Explication : Si cloud-init gère le réseau, une modification locale peut être régénérée au redémarrage ; utiliser la source de configuration propriétaire.*

3. **Insérer la configuration réseau statique** :
   ```yaml
   network:
     version: 2
     renderer: networkd
     ethernets:
       eth0:
         dhcp4: no
         addresses:
           - 192.168.1.70/24
         routes:
           - to: default
             via: 192.168.1.1
         nameservers:
           addresses:
             - 192.168.1.10
   ```
   👉 *Explication : Remplacer l'interface, l'adresse, la passerelle et le résolveur interne par ceux du plan réseau. Ne pas ajouter un DNS public sans validation de la politique réseau.*

4. **Tester et appliquer la configuration sans risque de coupure** :
   ```bash
   sudo netplan try
   ```
   👉 *Explication : Netplan teste la syntaxe pendant 120 secondes. Si tu ne valides pas, il annule automatiquement pour éviter de te bloquer.*

5. **Vérifier après confirmation** :
   ```bash
  ip -br addr
  ip route
  resolvectl status
   ```
  👉 *Explication : `netplan try` applique la configuration et la conserve après confirmation ; vérifier adresse, route et DNS depuis la console avant de fermer l'accès de secours.*