# Fiche_Simple_-_VM_Ubuntu_24.04_BlueMind_Prerequis_Limites

- **Environnement** : VM Ubuntu Server 24.04; BlueMind 5.7; guide public, matrice OS à revalider
- **OS / Version** : Ubuntu Server 24.04
- **Catégorie** : Vie du logiciel / BlueMind — Prérequis et limites

---

## Problème précis à résoudre

Confirmer OS, capacité et prérequis de la version BlueMind visée.

## 1. Hors-Production (Lab / Test / POC)

1. Prérequis et limites :
   ```bash
   cat /etc/os-release | head -5
hostname -f
timedatectl status
free -h
df -h /
printf "%s\n" "https://doc.bluemind.net/release/5.7/guide-d-installation"
   ```
   👉 Explication : Le guide public est la source de référence; confirmer explicitement Ubuntu 24.04 dans la matrice de la release choisie.

## 2. Production — Contrôles

Serveur dédié, DNS/MX/PTR, ressources, stockage et sauvegarde doivent être prévus.

## 3. Production — Sécurité

Ne pas installer sur un serveur mail/web mutualisé ni transposer un support d’une release à l’autre.

## Validation et retour arrière

- **Validation** : Version, OS, ressources et DNS validés.
- **Retour arrière** : Ne pas installer tant que la compatibilité n’est pas confirmée.

## Si le problème n'est pas résolu

- [Installer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/bluemind/fiche-simple-vm-ubuntu-24-04-bluemind-installer)
- [Configurer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/bluemind/fiche-simple-vm-ubuntu-24-04-bluemind-configurer)
- [Sécuriser](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/bluemind/fiche-simple-vm-ubuntu-24-04-bluemind-securiser)
- [Valider (recette)](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/bluemind/fiche-simple-vm-ubuntu-24-04-bluemind-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/bluemind/fiche-simple-vm-ubuntu-24-04-bluemind-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/bluemind/fiche-simple-vm-ubuntu-24-04-bluemind-mise-a-jour-retour-arriere)
- [Documentation officielle](https://doc.bluemind.net/release/5.7/guide-d-installation)