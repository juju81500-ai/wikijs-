# Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Prerequis_Limites

- **Environnement** : [[Glossary:VM]] Ubuntu Server 24-04; Postfix depuis les dépôts de la distribution
- **OS / Version** : Ubuntu Server 24-04
- **Catégorie** : Vie du logiciel / Postfix — Prérequis et limites
- **Tags** : `postfix`, `serveur`, `vie-du-logiciel`, `prerequis_limites`

---

## Problème précis à résoudre

Vérifier rôle, paquets et flux nécessaires à Postfix.

## 1. Hors-Production (Lab / Test / POC)

1. Prérequis et limites :
   ```bash
   cat /etc/os-release | head -5
free -h
df -h /
sudo ss -lntup
   ```
   👉 Explication : Confirme l’OS, ressources et sockets avant changement.


## 2. Production — Contrôles

Documenter rôle [[Glossary:SMTP]]/IMAP, domaines, réseaux autorisés et ports.

## 3. Production — Sécurité

Ne pas exposer de port avant configuration; sur Rocky, conserver SELinux enforcing.

## Validation et retour arrière

- **Validation** : Le paquet candidat et le plan de changement sont consignés.
- **Retour arrière** : Aucun changement; arrêter si provenance ou prérequis incertains.

## Si le problème n'est pas résolu

- [Installer](fiche-simple-vm-ubuntu-24-04-postfix-installer.md)
- [Configurer](fiche-simple-vm-ubuntu-24-04-postfix-configurer.md)
- [Sécuriser](fiche-simple-vm-ubuntu-24-04-postfix-securiser.md)
- [Valider (recette)](fiche-simple-vm-ubuntu-24-04-postfix-valider.md)
- [Sauvegarder / restaurer](fiche-simple-vm-ubuntu-24-04-postfix-sauvegarder-restaurer.md)
- [Mise à jour et retour arrière](fiche-simple-vm-ubuntu-24-04-postfix-mise-a-jour-retour-arriere.md)
- [Documentation officielle](https://www.postfix.org/documentation.html)
