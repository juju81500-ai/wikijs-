# 📄 VM_WinSrv_2022_ADDS_Joindre-Ou-Sortir-Domaine.md

- **Environnement** : VM / Serveur Physique
- **OS / Version** : Windows Server 2022 / Windows 11 / Windows 10
- **Catégorie** : Active Directory / Domaine

---

## 🎯 Problème précis à résoudre
Joindre un serveur Windows Server ou un poste de travail à un domaine Active Directory (`lab.local`), ou en sortir proprement pour revenir en groupe de travail (Workgroup).

---

## 🖥️ Méthode Interface Graphique (GUI Pas-à-Pas - "Clic-Clic")
### Avant la jonction
1. Vérifier que l'édition de Windows prend en charge la jonction à un domaine (Windows Pro/Enterprise ou Windows Server).
2. Dans les propriétés IPv4 de la carte réseau (`ncpa.cpl`), configurer comme DNS uniquement le ou les DNS internes Active Directory. Un DNS public en secondaire peut empêcher la découverte du contrôleur de domaine.
3. Vérifier que l'horloge est synchronisée et que le nom de l'ordinateur est conforme à la convention de nommage.

1. **Ouvrir les Propriétés Système** :
   - Appuyer sur les touches `Win + R` du clavier.
   - Saisir `sysdm.cpl` puis appuyer sur `Entrée`.
   - 👉 *Explication : Ouvre directement la fenêtre classique des Propriétés système.*

2. **Modifier l'appartenance au domaine** :
   - Dans l'onglet *Nom de l'ordinateur*, cliquer sur le bouton **Modifier...** en bas à droite.
   - En haut, dans le champ *Nom de l'ordinateur*, vérifier/saisir le nom d'hôte de la machine (ex: `SRV-APP-01`).
   - En bas, dans la section *Membre de*, cocher l'option **Domaine :**.
   - Saisir le nom FQDN du domaine Active Directory (ex: `lab.local`).
   - Cliquer sur **OK**.
   - 👉 *Explication : Lance la tentative de jonction au domaine AD via le réseau.*

3. **Authentification de l'administrateur du domaine** :
   - Une fenêtre d'invite de sécurité s'affiche : saisir l'identifiant d'un compte autorisé (ex: `LAB\Administrateur` ou `adm-jdupont`) et son mot de passe.
   - Cliquer sur **OK**.
   - Un message "Bienvenue dans le domaine lab.local" s'affiche : cliquer sur **OK**.
   - 👉 *Explication : Crée l'objet compte d'ordinateur dans l'Active Directory et valide la confiance.*

4. **Redémarrer la machine** :
   - Cliquer sur **Fermer** puis accepter le redémarrage immédiat en cliquant sur **Redémarrer maintenant**.
   - 👉 *Explication : Applique l'appartenance au domaine au démarrage du système.*

---

## 🧪 1. Hors-Production (Lab / Test / POC)
### Sortir du domaine en GUI
1. Ouvrir `sysdm.cpl`, onglet **Nom de l'ordinateur**, puis cliquer sur **Modifier...**.
2. Dans **Membre de**, sélectionner **Groupe de travail**, saisir `WORKGROUP`, puis cliquer sur **OK**.
3. Fournir un compte autorisé à quitter le domaine si demandé, valider les messages, puis redémarrer.
4. Avant l'opération, vérifier qu'un compte administrateur local connu et son mot de passe fonctionnent. Après le redémarrage, utiliser `.
om_utilisateur` pour ouvrir une session locale; l'accès et les stratégies du domaine ne seront plus disponibles.

1. **Jonction rapide au domaine en une ligne PowerShell** :
   ```powershell
   Add-Computer -DomainName "lab.local" -Credential (Get-Credential) -Restart
   ```
   👉 *Explication : Tu fais ça, une boîte de dialogue te demande l'identifiant admin AD, puis la machine rejoint le domaine et redémarre.*

---

## ⚡ 2. Production — Façon Simplifiée
1. **Jonction contrôlée avec spécification de l'Unité d'Organisation (OU) cible** :
   ```powershell
   Add-Computer -DomainName "lab.local" -OUPath "OU=TSSR_Serveurs,DC=lab,DC=local" -Credential (Get-Credential) -Restart -Force
   ```
   👉 *Explication : Tu places immédiatement la machine dans l'OU réservée aux serveurs pour lui appliquer directement les bonnes GPO dès le premier boot.*

2. **Sortie d'un domaine pour revenir en Workgroup (si nécessaire)** :
   ```powershell
   Remove-Computer -UnjoinDomaincredential (Get-Credential) -WorkgroupName "WORKGROUP" -Restart -Force
   ```
   👉 *Explication : Tu détaches proprement la machine du domaine AD et la remets en groupe de travail local.*

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. **Vérification préalable de la résolution DNS du domaine** :
   ```powershell
   Test-NetConnection -ComputerName "lab.local" -Port 53
   ```
   👉 *Explication : Tu vérifies que le serveur DNS AD réponds parfaitement sur le port 53 avant de lancer la procédure.*

2. **Jonction sécurisée avec chiffrement fort des canaux d'ouverture de session (Secure Channel)** :
   ```powershell
   Test-ComputerSecureChannel -Repair -Credential (Get-Credential)
   ```
   👉 *Explication : Tu revalides et répares la relation d'approbation entre l'ordinateur et le Contrôleur de Domaine.*