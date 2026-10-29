---
title: "Fiche Simple - VM Ubuntu 26.04 Sauvegarde Test Restauration"
description: "Prouver qu'une sauvegarde Ubuntu 26.04 est exploitable en la restaurant dans un répertoire isolé, puis en comparant les données restaurées avec la source, avant de compter dessus pour un incident réel."
published: true
date: 2026-10-29T20:22:42Z
tags: ["ubuntu2604", "borgbackup", "restauration", "pra", "sauvegarde", "integrite"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_26.04_Sauvegarde_Test_Restauration

- **Environnement** : VM ou serveur Ubuntu dont les données sont sauvegardées avec BorgBackup
- **OS / Version** : Ubuntu Server 26.04 LTS
- **Catégorie** : Sauvegarde / Test de restauration (PRA)
- **Tags** : `ubuntu2604`, `borgbackup`, `restauration`, `pra`, `sauvegarde`, `integrite`

---

## 🎯 Problème précis à résoudre

Prouver qu'une sauvegarde Ubuntu 26.04 est exploitable en la restaurant dans un répertoire isolé, puis en comparant les données restaurées avec la source, avant de compter dessus pour un incident réel.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Installer BorgBackup :
```bash
sudo apt update
sudo apt install -y borgbackup
borg --version
```
👉 Explication : Installe le client qui crée et restaure les archives. La version affichée doit être notée dans la fiche serveur, car le format d'archive doit rester compatible avec celui qui a créé la sauvegarde.

2. Lister les archives disponibles :
```bash
export BORG_REPO=<chemin_du_depot_ou_ssh://utilisateur@hote/chemin>
borg list $BORG_REPO
```
👉 Explication : Affiche les archives du dépôt avec leur nom et date. La phrase de passe doit être fournie de façon interactive ou via `BORG_PASSCOMMAND` ; ne pas l'écrire dans le shell.

3. Vérifier l'intégrité du dépôt :
```bash
borg check $BORG_REPO
```
👉 Explication : Contrôle la cohérence des segments et des index. Une erreur ici invalide la sauvegarde avant même la restauration.

4. Restaurer une archive dans un répertoire isolé :
```bash
sudo install -d -m 700 /srv/restauration_test
cd /srv/restauration_test && sudo borg extract $BORG_REPO::<nom_archive> <chemin_a_restaurer>
```
👉 Explication : Extrait le chemin demandé dans `/srv/restauration_test`, sans écraser les données de production. Le `cd` est nécessaire car borg restaure relativement au répertoire courant.

## ⚡ 2. Production — Façon Simplifiée

1. Comparer les données restaurées avec la source :
```bash
sudo diff -r <chemin_source> /srv/restauration_test/<chemin_a_restaurer>
```
👉 Explication : Aucune sortie signifie des fichiers identiques. Les fichiers modifiés depuis la sauvegarde apparaissent ; les vérifier avant de conclure à une erreur de restauration.

2. Mesurer le temps de restauration réel :
```bash
time sudo borg extract $BORG_REPO::<nom_archive> <chemin_a_restaurer>
```
👉 Explication : Le temps mesuré dans un environnement isolé est la base du RTO (durée maximale d'interruption) à inscrire dans le plan de reprise.

## 🔒 3. Production — Façon Sécurisée

1. Restaurer en environnement isolé, sans réseau vers la production (VM de test ou réseau sans route) :
👉 Explication : Une restauration sur la machine de production peut écraser des données récentes et expose les données restaurées à des services actifs.

2. Vérifier la présence des fichiers de configuration critiques :
```bash
sudo ls -l /srv/restauration_test/<chemin_a_restaurer>/etc/
```
👉 Explication : Confirme que la sauvegarde contient les éléments nécessaires à reconstruire le service (configuration, certificats, clés), sans les exposer à d'autres utilisateurs (droits `700` du répertoire).

3. Supprimer les données restaurées après le test :
```bash
sudo rm -rf /srv/restauration_test
```
👉 Explication : Évite de laisser une copie de données sensibles sur un poste ou une VM de test. À faire seulement après validation, et uniquement sur le chemin de test.

## ✅ Validation et retour arrière

- **Précontrôles** : accès au dépôt et à la phrase de passe, espace disque libre au moins égal à la taille de l'archive, environnement de test isolé.
- **Validation** : `borg check` sans erreur ; `diff -r` sans écart inattendu ; temps de restauration consigné dans la fiche serveur.
- **Retour arrière** : aucune donnée de production n'est modifiée par ce test. En cas d'échec, relancer `borg check` et choisir une archive antérieure ; supprimer `/srv/restauration_test` une fois le test terminé.