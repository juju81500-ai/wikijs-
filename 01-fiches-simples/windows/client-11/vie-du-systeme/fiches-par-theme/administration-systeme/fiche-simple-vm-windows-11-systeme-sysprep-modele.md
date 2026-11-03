# 📄 Fiche_Simple_-_VM_Windows_11_Systeme_Sysprep_Modele

- **Environnement** : VM (Windows 11, poste modèle destiné au clonage)
- **OS / Version** : Windows 11 - Famille Windows Client
- **Catégorie** : Système & Services / Images et modèles
- **Tags** : `[windows-11]`, `[sysprep]`, `[template]`, `[appx]`, `[dism]`, `[powershell]`

## 🎯 Problème précis à résoudre
Préparer un poste Windows 11 modèle, supprimer les applications Store qui bloquent Sysprep, puis généraliser la machine pour qu'elle puisse être clonée sans conflit de SID ni de nom.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lister les paquets Appx installés pour repérer ceux qui bloquent Sysprep :
   ```powershell
   Get-AppxPackage -AllUsers | Select-Object Name, PackageFullName | Sort-Object Name
   ```
   👉 Explication : Les applications Store installées pour un utilisateur sans être provisionnées peuvent faire échouer la généralisation. Les noter avant la capture.
2. Nettoyer les composants et fichiers temporaires :
   ```powershell
   Dism.exe /Online /Cleanup-Image /StartComponentCleanup
   Remove-Item -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue
   ```
   👉 Explication : Réduit la taille de l'image modèle et retire les fichiers temporaires de la session en cours.

**Équivalent interface graphique :**

- **Paramètres > Applications > Applications installées** pour repérer les applications Store.
  👉 Explication : équivalent visuel de `Get-AppxPackage`.
- Lancer **Win + R** > `C:\Windows\System32\Sysprep\sysprep.exe`, cocher **Generalize**, **Enter System Out-of-Box Experience (OOBE)**, arrêt : **Shutdown**, puis **OK**.
  👉 Explication : généralise l'image; ne le faire que sur la VM modèle, après snapshot.

## ⚡ 2. Production — Façon Simplifiée
1. Retirer les paquets provisionnés non souhaités dans l'image :
   ```powershell
   Get-AppxProvisionedPackage -Online | Select-Object DisplayName, PackageName
   Remove-AppxProvisionedPackage -Online -PackageName "<nom_du_paquet_provisionne>"
   ```
   👉 Explication : Le premier appel liste les paquets provisionnés (copiés pour chaque nouvel utilisateur). Le second retire celui indiqué, à remplacer par le nom exact du paquet.
2. Lancer Sysprep en généralisation, avec arrêt de la machine :
   ```powershell
   Start-Process -FilePath "C:\Windows\System32\Sysprep\sysprep.exe" -ArgumentList "/generalize /oobe /shutdown" -Wait
   ```
   👉 Explication : Supprime le SID et les données propres au poste, relance l'expérience de premier démarrage et éteint la machine. Ne pas redémarrer ensuite le modèle.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérifier le journal de Sysprep après un essai sur une copie du modèle :
   ```powershell
   Get-Content -Path "C:\Windows\System32\Sysprep\Panther\setupact.log" -Tail 30
   ```
   👉 Explication : Le fichier `setupact.log` donne la cause précise d'un échec (paquet Appx, fichier de réponses, pilote). Corriger sur une copie, jamais sur le modèle de référence.
2. Calculer l'empreinte de l'image modèle avant diffusion :
   ```powershell
   Get-FileHash -Algorithm SHA256 -Path "<chemin_image_modele>"
   ```
   👉 Explication : Permet de vérifier l'intégrité du modèle avant de le copier sur d'autres hyperviseurs ou postes de test.
3. Consigner la version du modèle dans la documentation :
   ```powershell
   Get-ComputerInfo -Property WindowsProductName, WindowsVersion, OsBuildNumber
   ```
   👉 Explication : Note l'édition, la version et le build du modèle. Cette trace sert au suivi des mises à jour et aux audits de conformité.
