# Fiche_Simple_-_VM_Debian_13_OpenLDAP_Verifier_OLC.md

- **Environnement** : VM Debian 13 avec slapd local
- **OS / Version** : Debian 13; OpenLDAP 2.6 / OLC `cn=config`
- **Catégorie** : annuaire / configuration

---

## Problème précis à résoudre

Lire le suffixe et le DN administrateur depuis OLC avant d'ajouter des entrées ou modifier l'annuaire.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le service :
   ```bash
   sudo systemctl status slapd --no-pager
   ```
   👉 Explication : le service doit être actif.

2. Vérifier l'identité locale par le socket `ldapi`:
   ```bash
   sudo ldapwhoami -Y EXTERNAL -H ldapi:/// -Q
   ```
   👉 Explication : la réponse attendue est `dn:gidNumber=0+uidNumber=0,cn=peercred,cn=external,cn=auth`.

3. Lister la configuration :
   ```bash
   sudo ldapsearch -LLLQ -Y EXTERNAL -H ldapi:/// -b cn=config -s one dn
   ```
   👉 Explication : on voit les objets de configuration (`cn=schema`, `olcDatabase={...}`).

4. Relever suffixe, administrateur et contrôles d'accès :
   ```bash
   sudo ldapsearch -LLLQ -Y EXTERNAL -H ldapi:/// -b "olcDatabase={1}mdb,cn=config" olcSuffix olcRootDN olcAccess
   ```
   👉 Explication : noter `olcSuffix` et `olcRootDN`; ils remplacent `dc=example,dc=org` dans les fiches suivantes. Ne jamais éditer `/etc/ldap/slapd.d` à la main.

## 2. Production — Contrôles

Faire relire chaque changement OLC, conserver l'export `slapcat -n 0` et planifier une fenêtre avec accès console local.

## 3. Production — Sécurité

- L'authentification `EXTERNAL` sur `ldapi:///` dépend de l'identité locale; limiter l'accès root.
- Ne pas publier des exports de `cn=config`, qui peuvent révéler des paramètres sensibles.
- Ne pas modifier ACL sans sauvegarde et test avec un compte non privilégié.

## Validation et retour arrière

- **Validation** : suffixe et root DN identifiés; aucune modification de configuration réalisée durant le contrôle.
- **Retour arrière** : conserver les valeurs et l'export avant tout changement OLC.

## Si le problème n'est pas résolu

- [OpenLDAP — configuration OLC](https://www.openldap.org/doc/admin26/slapdconf2.html)
- [OpenLDAP — Administrator's Guide](https://www.openldap.org/doc/admin26/)
- [Guide complet OpenLDAP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/87-deploiement-openldap-2-6-debian-13#3-verifier-la-configuration-olc)