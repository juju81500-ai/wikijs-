# 📄 Fiche_Simple_-_VM_Windows_11_Systeme_Nom_Et_Fuseau

- **Environnement** : VM / Poste de travail (Windows 11)
- **OS / Version** : Windows 11 - Famille Windows Client
- **Catégorie** : Système & Services / Identité et configuration de base

## 🎯 Problème précis à résoudre
Donner à un poste Windows 11 un nom conforme à la convention de nommage (15 caractères maximum pour le nom NetBIOS), régler le fuseau horaire et vérifier que l'horloge suit ce fuseau.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Contrôler le nom actuel, le fuseau horaire et l'appartenance au domaine :
   ```powershell
   Get-ComputerInfo -Property CsName, CsDomain, TimeZone
   ```
   👉 Explication : Affiche sans modification le nom du poste, le domaine éventuel et le fuseau actif.
2. Appliquer le fuseau de Paris par son identifiant Windows :
   ```powershell
   Get-TimeZone -ListAvailable | Where-Object { $_.Id -like "*Romance*" }
   Set-TimeZone -Id "Romance Standard Time"
   ```
   👉 Explication : Windows utilise l'identifiant (et non « Europe/Paris ») ; Romance Standard Time couvre Paris, Bruxelles et Madrid.
3. Renommer le poste et redémarrer :
   ```powershell
   Rename-Computer -NewName "<nom_du_poste>" -Restart
   ```
   👉 Explication : Remplace le nom NetBIOS (15 caractères maximum, sans espaces) et redémarre. En GUI, le même changement se fait dans **Paramètres** > **Système** > **Informations système** > **Renommer ce PC**.

---

## ⚡ 2. Production — Façon Simplifiée
1. Renommer un poste membre du domaine avec un compte habilité :
   ```powershell
   Rename-Computer -NewName "<nom_du_poste>" -DomainCredential (Get-Credential "<nom_domaine>\<compte_admin>") -Restart
   ```
   👉 Explication : Demande les identifiants d'un compte autorisé à modifier l'objet ordinateur dans Active Directory. Mettre à jour l'inventaire et le DNS après le redémarrage.
2. Vérifier la synchronisation horaire après le changement de fuseau :
   ```powershell
   w32tm /query /status
   ```
   👉 Explication : Confirme la source de temps utilisée et l'écart d'horloge, nécessaires à l'authentification Kerberos du domaine.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérifier que le nom cible n'est pas déjà utilisé dans l'annuaire :
   ```powershell
   Get-ADComputer -Filter "Name -eq '<nom_du_poste>'" -Properties DNSHostName, Enabled | Select-Object Name, DNSHostName, Enabled
   ```
   👉 Explication : Évite un conflit d'objet ordinateur ou de nom DNS avant le renommage.
2. Garder l'horloge matérielle en heure locale, comportement attendu sur Windows (et non en UTC) :
   ```powershell
   Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\TimeZoneInformation" -Name "RealTimeIsUniversal" -Value 0 -Type DWord
   ```
   👉 Explication : Valeur 0 = horloge CMOS en heure locale. Une valeur 1 créerait un décalage avec les autres systèmes (double démarrage Linux notamment).
3. Vérifier le fuseau effectif et le réglage de l'horloge :
   ```powershell
   Get-TimeZone
   Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\TimeZoneInformation" -Name "RealTimeIsUniversal"
   ```
   👉 Explication : Contrôle le fuseau et la valeur enregistrée avant d'archiver la fiche du poste.