# Fiche_Simple_-_VM_ESXi_8_VMware_vSphere_VCSA_Installer

- **Environnement** : vCenter Server Appliance 8.x et hôtes ESXi 8.x de laboratoire
- **OS / Version** : VMware vSphere 8.x
- **Catégorie** : virtualisation / vCenter
- **Tags** : `vmware-vsphere`, `vsphere8`, `vcenter`, `vcsa`, `installation`

---

## Problème précis à résoudre

Déployer un vCenter Server Appliance (VCSA) 8.x depuis l'ISO officiel.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'ISO du VCSA depuis le portail Broadcom (compte et droit d'usage requis) et vérifier sa somme de contrôle publiée. Prévoir un nom DNS (enregistrements A et PTR) et une adresse IP fixe : `VCSA_FQDN` et `VCSA_IP` sont à remplacer.
   👉 Explication : le DNS direct et inverse doit être correct avant le déploiement.
2. Monter l'ISO sur le poste d'administration et lancer l'installateur graphique (`vcsa-ui-installer`, dossier du système du poste : win32, lin64 ou mac). Choisir **Installer**, renseigner l'hôte ESXi cible, la taille de déploiement, le datastore, le réseau, puis valider.
   👉 Explication : l'étape 1 déploie l'appliance ; l'étape 2 configure le service : SSO, domaine, NTP, accès SSH.
   Mot de passe root et SSO : saisis dans l'assistant, jamais écrits en clair dans un fichier.
3. Équivalent CLI : copier un modèle de `vcsa-cli-installer/templates/install/`, le renseigner puis le contrôler avant exécution :
   ```bash
   ./vcsa-deploy install --precheck-only MODELE_A_REMPLACER.json
   ./vcsa-deploy install --accept-eula --acknowledge-ceip MODELE_A_REMPLACER.json
   ```
   👉 Explication : `MODELE_A_REMPLACER.json` est à remplacer ; ne pas stocker de mot de passe dans le JSON (laisser l'invite) ou protéger le fichier ; vérifier les options de la version publiée.
4. Se connecter ensuite à `https://VCSA_FQDN/ui` (vSphere Client) et à `https://VCSA_FQDN:5480` (VAMI).
   👉 Explication : la connexion SSO valide le déploiement.

## 2. Production — Contrôles

- Dimensionner l'appliance selon l'inventaire (hôtes, VM) ; la documentation précise les tailles.
- Synchroniser l'heure (NTP) et sauvegarder la configuration juste après l'installation (fiche Sauvegarde_Restauration_VAMI).

## 3. Production — Sécurité

- Désactiver SSH s'il n'est pas utilisé ; limiter l'accès au port 5480 aux postes d'administration ; changer les mots de passe initiaux selon la politique.

## Validation et retour arrière

- **Validation** : vSphere Client accessible, hôtes ajoutés, alarmes saines. **Retour arrière** : supprimer la VM VCSA déployée en lab ; en production, restaurer depuis la sauvegarde.

## Si le problème n'est pas résolu

- [Fiche d'entrée VMware vSphere](../../../../Logiciels/03-Virtualisation-et-conteneurisation/Fiche_Logiciel_-_VMware-vSphere.md)
- [Fiche voisine — Snapshots vSphere](Fiche_Simple_-_VM_ESXi_8_VMware_vSphere_Snapshots.md)
- [Broadcom — Documentation vSphere 8](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0.html)
