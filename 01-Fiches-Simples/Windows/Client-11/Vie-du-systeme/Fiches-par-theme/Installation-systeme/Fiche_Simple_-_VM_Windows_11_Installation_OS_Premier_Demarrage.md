# 📄 Fiche_Simple_-_VM_Windows_11_Installation_OS_Premier_Demarrage.md

- **Environnement** : VM ou poste client physique
- **OS / Version** : Windows 11 Pro ou Enterprise selon les besoins du domaine et de gestion
- **Catégorie** : Installation / Système
- **Tags** : `[windows-11]`, `[installation]`, `[oobe]`, `[uefi]`, `[tpm]`, `[premier-demarrage]`

## 🎯 Problème précis à résoudre
Installer Windows 11 sur un nouveau poste, vérifier l'édition et les prérequis matériels, puis préparer le premier démarrage avant l'inscription dans le domaine ou la gestion centralisée.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Utiliser un média d'installation officiel et vérifier l'édition, l'architecture et la compatibilité TPM 2.0/Secure Boot.
2. Créer la VM ou démarrer le poste sur le média; choisir la langue, le clavier et l'édition prévue par la licence.
3. Sélectionner uniquement le disque cible après vérification; effectuer l'installation UEFI et terminer l'OOBE selon le mode de gestion (compte local de lab ou inscription organisationnelle).
4. Après le premier démarrage, vérifier :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
   Get-Tpm
   Get-NetIPConfiguration
   Get-Service WinDefend, MpsSvc
   ```
   👉 *Explication : une VM peut ne pas présenter le TPM attendu tant que le vTPM n'a pas été configuré côté hyperviseur.*

**Équivalent interface graphique :**

- **Paramètres > Système > À propos** (édition, build), **Sécurité Windows > Sécurité des appareils > Processeur de sécurité** (TPM), **Paramètres > Réseau et Internet**.
  👉 Explication : équivalent graphique des commandes de contrôle après le premier démarrage.

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier l'édition/licence, le nom de l'appareil, l'affectation utilisateur et le scénario de gestion (AD DS, Entra ID ou poste autonome).
2. Installer pilotes et mises à jour depuis les sources approuvées; ne pas désactiver les exigences TPM/Secure Boot pour contourner une incompatibilité.
3. Configurer le compte de secours et les protections du poste, puis appliquer les fiches distinctes pour réseau, domaine, BitLocker, pare-feu et accès distant.
4. Redémarrer et vérifier l'état de la machine avant d'y transférer des données utilisateur.

## 🔒 3. Production — Façon Sécurisée
1. Ne pas inscrire des identifiants de production dans un script ou un fichier de réponse non protégé.
2. Activer BitLocker avec stockage vérifié de la clé de récupération et suivre la stratégie de l'organisation.
3. Garder Secure Boot et le pare-feu actifs; limiter les logiciels et droits administrateur local.

## ✅ Validation et retour arrière
- Confirmer édition, build, nom, réseau, mises à jour, TPM, Secure Boot, Defender et stratégie de gestion.
- Tester la récupération et l'accès de support; conserver une image de déploiement approuvée ou procédure de réinstallation.
- Si l'installation échoue, vérifier le média, l'édition et le disque cible avant de recommencer.