# Fiche_Simple_-_VM_Debian_13_phpIPAM_Perimetre.md

- **Environnement** : VM Debian 13, phpIPAM avec MariaDB locale, PHP-FPM et Nginx
- **OS / Version** : Debian 13 Trixie x86-64; phpIPAM 1.8.3; PHP 8.4
- **Catégorie** : IPAM / cadrage
- **Tags** : `debian13`, `phpipam`, `ipam`, `nginx`, `mariadb`, `prerequis`

---

## Problème précis à résoudre

Définir ce que phpIPAM va gérer avant l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Noter la version cible : phpIPAM 1.8.3 (PHP 7.2 à 8.5; Debian 13 fournit PHP 8.4).
   👉 Explication : la procédure détaillée amont vise Ubuntu, à valider en préproduction sur Debian 13.

2. Réserver un FQDN (exemple `ipam.example.net`, à remplacer), un certificat TLS, les administrateurs responsables et le plan d'adressage approuvé.
   👉 Explication : tout doit exister avant l'installation.

3. Exclure scans, pings automatiques, découverte d'hôtes, suppression automatique d'adresses inactives et exposition hors réseau d'administration.
   👉 Explication : le périmètre est l'inventaire IPAM saisi manuellement.

## 2. Production — Contrôles

Valider le plan d'adressage, les responsables et le réseau d'administration autorisé.

## 3. Production — Sécurité

- Ne pas exposer la console hors réseau d'administration.
- Ne pas activer de scan réseau sans autorisation.

## Validation et retour arrière

- **Validation** : périmètre, FQDN, certificat et plan d'adressage sont approuvés.
- **Retour arrière** : aucune modification à cette étape.

## Si le problème n'est pas résolu

- [phpIPAM — installation](https://phpipam.net/documents/installation/)
- [phpIPAM — releases officielles](https://github.com/phpipam/phpipam/releases)
- [Guide complet Déployer phpIPAM 1.8.3 sur Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/74_Deploiement_phpIPAM_1.8.3_Debian_13.md#1-perimetre-et-prerequis)
