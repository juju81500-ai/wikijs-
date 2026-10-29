# Fiche_Simple_-_VM_Debian_13_BlueMind_Prerequis_Limites

- **Environnement** : VM Debian 13; BlueMind 5.7; guide public
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Vie du logiciel / BlueMind — Prérequis et limites

---

## Problème précis à résoudre

Confirmer OS, capacité et prérequis de la version BlueMind visée.

## 1. Hors-Production (Lab / Test / POC)

1. Prérequis et limites :
   ```bash
   cat /etc/os-release | head -5
hostname -f
hostname -i
ip -br addr
locale -a | grep -i en_US
timedatectl status
free -h
df -h /
printf "%s\n" "https://doc.bluemind.net/release/5.7/guide-d-installation"
   ```
   👉 Explication : Le guide public est la source de référence; confirmer Debian 13 dans la matrice de la release choisie.

## 2. Production — Contrôles

Serveur dédié, DNS/MX/PTR, ressources, stockage et sauvegarde doivent être prévus.

## 3. Production — Sécurité

Ne pas installer sur un serveur mail/web mutualisé ni transposer un support d’une release à l’autre.

## Validation et retour arrière

- **Validation** : Version, OS, ressources et DNS validés.
- **Retour arrière** : Ne pas installer tant que la compatibilité n’est pas confirmée.

## Si le problème n'est pas résolu

- [Installer](/01-fiches-simples/debian/13/vie-du-logiciel/bluemind/fiche-simple-vm-debian-13-bluemind-installer)
- [Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/bluemind/fiche-simple-vm-debian-13-bluemind-configurer)
- [Sécuriser](/01-fiches-simples/debian/13/vie-du-logiciel/bluemind/fiche-simple-vm-debian-13-bluemind-securiser)
- [Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/bluemind/fiche-simple-vm-debian-13-bluemind-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/bluemind/fiche-simple-vm-debian-13-bluemind-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/bluemind/fiche-simple-vm-debian-13-bluemind-mise-a-jour-retour-arriere)
- [Guide officiel d’installation](https://doc.bluemind.net/release/5.7/guide-d-installation)
- [Prérequis officiels](https://doc.bluemind.net/release/5.7/guide_d_installation/prerequis_a_l_installation)