# 📄 Fiche_Simple_-_VMware_ESXi_8_Systeme_Correctifs_Mises_A_Jour.md

- **Environnement** : Hôte physique VMware ESXi 8 (ESXi Shell ou SSH, vSphere Lifecycle Manager)
- **OS / Version** : VMware ESXi 8.0 - Mises à jour par profil d'image
- **Catégorie** : Système & Services / Correctifs et mises à jour

---

## 🎯 Problème précis à résoudre
Identifier la version et le profil d'image d'un hôte ESXi 8, appliquer un correctif signé depuis un dépôt hors ligne avec `esxcli` ou vSphere Lifecycle Manager, et contrôler le résultat après redémarrage.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Identifier la version, le build et le profil d'image actuels :
```bash
vmware -vl
esxcli software profile get
```
👉 Explication : `vmware -vl` affiche la version et le build d'ESXi ; `esxcli software profile get` affiche le profil d'image actif, nécessaire pour choisir la mise à jour cible.

2. Lister les profils contenus dans le dépôt hors ligne :
```bash
esxcli software sources profile list --depot=/vmfs/volumes/<datastore>/<depot_hors_ligne>.zip
```
👉 Explication : lit le bundle `.zip` téléchargé depuis le portail Broadcom et affiche les profils d'image disponibles (ex. `ESXi-8.0U3x-...-standard`).

3. Simuler la mise à jour sans rien modifier :
```bash
esxcli software profile update --dry-run --depot=/vmfs/volumes/<datastore>/<depot_hors_ligne>.zip --profile=<nom_du_profil>
```
👉 Explication : l'option `--dry-run` affiche les VIB à installer, mettre à jour ou supprimer, et signale les conflits, sans modifier l'hôte.

4. Appliquer la mise à jour en mode maintenance puis redémarrer :
```bash
esxcli system maintenanceMode set --enable=true
esxcli software profile update --depot=/vmfs/volumes/<datastore>/<depot_hors_ligne>.zip --profile=<nom_du_profil>
esxcli system shutdown reboot --delay=10 --reason="Mise a jour ESXi 8"
```
👉 Explication : passe l'hôte en mode maintenance (les VM doivent être migrées ou arrêtées), installe le profil puis redémarre ; après le retour, `vmware -vl` doit afficher le nouveau build.

---

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier la conformité de l'hôte dans vSphere Lifecycle Manager :
```bash
esxcli software profile get
```
👉 Explication : dans vSphere Client, ouvrir Lifecycle Manager > Images, lancer « Check compliance » sur le cluster ou l'hôte, puis « Remediate » en mode maintenance. La commande confirme le profil avant et après remédiation.

2. Confirmer le passage en mode maintenance avant toute remédiation :
```bash
esxcli system maintenanceMode get
```
👉 Explication : doit renvoyer `Enabled` ; une remédiation effectuée hors mode maintenance échoue ou impose un arrêt non planifié des VM.

3. Contrôler la version après redémarrage :
```bash
vmware -vl
esxcli system maintenanceMode set --enable=false
```
👉 Explication : vérifie le build installé puis sort l'hôte du mode maintenance pour réintégrer les VM et la capacité du cluster.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérifier le niveau d'acceptation des VIB :
```bash
esxcli software acceptance get
```
👉 Explication : affiche le niveau d'acceptation (`VMwareCertified`, `VMwareAccepted`, `PartnerSupported`, `CommunitySupported`) ; un niveau inférieur à `PartnerSupported` doit être refusé en production.

2. Ne jamais contourner la vérification de signature :
```bash
esxcli software profile update --dry-run --depot=/vmfs/volumes/<datastore>/<depot_hors_ligne>.zip --profile=<nom_du_profil>
```
👉 Explication : la vérification des signatures est active par défaut ; l'option `--no-sig-check` ne doit pas être utilisée en production. Un bundle non signé doit être rejeté et son origine vérifiée.

3. Inventorier les VIB installées après mise à jour :
```bash
esxcli software vib list
```
👉 Explication : liste chaque VIB avec sa version, son fournisseur et son niveau d'acceptation ; cet inventaire sert de référence pour le dossier d'exploitation et la détection des dérives.

4. Consigner le profil et le build de référence :
```bash
esxcli software profile get
vmware -vl
```
👉 Explication : conserve le profil et le build validés dans la CMDB ; toute divergence entre hôtes d'un même cluster doit être corrigée avant la mise en production.