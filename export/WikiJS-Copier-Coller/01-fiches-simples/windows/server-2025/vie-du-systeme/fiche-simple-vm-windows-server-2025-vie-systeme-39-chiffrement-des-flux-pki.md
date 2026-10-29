# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_39_Chiffrement_Des_Flux_Pki

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 39 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Installer un certificat de serveur et activer HTTPS.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **certlm.msc > Personnel > Certificats > Toutes les tâches > Demander un nouveau certificat** (autorité interne AD CS) ou importer un certificat :
   ```powershell
   Get-ChildItem Cert:\LocalMachine\My | Select-Object Subject, NotAfter, Thumbprint
   ```
   👉 Explication : liste les certificats et leurs dates d'expiration.

2. Importer un certificat PFX (remplacer `FICHIER.pfx`) :
   ```powershell
   Import-PfxCertificate -FilePath C:\Certs\FICHIER.pfx -CertStoreLocation Cert:\LocalMachine\My -Password (Read-Host -AsSecureString 'Mot de passe PFX')
   ```
   👉 Explication : installe le certificat sans afficher le mot de passe.

3. Lier à un site IIS (**Gestionnaire IIS > Site > Liaisons > Ajouter https**) :
   ```powershell
   New-WebBinding -Name 'Default Web Site' -Protocol https -Port 443
   (Get-WebBinding -Name 'Default Web Site' -Protocol https).AddSslCertificate('EMPREINTE','My')
   ```
   👉 Explication : `EMPREINTE` est le thumbprint obtenu plus haut.

## 2. Production — Contrôles

Superviser les dates d'expiration et automatiser le renouvellement.

## 3. Production — Sécurité

Désactiver TLS 1.0/1.1 et protéger les clés privées (non exportables).

## Validation et retour arrière

- **Validation** : Le service répond en HTTPS avec un certificat valide.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2025](/01-fiches-simples/windows/server-2025/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2025)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)