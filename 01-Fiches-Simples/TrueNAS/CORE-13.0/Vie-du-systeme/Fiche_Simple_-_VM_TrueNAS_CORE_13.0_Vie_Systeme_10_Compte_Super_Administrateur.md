# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_10_Compte_Super_Administrateur

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 10 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-10`

---

## Problème précis à résoudre

Sécuriser le compte root.

## 1. Hors-Production (Lab / Test / POC)

1. Lors de l'installation, définir le mot de passe root (ne jamais le laisser vide). Changer : Compte > Utilisateurs > root > Modifier.
   ```sh
   midclt call user.query '[["username","=","root"]]' | head
   ```
   👉 Explication : vérifie le compte sans afficher le mot de passe.

2. Désactiver la connexion root SSH par mot de passe (étape 27).
   👉 Explication : root reste utilisable à la console et via la GUI.

## 2. Production — Contrôles

Mot de passe dans le coffre de l'équipe.

## 3. Production — Sécurité

Mot de passe long et unique ; limiter les accès GUI par adresse.

## Validation et retour arrière

- **Validation** : Connexion GUI réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
