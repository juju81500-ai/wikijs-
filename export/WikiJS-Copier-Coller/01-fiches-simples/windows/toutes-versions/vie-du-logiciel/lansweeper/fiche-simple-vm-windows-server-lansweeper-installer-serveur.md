# Fiche_Simple_-_VM_Windows_Server_Lansweeper_Installer_Serveur.md

- **Environnement** : Serveur Windows x64 avec Lansweeper Classic (SQL LocalDB ou SQL Server selon l'échelle)
- **OS / Version** : Windows Server 2022 recommandé; Lansweeper Classic selon la matrice officielle
- **Catégorie** : inventaire de parc / découverte réseau

---

## Problème précis à résoudre

Installer Lansweeper Classic en Easy ou Advanced.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'installateur depuis le site officiel Lansweeper et vérifier l'origine du fichier.
   👉 Explication : évite un installateur altéré.

2. Lancer l'installateur : choisir **Easy Install** (petite installation) ou **Advanced Install** (scan, SQL Server et console séparés).
   👉 Explication : Advanced permet la séparation des composants.

3. En installation répartie, installer d'abord la base, puis les services de scan, puis la console.
   👉 Explication : respecte l'ordre officiel.

4. Partager la clé `Encryption.txt` avec les autres serveurs de scan via le coffre.
   👉 Explication : elle doit être identique partout; ne jamais la laisser dans un partage ouvert.

5. Appliquer la licence ou lier l'installation à la plateforme selon le type de licence.
   👉 Explication : active le produit.

6. Configurer le compte de connexion à la console et activer seulement les rôles nécessaires.
   👉 Explication : moindre privilège.

7. Vérifier le service :
   ```powershell
   Get-Service | Where-Object { $_.Name -like 'Lansweeper*' }
   ```
   👉 Explication : liste le service de scan Lansweeper (état attendu: Running).

## 2. Production — Contrôles

Documenter version, licence, composants et emplacement de la clé `Encryption.txt` dans le coffre.

## 3. Production — Sécurité

- Protéger `Encryption.txt` (clé de chiffrement des identifiants).

## Validation et retour arrière

- **Validation** : la console répond et le service de scan est en cours d'exécution.
- **Retour arrière** : désinstaller via **Paramètres > Applications > Lansweeper** après sauvegarde de la base et de la clé.

## Si le problème n'est pas résolu

- [Lansweeper Classic — installer on-premises](https://docs.lansweeper.com/classic/docs/install-lansweeper-on-prem.md)
- [Lansweeper Classic — prérequis](https://docs.lansweeper.com/classic/docs/lansweeper-installation-requirements.md)
- [Guide complet](/02-fiches-completes/windows/server-2022/installation-deploiement/44-deploiement-lansweeper-classic-windows-server#2-installer-le-serveur)