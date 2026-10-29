# Fiche_Simple_-_VM_Debian_13_OpenLDAP_Cadrer.md

- **Environnement** : VM Debian 13 dédiée; annuaire LDAP pilote autonome
- **OS / Version** : Debian 13 Trixie; slapd 2.6
- **Catégorie** : annuaire / identité / cadrage
- **Tags** : `debian13`, `openldap`, `ldap`, `cadrage`, `pilote`

---

## Problème précis à résoudre

Confirmer qu'OpenLDAP correspond au besoin et préparer le périmètre avant d'installer un annuaire.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le nom d'hôte FQDN et la résolution DNS :
   ```bash
   hostname -f
   getent hosts $(hostname -f)
   ```
   👉 Explication : le FQDN doit être stable et résolu; il sert de base au suffixe et au certificat TLS.

2. Vérifier l'heure et les ressources :
   ```bash
   timedatectl show -p NTPSynchronized --value
   cat /etc/os-release | grep PRETTY_NAME
   df -h /var/lib
   ```
   👉 Explication : l'heure doit être synchronisée (`yes`); la VM doit être Debian 13.

3. Contrôler que les ports LDAP ne sont pas déjà utilisés :
   ```bash
   sudo ss -ltnp | grep -E ':(389|636)\b' || echo "ports 389/636 libres"
   ```
   👉 Explication : évite un conflit avec un autre annuaire.

4. Prendre un snapshot de la VM (interface de l'hyperviseur, par exemple Proxmox : **VM > Snapshots > Take Snapshot**) puis consigner suffixe prévu, applications clientes et responsable.
   👉 Explication : si Active Directory, Kerberos intégré ou CA/DNS intégrés sont requis, choisir Samba AD DC ou FreeIPA plutôt qu'OpenLDAP.

## 2. Production — Contrôles

Faire approuver les flux, le propriétaire de l'annuaire, le schéma, les comptes de service, les ACL, le plan de continuité, les objectifs de restauration et la procédure de changement.

## 3. Production — Sécurité

- Ne pas utiliser l'annuaire pilote comme source d'identité métier sans revue.
- Ne jamais exposer LDAP/389 à Internet.
- Protéger les sauvegardes et certificats; ne pas mettre les mots de passe dans le wiki.
- Ne pas remplacer AD/FreeIPA par OpenLDAP sans vérifier les fonctions exigées.

## Validation et retour arrière

- **Validation** : choix de produit, propriétaire, FQDN, suffixe et périmètre pilote documentés.
- **Arrêt** : ne pas installer si les dépendances d'identité ou le scénario de restauration sont inconnus.

## Si le problème n'est pas résolu

- [OpenLDAP — Administrator's Guide](https://www.openldap.org/doc/admin26/)
- [Debian — OpenLDAPSetup](https://wiki.debian.org/LDAP/OpenLDAPSetup)
- [Guide complet OpenLDAP Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/87_Deploiement_OpenLDAP_2.6_Debian_13.md#1-perimetre-et-choix)
