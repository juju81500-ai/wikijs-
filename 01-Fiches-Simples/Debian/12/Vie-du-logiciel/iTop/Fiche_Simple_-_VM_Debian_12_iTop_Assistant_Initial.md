# Fiche_Simple_-_VM_Debian_12_iTop_Assistant_Initial.md

- **Environnement** : VM Linux dédiée avec Apache, PHP 8.2 ou 8.3 et MariaDB 10.11 (serveur ITSM/CMDB)
- **OS / Version** : Debian 12 Bookworm (ou Ubuntu Server 24.04 LTS); iTop Community 3.3.0
- **Catégorie** : ITSM / CMDB / helpdesk
- **Tags** : `debian12`, `itop`, `itsm`, `cmdb`, `apache`, `mariadb`

---

## Problème précis à résoudre

Terminer l'installation par l'assistant web puis le verrouiller.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier qu'Apache tourne :
   ```bash
   sudo systemctl --no-pager status apache2
   ```
   👉 Explication : le service doit être actif.

2. Ouvrir **https://itsm.example.net/setup** (remplacer par votre nom DNS).
   👉 Explication : lance l'assistant.

3. Sélectionner la base dédiée, saisir l'utilisateur `itop` et son secret, puis vérifier les contrôles PHP et Graphviz.
   👉 Explication : le secret se saisit uniquement dans l'assistant.

4. Choisir les modules réellement nécessaires, créer le premier compte administrateur et terminer.
   👉 Explication : limite les modules actifs au besoin.

5. Appliquer la procédure officielle de protection de l'assistant setup et vérifier qu'il n'est plus accessible aux utilisateurs non autorisés.
   👉 Explication : évite une réinstallation ou une fuite d'information.

6. Configurer notifications SMTP, annuaire LDAP/AD si requis, profils et premières données CMDB.
   👉 Explication : finalise l'exploitation.

## 2. Production — Contrôles

Documenter modules, SMTP et profils; protéger `/setup` par le réseau ou l'authentification.

## 3. Production — Sécurité

- Restreindre `/setup` immédiatement après l'installation.
- Compte administrateur nominatif avec mot de passe fort.

## Validation et retour arrière

- **Validation** : connexion admin possible et `/setup` non accessible aux utilisateurs ordinaires.
- **Retour arrière** : avant fin d'assistant, supprimer la base et reprendre depuis l'étape 3; après, restaurer une sauvegarde de base et de `conf`.

## Si le problème n'est pas résolu

- [iTop — installation](https://www.itophub.io/wiki/page?id=latest:install:start)
- [iTop — installation et mise à niveau](https://www.itophub.io/wiki/page?id=latest:install:start)
- [Guide complet](../../../../../02-Fiches-Completes/Transverses/Multi-OS/Installation-Deploiement/40_Deploiement_iTop_3.3_Debian12_Ubuntu2404.md#5-executer-lassistant-initial)
