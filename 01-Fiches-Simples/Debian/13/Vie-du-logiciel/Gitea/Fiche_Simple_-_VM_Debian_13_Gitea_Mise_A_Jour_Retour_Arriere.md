# Fiche_Simple_-_VM_Debian_13_Gitea_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13 isolée; domaine et stockage définis
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : forge Git / administration
- **Tags** : `debian13`, `gitea`, `forge-git`, `tls`, `sauvegarde`
---

## Problème précis à résoudre

Mettre à niveau Gitea après lecture des consignes de migration et conserver une reprise cohérente.

## 1. Hors-Production (Lab / Test / POC)

1. Lire les notes et le chemin de mise à niveau
   ```bash
   /usr/local/bin/gitea --version
   sudo systemctl stop gitea
   ```
   👉 Explication : ne pas sauter de version majeure sans procédure officielle.

2. Effectuer et vérifier le backup préalable
   ```bash
   sudo -u git /usr/local/bin/gitea dump --config /etc/gitea/app.ini --file /var/backups/gitea/pre-update.zip
   sudo sha256sum /var/backups/gitea/pre-update.zip
   ```
   👉 Explication : confirmer qu’une restauration testée est disponible avant changement.

3. Installer un nouveau binaire vérifié à côté de l’ancien
   ```bash
   sudo install -o root -g root -m 0755 /tmp/gitea /usr/local/bin/gitea.new
   /usr/local/bin/gitea.new --version
   ```
   👉 Explication : utiliser uniquement l’artefact approuvé et vérifier son empreinte.

4. Redémarrer et refaire la recette
   ```bash
   sudo mv /usr/local/bin/gitea.new /usr/local/bin/gitea
   sudo systemctl start gitea
   sudo systemctl --no-pager status gitea
   sudo journalctl -u gitea -n 100 --no-pager
   ```
   👉 Explication : ne pas rétrograder le binaire après migration de base sans procédure compatible.

## 2. Production — Contrôles

Répéter sur clone, planifier une fenêtre et surveiller interface, dépôts, tâches et journaux.

## 3. Production — Sécurité

- Ne pas supposer qu’un downgrade du binaire annule une migration de schéma.
- Conserver binaire, base, dépôts et configuration cohérents.
- Arrêter l’opération si une migration échoue.

## Validation et retour arrière

- **Validation** : Version cible approuvée, interface et test Git fonctionnels, aucune migration inachevée.
- **Retour arrière** : Restaurer ensemble binaire, base, données et configuration du point de reprise testé.

## Si le problème n'est pas résolu

- [Gitea — installation depuis un binaire](https://docs.gitea.com/installation/install-from-binary)
- [Gitea — configuration](https://docs.gitea.com/administration/config-cheat-sheet)
- [Gitea — sauvegarde/restauration](https://docs.gitea.com/administration/backup-and-restore)
- [Fiche connexe](<Fiche_Simple_-_VM_Debian_13_Gitea_Prerequis_Limites.md>)
