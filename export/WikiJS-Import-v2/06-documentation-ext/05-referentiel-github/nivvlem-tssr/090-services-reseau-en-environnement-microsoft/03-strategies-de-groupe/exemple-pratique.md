---
title: "TP – Prise en main des stratégies de groupe (GPO)"
description: "- Lier à la racine du domaine nivvlem.local"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Prise en main des stratégies de groupe (GPO)

### 🔹 1. Pour tous les utilisateurs du domaine

#### 🧩 GPO : `GPO_Domaine_Utilisateurs`

- Lier à la racine du domaine `nivvlem.local`

**Paramètres utilisateur :**

- Désactiver EFS :
    - `Configuration ordinateur > Paramètres Windows > Paramètres de sécurité > Système de fichiers EFS > Interdire l’utilisation d’EFS`
- Désactiver le pare-feu :
    - `Configuration ordinateur > Paramètres Windows > Paramètres de sécurité > Pare-feu Windows Defender > Paramètres du profil domaine > État : désactivé`
- Proxy Internet Explorer (si IE encore utilisé) :
    - `Configuration utilisateur > Paramètres Windows > Maintenance d'Internet Explorer > Connexions > Paramètres de proxy`
    - Adresse : `172.28.10.248`, port : `8080`
- Politique de mot de passe :
    - `Configuration ordinateur > Paramètres Windows > Paramètres de sécurité > Stratégies de compte > Stratégie de mot de passe`
        - Longueur minimale : 5 caractères
        - Durée de vie max : 5 jours
        - Complexité : désactivée

---

### 🔹 2. Membres du service Commercial

#### 🧩 GPO : `GPO_Commercial_Prospects`

- Lier à l’OU `Commercial`

**Script de connexion** ou `Préférences > Paramètres Windows > Disques mappés` :

```powershell
New-PSDrive -Name P -PSProvider FileSystem -Root "\\W19-SRV1\Prospects" -Persist
```

- Monté automatiquement à l’ouverture de session

---

### 🔹 3. Membres du service Production

#### 🧩 GPO : `GPO_Imprimante_Production`

- Lier à l’OU `Production`

**Déploiement de l’imprimante partagée** :

- `Configuration utilisateur > Paramètres Windows > Imprimantes`
- Nom du partage : `\\W19-SRV1\M477`

---

### 🔹 4. Secrétaires

#### 🧩 GPO : `GPO_FondEcran_Secretaires`

- Lier à l’OU `Secretariat`

**Définir le fond d’écran** :

- `Configuration utilisateur > Modèles d’administration > Bureau > Active Desktop > Active Desktop Wallpaper`
- Chemin UNC ou local (ex : `\\W19-SRV1\Fond\entreprise.jpg`)

---

## 🔹 BONUS : GPO avancées

### 📂 Installation automatique d’un .msi (ex : Acrobat Reader)

- Créer une GPO liée à l’OU `Secretariat`
- `Configuration ordinateur > Paramètres logiciels > Installation de logiciels`
- Ajouter le .msi en accès UNC (ex : `\\W19-SRV1\Install\AcroRead.msi`)

### 📂 Redirection des Documents (sauf Informatique)

- Créer GPO + lien sur `monprenom.local`, appliquer **filtrage de sécurité** pour exclure groupe GG_Informatique
- `Configuration utilisateur > Paramètres Windows > Redirection de dossier`
    - Documents → `\\W19-SRV1\Profils\%USERNAME%`

### 📂 Heures de connexion

```powershell
Set-ADUser -Identity "isabelle" -LogonHours (New-TimeSpan -Start 9:00AM -End 6:00PM)
```

- Ou via l’interface graphique de l’AD dans les propriétés de compte

### 📂 Fermeture de session après 18h (intérimaires)

- Script de déconnexion + GPO liée à l’OU `Interim`

---

## 🧠 À retenir pour les révisions

- Chaque GPO est liée à une OU ou à l’ensemble du domaine
- Privilégier **une GPO par logique de gestion** (pas de surcharges inutiles)
- Utiliser les **préférences GPO** pour des montages de lecteurs, raccourcis, imprimantes
- Le **filtrage de sécurité** et les **WMI filters** permettent un ciblage avancé

---

## 📌 Bonnes pratiques professionnelles

|Pratique|Pourquoi ?|
|---|---|
|Nommer les GPO selon leur usage|Ex : `GPO_Production_Imprimantes` pour lisibilité|
|Grouper les paramètres similaires|Éviter de multiplier les GPO par OU inutilement|
|Tester chaque GPO avec un utilisateur dédié|Validation sans impacter la production|
|Filtrer les GPO avec les groupes AD|Ciblage fin sans recréer plusieurs OUs|
|Documenter chaque GPO et son objectif|Traçabilité, audit, simplification de maintenance|