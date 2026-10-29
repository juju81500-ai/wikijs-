# Fiche_Simple_-_VM_Windows_11_PuTTY_Installer.md

- **Environnement** : Poste Windows 11 x64 d'administration
- **OS / Version** : Windows 11 x64; PuTTY 0.85 Stable
- **Catégorie** : client SSH / installation

---

## Problème précis à résoudre

Installer PuTTY avec le MSI vérifié.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer l'installation interactive :
   ```powershell
   Start-Process msiexec.exe -Wait -ArgumentList '/i', (Join-Path $download 'putty-64bit-0.85-installer.msi')
   ```
   👉 Explication : l'installateur place les composants par défaut; `$download` est le dossier de l'étape précédente.

2. Vérifier la version : **Help > About PuTTY** ou :
   ```powershell
   & "$env:ProgramFiles\PuTTY\putty.exe" -V
   ```
   👉 Explication : doit afficher 0.85.

3. Ne pas lancer PuTTY en administrateur pour une session ordinaire.
   👉 Explication : réduit le risque en cas de compromission.

## 2. Production — Contrôles

Déployer sur un poste pilote avant généralisation.

## 3. Production — Sécurité

- Pas d'exécution en tant qu'administrateur pour SSH.

## Validation et retour arrière

- **Validation** : PuTTY 0.85 est installé.
- **Retour arrière** : **Paramètres > Applications > Applications installées > PuTTY > Désinstaller**.

## Si le problème n'est pas résolu

- [PuTTY — page officielle](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
- [PuTTY — clés de signature](https://www.chiark.greenend.org.uk/~sgtatham/putty/keys.html)
- [Guide complet — 3. Installer l'application](/02-fiches-completes/windows/client-11/installation-deploiement/84-deploiement-putty-0-85-windows-11#3-installer-lapplication)