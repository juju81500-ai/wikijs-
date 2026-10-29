# Fiche_Simple_-_VM_Debian_13_OCS_Inventory_Cadrer.md

- **Environnement** : VM Debian 13 dédiée, OCS Inventory 3.0 (Nginx, uWSGI, PostgreSQL local)
- **OS / Version** : Debian 13 Trixie; OCS Inventory 3.0; PostgreSQL 17
- **Catégorie** : inventaire de parc / ITSM
- **Tags** : `debian13`, `ocs-inventory`, `ocs3`, `postgresql`, `nginx`, `prerequis`

---

## Problème précis à résoudre

Valider l'architecture (backend API + console), les noms DNS, les ressources et les accès avant d'installer OCS Inventory 3.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier la version de Debian et les ressources de la VM :
   ```bash
   cat /etc/os-release
   free -h
   df -h /
   ```
   👉 Explication : OCS 3 demande au minimum 4 Go de RAM (8 Go recommandés) et un stockage adapté au volume des inventaires.

2. Vérifier que les noms DNS prévus résolvent vers la VM (remplacer `ocs.example.net` et `ocs-api.example.net` par vos noms réels) :
   ```bash
   getent hosts ocs.example.net
   getent hosts ocs-api.example.net
   ```
   👉 Explication : la console et l'API utilisent deux noms distincts; ils doivent exister avant la configuration TLS.

3. Contrôler qu'aucun paquet serveur OCS 2.x n'est installé :
   ```bash
   dpkg -l | grep -i ocsinventory
   ```
   👉 Explication : l'architecture OCS 3 (Django/uWSGI + console Vue.js) ne doit pas être mélangée avec les paquets serveur OCS 2.x.

## 2. Production — Contrôles

Documenter les noms DNS, certificats TLS, réseaux autorisés vers la console et l'API, serveur SMTP, et la destination des sauvegardes hors hôte.

## 3. Production — Sécurité

- Restreindre l'administration et l'API aux réseaux autorisés.
- Prévoir le chiffrement TLS dès la conception; ne pas exposer le port API sans TLS validé.

## Validation et retour arrière

- **Validation** : DNS résolus, ressources suffisantes, aucun paquet OCS 2.x présent.
- **Retour arrière** : Aucune modification n'a été faite à cette étape; rien à annuler.

## Si le problème n'est pas résolu

- [OCS Inventory — Installation essentielle](https://documentation.ocsinventory-ng.org/quickstart-guides/for-administrators/installation-essentials.md)
- [Guide complet OCS Inventory 3 Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/41_Deploiement_OCS_Inventory_3_Debian_13.md#1-architecture-et-prerequis)
