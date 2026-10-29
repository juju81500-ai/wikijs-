# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_14_Selection_Des_Composants_De

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 14 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-14`

---

## Problème précis à résoudre

Installer le strict nécessaire.

## 1. Hors-Production (Lab / Test / POC)

1. Choisir « Installation minimale » dans anaconda (ou `@^minimal-environment` en kickstart) :
   👉 Explication : réduit les paquets et la surface d'attaque.

2. Lister les groupes installés :
   ```bash
   dnf group list --installed
   ```
   👉 Explication : vérifie l'environnement choisi.

3. Compter les paquets présents :
   ```bash
   rpm -qa | wc -l
   ```
   👉 Explication : valeur de référence pour comparer par la suite.

## 2. Production — Contrôles

Ajouter les services par rôle, pas dans l'image de base.

## 3. Production — Sécurité

Pas d'interface graphique sur un serveur.

## Validation et retour arrière

- **Validation** : Environnement minimal confirmé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Rocky Linux 9](./Sommaire_-_Vie_du_systeme_Rocky_Linux_9.md)
- [Documentation officielle](https://docs.rockylinux.org/)
