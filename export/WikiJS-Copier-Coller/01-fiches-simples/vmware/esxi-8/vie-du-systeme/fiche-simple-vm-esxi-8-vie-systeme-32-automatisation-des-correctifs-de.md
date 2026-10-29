# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_32_Automatisation_Des_Correctifs_De

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 32 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Suivre et appliquer les correctifs de façon contrôlée.

## 1. Hors-Production (Lab / Test / POC)

1. Surveiller les avis de sécurité Broadcom (VMSA) et comparer à la version installée :
   ```sh
   esxcli system version get
   esxcli software profile get
   ```
   👉 Explication : indique le build à comparer au correctif publié.

2. Sous vCenter, utiliser les images de cluster de vSphere Lifecycle Manager (vSphere Client : **Cluster > Mises à jour > Image**).
   👉 Explication : applique et vérifie le correctif hôte par hôte avec vMotion.

3. Ne pas automatiser le redémarrage sans migration préalable des VM.
   👉 Explication : une mise à jour automatique peut interrompre des services.

## 2. Production — Contrôles

Fenêtre mensuelle ou trimestrielle de maintenance.

## 3. Production — Sécurité

Tester le correctif sur un hôte de pré-production.

## Validation et retour arrière

- **Validation** : Le build installé est à jour.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)