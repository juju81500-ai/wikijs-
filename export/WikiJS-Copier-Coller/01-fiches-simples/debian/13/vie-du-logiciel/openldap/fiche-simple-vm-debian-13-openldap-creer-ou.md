# Fiche_Simple_-_VM_Debian_13_OpenLDAP_Creer_OU.md

- **Environnement** : annuaire LDAP pilote avec suffixe confirmé
- **OS / Version** : Debian 13; OpenLDAP 2.6
- **Catégorie** : annuaire / structure des données

---

## Problème précis à résoudre

Créer les unités organisationnelles de test sous le suffixe vérifié.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le fichier LDIF (adapter le suffixe) :
   ```bash
   sudo tee /root/ou-base.ldif >/dev/null <<'EOF'
   dn: ou=People,dc=example,dc=org
   objectClass: organizationalUnit
   ou: People

   dn: ou=Groups,dc=example,dc=org
   objectClass: organizationalUnit
   ou: Groups
   EOF
   ```
   👉 Explication : remplacer `dc=example,dc=org` par le suffixe relevé à l'étape OLC.

2. Ajouter les entrées (mot de passe saisi à l'invite, jamais avec `-w`) :
   ```bash
   sudo ldapadd -x -D "cn=admin,dc=example,dc=org" -W -f /root/ou-base.ldif
   ```
   👉 Explication : `-W` demande le mot de passe en interactif.

3. Vérifier la création :
   ```bash
   ldapsearch -x -LLL -D "cn=admin,dc=example,dc=org" -W -b "dc=example,dc=org" -s one dn
   ```
   👉 Explication : `ou=People` et `ou=Groups` doivent apparaître.

4. Ne pas utiliser `cn=admin` pour les applications : créer des comptes de lecture dédiés et limiter `olcAccess`; ne pas ouvrir le port 389 vers Internet.
   👉 Explication : le compte administrateur ne sert qu'à l'administration.

## 2. Production — Contrôles

Valider la nomenclature, le propriétaire des branches, les droits de délégation et le processus de revue avant de créer des OU métier.

## 3. Production — Sécurité

- Ne pas placer le mot de passe admin après `-w` ni dans l'historique du shell.
- Ne pas utiliser `cn=admin` comme compte applicatif.
- Ne pas créer de branche métier sans approbation du propriétaire des données.
- Restreindre les permissions des fichiers LDIF et nettoyer les données de test selon la politique.

## Validation et retour arrière

- **Validation** : seules les OU prévues existent sous le suffixe attendu.
- **Retour arrière** : supprimer uniquement les entrées de test identifiées, après vérification des enfants et dépendances.

## Si le problème n'est pas résolu

- [OpenLDAP — ldapadd](https://www.openldap.org/software/man.cgi?query=ldapadd)
- [OpenLDAP — Access Control](https://www.openldap.org/doc/admin26/access-control.html)
- [Guide complet OpenLDAP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/87-deploiement-openldap-2-6-debian-13#4-creer-une-structure-minimale)