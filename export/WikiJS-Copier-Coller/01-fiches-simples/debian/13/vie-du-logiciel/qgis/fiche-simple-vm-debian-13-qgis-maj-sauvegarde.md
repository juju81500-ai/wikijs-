# Fiche_Simple_-_VM_Debian_13_QGIS_Maj_Sauvegarde.md

- **Environnement** : QGIS Desktop sur Debian 13 amd64
- **OS / Version** : Debian 13; QGIS 3.44 LTR
- **Catégorie** : SIG / maintenance

---

## Problème précis à résoudre

Mettre à jour QGIS prudemment et sauvegarder projets et profil.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les mises à jour QGIS disponibles :
   ```bash
   apt list --upgradable 2>/dev/null | grep -i qgis
   ```
   👉 Explication : À tester d'abord sur un poste pilote.

2. Mettre à jour QGIS seulement après essai pilote :
   ```bash
   sudo apt update
   sudo apt install --only-upgrade qgis
   ```
   👉 Explication : Met à niveau sans toucher aux autres paquets.

3. Sauvegarder le profil utilisateur (remplacer `~/SIG` par votre dossier de sauvegarde) :
   ```bash
   mkdir -p ~/SIG/sauvegarde
   tar -czf ~/SIG/sauvegarde/profil-qgis.tar.gz -C ~/.local/share/QGIS QGIS3
   ```
   👉 Explication : Préserve configuration, plugins et authentifications.

4. Sauvegarder le projet `.qgz` avec ses données ou documenter les sources distantes.
   👉 Explication : La sauvegarde du seul projet n'inclut pas les données externes.

## 2. Production — Contrôles

Vérifier la compatibilité des plugins, modèles, styles et projets avant généralisation; un projet récent peut utiliser des fonctions absentes d'anciennes versions. Tester la restauration sur un poste propre.

## 3. Production — Sécurité

- Protéger l'archive du profil : elle peut contenir des authentifications.

## Validation et retour arrière

- **Validation** : copie restaurée fonctionnelle sur un poste propre.
- **Retour arrière** : réinstaller la version précédente validée et restaurer l'archive du profil.

## Si le problème n'est pas résolu

- [QGIS — installation Linux](https://qgis.org/resources/installation-guide/)
- [QGIS — guide utilisateur 3.44](https://docs.qgis.org/3.44/en/docs/user_manual/)
- [Guide complet QGIS Debian 13](/02-fiches-completes/debian/13/installation-deploiement/75-deploiement-qgis-3-44-ltr-debian-13#7-mise-a-jour-et-sauvegarde)