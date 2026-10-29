# Fiche_Simple_-_VM_Debian_13_Postman_Prerequis_Limites

- **Environnement** : VM Debian 13 Trixie avec bureau graphique, Postman Desktop et Newman
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : API / prérequis

---

## Problème précis à résoudre

Valider les prérequis et limites de Postman Desktop et Newman sur Debian 13 avant installation : architecture, bibliothèques graphiques, compte, périmètre de test, compatibilité à vérifier.

## 1. Hors-Production (Lab / Test / POC)

1. Relever la version Debian et l'architecture :
   ```bash
   cat /etc/os-release | head -4
   dpkg --print-architecture
   ```
   👉 Explication : Contrôle Debian 13 ; l'archive Linux officielle de Postman cible x86_64 (`amd64`). Compatibilité arm64 à vérifier sur le site officiel.

2. Vérifier l'accès réseau aux domaines Postman :
   ```bash
   curl -sSI https://dl.pstmn.io/download/latest/linux64 | head -5
   ```
   👉 Explication : Confirme que HTTPS sortant est possible (redirection 302 attendue) ; passer par le proxy d'entreprise si nécessaire.

3. Installer les outils de base et vérifier les bibliothèques graphiques :
   ```bash
   sudo apt update
   sudo apt install -y ca-certificates curl tar
   sudo apt install -y libgtk-3-0t64 libnss3 libasound2t64
   ```
   👉 Explication : Postman Desktop est une application Electron ; ces bibliothèques sont courantes pour ce type d'application. Les noms de paquets t64 de Debian 13 sont à vérifier (`apt search libgtk-3-0`).

4. Définir le périmètre et les limites :
   ```text
   Fiche d'architecture > lister les API de test autorisées (URL_API_LAB) > noter qu'aucun paquet .deb officiel n'est fourni par Postman ; la méthode documentée est l'archive ou le snap (à vérifier).
   ```
   👉 Explication : Remplacer `URL_API_LAB` par l'URL de l'API de lab ; ne tester que des API autorisées.

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
- [Fiche connexe Installer](</01-fiches-simples/debian/13/vie-du-logiciel/postman/fiche-simple-vm-debian-13-postman-installer>)