# Fiche_Simple_-_VM_Debian_13_QGIS_Choisir_Version.md

- **Environnement** : QGIS Desktop sur Debian 13 amd64
- **OS / Version** : Debian 13; QGIS 3.44 LTR
- **Catégorie** : SIG / cadrage

---

## Problème précis à résoudre

Choisir la branche LTR et cadrer QGIS Desktop sur Debian 13.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l'architecture et la version de Debian :
   ```bash
   dpkg --print-architecture
   lsb_release -ds
   ```
   👉 Explication : Le dépôt QGIS LTR cible Trixie en amd64.

2. Contrôler la présence d'un environnement graphique :
   ```bash
   echo "$XDG_SESSION_TYPE"
   ```
   👉 Explication : `x11` ou `wayland` attendu; vide sans session graphique.

3. Vérifier si QGIS est déjà installé :
   ```bash
   apt-cache policy qgis
   ```
   👉 Explication : Repère le candidat Debian existant avant d'ajouter le dépôt LTR.

## 2. Production — Contrôles

Le périmètre couvre QGIS Desktop; QGIS Server, plugins tiers, scripts Python et données distantes nécessitent une revue distincte. Préparer données autorisées, CRS validé et emplacement de projet sauvegardé.

## 3. Production — Sécurité

- QGIS 4.x n'est pas empaqueté pour Debian 13 : ne pas prétendre le contraire.
- Protéger les données géographiques sensibles.

## Validation et retour arrière

- **Validation** : LTR 3.44 choisi, poste graphique amd64 prêt.
- **Retour arrière** : aucune modification; rien à annuler.

## Si le problème n'est pas résolu

- [QGIS — installation Linux](https://qgis.org/resources/installation-guide/)
- [QGIS — guide utilisateur 3.44](https://docs.qgis.org/3.44/en/docs/user_manual/)
- [Guide complet QGIS Debian 13](/02-fiches-completes/debian/13/installation-deploiement/75-deploiement-qgis-3-44-ltr-debian-13#1-choix-de-version-et-perimetre)