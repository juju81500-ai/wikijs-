# 📄 Fiche_Simple_-_Bitwarden_Self_Hosted_Verifier_Backup_Restauration.md

- **Environnement** : Bitwarden self-hosted Standard Deployment sous Docker
- **OS / Version** : Linux supporté par Docker Engine 26+
- **Catégorie** : Coffre de secrets / continuité

---

## 🎯 Problème précis à résoudre

Confirmer que les données et la configuration Bitwarden sont sauvegardées et restaurables.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Vérifier le contenu de la sauvegarde :
   ```bash
   ls -la /opt/bitwarden/bwdata
   sudo tar tzf /sauvegardes/bwdata-AAAA-MM-JJ.tgz | grep -E 'env/|core/attachments|mssql/backups|ssl/' | head
   ```
   👉 Explication : remplacer chemin et date; `env`, pièces jointes, base MSSQL et certificats doivent y figurer.

2. Vérifier date, intégrité et destination :
   ```bash
   ls -l --time-style=long-iso /sauvegardes/bwdata-AAAA-MM-JJ.tgz
   sha256sum -c /sauvegardes/bwdata-AAAA-MM-JJ.tgz.sha256
   ```
   👉 Explication : la sauvegarde est récente, intègre, chiffrée et sur une destination séparée du serveur.

3. Restaurer sur un serveur de test isolé :
   ```bash
   sudo tar xzf /sauvegardes/bwdata-AAAA-MM-JJ.tgz -C /opt/bitwarden
   cd /opt/bitwarden && ./bitwarden.sh restart
   ```
   👉 Explication : vérifier TLS, connexion d'un compte de test, éléments fictifs, pièces jointes et organisations.

4. Consigner durée et étapes sans publier mot de passe DB, ID d'installation, clé, tokens ou données de coffre.
   👉 Explication : ces informations restent dans le coffre de l'organisation.

## ⚡ 2. Production — Façon Simplifiée

1. Contrôler la sauvegarde nocturne et l'espace :
   ```bash
   ls -lt /opt/bitwarden/bwdata/mssql/backups | head -3
   df -h /opt/bitwarden /sauvegardes
   ```
   👉 Explication : superviser échecs et espace; planifier des tests de restauration périodiques et tester les versions avant upgrade.

## 🔒 3. Production — Façon Sécurisée

- Restreindre l'accès au répertoire `bwdata`; sauvegarder les clés/chiffreurs indépendamment du support.
- Ne pas considérer les backups DB intégrés comme couverture complète du serveur.
- Faire les tests de restauration hors ligne ou isolés, sans reconnecter les clients utilisateurs.

## ✅ Validation et retour arrière

- **Validation** : test sur une copie, accès TLS valide, données test restaurées, contrôle des logs.
- **Retour arrière** : conserver le serveur actif et sa sauvegarde; ne basculer le DNS qu'après approbation et test complet.

## 🔗 Si le problème n'est pas résolu

- [Bitwarden — Sauvegarder le serveur](https://bitwarden.com/help/backup-on-premise/)
- [Bitwarden — Déployer sous Linux](https://bitwarden.com/help/install-on-premise-linux/)