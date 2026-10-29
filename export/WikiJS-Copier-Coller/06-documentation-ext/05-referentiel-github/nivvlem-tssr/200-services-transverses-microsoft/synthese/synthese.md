# Synthèse - Services Transverses Microsoft
## 🏗️ Architecture globale

|Service|Rôle|
|---|---|
|Active Directory + DNS + DHCP|Base de l’infrastructure|
|WDS|Déploiement de Windows par le réseau (PXE)|
|MDT|Automatisation avancée des déploiements|
|RDS|Publication de bureaux ou d’applications distants|

---

## 🛠️ Outils clés

|Outil|Usage|
|---|---|
|WDS|Déploiement PXE + gestion des images WIM|
|MDT|Séquences de tâches, déploiement automatisé|
|ADK|Génération de WinPE, SIM, outils de réponse|
|RSAT|Gestion des rôles à distance|
|GPO|Contrôle des postes clients + RDS|

---

## ⚙️ Déploiement de Windows (WDS + MDT)

### WDS

- PXE → boot réseau → WinPE → déploiement image WIM
- Modes BIOS Legacy + UEFI (Windows 11 → UEFI only)
- Gestion des images boot + install + capture

### MDT

- Gère **séquences de tâches** :
    - Partition / formatage
    - Installation OS
    - Drivers
    - Applications
    - Configuration post-install
- **Fichiers clés** : Bootstrap.ini, CustomSettings.ini, Unattend.xml
- Monitoring en temps réel

### Spécificités Windows 11

|Élément|Obligation|
|---|---|
|UEFI|Oui|
|GPT|Oui|
|Secure Boot|Oui|
|TPM 2.0|Oui|
|ADK Windows 11|Oui|
|MDT >= 8456|Oui|

### Commandes utiles

```powershell
# Vérifier TPM
Get-WmiObject -Namespace root\cimv2\security\microsofttpm -Class Win32_Tpm

# Vérifier Secure Boot
Confirm-SecureBootUEFI
```

---

## 🖥️ RDS - Remote Desktop Services

### Fonctionnement

```text
Client RDP → RD Gateway → RD Connection Broker → RD Session Host → Bureau ou RemoteApp
```

### Services clés

|Service|Rôle|
|---|---|
|RD Session Host|Héberge les sessions / apps|
|RD Gateway|Sécurise l’accès externe|
|RD Broker|Gestion des connexions / load balancing|
|RD Licensing|Gestion des CAL RDS|
|RD Web Access|Portail HTML5|

### Modes d’utilisation

- Bureau complet distant
- Publication d’applications spécifiques (RemoteApp)

### Commandes utiles

```powershell
# Installer rôle RD Session Host
Install-WindowsFeature -Name RDS-RD-Server -IncludeAllSubFeature -IncludeManagementTools
```

---

## 📌 Bonnes pratiques professionnelles

### WDS + MDT

- Garder les images **à jour** (patches, drivers)
- Toujours utiliser **ADK compatible** avec les OS déployés
- Séparer les séquences **Windows 10 / Windows 11**
- Restreindre l’accès au partage MDT
- Documenter les séquences de tâches
- Tester sur plusieurs modèles (UEFI, TPM 2.0...)

### RDS

- Ne jamais exposer directement le port RDP → passer par Gateway
- Utiliser des **GPO restrictives** pour sécuriser les environnements RDS
- Superviser la charge des Session Host
- Planifier une redondance (Broker HA, Gateway HA)

### Global

- Mettre en place une supervision (logs déploiement, monitoring RDS)
- Automatiser au maximum
- Documenter toutes les configurations (MDT, WDS, RDS)
- Préparer des **plans de retour arrière** (images, snapshots)

---

## ⚠️ Pièges à éviter

- Vouloir déployer Windows 11 en BIOS Legacy → échec garanti  
- Laisser le PXE ouvert sur tout le réseau (risque de boot non maîtrisé)  
- Ne pas maintenir ADK / MDT à jour → WinPE incompatible  
- Ne pas tester les séquences en condition réelle  
- Ne pas sécuriser l’accès RDS  
- Oublier de surveiller la consommation CAL RDS

---

## ✅ À retenir pour les révisions

- **WDS + MDT** est la solution standard pour déploiement automatisé en PME/ETI
- **Windows 11 impose UEFI + Secure Boot + TPM 2.0**
- **MDT** permet une personnalisation complète des déploiements
- **RDS** offre un accès distant sécurisé aux bureaux et applications
- Une bonne supervision + documentation = clé d’un déploiement maîtrisé