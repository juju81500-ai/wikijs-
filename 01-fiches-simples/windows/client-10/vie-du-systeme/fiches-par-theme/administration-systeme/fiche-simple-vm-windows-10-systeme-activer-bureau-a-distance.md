# 📄 VM_Win10_Systeme_Activer-Bureau-A-Distance-RDP.md

- **Environnement** : VM / Poste client (Windows 10)
- **OS / Version** : Windows 10 - Famille Windows Client
- **Catégorie** : Système / Accès Distant (RDP)
- **Tags** : `[windows-10]`, `[rdp]`, `[bureau-a-distance]`, `[gui]`, `[hardening]`

## 🎯 Problème précis à résoudre
Activer le service Bureau à distance (RDP) sur un poste client Windows 10, autoriser les connexions dans le pare-feu local et imposer l'authentification NLA (Network Level Authentication).


## 🖥️ Méthode Interface Graphique (GUI pas-à-pas)

### Vérifier l'édition et le périmètre
- Seules les éditions Windows 10 Pro, Enterprise et Education peuvent héberger des connexions RDP entrantes ; Windows Home peut servir de client RDP mais pas d'hôte.
- N'activer RDP que sur un réseau de confiance. Pour l'accès distant hors site, utiliser un VPN ou une passerelle RD Gateway approuvée ; ne pas publier directement RDP sur Internet.

### Activer RDP et limiter l'accès
1. Ouvrir **Paramètres** > **Système** > **Bureau à distance**.
2. Activer **Activer le Bureau à distance**, confirmer, puis vérifier que l'option NLA est activée/recommandée. Ne pas désactiver NLA pour contourner un problème de client sans validation.
3. Ouvrir **Sélectionner les utilisateurs pouvant accéder à distance à ce PC** et ajouter uniquement le groupe ou les comptes autorisés. Les membres du groupe Administrateurs disposent déjà du droit.
4. Ouvrir **Pare-feu Windows Defender avec fonctions avancées de sécurité** (`wf.msc`) > **Règles de trafic entrant**. Activer les règles Bureau à distance uniquement sur les profils **Domaine**/**Privé** attendus et limiter les **Adresses IP distantes** au réseau d'administration si possible. Ne pas activer le profil **Public** sans justification.
5. Depuis un poste autorisé, lancer `mstsc`, saisir le nom DNS du PC et vérifier la connexion. Confirmer depuis un poste hors périmètre que la connexion est refusée.

Référence : [Microsoft Learn — Activer le Bureau à distance](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remotepc/remote-desktop-allow-access).
---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Activation rapide du service Bureau à distance dans le registre Windows :
   `Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0`
   👉 Explication : Autorise les connexions RDP entrantes sur le système local.
2. Ouverture globale du port RDP dans le pare-feu local :
   `Enable-NetFirewallRule -DisplayGroup "Bureau à distance"`
   👉 Explication : Active les règles de pare-feu prédéfinies pour le trafic RDP.

---

## ⚡ 2. Production — Façon Simplifiée
1. Activation du RDP et bascule du service en démarrage automatique :
   `Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0`
   `Set-Service -Name "TermService" -StartupType Automatic -Status Running`
   👉 Explication : S'assure que le service de bureau à distance reste actif au démarrage.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Imposition stricte de l'authentification NLA (Network Level Authentication) :
   `Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name "UserAuthentication" -Value 1`
   👉 Explication : Exige que l'utilisateur s'authentifie avant d'établir la session graphique RDP.