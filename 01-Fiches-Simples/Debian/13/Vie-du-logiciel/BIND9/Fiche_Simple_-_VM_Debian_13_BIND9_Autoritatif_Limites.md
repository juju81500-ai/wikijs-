# Fiche_Simple_-_VM_Debian_13_BIND9_Autoritatif_Limites.md

- **Environnement** : VM Debian 13 pilote avec bind9
- **OS / Version** : Debian 13 Trixie; paquets bind9 de la distribution
- **Catégorie** : dns / recette
- **Tags** : `debian13`, `bind9`, `limites`, `recette`

---

## Problème précis à résoudre

Connaître ce que la procédure ne prouve pas avant utilisation en production.

## 1. Hors-Production (Lab / Test / POC)

1. Relever la version réellement installée :
   ```bash
   named -V
   ```
   👉 Explication : les commandes du guide proviennent des documentations BIND et Debian; elles n'ont pas été exécutées sur Debian 13 dans ce workspace.

2. Tester l'écoute réseau réelle :
   ```bash
   sudo ss -lntup '( sport = :53 )'
   ```
   👉 Explication : la validation structurelle ne prouve pas l'écoute réseau; on la constate sur le serveur.

3. Tester la résolution depuis un vrai client autorisé (adresse d'exemple à remplacer) :
   ```bash
   dig @192.0.2.53 srv1.lab.example.test A +norecurse
   ```
   👉 Explication : la réponse doit être autoritative; c'est le seul test qui prouve le fonctionnement de bout en bout.

## 2. Production — Contrôles

Valider sur un pilote avant généralisation et consigner les écarts observés.

## 3. Production — Sécurité

- Ne pas présenter la page comme prouvée en production.
- Ne pas publier de topologie réelle dans la documentation.

## Validation et retour arrière

- **Validation** : Résolution de bout en bout confirmée depuis un client autorisé.
- **Retour arrière** : Revenir à la sauvegarde de configuration si un écart est constaté.

## Si le problème n'est pas résolu

- [ISC BIND 9 — Manpages](https://bind9.readthedocs.io/en/latest/manpages.html)
- [Debian — paquet bind9 Trixie](https://packages.debian.org/trixie/bind9)
- [Guide complet BIND9 Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/63_Deploiement_BIND9_Autoritatif_Debian_13.md#7-limites-de-validation)
