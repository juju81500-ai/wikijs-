# Le partage de ressources

## 📁 Concepts de base

- Un **partage** permet de rendre accessible une ressource (fichier, dossier, imprimante) à d'autres machines du réseau.
- Il est nécessaire d’avoir des **droits administratifs** pour créer un partage.
- Les droits d’accès sont gérés à deux niveaux :
    - **Autorisations de partage** (Lecture, Modification, Contrôle total)
    - **Droits NTFS** (s’appliquent localement sur les fichiers)
- ⚠️ L’accès effectif est **le plus restrictif** des deux niveaux.

---

## 🛠️ Accès à un partage distant

### 🔹 Depuis l’explorateur Windows

- Accès ponctuel : `\\serveur\partage`
- Connexion permanente : clic droit > **Connecter un lecteur réseau**
- Lettre mappée (Z:, Y:, etc.), associée au profil utilisateur

### 🔹 En ligne de commande

```cmd
net use Z: \\SRV-FIC\Compta
```

### 🔹 En PowerShell

```powershell
New-SmbMapping -LocalPath 'R:' -RemotePath '\\SRV-FIC\Compta'
```

---

## 📤 3. Création d’un partage de fichiers

### 🔹 Via Explorateur Windows

- Clic droit sur dossier > Propriétés > Partage > Partage avancé
- Définir un nom de partage et gérer les permissions
- Éviter d'utiliser "Tout le monde" → préférer **Utilisateurs authentifiés**

### 🔹 Via `fsmgmt.msc`

- Console MMC "Dossiers partagés"
- Affiche les partages existants, les utilisateurs connectés, fichiers ouverts

### 🔹 En ligne de commande

```cmd
net share commun=D:\Partages\Docs /grant:"Utilisateurs authentifiés",FULL
```

### 🔹 En PowerShell

```powershell
New-SmbShare -Name "Docs" -Path "D:\Partages\Docs" -FullAccess "Authenticated Users"
```

---

## 🖥️ Accès à distance – Bureau à distance (RDP)

### 🔹 Conditions nécessaires

- Activer l’accès distant :
    - Panneau de configuration > Système > Paramètres système avancés > Utilisation à distance
- Autoriser uniquement les **administrateurs** ou ajouter des utilisateurs via l’onglet "Sélectionner les utilisateurs"
- Le pare-feu Windows ouvre automatiquement le port 3389
- Vérifier que l’emplacement réseau est en **Privé**

### 🔹 Connexion au poste distant

- Via l’outil **mstsc**

```cmd
mstsc /v:nom_du_poste
```

- Possibilité de **mapper des disques locaux**, **sauvegarder les options**, **gérer l’affichage**

### 🔹 Authentification

- Utilisation d’un **compte local** ou **de domaine** avec mot de passe
- **NLA (Network Level Authentication)** activée par défaut : augmente la sécurité

---

## ✅ À retenir pour les révisions

- Partage = mise à disposition d'une ressource à travers le réseau
- Deux niveaux de sécurité : **partage** et **NTFS**
- L’accès se fait via Explorateur, `net use`, ou PowerShell
- Préférer "Utilisateurs authentifiés" à "Tout le monde"
- `fsmgmt.msc` permet de **visualiser et gérer** les partages
- RDP nécessite une configuration côté serveur + pare-feu ouvert sur 3389

---

## 📌 Bonnes pratiques professionnelles

|Bonnes pratiques|Pourquoi ?|
|---|---|
|Ne pas partager à "Tout le monde"|Risque d’exposition non contrôlée|
|Toujours associer les droits aux **groupes**|Meilleure gestion dans un environnement pro|
|Éviter le partage simplifié|Peu précis et difficile à auditer|
|Nommer les partages de façon explicite|Ex : `DocsRH`, `ComptaShare`, `Public_Tech`|
|Vérifier régulièrement les utilisateurs actifs|Prévenir les fuites de données ou accès prolongés|