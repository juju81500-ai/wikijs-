# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_09_Identite_De_La_Machine

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 09 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2025`, `vie-du-systeme`, `cycle-de-vie`, `etape-09`

---

## Problème précis à résoudre

Nommer le serveur selon la convention.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Gestionnaire de serveur > Serveur local > Nom de l'ordinateur** ou **Paramètres > Système > À propos de > Renommer ce PC**.
   ```powershell
   Rename-Computer -NewName NOM_SERVEUR -Restart
   ```
   👉 Explication : `NOM_SERVEUR` respecte la convention (15 caractères maximum, lettres, chiffres, tiret); le redémarrage applique le nom.

2. Définir le suffixe DNS principal si le serveur n'est pas encore dans un domaine (**Nom de l'ordinateur > Modifier > Autres > Suffixe DNS principal**) :
   ```powershell
   Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters' -Name 'NV Domain' -Value 'EXEMPLE.LOCAL'
   Set-DnsClientGlobalSetting -SuffixSearchList @('EXEMPLE.LOCAL')
   ```
   👉 Explication : `EXEMPLE.LOCAL` est le domaine DNS interne à adapter.

3. Vérifier le nom :
   ```powershell
   hostname
   [System.Net.Dns]::GetHostByName($env:COMPUTERNAME).HostName
   ```
   👉 Explication : affiche le nom court puis le nom complet (FQDN).

## 2. Production — Contrôles

Enregistrer le nom dans le DNS et la CMDB avant la mise en service.

## 3. Production — Sécurité

Ne pas révéler le rôle ou la sensibilité de la machine dans son nom.

## Validation et retour arrière

- **Validation** : `hostname` renvoie le nom attendu après redémarrage.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2025](./Sommaire_-_Vie_du_systeme_Windows_Server_2025.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
