---
title: "Fiche Simple - Hote VMware ESXi 8 ESXi Configurer Services Essentiels"
description: "Configurer heure, DNS, réseau, stockage et journaux."
published: true
date: 2026-10-29T20:22:42Z
tags: ["vmware", "esxi", "vsphere8", "hyperviseur", "ntp", "dns", "syslog", "vswitch"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Fiche_Simple_-_Hote_VMware_ESXi_8_ESXi_Configurer_Services_Essentiels.md

- **Environnement** : Hôte physique VMware ESXi 8.0 pilote autonome (DCUI, Host Client, vCenter)
- **OS / Version** : VMware ESXi 8.0, build et image OEM validés sur le matériel
- **Catégorie** : virtualisation / configuration
- **Tags** : `vmware`, `esxi`, `vsphere8`, `hyperviseur`, `ntp`, `dns`, `syslog`, `vswitch`

---

## Problème précis à résoudre

Configurer heure, DNS, réseau, stockage et journaux.

## 1. Hors-Production (Lab / Test / POC)

1. Configurer l'heure et NTP : **Host Client > Manage > System > Time & date > Edit NTP Settings**
   👉 Explication : un ESXi à l'heure est indispensable aux journaux et à vCenter.
   Équivalent en ligne de commande (ESXi Shell, adresses d'exemple à remplacer) :
   ```bash
   esxcli system ntp set --enabled=true --server=192.0.2.1
   esxcli system ntp get
   ```
   👉 Explication : définit le serveur de temps et affiche la configuration.

2. Configurer DNS : **Host Client > Networking > TCP/IP stacks > Default TCP/IP stack > Edit settings**
   👉 Explication : confirmer la résolution directe et inverse du FQDN.
   Équivalent en ligne de commande (ESXi Shell, adresses d'exemple à remplacer) :
   ```bash
   esxcli network ip dns server add --server=192.0.2.53
   esxcli network ip dns server list
   ```
   👉 Explication : ajoute et liste les serveurs DNS.

3. Créer vSwitch et port groups : **Host Client > Networking > Virtual switches / Port groups**
   👉 Explication : isoler la gestion des réseaux VM; ne pas relier un port group à un uplink non validé.
   Équivalent en ligne de commande (ESXi Shell, adresses d'exemple à remplacer) :
   ```bash
   esxcli network vswitch standard list
   esxcli network vswitch standard portgroup list
   ```
   👉 Explication : liste les vSwitch et port groups pour contrôler le design.

4. Créer ou monter les datastores : **Host Client > Storage > New datastore**
   👉 Explication : vérifier signatures, volumes et chemins multipath; ne pas initialiser un volume contenant des données.
   Équivalent en ligne de commande (ESXi Shell, adresses d'exemple à remplacer) :
   ```bash
   esxcli storage filesystem list
   ```
   👉 Explication : liste les datastores montés; aucune initialisation n'est faite.

5. Configurer le syslog distant : **Manage > System > Advanced settings > Syslog.global.logHost**
   👉 Explication : vérifier la réception côté serveur de journaux.
   Équivalent en ligne de commande (ESXi Shell, adresses d'exemple à remplacer) :
   ```bash
   esxcli system syslog config set --loghost='udp://192.0.2.20:514'
   esxcli system syslog reload
   ```
   👉 Explication : définit le collecteur distant puis recharge le service.

6. Contrôler SSH et ESXi Shell : **Host Client > Manage > Services > TSM-SSH / ESXi Shell > Stop**
   👉 Explication : les désactiver lorsqu'inutiles; restreindre le Host Client au réseau d'administration.
   Équivalent en ligne de commande (ESXi Shell, adresses d'exemple à remplacer) :
   ```bash
   vim-cmd hostsvc/stop_ssh
   ```
   👉 Explication : arrête le service SSH.

## 2. Production — Contrôles

Préserver l'espace des journaux locaux et restreindre l'accès au réseau d'administration.

## 3. Production — Sécurité

- Ne pas laisser SSH ou l'ESXi Shell actifs en permanence.

## Validation et retour arrière

- **Validation** : NTP synchronisé, DNS résolu, syslog reçu.
- **Retour arrière** : revenir aux paramètres précédents depuis le Host Client ou la DCUI.

## Si le problème n'est pas résolu

- [Broadcom — ESXi Installation and Setup 8.0](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0.html)
- [Broadcom — configurer ESXi après installation](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0/installing-and-setting-up-esxi-install/setting-up-esxi-install.html)
- [Guide complet VMware ESXi 8.0](/02-fiches-completes/vmware/esxi-8/installation-deploiement/56-deploiement-vmware-esxi-8-0#3-configurer-les-services-essentiels)