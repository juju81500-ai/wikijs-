# Fiche_Simple_-_VM_Windows_11_Postman_Prerequis_Limites

- **Environnement** : Poste Windows 11 géré, compte standard, Postman Desktop et Newman
- **OS / Version** : Windows 11 Client
- **Catégorie** : API / prérequis

---

## Problème précis à résoudre

Valider les prérequis et les limites de Postman Desktop et Newman sur un poste Windows 11 avant installation : compte, réseau, architecture, périmètre de test.

## 1. Hors-Production (Lab / Test / POC)

1. Relever la version de Windows et l'architecture :
   ```powershell
   Get-ComputerInfo | Select-Object OsName,OsVersion,OsArchitecture
   ```
   👉 Explication : Contrôle que le poste est un Windows 11 64 bits ; Postman publie des installeurs Windows 64 bits (vérifier la page de téléchargement officielle pour ARM64).

2. Vérifier l'accès réseau aux domaines Postman :
   ```powershell
   Test-NetConnection -ComputerName dl.pstmn.io -Port 443
   ```
   👉 Explication : Confirme que HTTPS vers le site de téléchargement n'est pas bloqué par le proxy ou le pare-feu ; `TcpTestSucceeded : True` attendu.

3. Vérifier la présence de winget (installation et mise à jour scriptées) :
   ```powershell
   winget --version
   ```
   👉 Explication : winget est fourni avec l'Installateur d'application ; s'il est absent, utiliser l'installeur téléchargé depuis le site officiel.

4. Définir le périmètre et les limites :
   ```text
   Fiche d'architecture > lister les API de test autorisées (URL_API_LAB) > noter qu'un compte Postman est requis pour la synchronisation cloud, le mode hors-ligne étant limité (à vérifier selon la version publiée).
   ```
   👉 Explication : Postman ne doit cibler que des API dont vous avez l'autorisation ; remplacer `URL_API_LAB` par l'URL de l'API de lab.

## 2. Production — Contrôles

Inventorier les postes concernés, la version cible, le besoin d'un compte Postman (licence/équipe), la politique d'accès au cloud Postman et la conformité RGPD des données envoyées dans les collections.

## 3. Production — Sécurité

- Ne tester que des API dont l'accès est autorisé par écrit.
- Ne jamais importer de données personnelles réelles dans un workspace synchronisé.
- Valider auprès de la sécurité si la synchronisation cloud est autorisée.

## Validation et retour arrière

- **Validation** : Prérequis relevés et validés, périmètre d'API de test écrit.
- **Retour arrière** : Aucun changement système à annuler à ce stade ; supprimer les paquets de test installés si le lot est abandonné.

## Si le problème n'est pas résolu

- [Postman — documentation officielle](https://learning.postman.com/docs/)
- [Postman — téléchargement](https://www.postman.com/downloads/)
- [Newman — documentation](https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/)
- [Fiche d'entrée Postman](/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-postman)
- [Fiche connexe Installer](</01-fiches-simples/windows/client-11/vie-du-logiciel/postman/fiche-simple-vm-windows-11-postman-installer>)