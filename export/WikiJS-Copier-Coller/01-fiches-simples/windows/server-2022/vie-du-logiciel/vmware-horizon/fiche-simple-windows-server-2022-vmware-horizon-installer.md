# Fiche_Simple_-_Windows_Server_2022_VMware_Horizon_Installer

- **Environnement** : Serveurs Windows Server 2022 (Connection Server), vCenter, UAG, compte administrateur nominatif
- **OS / Version** : Windows Server 2022; version Horizon à vérifier auprès de l'éditeur
- **Catégorie** : VDI / Horizon

---

## Problème précis à résoudre

Installer le Connection Server Horizon et l'Horizon Agent, puis ouvrir la console.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'empreinte du programme d'installation téléchargé depuis le portail officiel. PowerShell :
```powershell
Get-FileHash -Algorithm SHA256 -Path CHEMIN_INSTALLEUR_CS
```
   👉 Explication : CHEMIN_INSTALLEUR_CS est à remplacer par le fichier téléchargé.

2. Sur CS1_HORIZON, lancer l'installeur en administrateur ; choisir **Horizon Standard Server**, saisir le mot de passe de récupération des données (saisi, jamais écrit ici), accepter la règle pare-feu proposée.
   👉 Explication : ce mot de passe protège les sauvegardes LDAP ; le stocker dans un coffre.

3. Ouvrir la console : https://CS1_HORIZON/admin, GUI **Settings > Product Licensing and Usage > Edit License** et saisir la clé.
   👉 Explication : active les fonctions selon l'édition.

4. Ajouter vCenter : GUI **Settings > Servers > vCenter Servers > Add**, saisir VCENTER_FQDN, COMPTE_HORIZON_VC et accepter le certificat après vérification de l'empreinte.
   👉 Explication : permet à Horizon de provisionner les VM.

5. Installer l'Horizon Agent sur VM_MODELE : installeur Horizon Agent, options de protocole et USB selon besoin, puis redémarrer.
   👉 Explication : le nom exact des options varie selon la version.

6. Contrôler les services. PowerShell :
```powershell
Get-Service -DisplayName '*VMware Horizon*' | Format-Table Name,DisplayName,Status
```
   👉 Explication : les services Connection Server portent un nom contenant VMware Horizon ; confirmer sur votre version.

## 2. Production — Contrôles

- Noter la version installée.
- Snapshot de VM_MODELE et CS1_HORIZON avant installation.

## 3. Production — Sécurité

- Compte d'installation nominatif.
- Ne pas laisser les ports d'administration ouverts au réseau utilisateur.

## Validation et retour arrière

- **Validation** : Console accessible, vCenter en état vert, agent démarré.
- **Retour arrière** : Restaurer le snapshot ; désinstaller via appwiz.cpl en dernier recours.

## Si le problème n'est pas résolu

- [Documentation Horizon (Omnissa/VMware)](https://docs.omnissa.com/)
- [Broadcom TechDocs — Horizon](https://techdocs.broadcom.com/)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-vmware-horizon)