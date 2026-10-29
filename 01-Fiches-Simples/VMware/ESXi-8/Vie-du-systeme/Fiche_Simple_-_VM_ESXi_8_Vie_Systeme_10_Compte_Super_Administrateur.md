# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_10_Compte_Super_Administrateur

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 10 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-10`

---

## Problème précis à résoudre

Définir le mot de passe root.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur : écran **Root password** (7 caractères minimum, mélange de classes exigé par la politique). Pour le changer ensuite (Host Client : **Gérer > Sécurité > Utilisateurs > root > Modifier**) :
   ```sh
   passwd root
   ```
   👉 Explication : demande le nouveau mot de passe deux fois.

2. Stocker le mot de passe dans le coffre-fort de l'équipe.
   👉 Explication : ce compte donne tous les droits sur l'hôte.

3. Vérifier la politique de mot de passe :
   ```sh
   esxcli system settings advanced list -o /Security/PasswordQualityControl
   ```
   👉 Explication : l'option impose longueur et complexité.

## 2. Production — Contrôles

Mot de passe long, unique, dans le coffre-fort.

## 3. Production — Sécurité

Ne pas utiliser root au quotidien : comptes nominatifs ou annuaire.

## Validation et retour arrière

- **Validation** : Connexion au Host Client réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
