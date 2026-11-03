# 📄 Fiche Simple : GPO Hardening & Baseline Sécurité Windows Server 2022

- **Environnement** : VM Windows Server 2022
- **OS / Version** : Windows Server 2022 Datacenter / Standard
- **Catégorie** : Active Directory / GPO Sécurité
- **Tags** : `winsrv2022`, `gpo`, `hardening`, `active-directory` 

---

## 🎯 Problème précis à résoudre
Déployer une baseline de sécurité par GPO Active Directory : désactiver LLMNR/NetBIOS, forcer le Pare-feu Windows et sécuriser Kerberos.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Création rapide d'une GPO de test en PowerShell :
   New-GPO -Name "GPO_Test_Baseline"
   👉 Explication : Instancie un nouvel objet de stratégie de groupe vierge.

---

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder la GPO et valider sa portée sur une OU de préproduction avant liaison :
   ```powershell
   Backup-GPO -Name "GPO_Test_Baseline" -Path "C:\GPO-Backup"
   Get-GPInheritance -Target "OU=Serveurs-Test,DC=lab,DC=local"
   ```
   👉 Explication : Vérifie l'héritage, les filtres de sécurité et l'OU visée avant tout déploiement large.
2. Lier la GPO uniquement à l'OU de test validée, puis contrôler le lien :
   `New-GPLink -Name "GPO_Test_Baseline" -Target "OU=Serveurs-Test,DC=lab,DC=local"`

---

## 🔒 3. Production — Façon Sécurisée (Hardening)
1. Désactivation du protocole empoisonnable LLMNR via Registre GPO :
   Set-GPRegistryValue -Name "GPO_Test_Baseline" -Key "HKLM\Software\Policies\Microsoft\Windows NT\DNSClient" -ValueName "EnableMulticast" -Type DWord -Value 0
   👉 Explication : Bloque la résolution de noms multicast LLMNR pour contrecarrer les attaques d'interception de hachages NTLM (Responder).
2. Sur un serveur pilote membre de l'OU, appliquer et vérifier le résultat :
   ```powershell
   gpupdate /target:computer /force
   gpresult /scope computer /r
   ```
   👉 Explication : Ne pas lancer le test sur tous les serveurs d'un coup ; vérifier les événements de stratégie et la connectivité d'administration avant généralisation.