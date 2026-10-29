# Fiche_Simple_-_VM_pfSense_Vie_Systeme_11_Compte_D_Administration_Delegue

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 11 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-11`

---

## Problème précis à résoudre

Éviter l'usage quotidien de `admin`.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un groupe dans System > User Manager > Groups > Add (ex. `admins-fw`) puis l'onglet Assigned Privileges pour lui attribuer des droits (ex. `WebCfg - All pages`).
   👉 Explication : les droits sont attribués au groupe, pas aux personnes.

2. Créer l'utilisateur dans System > User Manager > Users > Add : nom `ADMIN01`, mot de passe fort, groupe `admins-fw`; ajouter le privilège `User - System: Shell account access` pour SSH.
   👉 Explication : `ADMIN01` est le compte nominatif de l'administrateur.

3. Contrôler en shell :
   ```sh
   pw usershow ADMIN01
   id ADMIN01
   ```
   👉 Explication : affiche l'UID, le shell et les groupes du compte.

## 2. Production — Contrôles

Un compte nominatif par administrateur, jamais de compte partagé.

## 3. Production — Sécurité

Appliquer le moindre privilège et supprimer le compte au départ de l'équipe.

## Validation et retour arrière

- **Validation** : Connexion web et SSH réussies avec `ADMIN01`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire pfSense CE](./Sommaire_-_Vie_du_systeme_pfSense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
