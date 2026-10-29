# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_39_Chiffrement_Des_Flux_Et

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 39 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Déployer le certificat de l'autorité interne et vérifier TLS.

## 1. Hors-Production (Lab / Test / POC)

1. Importer l'autorité de certification racine interne : **certlm.msc > Autorités de certification racines de confiance > Certificats > Toutes les tâches > Importer**.
   ```powershell
   Import-Certificate -FilePath 'C:\Certs\AC_RACINE.cer' -CertStoreLocation Cert:\LocalMachine\Root
   ```
   👉 Explication : ajoute la racine au magasin machine (`AC_RACINE.cer` fourni par la PKI de l'entreprise).

2. Lister et contrôler les certificats : **certlm.msc > Personnel**.
   ```powershell
   Get-ChildItem Cert:\LocalMachine\My | Select-Object Subject,Thumbprint,NotAfter
   Get-ChildItem Cert:\LocalMachine\Root | Where-Object NotAfter -lt (Get-Date).AddDays(60)
   ```
   👉 Explication : affiche les certificats et ceux qui expirent dans moins de 60 jours.

3. Demander un certificat machine à l'autorité interne (inscription automatique par GPO recommandée).
   ```powershell
   Get-Certificate -Template 'Machine' -CertStoreLocation Cert:\LocalMachine\My
   ```
   👉 Explication : demande un certificat à l'autorité de l'annuaire.

4. Tester une connexion TLS et la chaîne de certificats.
   ```powershell
   Test-NetConnection NOM_SERVEUR.DOMAINE.LOCAL -Port 443
   certutil -verify -urlfetch "C:\Certs\SERVEUR.cer"
   ```
   👉 Explication : valide le port et la chaîne de confiance.

## 2. Production — Contrôles

Certificats émis par la PKI de l'entreprise, avec alerte avant expiration.

## 3. Production — Sécurité

Ne jamais importer de racine inconnue; protéger les clés privées (non exportables).

## Validation et retour arrière

- **Validation** : La chaîne est valide et aucune alerte de certificat n'apparaît.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 10](/01-fiches-simples/windows/client-10/vie-du-systeme/sommaire-vie-du-systeme-windows-10)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)