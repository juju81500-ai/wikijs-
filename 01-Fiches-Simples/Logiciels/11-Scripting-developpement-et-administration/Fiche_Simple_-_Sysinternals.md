# 📄 Sysinternals

- **Environnement** : VM ou poste Windows 11 de test (compte standard, élévation uniquement si requise)
- **OS / Version** : Windows 11 x64 - Sysinternals Suite (Autoruns, Process Explorer ; version à relever dans les propriétés des binaires, à vérifier sur la version déployée)
- **Catégorie** : Scripting, développement et administration
- **Tags** : `[windows-11]`, `[sysinternals]`, `[autoruns]`, `[process-explorer]`, `[audit]`, `[diagnostic]`, `[securite]`

## 🎯 Problème précis à résoudre
Auditer localement un poste Windows 11 à l'aide des outils Microsoft Sysinternals signés : lister les éléments de démarrage automatique (Autoruns) et examiner les processus en cours (Process Explorer), afin de repérer des éléments inattendus. Ce parcours est uniquement un audit en lecture seule ; il ne contient aucune procédure offensive. Toute suppression d'entrée de démarrage relève d'une remédiation distincte, tracée dans un ticket.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Création d'un dossier de travail dédié :
   ```powershell
   New-Item -ItemType Directory -Path "C:\Audit\Sysinternals" -Force
   ```
   👉 Explication : Sépare les outils et les rapports d'audit du reste du poste.

2. Téléchargement de la suite officielle depuis le site Microsoft Sysinternals :
   ```powershell
   Invoke-WebRequest -Uri "https://download.sysinternals.com/files/SysinternalsSuite.zip" -OutFile "C:\Audit\SysinternalsSuite.zip"
   ```
   👉 Explication : Télécharge l'archive complète. Le partage `live.sysinternals.com` n'est pas utilisé : il exécute directement des binaires distants, ce qui est déconseillé en production. Adresse à vérifier sur la version déployée.

3. Extraction de la suite :
   ```powershell
   Expand-Archive -Path "C:\Audit\SysinternalsSuite.zip" -DestinationPath "C:\Audit\Sysinternals" -Force
   ```
   👉 Explication : Décompresse les outils dans le dossier de travail.

4. Ouverture d'Autoruns en interface graphique :
   ```powershell
   Start-Process -FilePath "C:\Audit\Sysinternals\Autoruns64.exe"
   ```
   👉 Explication : Ouvre Autoruns pour une première exploration. Accepter la licence au premier lancement, puis ne rien désactiver ni supprimer pendant l'audit.

---

## ⚡ 2. Production — Façon Simplifiée
1. Vérification de la signature des binaires utilisés :
   ```powershell
   Get-AuthenticodeSignature -FilePath "C:\Audit\Sysinternals\Autoruns64.exe", "C:\Audit\Sysinternals\procexp64.exe" | Select-Object Path, Status
   ```
   👉 Explication : `Status` doit valoir `Valid` pour chaque fichier. Le signataire doit être Microsoft ; un binaire non valide n'est pas utilisé.

2. Audit de démarrage automatique en ligne de commande (lecture seule) :
   ```powershell
   & "C:\Audit\Sysinternals\autorunsc64.exe" -accepteula -a * -c -s -h -nobanner | Out-File -Encoding utf8 "C:\Audit\autoruns-$(Get-Date -Format yyyyMMdd-HHmm).csv"
   ```
   👉 Explication : `-a *` couvre toutes les catégories de démarrage, `-c` produit un CSV, `-s` vérifie les signatures et `-h` ajoute les empreintes des fichiers. Le rapport est horodaté. Options à vérifier sur la version déployée.

3. Examen des processus avec Process Explorer :
   ```powershell
   Start-Process -FilePath "C:\Audit\Sysinternals\procexp64.exe"
   ```
   👉 Explication : Dans **Options** > **Verify Image Signatures**, activer la vérification. Repérer les processus non signés, les chemins inattendus et les processus parents suspects. Ne pas terminer de processus pendant l'audit.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Empreinte du rapport d'audit pour garantir son intégrité :
   ```powershell
   Get-ChildItem -Path "C:\Audit" -Filter "autoruns-*.csv" | Get-FileHash -Algorithm SHA256
   ```
   👉 Explication : Calcule le SHA-256 de chaque rapport. Conserver la valeur avec le rapport pour prouver qu'il n'a pas été modifié.

2. Restriction d'accès au dossier d'audit (les rapports listent les chemins et les éditeurs du poste) :
   ```powershell
   icacls "C:\Audit" /inheritance:r /grant:r "$env:USERNAME:(OI)(CI)F" "Administrateurs:(OI)(CI)F"
   ```
   👉 Explication : Supprime l'héritage des droits et n'autorise que l'utilisateur courant et le groupe Administrateurs. Le nom du groupe est localisé : à vérifier sur la version déployée (Windows en anglais : `Administrators`).

3. Comparaison avec un audit de référence, à réaliser entre deux rapports horodatés :
   ```powershell
   Compare-Object -ReferenceObject (Get-Content "C:\Audit\<rapport_reference>.csv") -DifferenceObject (Get-Content "C:\Audit\<rapport_recent>.csv")
   ```
   👉 Explication : `<rapport_reference>` est le rapport d'audit validé précédemment, `<rapport_recent>` le dernier rapport. Les lignes affichées sont à analyser avec le référent sécurité ; une différence n'est pas automatiquement une compromission.
