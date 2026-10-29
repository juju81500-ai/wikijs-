# Fiche_Simple_-_Hote_VMware_ESXi_8_ESXi_Ajouter_vCenter_Premier_Invite.md

- **Environnement** : Hôte physique VMware ESXi 8.0 pilote autonome (DCUI, Host Client, vCenter)
- **OS / Version** : VMware ESXi 8.0, build et image OEM validés sur le matériel
- **Catégorie** : virtualisation / vCenter
- **Tags** : `vmware`, `esxi`, `vsphere8`, `hyperviseur`, `vcenter`, `vm-pilote`

---

## Problème précis à résoudre

Intégrer l'hôte à vCenter et déployer une VM de test.

## 1. Hors-Production (Lab / Test / POC)

1. Déployer vCenter Server Appliance selon la documentation de la version retenue : **Installateur vCenter > Install > Stage 1 / Stage 2**
   👉 Explication : vérifier compatibilité ESXi/vCenter, DNS, NTP, stockage et certificat avant l'enrôlement.

2. Ajouter l'hôte à l'inventaire : **vSphere Client > Datacenter > Add Host**
   👉 Explication : utiliser des rôles et comptes nominatifs plutôt que root.

3. Créer la VM pilote : **Clic droit sur le cluster/hôte > New Virtual Machine**
   👉 Explication : image approuvée, ressources documentées, réseau isolé ou explicitement autorisé.

## 2. Production — Contrôles

Créer dossier, resource pool si justifié, datastore et réseau pilote; tester sauvegarde puis restauration isolée avant production.

## 3. Production — Sécurité

- Éviter l'usage courant de root.

## Validation et retour arrière

- **Validation** : VM de test démarrée, console et accès fonctionnels.
- **Retour arrière** : supprimer la VM de test et retirer l'hôte de l'inventaire.

## Si le problème n'est pas résolu

- [Broadcom — ESXi Installation and Setup 8.0](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0.html)
- [Broadcom — configurer ESXi après installation](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0/installing-and-setting-up-esxi-install/setting-up-esxi-install.html)
- [Guide complet VMware ESXi 8.0](../../../../../../02-Fiches-Completes/VMware/ESXi-8/Installation-Deploiement/56_Deploiement_VMware_ESXi_8_0.md#4-ajouter-vcenter-et-un-premier-invite)
