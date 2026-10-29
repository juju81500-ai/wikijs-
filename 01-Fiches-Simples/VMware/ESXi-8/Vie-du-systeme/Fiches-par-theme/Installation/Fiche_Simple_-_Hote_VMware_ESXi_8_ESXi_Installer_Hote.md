# Fiche_Simple_-_Hote_VMware_ESXi_8_ESXi_Installer_Hote.md

- **Environnement** : Hôte physique VMware ESXi 8.0 pilote autonome (DCUI, Host Client, vCenter)
- **OS / Version** : VMware ESXi 8.0, build et image OEM validés sur le matériel
- **Catégorie** : virtualisation / installation
- **Tags** : `vmware`, `esxi`, `vsphere8`, `hyperviseur`, `dcui`, `iso`

---

## Problème précis à résoudre

Installer ESXi depuis l'ISO ou l'image OEM vérifiée.

## 1. Hors-Production (Lab / Test / POC)

1. Démarrer sur le média : **Console BMC/iDRAC/iLO > Média virtuel > Monter l'ISO ESXi**
   👉 Explication : méthode interactive recommandée pour un premier hôte.

2. Dans l'installateur, choisir le disque système après double contrôle : **Select a Disk to Install or Upgrade**
   👉 Explication : vérifier le numéro de périphérique: ce disque sera écrasé.

3. Créer le mot de passe root initial selon la politique du coffre : **Enter a root password**
   👉 Explication : ne jamais le saisir dans un ticket.

4. Après redémarrage, dans la DCUI : **F2 Customize System > Configure Management Network**
   👉 Explication : fixer interface, VLAN de management, IP, masque, passerelle, DNS et hostname.

5. Tester depuis un poste du réseau d'administration :
   ```bash
   ping -c 3 192.0.2.50
   ```
   👉 Explication : avant de quitter la console.

## 2. Production — Contrôles

Choisir la méthode supportée selon l'échelle (interactive, scriptée ou Auto Deploy).

## 3. Production — Sécurité

- Utiliser une image signée du fabricant.

## Validation et retour arrière

- **Validation** : version/build confirmés et hôte joignable.
- **Retour arrière** : réinstaller depuis l'image ou restaurer la configuration sauvegardée.

## Si le problème n'est pas résolu

- [Broadcom — ESXi Installation and Setup 8.0](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0.html)
- [Broadcom — configurer ESXi après installation](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0/installing-and-setting-up-esxi-install/setting-up-esxi-install.html)
- [Broadcom — installer et configurer ESXi](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0/installing-and-setting-up-esxi-install.html)
- [Guide complet VMware ESXi 8.0](../../../../../../02-Fiches-Completes/VMware/ESXi-8/Installation-Deploiement/56_Deploiement_VMware_ESXi_8_0.md#2-installer-esxi)
