---
title: "TP - WDS + MDT"
description: "✅ DEPLOY intégré au domaine nivvlem.tssr.eni"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP - WDS + MDT  
## 🏗️ Pré-requis

✅ `DEPLOY` intégré au domaine `nivvlem.tssr.eni`  
✅ Image ISO Windows 10 disponible  
✅ VM `CliNvx` prête (snapshot "Atelier 1 OK")  

---

## ⚙️ Étapes de mise en œuvre
### 1️⃣ Installation des outils de déploiement

#### Sur `DEPLOY` :

- Installer **VMware Tools** si besoin  
- Copier les sources d’installation de **ADK**, **WinPE**, **MDT** depuis `distrib`  
- Installer dans l’ordre :
    1. **ADK**
    2. **ADK WinPE**
    3. **MDT**

---

### 2️⃣ Configuration minimale MDT

#### Créer le compte de service dans AD :

```powershell
New-ADUser -Name "svc-mdt" -SamAccountName "svc-mdt" -AccountPassword (ConvertTo-SecureString "P@ssw0rd!" -AsPlainText -Force) -PasswordNeverExpires $true -CannotChangePassword $true -Enabled $true
```

#### Créer le dossier MDT :

- `F:\MDT`

#### Créer le **partage de déploiement** :

- Utiliser la console MDT  
- Nouveau partage → `F:\MDT`  
- Objectif : déploiement **totalement automatisé**  

#### Créer une **séquence de tâches** :

| Paramètre           | Valeur |
|---------------------|--------|
| Identifiant         | 13 (numéro de stagiaire) |
| Nom                 | DEP-W10-PRON |
| Modèle              | Client Standard |
| Système cible       | Windows 10 Pro N |

##### Compléter la séquence à votre convenance.

---

#### Mettre à jour le partage MDT :

- Forcer la prise en compte des modifications.

#### Droits d’accès sur F:\MDT :

| Groupe                  | Droit |
|-------------------------|-------|
| Utilisateurs authentifiés | Contrôle Total |

---

### 3️⃣ Mise à jour de l’image de boot WDS

- Ouvrir **console WDS**  
- Remplacer l’image de démarrage existante par **celle générée par MDT** :

```plaintext
\DEPLOY\MDTDeploymentShare\Boot\LiteTouchPE_x64.wim
```

---

### 4️⃣ Test de déploiement client

#### Avant le test :

```plaintext
Réappliquer le snapshot "Atelier 1 OK" sur `CliNvx`
```

#### Démarrer `CliNvx` en PXE → Lancer WinPE → écran MDT :

1. Modifier la disposition clavier si besoin  
2. Lancer l’assistant de déploiement :
    - S’authentifier avec le compte `svc-mdt`
    - Accepter les valeurs par défaut
    - Lancer le déploiement

#### Vérifier :

- Le déploiement arrive **sans erreur** à son terme.

---

### 5️⃣ Automatisation complète (Bootstrap.ini / CustomSettings.ini)

#### Modifier **Bootstrap.ini** :

- Renseigner les informations d’authentification pour le partage MDT
- Masquer le message de bienvenue MDT

#### Questions posées → compléter **CustomSettings.ini** :

- Fournir les réponses automatiques aux questions restantes  
- Possibilité : poste en **workgroup** pour simplification

#### Vérifier :

- L’installation doit être **totalement automatisée**.

---

## 🚀 Pour aller plus loin

### Intégration au domaine AD

- Modifier **CustomSettings.ini** pour intégrer automatiquement le client au domaine `nivvlem.tssr.eni`.

### Déploiement automatisé d’une application

- Automatiser le déploiement de **Firefox (.msi)** disponible sur `distrib` :

Ajouter le package dans MDT → Applications → Nouvelle Application.

---

## 📌 Bonnes pratiques

✅ Toujours utiliser un **compte de service dédié** pour MDT  
✅ Garder **ADK / MDT** à jour (compatibilité Windows 11 !)  
✅ Utiliser **LiteTouchPE_x64.wim** générée par MDT pour éviter les erreurs  
✅ Automatiser au maximum → réduire les saisies manuelles  
✅ Tester chaque nouvelle version de séquence sur `CliNvx` vierge

---

## ⚠️ Pièges à éviter

- Oublier de mettre à jour l’image WDS → boot obsolète  
- Permissions incorrectes sur `F:\MDT` → blocage déploiement  
- Ne pas automatiser correctement Bootstrap.ini → saisie manuelle requise  
- Ne pas documenter les paramètres ajoutés dans **CustomSettings.ini**  
- Oublier de forcer les snapshots avant test → perte de la base de test