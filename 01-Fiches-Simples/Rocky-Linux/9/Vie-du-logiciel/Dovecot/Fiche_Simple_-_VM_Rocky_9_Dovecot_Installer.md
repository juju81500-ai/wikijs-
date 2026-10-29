# Fiche_Simple_-_VM_Rocky_9_Dovecot_Installer

- **Environnement** : VM Rocky Linux 9; Dovecot depuis les dépôts de la distribution
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Vie du logiciel / Dovecot — Installer
- **Tags** : `dovecot`, `serveur`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer Dovecot depuis les dépôts signés de la distribution.

## 1. Hors-Production (Lab / Test / POC)

1. Installer :
   ```bash
   sudo dnf install -y dovecot
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

- [Prérequis et limites](Fiche_Simple_-_VM_Rocky_9_Dovecot_Prerequis_Limites.md)
- [Configurer](Fiche_Simple_-_VM_Rocky_9_Dovecot_Configurer.md)
- [Sécuriser](Fiche_Simple_-_VM_Rocky_9_Dovecot_Securiser.md)
- [Valider (recette)](Fiche_Simple_-_VM_Rocky_9_Dovecot_Valider.md)
- [Sauvegarder / restaurer](Fiche_Simple_-_VM_Rocky_9_Dovecot_Sauvegarder_Restaurer.md)
- [Mise à jour et retour arrière](Fiche_Simple_-_VM_Rocky_9_Dovecot_Mise_A_Jour_Retour_Arriere.md)
- [Documentation officielle](https://doc.dovecot.org/)
