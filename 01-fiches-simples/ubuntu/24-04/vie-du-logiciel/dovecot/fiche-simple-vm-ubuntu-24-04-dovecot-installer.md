# Fiche_Simple_-_VM_Ubuntu_24.04_Dovecot_Installer

- **Environnement** : VM Ubuntu Server 24-04; Dovecot depuis les dépôts de la distribution
- **OS / Version** : Ubuntu Server 24-04
- **Catégorie** : Vie du logiciel / Dovecot — Installer
- **Tags** : `dovecot`, `serveur`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer Dovecot depuis les dépôts signés de la distribution.

## 1. Hors-Production (Lab / Test / POC)

1. Installer :
   ```bash
   sudo apt update && sudo apt install -y dovecot-core dovecot-imapd dovecot-pop3d
sudo systemctl enable --now dovecot
systemctl is-active dovecot
   ```
   👉 Explication : Installe les paquets de la famille OS cible puis démarre le service. Vérifier les noms disponibles sur la version visée.


## 2. Production — Contrôles

Valider dépôts, snapshot et fenêtre avant installation.

## 3. Production — Sécurité

Aucun port entrant avant configuration et recette.

## Validation et retour arrière

- **Validation** : Le service est actif et les paquets proviennent des dépôts approuvés.
- **Retour arrière** : Restaurer le snapshot avant exposition; ne pas purger les dépendances partagées.

## Si le problème n'est pas résolu

- [Prérequis et limites](fiche-simple-vm-ubuntu-24-04-dovecot-prerequis-limites.md)
- [Configurer](fiche-simple-vm-ubuntu-24-04-dovecot-configurer.md)
- [Sécuriser](fiche-simple-vm-ubuntu-24-04-dovecot-securiser.md)
- [Valider (recette)](fiche-simple-vm-ubuntu-24-04-dovecot-valider.md)
- [Sauvegarder / restaurer](fiche-simple-vm-ubuntu-24-04-dovecot-sauvegarder-restaurer.md)
- [Mise à jour et retour arrière](fiche-simple-vm-ubuntu-24-04-dovecot-mise-a-jour-retour-arriere.md)
- [Documentation officielle](https://doc.dovecot.org/)
