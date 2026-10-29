# Fiche_Simple_-_VM_Debian_13_NetBox_Valider_IPAM_Pilote.md

- **Environnement** : NetBox 4.7.4 pilote, client du réseau d'administration
- **OS / Version** : Debian 13; NetBox 4.7.4
- **Catégorie** : IPAM / DCIM / validation fonctionnelle
- **Tags** : `debian13`, `netbox`, `ipam`, `api`, `validation`

---

## Problème précis à résoudre

Vérifier un petit jeu de données IPAM et la tâche de fond avant d'importer des données d'autorité.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les services :
   ```bash
   sudo systemctl is-active netbox netbox-rq postgresql redis-server nginx
   ```
   👉 Explication : cinq réponses `active`.

2. Interface NetBox : ouvrir `https://FQDN/`, puis **Organization > Sites > Add** (site de lab), **IPAM > Aggregates > Add** (aggregate détenu), **IPAM > Prefixes > Add** (parent puis enfant, avec rôle et statut).
   👉 Explication : respecter le plan d'adressage approuvé; ne pas importer le plan complet avant de définir conventions, VRF, tenants et propriétaires.

3. **IPAM > IP Addresses > Add** : créer une adresse de test dans le préfixe enfant.
   👉 Explication : la hiérarchie et le calcul d'utilisation du préfixe doivent s'afficher; vérifier l'absence de chevauchement hors VRF.

4. Vérifier la tâche de fond : **Jobs** (menu Admin) après un petit import `IPAM > Prefixes > Import`, ou en ligne de commande :
   ```bash
   sudo systemctl status netbox-rq --no-pager
   sudo journalctl -u netbox-rq -n 20 --no-pager
   ```
   👉 Explication : la tâche doit se terminer sans erreur.

5. Tester l'API avec un compte à privilèges limités :
   ```bash
   read -rsp 'Jeton API : ' NB_TOKEN; echo
   curl -sk -H "Authorization: Bearer $NB_TOKEN" -H 'Accept: application/json' https://FQDN/api/ipam/prefixes/ | head -c 300
   unset NB_TOKEN
   ```
   👉 Explication : remplacer `FQDN`; le format du jeton dépend de la version (voir la documentation); révoquer le jeton après essai.

## 2. Production — Contrôles

Avant import, approuver conventions de statuts, rôles, VRF, tenants, propriétaires, sources d'autorité, validation des données et permissions API.

## 3. Production — Sécurité

- Ne pas importer un plan complet avant revue des chevauchements et de la qualité.
- Ne pas utiliser un jeton administrateur pour les intégrations.
- Protéger, limiter et révoquer les jetons après les essais.
- Ne pas publier des exports IPAM pouvant révéler la topologie à des personnes non autorisées.

## Validation et retour arrière

- **Validation** : données de test cohérentes, tâche en file terminée, API limitée et jeton révocable.
- **Retour arrière** : supprimer uniquement les objets explicitement créés pour le pilote après vérification de leur identifiant et de leurs dépendances.

## Si le problème n'est pas résolu

- [NetBox — IPAM](https://netbox.readthedocs.io/en/stable/features/ipam/)
- [NetBox — permissions d'objet](https://netbox.readthedocs.io/en/stable/administration/permissions/)
- [Guide complet NetBox Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/73_Deploiement_NetBox_4.7.4_Debian_13.md#8-verifier-un-flux-ipam-pilote)
