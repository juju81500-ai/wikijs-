# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_19_Configuration_Des_Depots_Logiciels

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 19 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Définir les dépôts d'`apk` pour 3.19.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les dépôts actifs :
   ```sh
   cat /etc/apk/repositories
   ```
   👉 Explication : doit contenir `https://dl-cdn.alpinelinux.org/alpine/v3.19/main` et `.../community`, jamais `edge`.

2. Fixer la branche 3.19 de façon explicite (adapter au miroir interne si besoin) :
   ```sh
   cat > /etc/apk/repositories <<'EOF'
   https://dl-cdn.alpinelinux.org/alpine/v3.19/main
   https://dl-cdn.alpinelinux.org/alpine/v3.19/community
   EOF
   apk update
   ```
   👉 Explication : épingle la version stable; `apk update` charge l'index et signale tout dépôt injoignable.

3. Vérifier l'origine d'un paquet :
   ```sh
   apk policy openssh
   ```
   👉 Explication : indique la version candidate et le dépôt d'où elle vient.

## 2. Production — Contrôles

Utiliser un miroir interne pour maîtriser les versions.

## 3. Production — Sécurité

Ne pas activer `testing` ni `edge` en production; les clés du dépôt sont dans `/etc/apk/keys`.

## Validation et retour arrière

- **Validation** : `apk update` termine sans erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)