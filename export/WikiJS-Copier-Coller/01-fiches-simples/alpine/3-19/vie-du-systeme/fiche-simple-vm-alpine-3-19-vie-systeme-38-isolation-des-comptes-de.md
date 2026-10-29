# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_38_Isolation_Des_Comptes_De

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 38 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Faire tourner chaque service sous un compte dédié.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un compte système sans connexion (remplacer `APPLI`) :
   ```sh
   doas addgroup -S APPLI
   doas adduser -S -D -H -s /sbin/nologin -G APPLI APPLI
   ```
   👉 Explication : crée un compte système sans mot de passe, sans répertoire personnel et sans interpréteur.

2. Créer le répertoire de données et donner les droits :
   ```sh
   doas install -d -o APPLI -g APPLI -m 0750 /var/lib/APPLI
   ```
   👉 Explication : seul le compte du service accède aux données.

3. Contrôler le compte :
   ```sh
   getent passwd APPLI
   id APPLI
   ```
   👉 Explication : doit afficher l'interpréteur `/sbin/nologin`.

## 2. Production — Contrôles

Un compte par service.

## 3. Production — Sécurité

Pas de `wheel` pour un compte de service.

## Validation et retour arrière

- **Validation** : `getent passwd APPLI` retourne le compte sans interpréteur de connexion.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)