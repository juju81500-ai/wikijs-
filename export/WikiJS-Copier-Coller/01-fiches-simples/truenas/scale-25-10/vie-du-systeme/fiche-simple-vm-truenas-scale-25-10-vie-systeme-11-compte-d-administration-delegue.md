# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_11_Compte_D_Administration_Delegue

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 11 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Créer un compte nominatif pour chaque administrateur.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Identifiants > Utilisateurs > Ajouter (nom, mot de passe, rôle Administrateur complet).
   ```bash
   sudo midclt call user.create '{"username":"ADMIN1","full_name":"Prénom Nom","password":"MOT_DE_PASSE","group_create":true,"roles":["FULL_ADMIN"]}'
   ```
   👉 Explication : ADMIN1 est le nom du compte ; MOT_DE_PASSE à saisir sans l'enregistrer dans l'historique.

2. Contrôler :
   ```bash
   sudo midclt call user.query '[["username","=","ADMIN1"]]' | python3 -m json.tool | head
   ```
   👉 Explication : confirme le compte et ses rôles.

## 2. Production — Contrôles

Un compte par personne, aucun compte partagé.

## 3. Production — Sécurité

Appliquer le moindre privilège : rôle lecture seule pour la supervision.

## Validation et retour arrière

- **Validation** : Connexion de ADMIN1 réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)