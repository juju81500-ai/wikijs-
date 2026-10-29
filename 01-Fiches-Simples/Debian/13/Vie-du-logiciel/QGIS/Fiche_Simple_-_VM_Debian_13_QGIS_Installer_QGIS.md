# Fiche_Simple_-_VM_Debian_13_QGIS_Installer_QGIS.md

- **Environnement** : QGIS Desktop sur Debian 13 amd64
- **OS / Version** : Debian 13; QGIS 3.44 LTR
- **Catégorie** : SIG / installation
- **Tags** : `debian13`, `qgis`, `apt`, `grass`

---

## Problème précis à résoudre

Installer QGIS Desktop depuis le dépôt LTR et vérifier la branche.

## 1. Hors-Production (Lab / Test / POC)

1. Mettre à jour l'index et contrôler le candidat :
   ```bash
   sudo apt update
   apt-cache policy qgis
   ```
   👉 Explication : Le candidat doit venir de qgis.org et être en 3.44.

2. Installer QGIS et le fournisseur GRASS si requis :
   ```bash
   sudo apt install -y qgis qgis-plugin-grass
   ```
   👉 Explication : GRASS n'est utile que si le cours ou le métier l'exige.

3. Vérifier la version :
   ```bash
   qgis --version
   ```
   👉 Explication : Doit appartenir à la branche 3.44 LTR.

## 2. Production — Contrôles

En environnement géré, valider la mise à jour sur un poste pilote.

## 3. Production — Sécurité

- Ne pas forcer l'installation en mélangeant paquets Debian et QGIS en cas de conflit.

## Validation et retour arrière

- **Validation** : `qgis --version` retourne 3.44.x.
- **Retour arrière** : `sudo apt remove qgis qgis-plugin-grass`.

## Si le problème n'est pas résolu

- [QGIS — installation Linux](https://qgis.org/resources/installation-guide/)
- [QGIS — guide utilisateur 3.44](https://docs.qgis.org/3.44/en/docs/user_manual/)
- [Guide complet QGIS Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/75_Deploiement_QGIS_3.44_LTR_Debian_13.md#3-installer-qgis-desktop)
