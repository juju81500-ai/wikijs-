# 📄 Fiche_Simple_-_VMware_ESXi_8_Sauvegarde_Configuration_Hote.md

- **Environnement** : Hôte physique VMware ESXi 8 (ESXi Shell ou SSH, poste d'administration avec vCLI ou PowerCLI)
- **OS / Version** : VMware ESXi 8.0 - Sauvegarde de configuration
- **Catégorie** : Sauvegarde / Configuration de l'hôte

---

## 🎯 Problème précis à résoudre
Sauvegarder la configuration complète d'un hôte ESXi 8 (réseau, stockage, comptes, paramètres avancés) hors de l'hôte, la protéger par chiffrement, et s'assurer qu'elle peut être restaurée.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Inventorier les machines virtuelles et les datastores :
```bash
vim-cmd vmsvc/getallvms
esxcli storage filesystem list
```
👉 Explication : liste les VM enregistrées sur l'hôte avec leur identifiant, et les datastores montés avec leur taille et leur espace libre.

2. Générer la sauvegarde de configuration depuis l'ESXi Shell :
```bash
vim-cmd hostsvc/firmware/backup_config
```
👉 Explication : crée une archive `firmware-*.tgz` dans `/scratch/downloads/` et affiche l'URL de téléchargement sous la forme `http://<nom_de_l_hote>/scratch/downloads/...`.

3. Vérifier la présence de l'archive :
```bash
ls -lh /scratch/downloads/
```
👉 Explication : contrôle que l'archive existe et que sa taille est cohérente (quelques centaines de Ko) ; une archive vide signale un échec de génération.

**Équivalent interface graphique :**

- **Host Client > Virtual Machines** (inventaire des VM) et **Storage > Datastores** (taille et espace libre).
  👉 Explication : équivalent de `vim-cmd vmsvc/getallvms` et `esxcli storage filesystem list`.
- Télécharger l'archive depuis le navigateur à l'URL affichée par la commande de sauvegarde (`http://<nom_de_l_hote>/scratch/downloads/...`).
  👉 Explication : la génération de l'archive se fait en shell ou en PowerCLI; le téléchargement peut se faire en GUI.

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder la configuration depuis un poste d'administration :
```bash
vicfg-cfgbackup --server <nom_de_l_hote> --username root --save /chemin/sauvegarde/<nom_de_l_hote>-$(date +%F).tgz
```
👉 Explication : utilise vCLI ou PowerCLI (`vicfg-cfgbackup`) pour enregistrer la configuration hors de l'hôte ; le mot de passe root est demandé à l'exécution.

2. Vérifier la taille et la date du fichier sauvegardé :
```bash
ls -lh /chemin/sauvegarde/
```
👉 Explication : confirme que la sauvegarde de l'hôte a bien été écrite sur le poste ou le serveur de sauvegarde.

3. Consigner la sauvegarde dans l'inventaire :
```bash
vim-cmd vmsvc/getallvms
```
👉 Explication : relever les identifiants des VM présentes au moment de la sauvegarde ; le dossier d'exploitation doit associer chaque sauvegarde à la version ESXi et au build.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Calculer l'empreinte SHA-256 de la sauvegarde :
```bash
sha256sum /chemin/sauvegarde/<nom_de_l_hote>-<date>.tgz > /chemin/sauvegarde/<nom_de_l_hote>-<date>.tgz.sha256
```
👉 Explication : exécutée sur le poste ou le serveur de sauvegarde, cette commande crée un fichier d'empreinte qui permet de détecter toute altération de l'archive.

2. Chiffrer la sauvegarde avant stockage distant :
```bash
gpg --symmetric --cipher-algo AES256 /chemin/sauvegarde/<nom_de_l_hote>-<date>.tgz
```
👉 Explication : produit `<nom_de_l_hote>-<date>.tgz.gpg` chiffré en AES-256 ; l'archive contient des condensats de mots de passe et des secrets, elle ne doit jamais être stockée en clair sur un partage accessible.

3. Vérifier l'intégrité de l'archive chiffrée :
```bash
sha256sum -c /chemin/sauvegarde/<nom_de_l_hote>-<date>.tgz.sha256
```
👉 Explication : contrôle que le fichier correspond à son empreinte d'origine ; le résultat `OK` valide l'intégrité avant transfert vers le coffre de sauvegarde.

4. Tester la restauration sur un hôte de lab :
```bash
vicfg-cfgbackup --server <nom_de_l_hote_de_test> --username root --load /chemin/restauration/<nom_de_l_hote>-<date>.tgz
```
👉 Explication : restaure la configuration sur un hôte de test identique (la restauration écrase la configuration de la cible, à ne jamais lancer sur un hôte de production sans plan validé) ; le test valide que la sauvegarde est exploitable.