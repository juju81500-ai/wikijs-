# Fiche_Simple_-_Hote_VMware_ESXi_8_ESXi_Verifier_Maintenir.md

- **Environnement** : Hôte physique VMware ESXi 8.0 pilote autonome (DCUI, Host Client, vCenter)
- **OS / Version** : VMware ESXi 8.0, build et image OEM validés sur le matériel
- **Catégorie** : virtualisation / exploitation

---

## Problème précis à résoudre

Vérifier l'état et organiser la maintenance.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler version/build, état matériel, datastores, uplinks, alertes, heure, DNS et syslog : **Host Client > Monitor > Hardware / Events**
   👉 Explication : un contrôle régulier détecte les dérives.

2. Lire la version depuis l'ESXi Shell (SSH activé temporairement et désactivé après) :
   ```bash
   vmware -vl
   ```
   👉 Explication : confirme build et version.

3. Installer les correctifs seulement par la méthode supportée par la version et l'image OEM : **vSphere Client > Lifecycle Manager**
   👉 Explication : planifier fenêtre, bascule et retour arrière après sauvegarde de configuration.

## 2. Production — Contrôles

Définir propriétaires, capacités, RPO/RTO et responsabilités de licence.

## 3. Production — Sécurité

- Un RAID, un datastore répliqué ou un snapshot ne remplace pas une sauvegarde restaurable.

## Validation et retour arrière

- **Validation** : état sain, version attendue, sauvegarde testée.
- **Retour arrière** : restaurer la configuration sauvegardée ou revenir au profil de démarrage précédent selon la procédure du fabricant.

## Si le problème n'est pas résolu

- [Broadcom — ESXi Installation and Setup 8.0](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0.html)
- [Broadcom — configurer ESXi après installation](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0/installing-and-setting-up-esxi-install/setting-up-esxi-install.html)
- [Guide complet VMware ESXi 8.0](/02-fiches-completes/vmware/esxi-8/installation-deploiement/56-deploiement-vmware-esxi-8-0#5-verification-et-maintenance)