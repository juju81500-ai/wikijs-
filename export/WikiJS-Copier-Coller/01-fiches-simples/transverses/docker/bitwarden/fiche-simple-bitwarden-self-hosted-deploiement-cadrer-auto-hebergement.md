# Fiche_Simple_-_Bitwarden_Self_Hosted_Deploiement_Cadrer_Auto_Hebergement.md

- **Environnement** : Serveur Linux x86-64 avec Docker Engine et Compose (déploiement standard Bitwarden)
- **OS / Version** : Linux x86-64 supporté; Docker Engine 26+
- **Catégorie** : coffre de mots de passe / secrets

---

## Problème précis à résoudre

Décider si l'auto-hébergement est adapté et réunir les prérequis.

## 1. Hors-Production (Lab / Test / POC)

1. Comparer le besoin avec Bitwarden SaaS et vérifier les licences d'organisation.
   👉 Explication : certaines fonctions d'organisation exigent une licence.

2. Prévoir un FQDN dédié, TLS valide, SMTP, stockage persistant, supervision, sauvegarde hors hôte et procédure de mise à jour.
   👉 Explication : éléments indispensables avant installation.

3. Contrôler les ressources de l'hôte :
   ```bash
   nproc
   free -h
   df -h /opt
   ```
   👉 Explication : le déploiement standard annonce 2 vCPU, 4 Go de RAM et 12 Go de stockage minimum (25 Go recommandés).

4. Retenir que la base MSSQL Express intégrée est limitée; une base externe suit les instructions Bitwarden.
   👉 Explication : dimensionner selon comptes, pièces jointes, sauvegardes et journaux.

## 2. Production — Contrôles

Valider licence, FQDN, TLS et dimensionnement avec le responsable.

## 3. Production — Sécurité

- Ne pas exposer l'administration Docker ni l'interface d'administration Bitwarden sur Internet.

## Validation et retour arrière

- **Validation** : décision documentée et ressources suffisantes.
- **Retour arrière** : aucune modification n'est faite par cette fiche; rien à annuler.

## Si le problème n'est pas résolu

- [Bitwarden — exigences réseau](https://bitwarden.com/help/networking-requirements/)
- [Bitwarden — déploiement Linux](https://bitwarden.com/help/install-on-premise-linux/)
- [Guide complet](/02-fiches-completes/transverses/docker/installation-deploiement/62-deploiement-bitwarden-self-hosted-linux-docker#1-cadrer-lauto-hebergement)