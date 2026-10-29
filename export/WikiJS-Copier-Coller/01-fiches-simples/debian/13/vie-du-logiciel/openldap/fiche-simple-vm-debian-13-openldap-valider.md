# Fiche_Simple_-_VM_Debian_13_OpenLDAP_Valider.md

- **Environnement** : serveur OpenLDAP pilote et client LDAP autorisé avec CA de confiance
- **OS / Version** : Debian 13; OpenLDAP 2.6
- **Catégorie** : annuaire / validation fonctionnelle

---

## Problème précis à résoudre

Vérifier disponibilité locale, entrées attendues, TLS client et filtrage des ports LDAP.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le service et l'identité locale :
   ```bash
   sudo systemctl is-active slapd
   sudo ldapwhoami -Y EXTERNAL -H ldapi:/// -Q
   ```
   👉 Explication : `active` puis `dn:gidNumber=0+uidNumber=0,cn=peercred,cn=external,cn=auth`.

2. Lire les unités organisationnelles :
   ```bash
   ldapsearch -x -LLL -D "cn=admin,dc=example,dc=org" -W -b "dc=example,dc=org" -s one dn
   ```
   👉 Explication : `ou=People` et `ou=Groups` doivent être listées.

3. Tester la chaîne TLS depuis un client :
   ```bash
   LDAPTLS_CACERT=/chemin/ca.crt ldapsearch -x -H ldaps://FQDN -b "dc=example,dc=org" -s base
   ```
   👉 Explication : remplacer `FQDN` et le chemin; une réponse sans erreur de certificat valide TLS.

4. Contrôler le filtrage des ports et les sauvegardes :
   ```bash
   sudo ss -ltnp | grep -E ':(389|636)\b'
   sudo nft list ruleset 2>/dev/null | grep -E '389|636'
   sudo ls -l /var/backups/ldap
   ```
   👉 Explication : 389/636 doivent être limités aux clients autorisés; les LDIF existent et ne sont pas vides.

## 2. Production — Contrôles

Faire valider les tests par le propriétaire applicatif et vérifier intégrations, ACL, journaux d'accès, disponibilité et alertes.

## 3. Production — Sécurité

- Ne pas tester avec le compte admin quand un compte de lecture dédié suffit.
- Ne pas publier un résultat `ldapsearch` contenant des attributs personnels.
- Ne pas ouvrir les ports LDAP plus largement que nécessaire.
- Ne pas imposer le chiffrement avant validation des clients concernés.

## Validation et retour arrière

- **Validation** : service sain, entrées attendues lisibles, TLS vérifié par client et flux minimaux.
- **Retour arrière** : en cas d'échec TLS ou ACL, rétablir les valeurs précédentes via LDIF inverse et vérifier le service.

## Si le problème n'est pas résolu

- [OpenLDAP — TLS](https://www.openldap.org/doc/admin26/tls.html)
- [OpenLDAP — Access Control](https://www.openldap.org/doc/admin26/access-control.html)
- [Guide complet OpenLDAP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/87-deploiement-openldap-2-6-debian-13#8-validation)