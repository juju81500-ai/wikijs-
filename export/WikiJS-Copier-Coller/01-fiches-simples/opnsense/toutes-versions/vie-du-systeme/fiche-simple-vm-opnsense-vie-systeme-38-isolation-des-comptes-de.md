# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_38_Isolation_Des_Comptes_De

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 38 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Utiliser des identifiants dédiés pour les automatisations.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un utilisateur API : Système > Accès > Utilisateurs > ADMIN-API > Clés API > `+` (télécharge un fichier contenant clé et secret).
   👉 Explication : permet d'automatiser sans utiliser de mot de passe humain.

2. Limiter ses droits via un groupe restreint (Système > Accès > Groupes) et tester :
   ```sh
   curl -sk -u CLE_API:SECRET_API https://IP_LAN/api/core/firmware/status
   ```
   👉 Explication : `CLE_API` et `SECRET_API` proviennent du fichier téléchargé; la réponse JSON prouve l'accès.

## 2. Production — Contrôles

Une clé API par outil, stockée dans un coffre-fort.

## 3. Production — Sécurité

Ne jamais mettre `CLE_API`/`SECRET_API` dans un script en clair; renouveler à intervalle régulier.

## Validation et retour arrière

- **Validation** : L'API répond avec la clé dédiée et refuse les actions hors droits.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)