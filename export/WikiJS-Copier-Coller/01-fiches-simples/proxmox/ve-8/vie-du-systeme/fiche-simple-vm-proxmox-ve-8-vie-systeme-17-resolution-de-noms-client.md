# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_17_Resolution_De_Noms_Client

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 17 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Configurer les serveurs DNS de l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : **Nœud > System > DNS > Edit** (domaine de recherche, DNS 1/2/3). En ligne de commande :
   ```bash
   cat /etc/resolv.conf
   pvesh set /nodes/NOEUD/dns --search domaine.local --dns1 IP_DNS
   ```
   👉 Explication : `NOEUD` = nom du nœud; `IP_DNS` = serveur DNS interne.

2. Tester la résolution :
   ```bash
   getent hosts www.proxmox.com
   host $(hostname -f)
   ```
   👉 Explication : le nom externe et le FQDN de l'hôte doivent se résoudre.

3. Prévoir au moins deux serveurs DNS.
   👉 Explication : évite une panne totale si un serveur DNS tombe.

## 2. Production — Contrôles

Utiliser les DNS internes (résolution de l'annuaire et des autres nœuds).

## 3. Production — Sécurité

Ne pas utiliser de DNS public non maîtrisé sur un hôte de production.

## Validation et retour arrière

- **Validation** : `getent hosts` renvoie une adresse.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : Hote Proxmox VE 8 Cluster Preparer](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-preparer>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)