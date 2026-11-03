# Réplication et haute disponibilité : OpenLDAP et FreeIPA (guide comparatif)

- **Environnement** : Annuaires [[Glossary:LDAP]] sur Linux, en complément de [OpenLDAP sur Debian 13](../../../debian/13/installation-deploiement/87-deploiement-openldap-2-6-debian-13.md) et [FreeIPA sur Rocky Linux 9](../../../rocky-linux/9/installation-deploiement/88-deploiement-freeipa-rocky-linux-9.md)
- **Tags** : `ldap`, `openldap`, `freeipa`, `replication`, `ha`, `syncrepl`
- **Statut de validation** : **Verdict : Non testé sur plateforme cible.** Les procédures ci-dessous sont issues de la méthode documentaire et doivent être rejouées en laboratoire avant toute production.

## 1. Périmètre et prérequis

Deux variantes distinctes, à ne pas mélanger :
| Critère | Variante A : OpenLDAP | Variante B : FreeIPA |
|---|---|---|
| Mécanisme | `syncrepl` (provider/consumer) ou multi-provider (MirrorMode / N-way) | Réplication multi-maître native entre réplicas (accords de réplication) |
| Mise en place | Configuration manuelle `cn=config` | `ipa-replica-install`, topologie gérée |
| Services inclus | LDAP seul | LDAP, Kerberos, [[Glossary:DNS]] (option), [[Glossary:CA]], [[Glossary:SSSD]] |
| HA des clients | À organiser (DNS, load balancer, liste d'URI) | Les clients SSSD découvrent les serveurs par SRV/DNS |

Prérequis communs : DNS direct/inverse cohérent, [[Glossary:NTP]] synchronisé, certificats valides, ports ouverts entre nœuds, sauvegarde complète et testée, fenêtre de maintenance validée, au moins deux nœuds (voir quorum ci-dessous).

## 2. Exigences de version et licence

- **Versions à figer avant déploiement** : mêmes versions mineures de logiciel sur tous les nœuds, selon la documentation de la version retenue.
- OpenLDAP : licence libre (OpenLDAP Public License). FreeIPA : logiciel libre ; la version supportée commercialement est Red Hat Identity Management (abonnement [[Glossary:RHEL]] requis).

## 3. Quorum et choix d'architecture

- La réplication multi-maître **n'offre pas de quorum** : en cas de partition réseau, deux nœuds peuvent accepter des écritures divergentes. Prévoir un nœud d'écriture préféré, ou limiter les écritures à un seul nœud avec bascule contrôlée.
- OpenLDAP : un provider unique + consommateurs en lecture est le plus simple et le plus sûr. Multi-provider : réservé aux équipes maîtrisant la résolution de conflits.
- FreeIPA : maintenir au moins deux réplicas avec CA ; désigner explicitement le serveur de rôle CA et celui des renouvellements de certificats. Éviter une topologie en chaîne sans redondance de liens.

## 4. Procédure – Variante A : OpenLDAP syncrepl

1. Sauvegarder la configuration et les données sur chaque serveur :
```bash
sudo slapcat -n 0 -l /var/backups/ldap-config.ldif
sudo slapcat -n 1 -l /var/backups/ldap-data.ldif
```
2. Sur le provider : charger le module `syncprov` et l'overlay, après avoir défini `olcServerID`.
3. Créer un compte de réplication en lecture seule avec [[Glossary:ACL]] minimales ; [[Glossary:TLS]] obligatoire (`ldaps` ou StartTLS).
4. Sur le consumer : ajouter `olcSyncrepl` vers le provider (type `refreshAndPersist`, `starttls=critical`).
5. Contrôler la convergence : comparer `contextCSN`.
```bash
ldapsearch -x -H ldap://provider -s base -b "dc=exemple,dc=org" contextCSN
ldapsearch -x -H ldap://consumer -s base -b "dc=exemple,dc=org" contextCSN
```
6. Tester l'ajout d'une entrée de test sur le provider et sa présence sur le consumer, puis la supprimer.
7. Configurer côté clients plusieurs URI LDAP ou un [[Glossary:VIP]]/DNS.

## 5. Procédure – Variante B : FreeIPA réplicas

1. Sauvegarder le serveur existant :
```bash
sudo ipa-backup
ipa-healthcheck
```
2. Préparer le futur réplica : même OS/version majeure, nom DNS résolu, client IPA enrôlé (`ipa-client-install`).
3. Installer le paquet serveur puis promouvoir :
```bash
sudo ipa-replica-install --setup-ca
```
4. Vérifier la topologie et la santé :
```bash
ipa topologysegment-find domain
ipa-replica-manage list
ipactl status
```
5. Tester l'authentification Kerberos et la résolution d'un utilisateur depuis un client, en coupant temporairement un serveur (en maintenance planifiée).

## 6. Vérifications et rollback

- Convergence des données (CSN ou topologie), absence d'erreurs de réplication dans les journaux, authentification fonctionnelle sur chaque nœud.
- Rollback OpenLDAP : retirer `olcSyncrepl` du consumer et restaurer depuis `slapcat` ; ne jamais restaurer un ancien dump sur un provider actif sans arrêter la réplication.
- Rollback FreeIPA : retirer un réplica avec `ipa-replica-manage del` / `ipa server-del` selon la version ; restauration par `ipa-restore` uniquement hors procédure normale et sur tous les nœuds de façon coordonnée.
- Risques : divergence d'écriture, certificats expirés, désynchronisation d'horloge, suppression du dernier serveur CA. Aucune de ces opérations ne doit être faite hors fenêtre de maintenance.

## 7. Documentation officielle

- <https://www.openldap.org/doc/admin26/>
- <https://www.freeipa.org/page/Documentation>
- <https://docs.redhat.com/>
