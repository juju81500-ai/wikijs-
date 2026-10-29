---
title: "TP - RDS et RemoteApps"
description: "✅ RDS intégré au domaine nivvlem.tssr.eni"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP - RDS et RemoteApps  
## 🏗️ Pré-requis

✅ RDS intégré au domaine `nivvlem.tssr.eni`  
✅ Collection RDS existante (`RDS-Session-Collection`)  
✅ Groupes et utilisateurs existants :

| Groupe        | Membres                      |
|---------------|------------------------------|
| Direction     | Estelle, Baptiste            |
| Pédagogique   | Frédéric, Mathieu            |
| Informatique  | Benoît, VotrePrénom (Admin)  |

---

## ⚙️ Étapes de mise en œuvre
### 1️⃣ Préparation du serveur RDS

#### Installer Filezilla :

- Télécharger depuis `distrib`
- Copier sur `RDS`
- Installation par défaut

**Vérification** :

```
Menu Démarrer → Filezilla → Lancement OK
```

---

### 2️⃣ Publication d’applications RemoteApp

#### Publier les applications suivantes :

| Application         | Catégorie |
|---------------------|-----------|
| LibreOffice Calc    | Bureautique |
| LibreOffice Writer  | Bureautique |
| Filezilla           | Outils      |

#### Étapes :

1. Ouvrir **Gestionnaire de serveur** → **Remote Desktop Services**  
2. Aller dans **Collections** → `RDS-Session-Collection`  
3. Cliquer sur **Tâches** → **Publier RemoteApp programs**  
4. Sélectionner :  
    - `soffice.exe` → Writer  
    - `scalc.exe` → Calc  
    - `filezilla.exe` → Filezilla  
5. Organiser dans les dossiers :  
    - `Bureautique` → LibreOffice  
    - `Outils` → Filezilla  

---

### 3️⃣ Test du portail RDS Web Access

#### Accéder depuis `Cli10` :

URL → [https://rds.nivvlem.tssr.eni/RDweb](https://rds.nivvlem.tssr.eni/RDweb)

---

#### Tester accès :

| Utilisateur | Attendu |
|-------------|---------|
| Frédéric    | RemoteApps OK |
| Baptiste    | RemoteApps OK |
| Benoît      | RemoteApps OK |

---

#### Restriction d’accès :

##### À toutes les applications :

Autoriser uniquement :

```
Direction
Pédagogique
Informatique
```

##### À Filezilla :

Autoriser uniquement :

```
Informatique
```

**Test attendu** :

| Utilisateur | Applications visibles |
|-------------|-----------------------|
| Frédéric    | LibreOffice seulement |
| Baptiste    | LibreOffice seulement |
| Benoît      | LibreOffice + Filezilla |

---

### 4️⃣ Sécurisation avec certificat

#### Exporter le certificat :

Depuis `INFRA` → IE :

```
https://rds.nivvlem.tssr.eni/RDweb
```

- Cliquer sur **Erreur de certificat** → **Afficher les certificats**  
- **Exporter** en format `X509 Base 64 (.cer)`  
- Nommer : `RDS.cer`  

---

#### Déployer via GPO :

1. Ouvrir **GPMC** sur `INFRA`  
2. Créer une GPO : `Deploy-Certificats-Clients`  
3. Lier au domaine  
4. Éditer :

```
Configuration ordinateur → Stratégies → Paramètres Windows → Paramètres de sécurité → Stratégie de clé publique → Autorités de certification racines de confiance
```

5. Importer `RDS.cer`

---

#### Forcer l’actualisation GPO sur `Cli10` :

```powershell
gpupdate /force
```

#### Vérifier :

Revenir sur `https://rds.nivvlem.tssr.eni/RDweb` → **plus d’erreur de certificat**.

---

### 5️⃣ Déploiement des raccourcis RemoteApp

#### Pour Estelle :

Configurer :

```
Paramètre : Connexion RemoteApp et aux services Bureau à distance
URL : https://rds.nivvlem.tssr.eni/RDweb/feed/webfeed.aspx
```

#### Vérifier dans **Menu Démarrer** :

- **Applications accessibles** : LibreOffice Writer, LibreOffice Calc

---

#### Pour Benoît :

Même procédure.  
**Applications accessibles** : LibreOffice Writer, LibreOffice Calc, Filezilla.

---

### 6️⃣ Snapshot

Machines concernées :

| VM     | Action |
|--------|--------|
| INFRA  | Snapshot "Atelier 3 OK" |
| RDS    | Snapshot "Atelier 3 OK" |
| Cli10  | Snapshot "Atelier 3 OK" |

---

## 📌 Bonnes pratiques

✅ Toujours **organiser les RemoteApp** en dossiers clairs  
✅ Restreindre l’accès → **principe de moindre privilège**  
✅ Toujours **déployer le certificat** pour éviter les erreurs HTTPS  
✅ **Documenter les flux RemoteApp** (important en prod !)  
✅ Valider **l’expérience utilisateur** (menu Démarrer)

---

## ⚠️ Pièges à éviter

- Oublier d’exporter un certificat valide  
- Publier les apps sur la mauvaise collection  
- Mauvais droits sur Filezilla → utilisateurs non autorisés voient l’app  
- Oublier de forcer les GPO → toujours valider avec `gpupdate /force`  
- Oublier de faire un snapshot post-validation !