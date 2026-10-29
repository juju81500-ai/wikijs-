# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_48_Test_De_Restauration_Pra

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 48 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Prouver qu'une sauvegarde est restaurable.

## 1. Hors-Production (Lab / Test / POC)

1. Veeam : console **Home > Backups > clic droit sur la VM > Restore entire VM** vers un nouvel emplacement ou un nouveau nom (sans réseau de production).
   👉 Explication : ne jamais écraser la VM d'origine pour un test.

2. Restauration de la configuration de l'hôte (hôte de test) :
   ```sh
   esxcli system maintenanceMode set --enable true
   vim-cmd hostsvc/firmware/restore_config /tmp/configBundle.tgz
   ```
   👉 Explication : le build doit être identique; l'hôte redémarre.

3. Mesurer la durée, noter le résultat, supprimer la VM de test (Host Client : **VM > Actions > Supprimer**).
   👉 Explication : la durée donne le RTO réel.

## 2. Production — Contrôles

Test de restauration au moins trimestriel.

## 3. Production — Sécurité

Supprimer la VM restaurée après le test.

## Validation et retour arrière

- **Validation** : La VM restaurée démarre et ses données sont intactes.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)