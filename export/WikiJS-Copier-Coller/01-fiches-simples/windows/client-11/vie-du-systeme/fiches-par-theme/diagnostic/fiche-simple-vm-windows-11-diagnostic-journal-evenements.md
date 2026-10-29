# 📄 Fiche_Simple_-_VM_Windows_11_Diagnostic_Journal_Evenements

- **Environnement** : VM / Poste de travail (Windows 11)
- **OS / Version** : Windows 11 - Famille Windows Client
- **Catégorie** : Système & Services / Diagnostic et journaux

## 🎯 Problème précis à résoudre
Diagnostiquer un poste Windows 11 qui présente des erreurs, des plantages d'applications ou des arrêts inattendus, en utilisant l'Observateur d'événements (interface graphique) puis PowerShell pour filtrer et exporter les événements.

---

## 🖥️ Méthode Interface Graphique (GUI)
1. Ouvrir l'**Observateur d'événements** (taper `eventvwr.msc` dans la recherche Windows).
2. Dans **Journaux Windows** > **Système**, cliquer sur **Filtrer le journal actuel...** et cocher les niveaux **Critique**, **Erreur** et **Avertissement**.
3. Pour conserver un filtre, utiliser **Action** > **Créer un affichage personnalisé**, puis choisir la période et les sources. L'affichage est enregistré dans **Affichages personnalisés**.
4. Pour l'export, clic droit sur le journal > **Enregistrer tous les événements sous...** (format `.evtx`).

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lister la taille et le nombre d'événements des journaux principaux :
   ```powershell
   Get-WinEvent -ListLog System, Application, Security | Select-Object LogName, RecordCount, MaximumSizeInBytes, IsEnabled
   ```
   👉 Explication : Montre si un journal approche de sa limite (et risque de perdre des événements).
2. Afficher les erreurs et avertissements des dernières 24 heures :
   ```powershell
   Get-WinEvent -FilterHashtable @{ LogName = 'System', 'Application'; Level = 1, 2, 3; StartTime = (Get-Date).AddHours(-24) } -MaxEvents 50 -ErrorAction SilentlyContinue | Select-Object TimeCreated, LogName, Id, LevelDisplayName, ProviderName, Message
   ```
   👉 Explication : Équivalent PowerShell du filtre GUI. `-ErrorAction SilentlyContinue` évite l'erreur lorsqu'aucun événement ne correspond.

---

## ⚡ 2. Production — Façon Simplifiée
1. Repérer les plantages d'applications (identifiants 1000 et 1001) :
   ```powershell
   Get-WinEvent -FilterHashtable @{ LogName = 'Application'; Id = 1000, 1001 } -MaxEvents 30 -ErrorAction SilentlyContinue | Select-Object TimeCreated, Id, ProviderName, Message
   ```
   👉 Explication : 1000 = erreur d'application (plantage), 1001 = rapport Windows Error Reporting associé. Le champ Message indique le module fautif.
2. Augmenter la taille maximale du journal Application à 100 Mo :
   ```powershell
   wevtutil sl Application /ms:104857600
   wevtutil gl Application
   ```
   👉 Explication : Limite la perte d'événements sur un poste très sollicité. La seconde commande confirme la nouvelle taille.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Exporter le journal Système avec son empreinte SHA256 :
   ```powershell
   New-Item -ItemType Directory -Path "C:\Diagnostic" -Force | Out-Null
   wevtutil epl System "C:\Diagnostic\System_poste.evtx"
   Get-FileHash -Algorithm SHA256 -Path "C:\Diagnostic\System_poste.evtx"
   ```
   👉 Explication : Conserve une copie intégrable au dossier d'incident. L'empreinte permet de démontrer l'absence de modification.
2. Relire l'export sur un poste d'analyse, sans toucher au journal du poste d'origine :
   ```powershell
   Get-WinEvent -Path "C:\Diagnostic\System_poste.evtx" -MaxEvents 100 | Select-Object TimeCreated, Id, LevelDisplayName, Message
   ```
   👉 Explication : Analyse l'export EVTX. Le journal source reste intact pour d'éventuelles investigations.