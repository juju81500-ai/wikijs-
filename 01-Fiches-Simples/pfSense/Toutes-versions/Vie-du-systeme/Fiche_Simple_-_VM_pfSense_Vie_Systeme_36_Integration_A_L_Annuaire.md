# Fiche_Simple_-_VM_pfSense_Vie_Systeme_36_Integration_A_L_Annuaire

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 36 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-36`

---

## Problème précis à résoudre

Authentifier les administrateurs par l'annuaire.

## 1. Hors-Production (Lab / Test / POC)

1. Ajouter un serveur LDAP dans System > User Manager > Authentication Servers > Add (Type `LDAP`, hôte `IP_ANNUAIRE`, port 636 SSL, base `DC=exemple,DC=lan`, compte de liaison `CN=svc-fw,...`).
   👉 Explication : `IP_ANNUAIRE` est le contrôleur de domaine; un compte de service en lecture suffit.

2. Tester dans Diagnostics > Authentication avec un compte de l'annuaire, puis choisir le serveur dans System > User Manager > Settings.
   👉 Explication : les administrateurs utilisent leur compte du domaine.

3. Contrôler la joignabilité en shell :
   ```sh
   nc -zv IP_ANNUAIRE 636
   drill -t SRV _ldap._tcp.exemple.lan @127.0.0.1
   ```
   👉 Explication : vérifie l'accès LDAPS et l'enregistrement DNS.

## 2. Production — Contrôles

Mapper un groupe de l'annuaire sur un groupe pfSense.

## 3. Production — Sécurité

Utiliser LDAPS (port 636) uniquement; conserver un compte local de secours.

## Validation et retour arrière

- **Validation** : Connexion réussie avec un compte de l'annuaire.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire pfSense CE](./Sommaire_-_Vie_du_systeme_pfSense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
