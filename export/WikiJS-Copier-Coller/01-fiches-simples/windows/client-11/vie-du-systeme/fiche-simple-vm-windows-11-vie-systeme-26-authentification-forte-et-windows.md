# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_26_Authentification_Forte_Et_Windows

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 26 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Remplacer le mot de passe seul par le code PIN, Windows Hello Entreprise ou une clé de sécurité.

## 1. Hors-Production (Lab / Test / POC)

1. Configurer Windows Hello : **Paramètres > Comptes > Options de connexion > PIN (Windows Hello) > Configurer**.
   ```powershell
   dsregcmd /status | Select-String 'NgcSet|WamDefaultSet|AzureAdPrt'
   ```
   👉 Explication : `NgcSet : YES` indique qu'un code PIN Hello est configuré.

2. Activer Windows Hello pour l'entreprise par stratégie : **Intune > Appareils > Inscription > Windows Hello Entreprise**, ou GPO **Configuration ordinateur > Modèles d'administration > Composants Windows > Windows Hello Entreprise**.
   ```powershell
   gpresult /r /scope computer | Select-String 'Hello'
   ```
   👉 Explication : vérifie que la stratégie est appliquée.

3. Enregistrer une clé de sécurité FIDO2 : **Paramètres > Comptes > Options de connexion > Clé de sécurité > Gérer**.
   👉 Explication : permet une authentification sans mot de passe résistante à l'hameçonnage.

4. Imposer l'authentification multifacteur sur le compte (stratégie d'accès conditionnel Entra ID).
   👉 Explication : décision de l'équipe identité; le poste n'a rien à configurer en plus.

## 2. Production — Contrôles

MFA obligatoire pour les comptes à privilèges et l'accès distant.

## 3. Production — Sécurité

Le code PIN reste local à l'appareil et protégé par le TPM; aucune biométrie n'est enregistrée sans consentement.

## Validation et retour arrière

- **Validation** : Connexion par PIN ou clé de sécurité réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 11](/01-fiches-simples/windows/client-11/vie-du-systeme/sommaire-vie-du-systeme-windows-11)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)