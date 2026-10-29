# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_30_Protection_Contre_Les_Tentatives

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 30 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Limiter les attaques par force brute en verrouillant les comptes.

## 1. Hors-Production (Lab / Test / POC)

1. Définir la politique de verrouillage : **Stratégie de sécurité locale (secpol.msc) > Stratégies de comptes > Stratégie de verrouillage du compte**.
   ```powershell
   net accounts /lockoutthreshold:5 /lockoutduration:15 /lockoutwindow:15
   net accounts
   ```
   👉 Explication : verrouille 15 minutes après 5 échecs.

2. Détecter les échecs : **Observateur d'événements > Journaux Windows > Sécurité**, événement 4625.
   ```powershell
   Get-WinEvent -FilterHashtable @{LogName='Security';Id=4625} -MaxEvents 20 | Select-Object TimeCreated,Message
   ```
   👉 Explication : liste les échecs d'authentification récents.

3. Activer l'audit des échecs de connexion.
   ```powershell
   auditpol /set /subcategory:"Ouverture de session" /success:enable /failure:enable
   auditpol /get /subcategory:"Ouverture de session"
   ```
   👉 Explication : enregistre succès et échecs (nom de la sous-catégorie en anglais : `Logon`).

4. Bloquer une adresse source abusive sur RDP/SSH.
   ```powershell
   New-NetFirewallRule -DisplayName 'Bloquer ADRESSE_SOURCE' -Direction Inbound -RemoteAddress ADRESSE_SOURCE -Action Block
   ```
   👉 Explication : ferme l'accès à l'adresse observée (`ADRESSE_SOURCE`).

## 2. Production — Contrôles

Alerte SIEM au-delà d'un seuil d'événements 4625; la politique de verrouillage vient de la GPO du domaine.

## 3. Production — Sécurité

Éviter un seuil trop bas qui permettrait un déni de service par verrouillage volontaire.

## Validation et retour arrière

- **Validation** : Le compte test se verrouille après 5 échecs.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 10](/01-fiches-simples/windows/client-10/vie-du-systeme/sommaire-vie-du-systeme-windows-10)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)