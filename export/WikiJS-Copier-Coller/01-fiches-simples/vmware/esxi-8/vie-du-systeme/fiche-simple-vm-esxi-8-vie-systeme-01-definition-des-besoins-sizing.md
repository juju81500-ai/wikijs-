# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_01_Definition_Des_Besoins_Sizing

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 01 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Dimensionner l'hôte ESXi avant l'achat ou l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les VM à héberger avec vCPU, RAM et disque. Sur un hôte existant, relever les ressources (Host Client : **Hôte > Surveiller > Performances**; SSH) :
   ```sh
   esxcli hardware cpu global get
   esxcli hardware memory get
   esxcli storage core device list | grep -E 'Display Name|Size'
   ```
   👉 Explication : donne le nombre de cœurs, la RAM et la taille des disques.

2. Calculer le total : vCPU (ratio de sur-allocation 3:1 à 5:1 selon la charge), RAM des VM + environ 4 Go pour l'hyperviseur.
   👉 Explication : ESXi peut sur-allouer la RAM (ballooning) mais les performances chutent.

3. Prévoir réseau et stockage : 2 cartes minimum pour la gestion (redondance), cartes dédiées vMotion/stockage, datastore local SSD/NVMe ou stockage partagé.
   👉 Explication : un hôte à 1 seule carte réseau n'a aucune redondance.

## 2. Production — Contrôles

Ajouter 20 à 30 % de marge; prévoir N+1 si plusieurs hôtes sous vCenter.

## 3. Production — Sécurité

Vérifier la compatibilité du matériel dans le guide de compatibilité Broadcom (VMware Compatibility Guide).

## Validation et retour arrière

- **Validation** : Tableau de sizing validé par le propriétaire du service.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)