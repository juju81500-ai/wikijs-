---
title: "TP – Les pilotes et les imprimantes"
description: "driverquery /v /fo csv > pilotesdetail.csv"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Les pilotes et les imprimantes

## 🖥️ 1. Inventaire des pilotes sur Win10-MD

### 🔹 Génération de rapports CSV

```cmd
driverquery /v /fo csv > pilotes_detail.csv
driverquery /si /fo csv > pilotes_signature.csv
```

- Le fichier `pilotes_detail.csv` contient la liste détaillée des pilotes
- Le fichier `pilotes_signature.csv` contient des informations sur leur signature numérique
- Ces fichiers peuvent être ouverts dans Excel :
    - Sélectionner colonne A → Données → Convertir → Délimité → Virgule


### 🔹 Identification manuelle du VENDOR_ID et DEVICE_ID

```cmd
devmgmt.msc
```

- Déployer les **cartes graphiques**
- Clic droit sur _VMware SVGA 3D_ > Propriétés > Détails > ID de matériel
- Exemple : VENDOR_ID = `15AD`, DEVICE_ID = `0405`

> 🔎 Ces informations peuvent être vérifiées sur [https://www.pcilookup.com](https://www.pcilookup.com)

---

## 🖨️ 2. Gestion des imprimantes locales

### 🔹 Imprimantes installées par défaut

- `FAX`
- `Microsoft Print to PDF`
- `Microsoft XPS Document Writer`

> Ces imprimantes apparaissent dans :

```cmd
control printers
```

> Et également dans :

```cmd
devmgmt.msc → Files d’attente à l’impression
```

### 🔹 Configuration de Microsoft Print to PDF

- Clic droit > **Définir comme imprimante par défaut**
- Clic droit > **Propriétés de l’imprimante** > Préférences > Orientation : **Paysage**
- Imprimer une page de test (fichier PDF généré sur le Bureau)

---

## 🌐 3. Connexion à une imprimante réseau partagée

### 🔹 Depuis Win10-MD

- Ouvrir l’explorateur de fichiers :

```cmd
\\172.28.20.20\HP_LaserJet_Accueil_RDC_Bât2
```

- Authentifier avec un compte autorisé (ex : `adm` / `Pa$$w0rd`)
- Clic droit > **Connecter**
- Attendre l’installation automatique du pilote
- Vérifier dans :
    - `control printers`
    - `devmgmt.msc`

---

## 🧪 4. Informations via PowerShell sur Discovery

### 🔹 Commandes utiles

```powershell
Get-Printer -Name "HP LaserJet"
Get-Printer -Name "HP LaserJet" | Select Name, Shared, ShareName, PortName, Location, Priority
```

> Ces commandes permettent d’obtenir toutes les informations techniques de l’imprimante installée (partage, port, emplacement, etc.)

---

## ✅ Vérifications

|Élément|Validation|
|---|---|
|Fichiers `pilotes_detail.csv` et `pilotes_signature.csv` générés|Contiennent des données exploitables avec Excel|
|VENDOR_ID et DEVICE_ID identifiés|Ex : 15AD / 0405|
|Imprimante PDF par défaut|Impression test en orientation **paysage**|
|Connexion à imprimante HP via réseau|Accessible depuis `control printers`|
|Informations PowerShell complètes|`Get-Printer` retourne les bonnes propriétés|

---

## 📌 Bonnes pratiques professionnelles

|Pratique|Pourquoi ?|
|---|---|
|Sauvegarder les rapports pilotes|Pour analyse, audit ou diagnostic|
|Utiliser les outils PowerShell (`Get-Printer`)|Automatisable et plus précis que l’interface graphique|
|Toujours vérifier les propriétés du pilote|Pour assurer une compatibilité optimale avec les usages|
|Utiliser des noms UNC clairs pour les imprimantes|Facilite la connexion et la documentation|
|Vérifier les autorisations de partage|Évite les erreurs d’accès aux imprimantes partagées|