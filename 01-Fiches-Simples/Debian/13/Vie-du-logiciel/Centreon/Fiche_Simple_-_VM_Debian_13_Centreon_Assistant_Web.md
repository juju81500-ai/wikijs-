# Fiche_Simple_-_VM_Debian_13_Centreon_Assistant_Web.md

- **Environnement** : VM Debian 13 dédiée, serveur Centreon Central avec MariaDB locale
- **OS / Version** : Debian 13 Trixie; Centreon 26.10
- **Catégorie** : supervision / configuration
- **Tags** : `debian13`, `centreon`, `supervision`, `wizard`, `admin`

---

## Problème précis à résoudre

Finaliser Centreon via son assistant Web et créer le compte administrateur.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir `https://centreon.example.net/centreon` (nom d'exemple à remplacer par votre FQDN) depuis le réseau d'administration.
   👉 Explication : accède à l'assistant d'installation.

2. Suivre l'assistant : vérifier les dépendances, garder les chemins recommandés.
   👉 Explication : les valeurs par défaut sont validées par Centreon.

3. Créer le compte `admin` avec un mot de passe unique saisi dans l'assistant et conservé dans un coffre.
   👉 Explication : le secret n'est jamais mis en ligne de commande.

4. Laisser l'assistant initialiser les bases et modules, puis vérifier le certificat TLS présenté par le navigateur.
   👉 Explication : confirme que HTTPS utilise le certificat attendu.

## 2. Production — Contrôles

Après installation, l'accès à la page d'installation ne doit plus être possible; vérifier la redirection HTTP vers HTTPS selon la politique approuvée.

## 3. Production — Sécurité

- Mot de passe `admin` unique, stocké au coffre.
- Accès limité au réseau d'administration.
- Ne pas laisser l'installateur accessible.

## Validation et retour arrière

- **Validation** : connexion admin possible, TLS correct, page d'installation inaccessible.
- **Retour arrière** : relancer l'assistant sur une VM restaurée si l'initialisation a échoué.

## Si le problème n'est pas résolu

- [Centreon — installation Web et post-installation](https://docs.centreon.com/docs/installation/web-and-post-installation/)
- [Guide complet Déployer Centreon 26.10 sur Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/48_Deploiement_Centreon_26.10_Debian_13.md#4-terminer-lassistant-web)
