# Fiche_Simple_-_VM_pfSense_Vie_Systeme_38_Isolation_Des_Comptes_De

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 38 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-38`

---

## Problème précis à résoudre

Utiliser des identifiants dédiés pour les automatisations.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un compte dédié : System > User Manager > Users > Add, nom `ADMIN-API`, groupe aux privilèges limités, sans accès shell.
   👉 Explication : permet d'automatiser sans utiliser de mot de passe humain.

2. Installer le paquet `API` ou utiliser `pfSsh.php` en lecture et tester l'accès :
   ```sh
   curl -sk -u ADMIN-API:MOT_DE_PASSE_API https://IP_LAN/api/v2/status/system
   ```
   👉 Explication : `MOT_DE_PASSE_API` est le secret du compte dédié; la réponse JSON prouve l'accès (selon le paquet API installé).

## 2. Production — Contrôles

Un compte de service par outil, avec son secret dans un coffre-fort.

## 3. Production — Sécurité

Ne jamais mettre `MOT_DE_PASSE_API` dans un script en clair; renouveler régulièrement.

## Validation et retour arrière

- **Validation** : L'accès fonctionne avec le compte dédié et échoue hors de ses droits.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire pfSense CE](./Sommaire_-_Vie_du_systeme_pfSense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
