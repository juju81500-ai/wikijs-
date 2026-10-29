# Fiche_Simple_-_Bitwarden_Self_Hosted_Deploiement_Sauvegardes_Mises_A_Jour_Reprise.md

- **Environnement** : Serveur Linux x86-64 avec Docker Engine et Compose (déploiement standard Bitwarden)
- **OS / Version** : Linux x86-64 supporté; Docker Engine 26+
- **Catégorie** : coffre de mots de passe / secrets

---

## Problème précis à résoudre

Sauvegarder, mettre à jour et restaurer sans perte.

## 1. Hors-Production (Lab / Test / POC)

1. Arrêter le service avant copie :
   ```bash
   sudo -iu bitwarden /opt/bitwarden/bitwarden.sh stop
   ```
   👉 Explication : garantit la cohérence de la copie.

2. Copier tout `bwdata` (env, pièces jointes, base MSSQL, certificats, secrets) vers une destination chiffrée hors hôte (remplacer SAUVEGARDE_CHIFFREE par la destination réelle) :
   ```bash
   sudo tar -czf /srv/SAUVEGARDE_CHIFFREE/bwdata.tar.gz -C /opt/bitwarden bwdata
   ```
   👉 Explication : archive complète à stocker chiffrée; les sauvegardes nocturnes intégrées de la base ne la remplacent pas.

3. Redémarrer :
   ```bash
   sudo -iu bitwarden /opt/bitwarden/bitwarden.sh start
   ```
   👉 Explication : remet le service en marche.

4. Tester la restauration sur un hôte et un réseau isolés, sans DNS public ni clients.
   👉 Explication : prouve la restaurabilité.

5. Mettre à jour dans une fenêtre contrôlée :
   ```bash
   sudo -iu bitwarden /opt/bitwarden/bitwarden.sh updateself
   sudo -iu bitwarden /opt/bitwarden/bitwarden.sh update
   ```
   👉 Explication : conserver la sauvegarde avant migration de schéma; contrôler logs et santé des conteneurs après chaque opération.

## 2. Production — Contrôles

Planifier sauvegardes chiffrées hors hôte, essais de restauration et mises à jour.

## 3. Production — Sécurité

- Chiffrer la sauvegarde `bwdata` (elle contient des secrets).
- Accès restreint à la destination.

## Validation et retour arrière

- **Validation** : restauration isolée réussie et conteneurs sains après mise à jour.
- **Retour arrière** : restaurer `bwdata` sauvegardé avant la mise à jour puis `start`.

## Si le problème n'est pas résolu

- [Bitwarden — sauvegarde](https://bitwarden.com/help/backup-on-premise/)
- [Bitwarden — mise à jour](https://bitwarden.com/help/updating-on-premise/)
- [Bitwarden — déploiement Linux](https://bitwarden.com/help/install-on-premise-linux/)
- [Guide complet](/02-fiches-completes/transverses/docker/installation-deploiement/62-deploiement-bitwarden-self-hosted-linux-docker#6-sauvegardes-mises-a-jour-et-reprise)