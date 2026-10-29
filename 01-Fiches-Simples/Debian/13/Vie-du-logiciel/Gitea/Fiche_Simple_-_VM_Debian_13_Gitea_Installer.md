# Fiche_Simple_-_VM_Debian_13_Gitea_Installer

- **Environnement** : VM Debian 13 isolée; domaine et stockage définis
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : forge Git / administration
- **Tags** : `debian13`, `gitea`, `forge-git`, `tls`, `sauvegarde`
---

## Problème précis à résoudre

Installer une version Gitea contrôlée depuis la distribution officielle après vérification de son empreinte.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un compte de service et les répertoires
   ```bash
   sudo apt update
   sudo apt install -y git curl ca-certificates
   sudo adduser --system --group --disabled-password --home /var/lib/gitea --shell /bin/bash git
   sudo install -d -o git -g git -m 0750 /var/lib/gitea/{custom,data,log}
   sudo install -d -o root -g git -m 0750 /etc/gitea
   ```
   👉 Explication : isoler données et configuration du compte administrateur.

2. Télécharger le binaire de version approuvée
   ```bash
   GITEA_VERSION="1.XX.Y"  # remplacer par la version approuvée
   curl -fsSLo /tmp/gitea "https://dl.gitea.com/gitea/${GITEA_VERSION}/gitea-${GITEA_VERSION}-linux-amd64"
   /usr/bin/sha256sum /tmp/gitea
   ```
   👉 Explication : remplacer la version à remplacer; comparer le SHA-256 affiché à la valeur de la publication officielle avant installation.

3. Installer le binaire vérifié
   ```bash
   sudo install -o root -g root -m 0755 /tmp/gitea /usr/local/bin/gitea
   /usr/local/bin/gitea --version
   ```
   👉 Explication : n’installer que si le checksum correspond et que l’architecture de la VM est confirmée.

4. Examiner le modèle systemd officiel
   ```bash
   curl -fsSLo /tmp/gitea.service https://raw.githubusercontent.com/go-gitea/gitea/main/contrib/systemd/gitea.service
   less /tmp/gitea.service
   ```
   👉 Explication : relire et adapter utilisateur, chemins et version; ne pas copier un modèle de branche mobile sans contrôle.

## 2. Production — Contrôles

Répéter sur une VM pilote et épingler la version, le checksum, l’unité et les dépendances avant changement de production.

## 3. Production — Sécurité

- Exécuter sous l’utilisateur git, jamais root.
- Vérifier le checksum officiel avant installation; garder l’ancien binaire pour reprise.
- Ne pas télécharger ni exécuter un installateur non relu avec privilèges root.

## Validation et retour arrière

- **Validation** : Le binaire affiche la version approuvée et le service pilote démarre sans erreur.
- **Retour arrière** : Arrêter le service, remettre le binaire vérifié précédent et restaurer la base/configuration de la même sauvegarde.

## Si le problème n'est pas résolu

- [Gitea — installation depuis un binaire](https://docs.gitea.com/installation/install-from-binary)
- [Gitea — configuration](https://docs.gitea.com/administration/config-cheat-sheet)
- [Gitea — sauvegarde/restauration](https://docs.gitea.com/administration/backup-and-restore)
- [Fiche connexe](<Fiche_Simple_-_VM_Debian_13_Gitea_Prerequis_Limites.md>)
