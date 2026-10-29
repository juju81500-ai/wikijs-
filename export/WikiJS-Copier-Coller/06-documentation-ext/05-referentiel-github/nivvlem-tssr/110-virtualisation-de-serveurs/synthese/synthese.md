# 📘 Synthèse – Virtualisation de serveurs

## 🧱 Concepts fondamentaux

- **Virtualisation** = exécution de plusieurs OS sur une même machine physique via un **hyperviseur**.
- Elle repose sur la **mutualisation, consolidation et rationalisation** des ressources IT.

### Types d’hyperviseurs

|Type|Caractéristique|Exemples|
|---|---|---|
|Type 1|Exécuté directement sur le matériel|VMware ESXi, Hyper-V, KVM|
|Type 2|Installé sur un OS hôte|VirtualBox, VMware Workstation|

### Autres formes

- **Paravirtualisation** : OS modifié (Xen)
- **Containers** : virtualisation d’environnement (Docker)

---

## 🔧 Infrastructures clés (VMware / Microsoft)

### VMware vSphere

- **ESXi** = hyperviseur natif
- **vCenter Server** = gestion centralisée (cluster, HA, DRS, vMotion...)
- **vSwitchs** = réseau virtuel (Standard ou Distribué)
- **Datastores** = stockage VMFS ou NFS
- **Templates OVF / VMTX** = déploiement automatisé

### Microsoft Hyper-V

- Intégré à Windows Server / Windows 10+
- Console MMC : Hyper-V Manager
- Support de snapshot, Live Migration, switch virtuel (externe, interne, privé)

---

## 📦 Stockage

- **DAS** (local), **SAN** (iSCSI/FC), **NAS** (NFS/CIFS)
- Formats disques : VMDK (VMware), VHD/VHDX (Microsoft)
- **VMFS** : système de fichiers utilisé pour les LUN ESXi
- **Provisionnement** : Thin vs Thick
- RDM = accès direct à un LUN physique (cas particuliers)

---

## 🌐 Réseau

- **vSwitch** (local) vs **vSwitch Distribué** (centralisé via vCenter)
- **Port groups** = affectation logique des flux : VM Network, Management, vMotion, iSCSI...
- **VLANs** : standard 802.1Q, tagging par port group ou OS invité
- **Teaming** : redondance + agrégation de bande passante

---

## 📊 Services avancés (vCenter)

|Service|Fonction|
|---|---|
|**vMotion**|Migration à chaud d’une VM entre hôtes|
|**Storage vMotion**|Déplacement à chaud du stockage|
|**DRS**|Répartition intelligente des ressources|
|**HA**|Redémarrage auto d’une VM sur autre hôte si crash|
|**FT**|Redondance temps réel d’une VM (zéro perte)|

> Ces services nécessitent un **vCenter actif** + licences adaptées

---

## 🧠 Gestion des utilisateurs

- Créer des **groupes + rôles personnalisés** (principe de moindre privilège)
- Utiliser **SSO + Active Directory** si possible
- Appliquer les droits **le plus haut possible** dans l’arborescence (héritage activé)

---

## ✅ À retenir pour les révisions

- L’hyperviseur **ESXi** est un composant clé pour une infrastructure professionnelle
- **Hyper-V** est idéal pour les environnements Windows (intégré, facile à déployer)
- La **gestion réseau et stockage** est aussi critique que la gestion des VMs
- Le **vCenter Server Appliance (VCSA)** simplifie la supervision d’un datacenter
- **Sysprep + templates** permettent un déploiement automatisé et cohérent

---

## 📌 Bonnes pratiques professionnelles

- Déployer une architecture **documentée** : VM, datastores, VLAN, IPs, DNS...
- Séparer les flux critiques (VM / gestion / stockage / sauvegarde) sur des réseaux ou VLANs dédiés
- Sauvegarder le **vCenter** et les **configurations des hôtes**
- Ne jamais migrer une VM avec **ISO encore monté** ou **snapshot actif**
- Toujours vérifier **l’adressage IP + DNS + routage** avant déployer vCSA
- Nommer clairement les objets : `DS-PROD`, `SRV-AD-01`, `GRP-VMNET`, etc.

---

## 🔗 Commandes et outils à connaître

```powershell
# Hyper-V
Get-VM, New-VM, Start-VM, Export-VM, Import-VM

# vSphere CLI (PowerCLI / ESXCLI)
esxcli storage filesystem list
esxcli network vswitch standard list

# DNS (SRV_2K19)
dnsmgmt.msc, nslookup, ping, ipconfig /all

# vSphere Web Client (port 443)
https://vcenter.domain.local
```