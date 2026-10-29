# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_11_Compte_D_Administration_Delegue

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 11 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Créer un compte nominatif et lui donner les droits d'administration avec `doas`.

## 1. Hors-Production (Lab / Test / POC)

1. Installer `doas` et créer le compte (remplacer `ADMIN`) :
   ```sh
   apk add doas
   adduser ADMIN
   adduser ADMIN wheel
   ```
   👉 Explication : `adduser` demande un mot de passe; le second appel ajoute le compte au groupe `wheel`.

2. Autoriser le groupe `wheel` à utiliser `doas` :
   ```sh
   install -d -m 0755 /etc/doas.d
   cat > /etc/doas.d/10-wheel.conf <<'EOF'
   permit persist :wheel
   EOF
   chmod 0400 /etc/doas.d/10-wheel.conf
   ```
   👉 Explication : `persist` garde l'authentification quelques minutes; le fichier est lu par `doas`.

3. Tester avec le nouveau compte :
   ```sh
   su - ADMIN
   doas id
   ```
   👉 Explication : doit afficher `uid=0(root)` après saisie du mot de passe de ADMIN.

## 2. Production — Contrôles

Un compte par administrateur, avec revue périodique de la liste du groupe `wheel`.

## 3. Production — Sécurité

Pas de `permit nopass` sauf cas documenté, pas de partage de compte.

## Validation et retour arrière

- **Validation** : `doas id` retourne `uid=0(root)` pour ADMIN seul.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)