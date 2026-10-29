# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_28_Gestion_Fine_Des_Privileges

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 28 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-28`

---

## Problème précis à résoudre

Donner des droits précis sans partager root.

## 1. Hors-Production (Lab / Test / POC)

1. ESXi n'a pas de `sudo` : les droits se gèrent par rôles (Host Client : **Hôte > Actions > Autorisations**). En ligne de commande :
   ```sh
   esxcli system permission list
   esxcli system permission set -i ADMIN1 -r ReadOnly
   ```
   👉 Explication : rôles disponibles : `Admin`, `ReadOnly`, `NoAccess`.

2. Sous vCenter, créer des rôles personnalisés (vSphere Client : **Administration > Contrôle d'accès > Rôles > Ajouter**).
   👉 Explication : permet de limiter les actions (accès console, snapshot, etc.).

3. Autoriser seulement certains comptes à l'accès shell (Host Client : **Gérer > Sécurité > Utilisateurs**), via la liste `DCUI.Access` :
   ```sh
   esxcli system settings advanced set -o /DCUI/Access -s root
   ```
   👉 Explication : limite les comptes pouvant se connecter à la DCUI en mode verrouillage.

## 2. Production — Contrôles

Privilèges limités par rôle.

## 3. Production — Sécurité

Journaliser les actions administratives.

## Validation et retour arrière

- **Validation** : `esxcli system permission list` liste les rôles attendus.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
