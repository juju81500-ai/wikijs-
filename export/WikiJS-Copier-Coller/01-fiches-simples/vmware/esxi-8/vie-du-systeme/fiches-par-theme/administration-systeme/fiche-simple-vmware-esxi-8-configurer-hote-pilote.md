# 📄 Fiche_Simple_-_VMware_ESXi_8_Configurer_Hote_Pilote.md

- **Environnement** : Hôte physique VMware ESXi 8.0 et console d'administration
- **OS / Version** : ESXi 8.0 build/image validée par l'OEM
- **Catégorie** : Virtualisation / mise en service

---

## 🎯 Problème précis à résoudre

Finaliser les paramètres d'un hôte ESXi pilote avant de le rattacher à une plateforme de production.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Confirmer build et matériel : **Host Client > Manage > System > ... / Host > Summary**, ou en SSH :
   ```sh
   vmware -vl
   esxcli hardware platform get
   esxcli storage filesystem list
   ```
   👉 Explication : comparer à la liste de compatibilité (HCL); garder l'accès console (iLO/iDRAC ou DCUI).

2. Définir hostname, IP de management, DNS et passerelle : **DCUI (F2) > Configure Management Network**, ou Host Client **Networking > VMkernel NICs**, **TCP/IP stacks**, ou :
   ```sh
   esxcli system hostname set --host=esxi01 --domain=example.net
   esxcli network ip interface ipv4 set -i vmk0 -t static -I 192.0.2.10 -N 255.255.255.0
   esxcli network ip route ipv4 add -n default -g 192.0.2.1
   esxcli network ip dns server add -s 192.0.2.53
   ```
   👉 Explication : remplacer par les valeurs validées; une erreur coupe l'accès réseau, d'où la console.

3. Configurer NTP : **Host Client > Manage > System > Time & date > Edit settings** (NTP), ou :
   ```sh
   esxcli system ntp set -s 192.0.2.123 -e yes
   esxcli system ntp get
   ```
   👉 Explication : l'heure conditionne certificats et vCenter.

4. Créer un port group et un datastore de test après identification des uplinks et périphériques : **Networking > Port groups > Add port group** et **Storage > New datastore**, ou :
   ```sh
   esxcli network nic list
   esxcli network vswitch standard portgroup add -p PG-LAB -v vSwitch0
   esxcli storage core device list | grep -E 'Display Name|Size'
   ```
   👉 Explication : identifier le bon disque avant de créer le datastore; ne jamais effacer un LUN existant.

5. Envoyer les logs vers un collecteur pilote : **Manage > System > Advanced settings > Syslog.global.logHost**, ou :
   ```sh
   esxcli system syslog config set --loghost='udp://192.0.2.50:514'
   esxcli system syslog reload
   esxcli network firewall ruleset set -r syslog -e true
   ```
   👉 Explication : remplacer le collecteur; vérifier la réception depuis le réseau d'administration.

## ⚡ 2. Production — Façon Simplifiée

1. Contrôler uplinks, VLANs, stockage, multipath, heure, DNS, syslog, licences et certificats :
   ```sh
   esxcli network nic list
   esxcli network vswitch standard list
   esxcli storage core path list | head
   esxcli system ntp get
   esxcli system syslog config get
   ```
   👉 Explication : GUI : **Host Client > Networking / Storage / Manage > Licensing / Certificates**; rattacher ensuite à vCenter selon le design et les droits.

## 🔒 3. Production — Façon Sécurisée

- Restreindre Host Client, SSH et ESXi Shell aux réseaux d'administration; fermer SSH/shell après usage.
- Appliquer comptes nominatifs/roles least privilege et placer la gestion hors du réseau des VM.
- Vérifier sauvegarde/restauration de configuration et VM avant d'héberger des charges réelles.

## ✅ Validation et retour arrière

- **Validation** : gestion accessible, DNS/NTP valides, uplinks/datastores sains, logs distants reçus, événements sans erreur bloquante.
- **Retour arrière** : conserver accès console, sauvegarde config et plan de restauration de l'image/build; ne pas reformater un datastore sans identifier son contenu.

## 🔗 Si le problème n'est pas résolu

- [Broadcom — Parcours d'installation ESXi 8](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0/overview-of-the-installation-and-setup-process_esx-install.html)
- [Broadcom — Configurer ESXi après installation](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0/installing-and-setting-up-esxi-install/setting-up-esxi-install.html)