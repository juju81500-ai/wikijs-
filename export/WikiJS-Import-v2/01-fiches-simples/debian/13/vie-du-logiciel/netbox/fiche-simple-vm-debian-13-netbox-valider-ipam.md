---
title: "Fiche Simple - VM Debian 13 NetBox Valider IPAM"
description: "Confirmer qu'un inventaire IPAM pilote est cohérent, accessible aux bons rôles et sauvegardable/restaurable."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "netbox", "ipam", "dcim", "validation", "backup"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_NetBox_Valider_IPAM.md

- **Environnement** : NetBox 4.7.4 sur Debian 13, base et tâche de fond disponibles
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : IPAM / DCIM
- **Tags** : `debian13`, `netbox`, `ipam`, `dcim`, `validation`, `backup`

---

## Problème précis à résoudre

Confirmer qu'un inventaire IPAM pilote est cohérent, accessible aux bons rôles et sauvegardable/restaurable.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les services :
   ```bash
   sudo systemctl is-active netbox netbox-rq postgresql redis-server nginx
   ```
   👉 Explication : cinq réponses `active`.

2. Interface NetBox : créer un site (**Organization > Sites**), un aggregate (**IPAM > Aggregates**), un préfixe parent et un enfant (**IPAM > Prefixes**) avec rôle et statut cohérents.
   👉 Explication : on contrôle la hiérarchie et le statut des objets.

3. **IPAM > IP Addresses > Add** : ajouter une adresse de test, puis ouvrir **IPAM > Prefixes** pour vérifier le calcul d'utilisation.
   👉 Explication : aucune adresse en double hors VRF ne doit exister.

4. Tester les permissions : se connecter avec le compte opérateur (**Admin > Permissions** pour le périmètre) et tenter de modifier un objet hors périmètre.
   👉 Explication : l'opération doit être refusée.

5. Exporter un dump et le restaurer sur une instance isolée :
   ```bash
   sudo -u postgres pg_dump --format=custom --file=/var/backups/netbox-$(date +%F).dump netbox
   sudo -u postgres pg_restore --list /var/backups/netbox-$(date +%F).dump | head
   ```
   👉 Explication : la liste doit montrer les tables IPAM; restaurer ensuite le dump sur l'instance de test et vérifier un objet et son historique.

## 2. Production — Contrôles

Définir les propriétaires et le processus de changement avant de faire de NetBox une source d'autorité. Contrôler périodiquement les préfixes orphelins, chevauchements, VRF, statuts, doublons et tâches de fond en erreur.

## 3. Production — Sécurité

- HTTPS obligatoire; Nginx, PostgreSQL et Redis ne sont accessibles que depuis les composants nécessaires.
- Protéger `configuration.py`, `SECRET_KEY`, `API_TOKEN_PEPPERS`, secrets de base et jetons API.
- Accorder les permissions NetBox aux groupes et périmètres minimums; ne pas réutiliser un compte administrateur pour les intégrations.
- Stocker les dumps chiffrés hors de l'hôte et tester régulièrement une restauration.

## Validation et retour arrière

- **Validation** : préfixes/adresses cohérents, autorisations testées, tâche de fond terminée, dump restaurable.
- **Retour arrière** : conserver le dump et la configuration précédant l'import; supprimer uniquement les objets de test clairement identifiés.

## Si le problème n'est pas résolu

- [NetBox — documentation IPAM](https://netbox.readthedocs.io/en/stable/features/ipam/)
- [NetBox — permissions d'objet](https://netbox.readthedocs.io/en/stable/administration/permissions/)
- [Guide complet NetBox 4.7.4 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/73-deploiement-netbox-4-7-4-debian-13)