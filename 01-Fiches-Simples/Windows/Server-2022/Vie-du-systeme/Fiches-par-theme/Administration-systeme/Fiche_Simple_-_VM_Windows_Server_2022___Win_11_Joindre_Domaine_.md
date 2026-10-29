# 📄 VM_WinSrv_2022_ADDS_Joindre-Domaine.md

- **Environnement** : VM / Serveur client (Windows Server 2022 / Windows 10/11)
- **OS / Version** : Windows Server 2022 / Win 10-11 - Famille Windows
- **Catégorie** : Système & Annuaire / Active Directory
- **Tags** : `[windows-server]`, `[windows-11]`, `[active-directory]`, `[domain-join]`, `[gui]`, `[powershell]`

---

## 🎯 Problème précis à résoudre
Joindre un serveur ou un poste client à un domaine Active Directory (ex: `lab.local`) via l'interface graphique système (`sysdm.cpl`) ou en ligne de commande PowerShell.

---

## 🖥️ Méthode Interface Graphique (GUI Pas-à-Pas)

1. **Ouvrir les Propriétés Système** :
   - Appuyer sur les touches `Win + R` du clavier.
   - Taper `sysdm.cpl` puis appuyer sur `Entrée`.
   - 👉 *Explication : Cela ouvre la fenêtre classique "Propriétés système".*

2. **Accéder à la modification du nom et du domaine** :
   - Dans l'onglet *Nom de l'ordinateur*, cliquer sur le bouton **Modifier...** (en bas à droite).
   - 👉 *Explication : Ouvre la boîte de dialogue de changement de nom et d'affiliation au domaine.*

3. **Joindre le domaine Active Directory** :
   - Dans la section *Membre de*, cocher l'option **Domaine**.
   - Taper le nom FQDN du domaine (ex: `lab.local`).
   - Cliquer sur **OK**.

4. **Saisir les identifiants d'administration** :
   - Dans la fenêtre d'authentification qui apparaît, saisir les identifiants d'un compte autorisé à joindre les machines au domaine (ex: `LAB\\adm-jdupont` et son mot de passe).
   - Cliquer sur **OK**.
   - Un message s'affiche : *"Bienvenue dans le domaine lab.local"*.
   - Cliquer sur **OK**, puis redémarrer la machine lorsque le système le demande.

---

## ⚡ Méthode Ligne de commande PowerShell

1. **Vérifier au préalable la résolution DNS du domaine** :
   ```powershell
   Test-Connection -TargetName "lab.local" -Count 2
   ```
   👉 *Explication : Tu contrôles que la machine communique bien avec les contrôleurs de domaine DNS.*

2. **Lancer la jonction au domaine et redémarrer** :
   ```powershell
   Add-Computer -DomainName "lab.local" -Credential (Get-Credential) -Restart
   ```
   👉 *Explication : Tu déclenches la jonction au domaine en demandant les identifiants d'administration puis la machine redémarre seule.*