# Fiche_Simple_-_VM_Debian_13_NetBox_Sauvegarder_Mettre_A_Jour.md

- **Environnement** : NetBox 4.7.4 sur Debian 13, stockage et sauvegardes chiffrées hors hôte
- **OS / Version** : Debian 13; NetBox et PostgreSQL
- **Catégorie** : IPAM / DCIM / sauvegarde et maintenance
- **Tags** : `debian13`, `netbox`, `backup`, `restore`, `upgrade`

---

## Problème précis à résoudre

Protéger la base, la configuration, les médias et les fichiers locaux, puis démontrer la restauration et la mise à niveau.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la base :
   ```bash
   sudo install -d -m 0700 /var/backups/netbox
   sudo -u postgres pg_dump --format=custom --file=/var/backups/netbox/netbox-$(date +%F).dump netbox
   ```
   👉 Explication : le format `custom` permet une restauration sélective; le dossier est réservé à `root`.

2. Sauvegarder configuration, médias et configuration Nginx :
   ```bash
   sudo tar -czf /var/backups/netbox/fichiers-$(date +%F).tar.gz /opt/netbox/netbox/netbox/configuration.py /opt/netbox/netbox/media /etc/nginx/sites-available/netbox
   sudo sha256sum /var/backups/netbox/*
   ```
   👉 Explication : ces fichiers contiennent des secrets; chiffrer et copier hors serveur.

3. Restaurer sur une instance de test :
   ```bash
   sudo -u postgres createdb netbox_test
   sudo -u postgres pg_restore --dbname=netbox_test /var/backups/netbox/netbox-AAAA-MM-JJ.dump
   ```
   👉 Explication : remplacer la date; l'extension `ltree` doit être restaurée avec le schéma; vérifier connexion, consultation d'objets et export.

4. Mettre à niveau dans un répertoire versionné distinct :
   ```bash
   cd /tmp
   curl --fail --location -o netbox-vX.Y.Z.tar.gz https://github.com/netbox-community/netbox/archive/refs/tags/vX.Y.Z.tar.gz
   sudo tar -xzf netbox-vX.Y.Z.tar.gz -C /opt
   ```
   👉 Explication : remplacer `X.Y.Z`; copier `configuration.py` et les médias dans la nouvelle arborescence, exécuter son `upgrade.sh`, puis basculer le lien `/opt/netbox` et redémarrer `netbox` et `netbox-rq`.

5. En cas de migration depuis 4.7.0/4.7.1, renouveler les jetons API créés par tâches de masse (considérés compromis).
   👉 Explication : NetBox 4.7.2 corrige l'exposition de ces jetons dans les résultats de jobs.

## 2. Production — Contrôles

Documenter RPO/RTO, fréquence, rétention, chiffrement, responsables, procédure de restauration et tests réguliers avant mise à niveau.

## 3. Production — Sécurité

- Une sauvegarde de base seule ne restaure pas configuration, médias et secrets.
- Protéger `configuration.py`, les dumps et les clés; limiter les accès au coffre.
- Ne pas écraser la release active ni supprimer l'ancienne version avant validation de la nouvelle.
- Révoquer les jetons potentiellement exposés; inspecter les journaux et intégrations concernées.

## Validation et retour arrière

- **Validation** : restauration d'essai réussie, données et médias accessibles, version cible testée.
- **Retour arrière** : remettre ensemble code, base, configuration et médias compatibles depuis une sauvegarde cohérente.

## Si le problème n'est pas résolu

- [NetBox — releases](https://github.com/netbox-community/netbox/releases)
- [NetBox — installation](https://netbox.readthedocs.io/en/stable/installation/)
- [Guide complet NetBox Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/73_Deploiement_NetBox_4.7.4_Debian_13.md#9-sauvegardes-restauration-et-mises-a-niveau)
