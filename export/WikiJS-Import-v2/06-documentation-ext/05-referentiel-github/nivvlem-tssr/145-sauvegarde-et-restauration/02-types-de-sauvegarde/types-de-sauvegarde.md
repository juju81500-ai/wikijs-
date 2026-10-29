---
title: "Types de sauvegarde"
description: "- Copie de tous les fichiers, qu’ils soient modifiés ou non"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Types de sauvegarde

## 🔁 Sauvegarde à chaud vs à froid

|Type|Avantages|Inconvénients|
|---|---|---|
|**À chaud**|Accessible immédiatement, sans interruption|Mise en œuvre complexe|
|**À froid**|Facile à restaurer, simple à configurer|Interruption des services nécessaire|

> La sauvegarde à chaud permet de sauvegarder en production, la sauvegarde à froid exige l’arrêt de l’application ou du système

---

## 🧠 Méthodes de sauvegarde

### Attributs utilisés

- **Bit d’archive (Microsoft)** : mis à 1 quand un fichier est modifié ; certaines sauvegardes le remettent à 0
- **Date de modification (Unix)** : comparaison avec la date de dernière sauvegarde

---

## 📦 Sauvegarde complète

- Copie **de tous les fichiers**, qu’ils soient modifiés ou non
- Ne se base pas sur les attributs
- **Modifie le bit d’archive** des fichiers

**Avantages** : restauration rapide, fiabilité élevée

**Inconvénients** : consomme beaucoup d’espace disque

---

## 🧩 Sauvegarde différentielle

- Copie **tous les fichiers modifiés depuis la dernière sauvegarde complète**
- Ne remet pas à zéro le bit d’archive
- Méthode cumulative

**Avantages** : rapide à restaurer, fiable

**Inconvénients** : devient volumineuse avec le temps

---

## 🔄 Sauvegarde incrémentale

- Copie **uniquement les fichiers modifiés depuis la dernière sauvegarde** (complète ou incrémentale)
- **Remet à zéro** le bit d’archive après la sauvegarde

**Avantages** : faible consommation espace, rapide à effectuer

**Inconvénients** : restauration plus complexe (besoin de toutes les sauvegardes intermédiaires)

---

## 🧮 Comparatif des méthodes

|Méthode|Données sauvegardées|Temps de sauvegarde|Temps de restauration|Espace disque|Points forts|Limites|
|---|---|---|---|---|---|---|
|Complète|Tous les fichiers|Lent|Rapide|Élevé|Fiabilité, simplicité|Stockage gourmand|
|Différentielle|Modifiés depuis la complète|Modéré|Rapide|Modéré|Facile à restaurer|Taille augmente avec le temps|
|Incrémentale|Modifiés depuis la dernière|Rapide|Long|Faible|Gain d’espace et de temps|Complexité de la restauration|

---

## 🔁 Rotation des supports – Stratégie GFS

**GFS = Grand-Père / Père / Fils**

|Période|Support|Recyclage|
|---|---|---|
|Quotidien|Fils|Tous les 4 jours|
|Hebdomadaire|Pères|Toutes les 5 semaines|
|Mensuel|Grands-pères|Tous les 12 mois|

> Une rotation GFS sur 5 jours nécessite **21 bandes par an**, sur 7 jours environ **23 bandes**

---

## 💾 Sauvegarde de bases de données

### Exemples

- **SQL Server** : via Management Studio
- **MySQL** : via `mysqldump`

```bash
mysqldump -u utilisateur -p mot_de_passe base > dump.sql
```

- **Oracle** : via `RMAN`, ex :

```bash
rman> backup incremental level 0 section size 512m database plus archivelog;
```

> Chaque moteur a ses propres méthodes et outils adaptés

---

## ♻️ Méthodes de restauration

### Types de restauration

- **Fichiers individuels** : sur emplacement d’origine ou ailleurs
- **Restauration système complète** : méthode **Bare Metal Recovery**
- **Restauration de base de données** : via fichier DUMP, outils spécifiques (SSMS, RMAN, etc.)

### Recommandations

- Toujours tester les restaurations (simulation)
- Éviter l’écrasement de fichiers existants
- Restaurer dans un environnement de test avant production

---

## ✅ À retenir pour les révisions

- La **sauvegarde complète** est la plus simple mais la plus lourde
- **Différentielle** : simple à restaurer, mais croît avec le temps
- **Incrémentale** : économe, mais restauration complexe
- La **stratégie GFS** est un standard professionnel pour la rotation des supports
- Chaque type de **base de données a son propre mécanisme** de sauvegarde/restauration

---

## 📌 Bonnes pratiques professionnelles

- Appliquer une stratégie **GFS ou similaire** pour rotation automatisée des supports
- Toujours **tester les restaurations** (au moins 1 fois/mois en production)
- Séparer les **volumes de sauvegarde** pour éviter la perte globale
- Documenter et tracer chaque job, test ou échec de restauration
- Créer des **scripts automatisés** pour dump/restauration des bases

---

## 🔗 Outils et commandes utiles

- `mysqldump`, `mysql`, SQL Server Management Studio (SSMS)
- `rman` pour Oracle
- Planification : GFS, calendrier de rotation
- Logiciels : Backup Exec, Veeam, scripts personnalisés