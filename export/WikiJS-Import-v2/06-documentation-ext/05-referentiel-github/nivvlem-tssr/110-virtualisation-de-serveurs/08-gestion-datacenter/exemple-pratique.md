---
title: "TP – Gestion des modèles et du datacenter vSphere"
description: "- Se connecter à l’hyperviseur ESXi1 via navigateur (Chrome/Firefox)"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Gestion des modèles et du datacenter vSphere

## Partie 1 – Gestion de modèles OVF

### 1. Export depuis ESXi1

- Se connecter à l’hyperviseur **ESXi1** via navigateur (Chrome/Firefox)
- Clic droit sur la VM `SRV-1` > **Exporter**
- Cocher toutes les cases **sauf nvram**
- Télécharger les fichiers `.ovf`, `.vmdk`, `.mf` localement

### 2. Import vers ESXi2

- Se connecter à **ESXi2** via navigateur
- Cliquer sur « Créer/Enregistrer une machine virtuelle »
- Importer les fichiers précédents
- Nommer la nouvelle VM **SRV-2**
- Choisir **DS-ISCSI** comme banque de données
- Ignorer les alertes de certificat ou erreurs et poursuivre
- Démarrer la VM `SRV-2` pour valider son fonctionnement

---

## Partie 2 – Déploiement de vCenter et gestion de datacenter

### I. Préparation de l’environnement DNS sur SRV_2K19

- Ajouter une **2e carte réseau** à SRV_2K19
    - IP : `10.5.100.21/16`, DNS local : `10.5.100.21`
- Renommer le serveur avec suffixe : `vmwareMD.lab`
- Installer le **rôle serveur DNS**
- Créer une **zone directe** nommée `vmwareMD.lab`
- Ajouter les enregistrements A pour : `ESXi1`, `ESXi2`, `vcenter.vmwareMD.lab`

### II. Déploiement de vCenter (VCSA)

- Télécharger l’OVA depuis `\\distrib\iso\virtualisation\vSphere 7`
- Ouvrir le fichier avec VMware Workstation
- Mode de déploiement : **Tiny with embedded PSC**
- Configurer :
    - IP statique : `10.107.100.10/16`
    - Passerelle : `10.107.255.254`
    - DNS : `10.107.100.21`
    - Nom FQDN : `vcenter.vmwareMD.lab`
    - Mot de passe root : attention au clavier **QWERTY** !

### III. Configuration du vCenter (via port 5480)

- Se connecter à `https://vcenter.vmwareMD.lab:5480`
- Suivre l’assistant de configuration
    - Créer un domaine SSO `vsphere.local`

### IV. Accès au vCenter Web (port 443)

- Se connecter à `https://vcenter.vmwareMD.lab`
- S’authentifier avec `administrator@vsphere.local`

### V. Création du datacenter et ajout des hôtes

- Créer un datacenter `DATAPROD`
- Ajouter les hôtes `ESXi1` et `ESXi2`
- Authentifier avec les mots de passe `root` des ESXi

---

## Partie 3 – Migrations vMotion et Storage vMotion

### vMotion (calcul)

- Démarrer `SRV-2` sur ESXi2
- Sans l’arrêter, clic droit > **Migrer** > migration de l’hôte
- Choisir **ESXi1** comme hôte destination
- Laisser les options par défaut (port group, ressources, etc.)

### Storage vMotion

- Démarrer `SRV-1` si nécessaire
- Clic droit > **Migrer** > migration du stockage
- Choisir **DS-NFS** comme nouvelle banque de données
- Suivre l’assistant jusqu’à la fin

### Vérification

- S’assurer que les deux VMs sont **toujours fonctionnelles** après migration
- Contrôler l’impact dans les tâches récentes et le stockage (DS-NFS et DS-ISCSI)

---

## ✅ À retenir pour les révisions

- L’export OVF permet de transférer une VM entre ESXi sans vCenter
- vCenter (vCSA) est nécessaire pour gérer le datacenter, les hôtes et les services avancés
- Le **déploiement vCSA** exige DNS fonctionnel et configuration réseau fiable
- **vMotion** et **Storage vMotion** nécessitent ressources partagées (réseau, datastore)

---

## 📌 Bonnes pratiques professionnelles

- Utiliser des noms explicites pour le DNS, les datacenters et les hôtes
- Toujours valider le fonctionnement des VMs après migration
- Documenter l’architecture : IP, nom FQDN, datastores, port groups
- Sauvegarder le vCenter régulièrement (snapshot, VDP, solution externe)
- Planifier les maintenances de VM avant migration pour éviter les pertes

---

## 🔗 Composants et outils utilisés

- vSphere Web Client : https (port 443)
- vCSA Console : https (port 5480)
- DNS Windows Server
- ISO `VMware-vCenter-Server-Appliance*.ova`
- Port groups, Datastores, Migrations, Templates OVF