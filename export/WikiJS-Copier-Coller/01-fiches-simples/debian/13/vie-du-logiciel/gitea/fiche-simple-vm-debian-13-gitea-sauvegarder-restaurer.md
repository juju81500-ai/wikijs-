# Fiche_Simple_-_VM_Debian_13_Gitea_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 isolée; domaine et stockage définis
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : forge Git / administration

---

## Problème précis à résoudre

Sauvegarder dépôts, base, données, configuration et secrets nécessaires; éprouver une reprise isolée.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le répertoire de sauvegarde protégé
   ```bash
   sudo install -d -o root -g root -m 0700 /var/backups/gitea
   ```
   👉 Explication : les archives contiennent code et données de comptes; protéger le chemin.

2. Exécuter le dump avec le compte de service
   ```bash
   sudo -u git /usr/local/bin/gitea dump --config /etc/gitea/app.ini --file /var/backups/gitea/gitea-dump.zip
   ```
   👉 Explication : vérifier le support du backend et la syntaxe de la version installée.

3. Sauvegarder la configuration et contrôler empreintes
   ```bash
   sudo cp -a /etc/gitea/app.ini /var/backups/gitea/app.ini
   sudo sha256sum /var/backups/gitea/*
   ```
   👉 Explication : chiffrer avant transfert; app.ini peut contenir des secrets.

4. Restaurer sur une instance isolée
   ```text
   Navigateur > ouvrir la documentation officielle : https://docs.gitea.com/installation/install-from-binary
   ```
   👉 Explication : ne jamais restaurer sur la production active pendant la recette. Détail à confirmer dans la documentation officielle avant application : Utiliser même version Gitea et backend compatible. Vérifier connexion, clonage d’un dépôt témoin et pièces jointes.

## 2. Production — Contrôles

Définir fréquence, chiffrement, rétention, RPO/RTO et tester l’intégralité de la restauration.

## 3. Production — Sécurité

- Protéger sauvegardes et clés de configuration par chiffrement et contrôle d’accès.
- Ne pas considérer un dump réussi comme preuve d’une restauration fonctionnelle.
- Séparer les identités de sauvegarde et d’administration.

## Validation et retour arrière

- **Validation** : Un clone isolé permet connexion et récupération du dépôt témoin.
- **Retour arrière** : Reprendre depuis une sauvegarde cohérente vérifiée; conserver l’instance d’essai pour diagnostic.

## Si le problème n'est pas résolu

- [Gitea — installation depuis un binaire](https://docs.gitea.com/installation/install-from-binary)
- [Gitea — configuration](https://docs.gitea.com/administration/config-cheat-sheet)
- [Gitea — sauvegarde/restauration](https://docs.gitea.com/administration/backup-and-restore)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/gitea/fiche-simple-vm-debian-13-gitea-prerequis-limites>)