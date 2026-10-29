# 📄 Fiche_Simple_-_VM_Windows_11_Administration_Installer_OpenSSH_Cle.md

- **Environnement** : VM ou poste client Windows
- **OS / Version** : Windows 11 Pro / Enterprise
- **Catégorie** : Installation / Administration / Sécurité
- **Tags** : `[windows-11]`, `[openssh]`, `[ssh]`, `[cle-ed25519]`, `[powershell]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer OpenSSH Server sur Windows 11, autoriser l'administration par clé et limiter l'accès réseau avant de réduire l'authentification par mot de passe.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Dans **Paramètres > Système > Fonctionnalités facultatives > Afficher les fonctionnalités**, rechercher **Serveur OpenSSH** et installer.
2. Démarrer le service et le configurer au démarrage :
   ```powershell
   Start-Service sshd
   Set-Service -Name sshd -StartupType Automatic
   Get-Service sshd
   ```
3. Vérifier depuis un client autorisé que le port 22 répond, puis tester une connexion au compte Windows ciblé.
   👉 *Explication : l'installation crée généralement une règle pare-feu entrante; inspecter et restreindre cette règle avant d'exposer le serveur.*

## ⚡ 2. Production — Façon Simplifiée
1. Depuis le client, générer une clé si nécessaire et transférer la clé publique au compte Windows :
   ```bash
   ssh-keygen -t ed25519
   ssh-copy-id -i ~/.ssh/id_ed25519.pub <utilisateur>@<nom-ou-ip>
   ```
2. Tester une nouvelle session par clé avant de modifier `C:\ProgramData\ssh\sshd_config`.
3. Définir les paramètres voulus sans dupliquer les entrées, puis vérifier et redémarrer le service :
   ```text
   PubkeyAuthentication yes
   PasswordAuthentication no
   ```
   ```powershell
   & "$env:WINDIR\System32\OpenSSH\sshd.exe" -t
   Restart-Service sshd
   ```
   👉 *Explication : désactiver les mots de passe uniquement après avoir validé l'accès par clé dans une seconde session.*

## 🔒 3. Production — Façon Sécurisée
1. Restreindre la règle pare-feu `OpenSSH-Server-In-TCP` au profil et aux sources d'administration; vérifier qu'aucune autre règle large ne maintient l'exposition.
2. Protéger `authorized_keys` avec les ACL attendues et ne jamais copier la clé privée sur Windows.
3. Pour un compte membre du groupe Administrateurs, respecter le chemin et les ACL particuliers de `administrators_authorized_keys`; ne pas réutiliser les permissions d'un compte standard.
4. Garder la console locale ou hyperviseur et un compte de secours avant de fermer l'authentification par mot de passe.

## ✅ Validation et retour arrière
- Tester une nouvelle connexion par clé depuis le réseau autorisé, puis vérifier le service et la règle pare-feu.
- En cas d'échec, restaurer `sshd_config`, exécuter `sshd.exe -t` et redémarrer `sshd` depuis la console.
- Examiner les journaux OpenSSH dans l'Observateur d'événements et confirmer que le port n'est pas accessible depuis des sources non prévues.