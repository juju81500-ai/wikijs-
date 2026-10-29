# Fiche_Simple_-_VM_ESXi_8_VMware_vSphere_VCSA_Sauvegarde_Restauration_VAMI

- **Environnement** : vCenter Server Appliance 8.x et hôtes ESXi 8.x de laboratoire
- **OS / Version** : VMware vSphere 8.x
- **Catégorie** : virtualisation / vCenter
- **Tags** : `vmware-vsphere`, `vsphere8`, `vcenter`, `vcsa`, `vami`, `sauvegarde`, `restauration`

---

## Problème précis à résoudre

Sauvegarder la configuration du VCSA par la VAMI et savoir la restaurer.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir `https://VCSA_FQDN:5480`, se connecter en `root`, puis **Sauvegarde > Configurer**.
   👉 Explication : la VAMI propose la sauvegarde sur un serveur externe ; les protocoles pris en charge (par exemple FTPS, HTTPS, SFTP, NFS, SMB) sont listés dans la documentation de la version.
2. Renseigner l'emplacement `PROTOCOLE://SERVEUR_SAUVEGARDE/CHEMIN`, un compte dédié à écriture seule, les éléments à inclure (stats, événements, tâches) et un chiffrement optionnel : valider avec **Créer**. Les mots de passe sont saisis dans l'interface.
   👉 Explication : la sauvegarde est de type « fichier » du VCSA : elle ne remplace pas la sauvegarde des VM.
3. Planifier : **Sauvegarde > Planification**, fréquence, rétention, puis lancer une sauvegarde immédiate **Sauvegarder maintenant**.
   👉 Explication : une sauvegarde non testée n'est pas une garantie.
4. Restauration : monter l'ISO d'installation, lancer l'installateur et choisir **Restaurer**, indiquer l'emplacement et la sauvegarde, puis valider.
   👉 Explication : la restauration déploie un nouveau VCSA et réinjecte la configuration ; prévoir la même version et un nom/IP identiques.

## 2. Production — Contrôles

- Rétention conforme à la politique ; stockage de sauvegarde distinct de l'infrastructure virtualisée ; test de restauration périodique.

## 3. Production — Sécurité

- Compte de sauvegarde dédié, mot de passe de chiffrement conservé dans un coffre, accès au dépôt restreint.

## Validation et retour arrière

- **Validation** : sauvegarde en état « Succès » et restauration testée sur un VCSA de lab. **Retour arrière** : supprimer le VCSA restauré de test ; ne jamais allumer deux VCSA identiques sur le même réseau.

## Si le problème n'est pas résolu

- [Fiche d'entrée VMware vSphere](../../../../Logiciels/03-Virtualisation-et-conteneurisation/Fiche_Logiciel_-_VMware-vSphere.md)
- [Fiche voisine — Snapshots vSphere](Fiche_Simple_-_VM_ESXi_8_VMware_vSphere_Snapshots.md)
- [Broadcom — Documentation vSphere 8](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0.html)
