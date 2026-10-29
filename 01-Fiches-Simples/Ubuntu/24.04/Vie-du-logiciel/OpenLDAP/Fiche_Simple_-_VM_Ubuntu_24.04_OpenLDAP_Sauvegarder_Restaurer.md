# Fiche_Simple_-_VM_Ubuntu_24.04_OpenLDAP_Sauvegarder_Restaurer

- **Environnement** : VM Ubuntu 24.04 avec FQDN stable, serveur OpenLDAP (slapd)
- **OS / Version** : Ubuntu 24.04 LTS Noble; slapd 2.6 des dépôts, version à vérifier
- **Catégorie** : annuaire OpenLDAP / sauvegarder / restaurer
- **Tags** : `openldap`, `ubuntu24-04`, `vie-du-logiciel`, `sauvegarder-restaurer`

---

## Problème précis à résoudre

Sauvegarder et restaurer cn=config et les données sur Ubuntu.

## 1. Hors-Production (Lab / Test / POC)

1. Exporter configuration et données :
   ```bash
   sudo install -d -m 0700 /var/backups/ldap
   sudo slapcat -n 0 -l /var/backups/ldap/config-$(date +%F).ldif
   sudo slapcat -n 1 -l /var/backups/ldap/data-$(date +%F).ldif
   sudo ls -l /var/backups/ldap
   ```
   👉 Explication : Les LDIF contiennent des condensats de mots de passe : accès root, chiffrement hors hôte. Les fichiers de sauvegarde ne sont lus que par root, pas par slapd, donc non soumis à AppArmor.

2. Restaurer sur un hôte de test : arrêter slapd, déplacer les bases, recharger :
   ```bash
   sudo systemctl stop slapd
   sudo mv /var/lib/ldap /var/lib/ldap.avant-restauration
   sudo install -d -o openldap -g openldap -m 0700 /var/lib/ldap
   sudo -u openldap slapadd -n 1 -l /var/backups/ldap/data-DATE.ldif
   sudo systemctl start slapd
   ```
   👉 Explication : DATE est la date de l'export (à remplacer). La restauration de cn=config suit la même logique : voir [la fiche Debian Restaurer Test](../../../../Debian/13/Vie-du-logiciel/OpenLDAP/Fiche_Simple_-_VM_Debian_13_OpenLDAP_Restaurer_Test.md).

## 2. Production — Contrôles

Comparer le nombre d'entrées avant/après; tester périodiquement.

## 3. Production — Sécurité

- Les LDIF restent chiffrés et hors de la VM.

## Validation et retour arrière

- **Validation** : Le nombre d'entrées restaurées correspond à l'export.
- **Retour arrière** : Remettre /var/lib/ldap.avant-restauration en place et redémarrer slapd.

## Si le problème n'est pas résolu

- [Étape suivante du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_OpenLDAP_Mise_A_Jour_Retour_Arriere.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_OpenLDAP.md)
- [Ubuntu Server — OpenLDAP (documentation officielle)](https://documentation.ubuntu.com/server/how-to/openldap/install-openldap/)
- [OpenLDAP — guide administrateur 2.6](https://www.openldap.org/doc/admin26/)
