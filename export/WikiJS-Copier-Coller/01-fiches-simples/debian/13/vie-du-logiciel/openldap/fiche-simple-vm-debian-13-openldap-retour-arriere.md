# Fiche_Simple_-_VM_Debian_13_OpenLDAP_Retour_Arriere.md

- **Environnement** : VM Debian 13 avec snapshot et LDIF précédents vérifiés
- **OS / Version** : Debian 13; slapd 2.6
- **Catégorie** : annuaire / changement et retour arrière

---

## Problème précis à résoudre

Annuler un changement OLC, TLS ou ACL sans perdre les données ni verrouiller l'accès à l'annuaire.

## 1. Hors-Production (Lab / Test / POC)

1. Avant toute modification de `cn=config`, exporter la configuration :
   ```bash
   sudo slapcat -n 0 -l /var/backups/ldap/config-avant-$(date +%F-%H%M).ldif
   ```
   👉 Explication : c'est la référence de retour.

2. En cas d'échec TLS ou ACL, remettre les anciennes valeurs avec un LDIF inverse :
   ```bash
   sudo ldapmodify -Q -Y EXTERNAL -H ldapi:/// -f /root/tls-inverse.ldif
   sudo systemctl restart slapd
   sudo systemctl status slapd --no-pager
   ```
   👉 Explication : `tls-inverse.ldif` reprend les valeurs initiales relevées avant la modification.

3. Sinon, restaurer le snapshot de la VM (hyperviseur : **VM > Snapshots > Rollback**).
   👉 Explication : c'est la méthode la plus rapide si l'annuaire était vide ou peu modifié.

4. En dernier recours, conserver les répertoires actuels en les renommant, puis restaurer les LDIF sur une base vide :
   ```bash
   sudo systemctl stop slapd
   sudo mv /var/lib/ldap /var/lib/ldap.avant-$(date +%F)
   sudo mv /etc/ldap/slapd.d /etc/ldap/slapd.d.avant-$(date +%F)
   ```
   👉 Explication : ne rien supprimer; recréer ensuite une base vide et appliquer l'étape de restauration.

## 2. Production — Contrôles

Exiger approbation de changement, sauvegarde vérifiée, opérateur de secours, fenêtre, critères d'arrêt et validation de connexion des applications.

## 3. Production — Sécurité

- Ne pas éditer `/etc/ldap/slapd.d` à la main.
- Ne pas supprimer les répertoires LDAP; les renommer uniquement dans le cadre d'une procédure de restauration approuvée.
- Préserver LDIF et journaux, qui peuvent contenir des données sensibles.
- Si l'accès est compromis, limiter les flux via le pare-feu approuvé et escalader au propriétaire.

## Validation et retour arrière

- **Validation** : slapd actif, connexion locale, données attendues, TLS/ACL confirmés et applications pilotes vérifiées.
- **Retour arrière** : ne restaurer la production qu'avec un plan éprouvé et des données compatibles; si l'état est incertain, isoler et escalader.

## Si le problème n'est pas résolu

- [OpenLDAP — configuration OLC](https://www.openldap.org/doc/admin26/slapdconf2.html)
- [OpenLDAP — maintenance](https://www.openldap.org/doc/admin26/maintenance.html)
- [Guide complet OpenLDAP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/87-deploiement-openldap-2-6-debian-13#9-retour-arriere)