# Fiche_Simple_-_VM_Debian_12_Znuny_Assistant.md

- **Environnement** : VM Debian 12 dédiée (Apache/mod_perl, MariaDB 10.11), Znuny 7.3.8
- **OS / Version** : Debian 12 Bookworm; Znuny 7.3.8
- **Catégorie** : ITSM / ticketing

---

## Problème précis à résoudre

Terminer l'installation de Znuny via l'assistant web, puis fermer l'accès à l'installateur.

## 1. Hors-Production (Lab / Test / POC)

1. Depuis le réseau d'administration, ouvrir temporairement `https://support.example.net/znuny/installer.pl` (remplacer par le vrai nom DNS).
   👉 Explication : l'assistant web configure la base, le courriel et le propriétaire du service.

2. Dans l'assistant, choisir la base `znuny` et le compte dédié créé à l'étape MariaDB.
   👉 Explication : on n'utilise jamais le compte `root` de la base.

3. Renseigner l'adresse de courriel de support, le propriétaire du service et les premières données.
   👉 Explication : ces valeurs alimentent la configuration initiale.

4. Terminer l'assistant, définir les identifiants initiaux, puis tester la connexion agent et client.
   👉 Explication : on vérifie que les deux interfaces fonctionnent.

5. Restreindre ou désactiver l'accès à l'installateur selon la documentation Znuny.
   👉 Explication : la page installateur ne doit pas rester accessible.

## 2. Production — Contrôles

Limiter l'installateur au réseau d'administration et noter la date de désactivation.

## 3. Production — Sécurité

- Ne pas laisser `installer.pl` accessible après la mise en service.
- Changer immédiatement les identifiants initiaux par un secret fort stocké dans le coffre.

## Validation et retour arrière

- **Validation** : Connexion agent et client réussie; `installer.pl` refusé ou désactivé.
- **Retour arrière** : Sur une installation vide : recréer la base `znuny` et relancer l'assistant; en production, restaurer la base et `Kernel/Config.pm` sauvegardés.

## Si le problème n'est pas résolu

- [Znuny — Installation officielle](https://doc.znuny.org/znuny/installation/index.html)
- [Znuny — Release 7.3.8](https://doc.znuny.org/znuny/releases/7_3_8/index.html)
- [Guide complet — exécuter l'assistant d'installation](/02-fiches-completes/debian/12/installation-deploiement/42-deploiement-znuny-7-3-8-debian-12#6-executer-lassistant-dinstallation)