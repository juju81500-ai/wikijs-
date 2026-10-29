# Fiche_Simple_-_VM_Debian_13_KeePassXC_Lancer.md

- **Environnement** : Poste Debian 13 amd64, KeePassXC AppImage en compte utilisateur
- **OS / Version** : Debian 13 Trixie amd64; KeePassXC 2.8.0
- **Catégorie** : gestionnaire de mots de passe local

---

## Problème précis à résoudre

Lancer KeePassXC avec le compte utilisateur, sans sudo.

## 1. Hors-Production (Lab / Test / POC)

1. Rendre l'AppImage exécutable et la lancer :
   ```bash
   cd "$HOME/Téléchargements/keepassxc-2.8.0"
   chmod 700 KeePassXC-2.8.0-1-x86_64.AppImage
   ./KeePassXC-2.8.0-1-x86_64.AppImage
   ```
   👉 Explication : le mode 700 réserve l'exécution à l'utilisateur; jamais de `sudo`.

2. Confirmer la version affichée dans **Help > About KeePassXC**.
   👉 Explication : doit indiquer 2.8.0.

3. Si le montage AppImage échoue (FUSE), installer uniquement la dépendance FUSE des dépôts Debian 13 :
   ```bash
   sudo apt update
   apt-cache search fuse | grep -i libfuse
   ```
   👉 Explication : choisir le paquet FUSE disponible pour Debian 13, puis relancer l'AppImage en simple utilisateur.

## 2. Production — Contrôles

Documenter l'emplacement de l'AppImage et le responsable des mises à jour.

## 3. Production — Sécurité

- Ne pas lancer le binaire en root.
- Ne pas désactiver les contrôles du système.

## Validation et retour arrière

- **Validation** : L'application démarre sous l'utilisateur standard et affiche 2.8.0.
- **Retour arrière** : Fermer l'application et supprimer le fichier AppImage.

## Si le problème n'est pas résolu

- [KeePassXC — téléchargements](https://keepassxc.org/download/)
- [Guide complet KeePassXC 2.8.0 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/79-deploiement-keepassxc-2-8-0-debian-13#3-lancer-lapplication-sans-privileges)