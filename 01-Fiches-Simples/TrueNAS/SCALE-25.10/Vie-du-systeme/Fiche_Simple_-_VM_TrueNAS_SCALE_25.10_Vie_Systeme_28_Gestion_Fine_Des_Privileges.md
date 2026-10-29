# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_28_Gestion_Fine_Des_Privileges

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 28 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-28`

---

## Problème précis à résoudre

Limiter les droits administrateur.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Identifiants > Utilisateurs > Modifier : définir la commande sudo autorisée ou le rôle (lecture seule, opérateur de partage).
   ```bash
   sudo midclt call user.query '[["username","=","ADMIN1"]]' | grep -i -E 'sudo|roles'
   ```
   👉 Explication : affiche les droits actuels.

2. Attribuer des rôles plus fins : Identifiants > Groupes > rôles.
   ```bash
   sudo midclt call privilege.query | python3 -m json.tool | head
   ```
   👉 Explication : liste les privilèges disponibles.

## 2. Production — Contrôles

Revoir les droits chaque trimestre.

## 3. Production — Sécurité

Pas de `NOPASSWD` global.

## Validation et retour arrière

- **Validation** : Chaque compte a le rôle minimal.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./Sommaire_-_Vie_du_systeme_TrueNAS_SCALE_25.10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
