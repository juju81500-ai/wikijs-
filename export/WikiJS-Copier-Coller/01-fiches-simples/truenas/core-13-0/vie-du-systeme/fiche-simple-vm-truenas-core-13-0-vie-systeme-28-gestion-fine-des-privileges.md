# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_28_Gestion_Fine_Des_Privileges

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 28 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Limiter les droits.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Compte > Utilisateurs > Modifier > Permettre sudo (ou groupe wheel).
   ```sh
   midclt call user.query '[["username","=","ADMIN1"]]' | grep -i sudo
   ```
   👉 Explication : affiche le droit sudo.

2. Limiter les groupes : Compte > Groupes.
   ```sh
   midclt call group.query | head -30
   ```
   👉 Explication : liste les groupes.

## 2. Production — Contrôles

Revue trimestrielle.

## 3. Production — Sécurité

Pas de sudo sans mot de passe général.

## Validation et retour arrière

- **Validation** : Chaque compte a le minimum.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)