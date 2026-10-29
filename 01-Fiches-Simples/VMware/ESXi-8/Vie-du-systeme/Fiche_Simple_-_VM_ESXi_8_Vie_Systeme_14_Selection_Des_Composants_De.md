# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_14_Selection_Des_Composants_De

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 14 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-14`

---

## Problème précis à résoudre

Contrôler la version et les composants de l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. ESXi n'a pas de sélection de paquets : l'image inclut les composants de base. Lister les VIB installés :
   ```sh
   esxcli software vib list | head -30
   esxcli software profile get
   ```
   👉 Explication : affiche le profil d'image et les VIB (pilotes, agents constructeur).

2. Vérifier la version et le build :
   ```sh
   vmware -vl
   esxcli system version get
   ```
   👉 Explication : à comparer au dernier correctif publié.

3. N'installer aucun VIB supplémentaire sans besoin (pilote, agent de supervision approuvé).
   👉 Explication : chaque VIB augmente la surface d'attaque et les risques de compatibilité.

## 2. Production — Contrôles

Tenir la liste des VIB ajoutés.

## 3. Production — Sécurité

N'installer que des VIB signés (niveau d'acceptation `PartnerSupported` ou supérieur).

## Validation et retour arrière

- **Validation** : `esxcli software profile get` affiche le profil attendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
