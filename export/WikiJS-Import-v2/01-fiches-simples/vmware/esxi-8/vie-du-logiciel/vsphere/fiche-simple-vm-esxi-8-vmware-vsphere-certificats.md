---
title: "Fiche Simple - VM ESXi 8 VMware vSphere Certificats"
description: "Remplacer ou renouveler les certificats du vCenter pour obtenir une chaîne de confiance valide."
published: true
date: 2026-10-29T21:24:09Z
tags: ["vmware-vsphere", "vsphere8", "vcenter", "certificats", "tls", "vmca"]
editor: markdown
dateCreated: 2026-10-29T21:24:09Z
dateModified: 2026-10-29T21:24:09Z
---

# Fiche_Simple_-_VM_ESXi_8_VMware_vSphere_Certificats

- **Environnement** : vCenter Server Appliance 8.x et hôtes ESXi 8.x de laboratoire
- **OS / Version** : VMware vSphere 8.x
- **Catégorie** : virtualisation / vCenter
- **Tags** : `vmware-vsphere`, `vsphere8`, `vcenter`, `certificats`, `tls`, `vmca`

---

## Problème précis à résoudre

Remplacer ou renouveler les certificats du vCenter pour obtenir une chaîne de confiance valide.

## 1. Hors-Production (Lab / Test / POC)

1. Dans vSphere Client : **Administration > Certificats > Gestion des certificats** ; consulter les dates d'expiration des certificats Machine SSL et des solutions.
   👉 Explication : contrôler régulièrement : un certificat expiré coupe l'accès.
2. Générer une demande de signature : **Actions > Certificat Machine SSL > Générer une demande de signature de certificat** avec le FQDN `VCSA_FQDN`, la faire signer par l'autorité interne.
   👉 Explication : la clé privée reste sur le vCenter.
3. Importer la chaîne signée par **Actions > Importer et remplacer le certificat**.
   👉 Explication : les services redémarrent ; vérifier les chaînes d'approbation sur les postes.
4. Option en CLI sur l'appliance (shell) : `/usr/lib/vmware-vmca/bin/certificate-manager`.
   👉 Explication : l'outil propose des options guidées ; suivre la documentation de la version.

## 2. Production — Contrôles

- Sauvegarder le VCSA avant tout remplacement ; planifier une fenêtre de maintenance.

## 3. Production — Sécurité

- Utiliser une AC interne, ne pas partager les clés privées, surveiller l'expiration.

## Validation et retour arrière

- **Validation** : le navigateur et les ESXi font confiance au certificat. **Retour arrière** : restaurer la sauvegarde ou le snapshot pris avant l'opération.

## Si le problème n'est pas résolu

- [Fiche d'entrée VMware vSphere](/01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-vmware-vsphere)
- [Fiche voisine — Snapshots vSphere](/01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-snapshots)
- [Broadcom — Documentation vSphere 8](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0.html)