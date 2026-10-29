# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_06_Langue_Et_Localisation_Locales

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 06 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-06`

---

## Problème précis à résoudre

Régler la langue de la session; Alpine utilise musl et n'a pas de `locale-gen`.

## 1. Hors-Production (Lab / Test / POC)

1. Constater la configuration actuelle :
   ```sh
   echo $LANG
   locale
   ```
   👉 Explication : sans réglage, la sortie est celle du jeu de caractères par défaut `C.UTF-8`.

2. Installer les messages français (musl-locales) :
   ```sh
   doas apk add musl-locales musl-locales-lang
   ```
   👉 Explication : ajoute les traductions pour les outils qui s'appuient sur `gettext`.

3. Définir la langue pour tous les comptes :
   ```sh
   doas sh -c 'cat > /etc/profile.d/lang.sh <<EOF
   export LANG=fr_FR.UTF-8
   export LC_COLLATE=C
   EOF'
   . /etc/profile.d/lang.sh
   locale
   ```
   👉 Explication : le fichier est lu à chaque connexion; `LC_COLLATE=C` conserve un tri prévisible pour les scripts.

## 2. Production — Contrôles

Choisir la langue de l'exploitation (français ou anglais) et la consigner.

## 3. Production — Sécurité

Ne pas changer la langue des comptes de service : les scripts attendent des sorties stables.

## Validation et retour arrière

- **Validation** : `locale` affiche `LANG=fr_FR.UTF-8` à la prochaine connexion.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
