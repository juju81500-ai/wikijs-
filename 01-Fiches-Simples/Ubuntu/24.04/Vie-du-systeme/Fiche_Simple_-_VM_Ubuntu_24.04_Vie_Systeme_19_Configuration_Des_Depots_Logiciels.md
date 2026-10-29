# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_19_Configuration_Des_Depots_Logiciels

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 19 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2404`, `vie-du-systeme`, `cycle-de-vie`, `etape-19`

---

## Problème précis à résoudre

Définir les sources APT.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les sources (Ubuntu 24.04 « noble », format deb822) :
   ```bash
   cat /etc/apt/sources.list.d/ubuntu.sources
   cat /etc/apt/sources.list
   apt-cache policy | head -20
   ```
   👉 Explication : doit lister `noble`, `noble-updates`, `noble-backports` et `noble-security`; le fichier `sources.list` est vide ou ne contient qu'un commentaire.

2. Exemple de `/etc/apt/sources.list.d/ubuntu.sources` (remplacer l'URI par le miroir interne si besoin) :
   ```bash
   sudo tee /etc/apt/sources.list.d/ubuntu.sources >/dev/null <<'EOT'
   Types: deb
   URIs: http://archive.ubuntu.com/ubuntu/
   Suites: noble noble-updates noble-backports
   Components: main restricted universe multiverse
   Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg

   Types: deb
   URIs: http://security.ubuntu.com/ubuntu/
   Suites: noble-security
   Components: main restricted universe multiverse
   Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
   EOT
   sudo apt update
   ```
   👉 Explication : remplace les sources par les dépôts officiels puis rafraîchit l'index; `universe` et `multiverse` sont des composants communautaires (pas de support Canonical sans Ubuntu Pro).

## 2. Production — Contrôles

Utiliser un miroir ou proxy interne si le parc est important.

## 3. Production — Sécurité

Toute source tierce (PPA ou autre) doit avoir sa clé dans `/etc/apt/keyrings/` (jamais `apt-key`) et être validée par la sécurité.

## Validation et retour arrière

- **Validation** : `apt update` sans erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Ubuntu 24.04](./Sommaire_-_Vie_du_systeme_Ubuntu_24.04.md)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
