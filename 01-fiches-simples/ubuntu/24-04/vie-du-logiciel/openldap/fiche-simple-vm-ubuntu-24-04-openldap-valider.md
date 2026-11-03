# Fiche_Simple_-_VM_Ubuntu_24.04_OpenLDAP_Valider

- **Environnement** : [[Glossary:VM]] Ubuntu 24-04 avec [[Glossary:FQDN]] stable, serveur OpenLDAP (slapd)
- **OS / Version** : Ubuntu 24-04 [[Glossary:LTS]] Noble; slapd 2.6 des dépôts, version à vérifier
- **Catégorie** : annuaire OpenLDAP / valider
- **Tags** : `openldap`, `ubuntu24-04`, `vie-du-logiciel`, `valider`

---

## Problème précis à résoudre

Recetter l'annuaire sur Ubuntu avec un client.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le service et l'identité locale :
   ```bash
   sudo systemctl is-active slapd
   sudo ldapwhoami -Y EXTERNAL -H ldapi:/// -Q
   ```
   👉 Explication : Réponse active puis l'identité du canal local (root via ldapi).

2. Lire l'annuaire en [[Glossary:TLS]] avec un compte de test :
   ```bash
   ldapsearch -x -ZZ -H ldap://FQDN -D COMPTE_DN -W -b DOMAINE_BASE -s one dn
   ```
   👉 Explication : COMPTE_DN est le [[Glossary:DN]] d'un compte de test (à remplacer); -W demande le mot de passe sans l'écrire. Les [[Glossary:OU]] attendues doivent apparaître.

3. Contrôler les ports exposés :
   ```bash
   sudo ss -ltnp | grep -E ':(389|636)\b'
   ```
   👉 Explication : Seuls les ports prévus écoutent.

## 2. Production — Contrôles

Consigner le résultat; le détail des contrôles est identique à [la fiche Debian Valider](../../../../debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-valider.md).

## 3. Production — Sécurité

- Utiliser un compte de test non administrateur.

## Validation et retour arrière

- **Validation** : Service actif, [[Glossary:STARTTLS]] valide, entrées attendues.
- **Retour arrière** : Désactiver l'accès réseau (ufw) et restaurer la configuration précédente.

## Si le problème n'est pas résolu

- [Étape suivante du guide](./fiche-simple-vm-ubuntu-24-04-openldap-sauvegarder-restaurer.md)
- [Fiche d'entrée du logiciel](../../../../logiciels/05-systemes-annuaires-et-services/fiche-logiciel-openldap.md)
- [Ubuntu Server — OpenLDAP (documentation officielle)](https://documentation.ubuntu.com/server/how-to/openldap/install-openldap/)
- [OpenLDAP — guide administrateur 2.6](https://www.openldap.org/doc/admin26/)
