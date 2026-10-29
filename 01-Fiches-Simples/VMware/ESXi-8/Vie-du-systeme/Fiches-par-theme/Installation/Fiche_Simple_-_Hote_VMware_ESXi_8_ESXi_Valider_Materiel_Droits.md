# Fiche_Simple_-_Hote_VMware_ESXi_8_ESXi_Valider_Materiel_Droits.md

- **Environnement** : Hôte physique VMware ESXi 8.0 pilote autonome (DCUI, Host Client, vCenter)
- **OS / Version** : VMware ESXi 8.0, build et image OEM validés sur le matériel
- **Catégorie** : virtualisation / cadrage
- **Tags** : `vmware`, `esxi`, `vsphere8`, `hyperviseur`, `compatibilite`, `licence`

---

## Problème précis à résoudre

Vérifier compatibilité matérielle et droits avant installation.

## 1. Hors-Production (Lab / Test / POC)

1. Consulter la matrice de compatibilité Broadcom pour serveur, CPU, contrôleur, NIC et firmware : **Broadcom Compatibility Guide > Systems / Servers**
   👉 Explication : l'image ESXi signée du fabricant doit correspondre au matériel.

2. Confirmer support, mode de licence et droits des fonctions voulues (vCenter, HA, migration, sauvegarde) : **Portail Broadcom Support > Licences**
   👉 Explication : éviter un achat ou un déploiement non couvert.

3. Préparer noms DNS, IP de management, VLAN, passerelle, DNS/NTP et accès console hors bande.
   👉 Explication : ces éléments sont demandés pendant l'installation.

## 2. Production — Contrôles

Inventorier le stockage et vérifier le numéro de périphérique avant installation; prévoir une procédure de restauration.

## 3. Production — Sécurité

- L'installation peut écraser les partitions du disque sélectionné.

## Validation et retour arrière

- **Validation** : matériel listé, licences confirmées, paramètres réseau préparés.
- **Retour arrière** : aucune modification: rien à annuler.

## Si le problème n'est pas résolu

- [Broadcom — ESXi Installation and Setup 8.0](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0.html)
- [Broadcom — configurer ESXi après installation](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0/installing-and-setting-up-esxi-install/setting-up-esxi-install.html)
- [Guide complet VMware ESXi 8.0](../../../../../../02-Fiches-Completes/VMware/ESXi-8/Installation-Deploiement/56_Deploiement_VMware_ESXi_8_0.md#1-valider-le-materiel-et-le-droit-dusage)
