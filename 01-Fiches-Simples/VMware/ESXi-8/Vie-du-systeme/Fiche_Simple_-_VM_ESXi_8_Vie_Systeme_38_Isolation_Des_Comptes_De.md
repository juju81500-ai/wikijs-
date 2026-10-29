# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_38_Isolation_Des_Comptes_De

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 38 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-38`

---

## Problème précis à résoudre

Séparer les accès techniques des comptes humains.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un compte de service en lecture seule pour la supervision (Host Client : **Gérer > Sécurité > Utilisateurs > Ajouter**) :
   ```sh
   esxcli system account add -i svc-supervision -d "Supervision" -p -c
   esxcli system permission set -i svc-supervision -r ReadOnly
   ```
   👉 Explication : le mot de passe est demandé; le rôle `ReadOnly` ne permet aucune modification.

2. Lister :
   ```sh
   esxcli system account list
   ```
   👉 Explication : vérifie les comptes créés.

3. Sous vCenter, créer des comptes de service dans l'annuaire avec des rôles précis.
   👉 Explication : évite d'utiliser `root` pour les outils.

## 2. Production — Contrôles

Un compte de service par usage; rotation des mots de passe.

## 3. Production — Sécurité

Ne pas donner `Admin` à un compte de service.

## Validation et retour arrière

- **Validation** : Le compte de service ne peut que lire.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
