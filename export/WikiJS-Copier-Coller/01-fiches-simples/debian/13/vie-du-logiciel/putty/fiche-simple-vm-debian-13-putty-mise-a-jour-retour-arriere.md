# Fiche_Simple_-_VM_Debian_13_PuTTY_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13 (Trixie), poste d'administration en ligne de commande
- **OS / Version** : Debian 13 (Trixie) — paquet putty-tools
- **Catégorie** : outils d'administration / SSH

---

## Problème précis à résoudre

Mettre à jour `putty-tools` et revenir à la version précédente si nécessaire.

## 1. Hors-Production (Lab / Test / POC)

1. Consulter les versions disponibles :
   ```bash
   apt policy putty-tools
   ```
   👉 Explication : noter la version installée avant mise à jour.
2. Mettre à jour :
   ```bash
   sudo apt update
   sudo apt install --only-upgrade putty-tools
   ```
   👉 Explication : met à jour uniquement ce paquet.
3. Revenir à une version antérieure disponible dans les dépôts (remplacer `VERSION_A_REMPLACER`) :
   ```bash
   sudo apt install putty-tools=VERSION_A_REMPLACER
   ```
   👉 Explication : possible seulement si cette version est encore disponible ; sinon passer par `snapshot.debian.org`, à vérifier.

## 2. Production — Contrôles

- Mettre à jour avec les correctifs de sécurité Debian.

## 3. Production — Sécurité

- Utiliser `unattended-upgrades` pour les mises à jour de sécurité.

## Validation et retour arrière

- **Validation** : `plink -V` affiche la version attendue. **Retour arrière** : réinstaller la version précédente.

## Si le problème n'est pas résolu

- [Fiche d'entrée PuTTY](/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-putty)
- [Debian — paquet putty-tools](https://packages.debian.org/trixie/putty-tools)
- [Documentation officielle PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html)