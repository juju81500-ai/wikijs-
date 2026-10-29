# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_11_Compte_D_Administration_Delegue

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 11 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-11`

---

## Problème précis à résoudre

Créer un compte nominatif avec droits limités.

## 1. Hors-Production (Lab / Test / POC)

1. Host Client : **Gérer > Sécurité > Utilisateurs > Ajouter un utilisateur**, puis **Hôte > Actions > Autorisations > Ajouter un utilisateur** (rôle `Admin` ou `ReadOnly`). En ligne de commande (remplacer `ADMIN1`) :
   ```sh
   esxcli system account add -i ADMIN1 -d "Admin nominatif" -p -c
   esxcli system permission set -i ADMIN1 -r Admin
   ```
   👉 Explication : crée le compte local (le mot de passe est demandé) et lui donne le rôle; à remplacer par l'annuaire (étape 36).

2. Lister :
   ```sh
   esxcli system account list
   esxcli system permission list
   ```
   👉 Explication : vérifie les comptes et leurs rôles.

3. Pour des droits limités, utiliser le rôle `ReadOnly` ou créer un rôle personnalisé (vCenter : **Administration > Contrôle d'accès > Rôles**).
   👉 Explication : principe du moindre privilège.

## 2. Production — Contrôles

Un compte par administrateur; pas de compte partagé.

## 3. Production — Sécurité

Limiter le nombre de comptes locaux; privilégier l'annuaire.

## Validation et retour arrière

- **Validation** : Connexion du compte nominatif réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
