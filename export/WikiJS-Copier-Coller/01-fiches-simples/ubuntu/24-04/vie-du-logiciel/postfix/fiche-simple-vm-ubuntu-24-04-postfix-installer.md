# Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Installer

- **Environnement** : VM Ubuntu Server 24.04; Postfix depuis les dépôts de la distribution
- **OS / Version** : Ubuntu Server 24.04
- **Catégorie** : Vie du logiciel / Postfix — Installer

---

## Problème précis à résoudre

Installer Postfix depuis les dépôts signés de la distribution.

## 1. Hors-Production (Lab / Test / POC)

1. Installer :
   ```bash
   sudo apt update && sudo apt install -y postfix mailutils swaks
sudo systemctl enable --now postfix
systemctl is-active postfix
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

- [Prérequis et limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-prerequis-limites)
- [Configurer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-configurer)
- [Sécuriser](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-securiser)
- [Valider (recette)](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/postfix/fiche-simple-vm-ubuntu-24-04-postfix-mise-a-jour-retour-arriere)
- [Documentation officielle](https://www.postfix.org/documentation.html)