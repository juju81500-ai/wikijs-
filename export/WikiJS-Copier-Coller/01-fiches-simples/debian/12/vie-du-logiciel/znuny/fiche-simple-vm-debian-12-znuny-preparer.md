# Fiche_Simple_-_VM_Debian_12_Znuny_Preparer.md

- **Environnement** : VM Debian 12 dédiée (Apache/mod_perl, MariaDB 10.11), Znuny 7.3.8
- **OS / Version** : Debian 12 Bookworm; Znuny 7.3.8
- **Catégorie** : ITSM / ticketing

---

## Problème précis à résoudre

Vérifier les prérequis (OS, Perl, espace, DNS, sauvegarde) avant d'installer Znuny 7.3.8.

## 1. Hors-Production (Lab / Test / POC)

1. Lire les notes de version et le support applicatif de Znuny 7.3.8 sur https://doc.znuny.org/znuny/releases/7_3_8/index.html.
   👉 Explication : on s'assure que Debian 12 est bien testée par l'éditeur avant d'aller plus loin.

2. Contrôler l'OS cible :
   ```bash
   grep PRETTY_NAME /etc/os-release
   ```
   👉 Explication : la sortie doit indiquer Debian GNU/Linux 12 (bookworm).

3. Vérifier la version de Perl (5.16 minimum requis) :
   ```bash
   perl -v | head -n 2
   ```
   👉 Explication : Znuny est écrit en Perl; une version trop ancienne bloque l'installation.

4. Vérifier l'espace disponible pour `/opt` et la base :
   ```bash
   df -h /opt /var/lib
   ```
   👉 Explication : le logiciel, les pièces jointes et la base de données ont besoin de place.

5. Vérifier la résolution DNS du nom prévu (remplacer `support.example.net` par le vrai nom) :
   ```bash
   getent hosts support.example.net
   ```
   👉 Explication : le nom du service doit exister avant de configurer Apache et TLS.

## 2. Production — Contrôles

Prévoir DNS, TLS, SMTP, sauvegarde hors hôte et accès console/SSH de secours. Valider d'abord sur une VM de test.

## 3. Production — Sécurité

- Utiliser un serveur dédié ou une VM de test avant la production.
- Ne pas installer Znuny sur un hôte Apache partagé sans avoir évalué l'impact du MPM prefork.

## Validation et retour arrière

- **Validation** : OS et Perl conformes, DNS résolu, espace suffisant et sauvegarde hors hôte prévue.
- **Retour arrière** : Cette étape ne modifie rien : aucun retour arrière nécessaire.

## Si le problème n'est pas résolu

- [Znuny — Installation officielle](https://doc.znuny.org/znuny/installation/index.html)
- [Znuny — Release 7.3.8](https://doc.znuny.org/znuny/releases/7_3_8/index.html)
- [Guide complet — préparer l'installation](/02-fiches-completes/debian/12/installation-deploiement/42-deploiement-znuny-7-3-8-debian-12#1-preparer-linstallation)