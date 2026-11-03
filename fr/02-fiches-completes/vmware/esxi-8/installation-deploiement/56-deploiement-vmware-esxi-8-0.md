---
title: "Installer et préparer un hôte VMware ESXi 8.0"
description: "Fiche simple : [valider le matériel et le droit d'usage](../../../../01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiches-par-theme/installation/fiche-simple-hote-vmware-esxi-8-esxi-valider-materiel-droits.md)."
published: true
date: 2026-11-03T09:36:14Z
tags: ["vmware", "esxi", "vsphere8", "hyperviseur", "datastore", "production"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Installer et préparer un hôte VMware ESXi 8.0

- **OS / Version** : VMware ESXi 8.0, build et image [[Glossary:OEM]] validés sur le matériel ciblé
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Hôte pilote autonome; rattachement vCenter selon licences et architecture
- **Catégorie** : Virtualisation / infrastructure
- **Tags** : `vmware`, `esxi`, `vsphere8`, `hyperviseur`, `datastore`, `production`

## 1. Valider le matériel et le droit d'usage

Fiche simple : [valider le matériel et le droit d'usage](/fr/01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiches-par-theme/installation/fiche-simple-hote-vmware-esxi-8-esxi-valider-materiel-droits).

Vérifier la compatibilité serveur, [[Glossary:CPU]], contrôleur de stockage, [[Glossary:NIC]], firmware et périphériques dans la matrice Broadcom; télécharger l'image ESXi signée et adaptée au fabricant. Confirmer l'accès au support, le mode de licence et les droits des fonctions nécessaires (vCenter, HA, migration, sauvegarde) avant achat et déploiement.

Préparer les noms [[Glossary:DNS]], [[Glossary:IP]] de management, [[Glossary:VLAN]], passerelle, DNS/NTP, datastore d'installation et accès console hors bande. L'installation peut écraser les partitions du disque sélectionné : inventorier le stockage, vérifier le numéro de périphérique et conserver une procédure de restauration.

## 2. Installer ESXi

Fiche simple : [installer ESXi](/fr/01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiches-par-theme/installation/fiche-simple-hote-vmware-esxi-8-esxi-installer-hote).

Choisir la méthode supportée (interactive sur média, scripted ou Auto Deploy selon l'échelle). Pour un premier hôte, suivre l'installation interactive depuis l'ISO/image OEM vérifiée, choisir le disque système après double contrôle et créer le mot de passe root initial selon la politique du coffre.

Après redémarrage, confirmer la version/build et utiliser DCUI pour fixer l'interface, le VLAN de management, IP, masque, passerelle, DNS et hostname. Tester depuis un poste du réseau d'administration avant de quitter l'accès console.

## 3. Configurer les services essentiels

Fiche simple : [configurer les services essentiels](/fr/01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiches-par-theme/installation/fiche-simple-hote-vmware-esxi-8-esxi-configurer-services-essentiels).

- Configurer heure/NTP et DNS forward/reverse; confirmer la résolution du [[Glossary:FQDN]] du host et vCenter.
- Créer des vSwitch/port groups selon le design et isoler la gestion des réseaux [[Glossary:VM]]; éviter de relier un port group à un uplink non validé.
- Créer/monter les datastores après vérification des signatures, volumes et chemins multipath. Ne pas initialiser un volume contenant des données attendues.
- Configurer le syslog distant et vérifier la réception; préserver suffisamment d'espace pour logs locaux.
- Restreindre ESXi Host Client/SSH/ESXi Shell au réseau d'administration et les désactiver lorsqu'inutiles.

## 4. Ajouter vCenter et un premier invité

Fiche simple : [ajouter vCenter et un premier invité](/fr/01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiches-par-theme/installation/fiche-simple-hote-vmware-esxi-8-esxi-ajouter-vcenter-premier-invite).

Déployer vCenter Server Appliance selon la documentation correspondant à la version retenue; vérifier compatibilité ESXi/vCenter, DNS, [[Glossary:NTP]], stockage et certificat avant l'enrôlement. Utiliser des rôles et comptes nominatifs plutôt qu'un usage courant de root.

Créer un dossier, resource pool si justifié, datastore et réseau pilote. Déployer une VM de test avec image approuvée, ressources documentées et réseau isolé ou explicitement autorisé. Tester console, démarrage, accès, sauvegarde puis restauration isolée avant mise en production.

## 5. Vérification et maintenance

Fiche simple : [vérification et maintenance](/fr/01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiches-par-theme/installation/fiche-simple-hote-vmware-esxi-8-esxi-verifier-maintenir).

Contrôler version/build, état hardware, datastore, uplinks, redondance, alertes, heure, DNS, syslog et événements dans Host Client/vCenter. Installer les correctifs uniquement via la méthode supportée par la version et l'image OEM; sauvegarder configuration et planifier la fenêtre, la bascule et le retour arrière.

Définir les propriétaires, capacités, [[Glossary:RPO]]/RTO et responsabilités de licence. Un [[Glossary:RAID]], un datastore répliqué ou un snapshot ne remplace pas une sauvegarde restaurable.

## Sources

- [Broadcom — ESXi Installation and Setup 8.0](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0.html)
- [Broadcom — Parcours d'installation et de configuration ESXi](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0/overview-of-the-installation-and-setup-process_esx-install.html)
- [Broadcom — Installer et configurer ESXi](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0/installing-and-setting-up-esxi-install.html)
- [Broadcom — Configurer ESXi après installation](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0/installing-and-setting-up-esxi-install/setting-up-esxi-install.html)