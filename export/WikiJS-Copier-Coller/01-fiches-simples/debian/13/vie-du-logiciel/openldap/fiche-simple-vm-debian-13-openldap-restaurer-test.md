# Fiche_Simple_-_VM_Debian_13_OpenLDAP_Restaurer_Test.md

- **Environnement** : VM Debian 13 de restauration isolée, base LDAP vide
- **OS / Version** : Debian 13; OpenLDAP 2.6
- **Catégorie** : annuaire / restauration

---

## Problème précis à résoudre

Démontrer la restauration des données LDAP sur une VM isolée sans toucher à la production.

## 1. Hors-Production (Lab / Test / POC)

1. Sur la VM de test uniquement (même suffixe, base vide), arrêter `slapd` :
   ```bash
   sudo systemctl stop slapd
   ```
   👉 Explication : `slapadd` écrit directement dans la base et exige `slapd` arrêté; ne jamais l'exécuter en production pour « tester ».

2. Importer les données sous l'utilisateur `openldap` :
   ```bash
   sudo -u openldap slapadd -n 1 -l /chemin/data-AAAA-MM-JJ.ldif
   ```
   👉 Explication : remplacer le chemin; l'utilisateur `openldap` évite des fichiers appartenant à root.

3. Redémarrer et comparer :
   ```bash
   sudo systemctl start slapd
   sudo ldapsearch -LLLQ -Y EXTERNAL -H ldapi:/// -b "dc=example,dc=org" dn | grep -c '^dn:'
   ```
   👉 Explication : le nombre doit égaler celui noté lors de la sauvegarde.

4. Ne restaurer `-n 0` (configuration) qu'après répétition sur la VM de test : consulter `man slapadd`.
   👉 Explication : c'est une reconstruction complète de la configuration.

## 2. Production — Contrôles

Mesurer RPO/RTO, vérifier cohérence des données et plan de bascule; faire approuver toute restauration de production avec fenêtre et responsable.

## 3. Production — Sécurité

- Ne jamais tester `slapadd` sur l'annuaire en service.
- `slapadd` écrit directement dans la base et exige un service arrêté; ne jamais l'exécuter sur une base non vide sans procédure spécialisée.
- Ne pas utiliser un dump non vérifié ou accessible à des tiers.
- Ne pas remplacer `/var/lib/ldap` ou `/etc/ldap/slapd.d` sans conserver l'état courant.

## Validation et retour arrière

- **Validation** : import de test réussi sur VM isolée, service démarré, mêmes entrées et permissions contrôlées.
- **Retour arrière** : abandonner la VM de test ou restaurer son snapshot; ne pas transférer la restauration sur production sans approbation.

## Si le problème n'est pas résolu

- [OpenLDAP — maintenance et sauvegarde](https://www.openldap.org/doc/admin26/maintenance.html)
- [Debian — slapadd](https://manpages.debian.org/trixie/slapd/slapadd.8.en.html)
- [Guide complet OpenLDAP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/87-deploiement-openldap-2-6-debian-13#7-restaurer-test-sur-une-vm-isolee)