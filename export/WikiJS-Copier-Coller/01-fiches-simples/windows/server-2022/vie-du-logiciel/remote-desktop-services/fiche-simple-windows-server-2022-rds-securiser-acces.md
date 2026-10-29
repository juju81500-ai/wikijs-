# Fiche_Simple_-_Windows_Server_2022_RDS_Securiser_Acces

- **Environnement** : Hôte de session RDS Windows Server 2022
- **OS / Version** : Windows Server 2022 Desktop Experience
- **Catégorie** : Vie du logiciel / Sécurité RDS

---

## Problème précis à résoudre

Limiter l'exposition et les droits des connexions RDS, en privilégiant une passerelle et des certificats approuvés plutôt qu'un port RDP exposé.

## 1. Hors-Production (Lab / Test / POC)

1. Dans **Gestionnaire de serveur** > **Serveur local** > **Bureau à distance**, ouvrir **Propriétés système** > **Utilisation à distance** et activer l'accès uniquement sur un hôte pilote; conserver NLA.
   👉 Explication : Vérifie que l'accès distant est approuvé. La procédure existante d'activation RDP couvre le réglage général; cette fiche vise les contrôles RDS complémentaires.
2. Contrôler les règles entrantes, dont le nom varie selon la langue du système :
   ```powershell
   Get-NetFirewallRule -DisplayGroup 'Bureau à distance' -ErrorAction SilentlyContinue | Select-Object DisplayName, Enabled, Profile
   Get-NetFirewallRule -DisplayGroup 'Remote Desktop' -ErrorAction SilentlyContinue | Select-Object DisplayName, Enabled, Profile
   ```
   👉 Explication : Examine les règles actives plutôt que d'ouvrir globalement tous les profils.
3. Dans `wf.msc` > **Règles de trafic entrant** > règle RDP > **Propriétés** > **Étendue**, limiter les adresses distantes au réseau d'administration de lab.
   👉 Explication : Les adresses du réseau autorisé sont à remplacer par le sous-réseau de lab effectivement approuvé.

## 2. Production — Contrôles

- Utiliser RD Gateway/VPN approuvée; ne pas publier directement le port RDP sur Internet.
- Vérifier NLA, certificat TLS, stratégie de chiffrement, correctifs, groupes et journaux.
- Dans **Gestionnaire de serveur** > **Services Bureau à distance** > **Vue d'ensemble** > **Tâches** > **Modifier les propriétés de déploiement** > **Certificats**, affecter des certificats valides lorsque la topologie le requiert.

## 3. Production — Sécurité

- Changer le port RDP ne remplace pas le filtrage réseau; coordonner pare-feu, clients, supervision et retour arrière.
- Ne pas activer un groupe large, le profil Public, ou une règle sans scope validé.
- Contrôler les redirections de presse-papiers, disques et périphériques selon le besoin métier.

## Validation et retour arrière

- **Validation** : connexion pilote réussie par la passerelle ou le réseau autorisé, NLA obligatoire, échec hors périmètre, certificat sans avertissement.
- **Retour arrière** : conserver l'accès console; rétablir les règles et stratégies précédentes puis retester.

## Si le problème n'est pas résolu

- [Microsoft Learn — Sécurité RDS](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-security)
- [Microsoft Learn — Accès distant avec RD Gateway](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-plan-access-from-anywhere)
- [Installer et configurer RDS](/01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-installer-configurer)