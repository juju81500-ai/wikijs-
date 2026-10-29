# Fiche_Simple_-_VM_Debian_13_NetBox_Cadrer.md

- **Environnement** : VM Debian 13 dédiée, NetBox 4.7.4, petit pilote IPAM/DCIM
- **OS / Version** : Debian 13 Trixie; NetBox 4.7.4
- **Catégorie** : IPAM / DCIM / cadrage
- **Tags** : `debian13`, `netbox`, `ipam`, `dcim`, `cadrage`

---

## Problème précis à résoudre

Définir l'usage de NetBox comme source de vérité et les responsabilités de données avant son installation.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les versions disponibles sur Debian 13 :
   ```bash
   python3 --version
   apt-cache policy postgresql redis-server | grep -E 'postgresql|redis|Candidate'
   ```
   👉 Explication : NetBox 4.7.x exige Python 3.12+, PostgreSQL 15+ et Redis 6+.

2. Vérifier le nom d'hôte, l'heure et les ressources :
   ```bash
   hostname -f
   timedatectl show -p NTPSynchronized --value
   free -h; df -h /opt /var/lib
   ```
   👉 Explication : le FQDN servira à `ALLOWED_HOSTS` et au certificat TLS.

3. Contrôler que les ports de service sont libres :
   ```bash
   sudo ss -ltnp | grep -E ':(80|443|5432|6379|8001)\b' || echo "ports libres"
   ```
   👉 Explication : évite un conflit avec un autre service web ou base.

4. Consigner FQDN, adresse de gestion, réseau d'administration, propriétaires, conservation et emplacement des sauvegardes.
   👉 Explication : NetBox est une source de vérité; ses données doivent avoir un propriétaire et un processus de revue.

## 2. Production — Contrôles

Avant le passage en production, approuver conventions de sites, tenants, VRF, états et rôles, source d'autorité, responsabilités de revue, rétention, API et intégrations.

## 3. Production — Sécurité

- N'exposer l'interface et l'API qu'en HTTPS sur le réseau autorisé.
- Ne pas importer le plan complet avant validation des conventions et de la qualité des données.
- Ne pas utiliser de données ou jetons réels dans le pilote.
- Ne pas considérer NetBox comme mécanisme automatique de découverte ou de contrôle d'accès réseau.

## Validation et retour arrière

- **Validation** : propriétaire, FQDN, données pilotes, contrôle d'accès, sauvegarde et restauration sont définis.
- **Arrêt** : ne pas installer si les règles de responsabilité ou de publication ne sont pas approuvées.

## Si le problème n'est pas résolu

- [NetBox — documentation d'installation](https://netbox.readthedocs.io/en/stable/installation/)
- [NetBox — IPAM](https://netbox.readthedocs.io/en/stable/features/ipam/)
- [Guide complet NetBox Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/73_Deploiement_NetBox_4.7.4_Debian_13.md#1-cadrer-linstallation)
