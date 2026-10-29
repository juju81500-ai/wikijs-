# Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Prerequis_Limites

- **Environnement** : VM Ubuntu Server 24.04; Postfix depuis les dépôts de la distribution
- **OS / Version** : Ubuntu Server 24.04
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

Documenter rôle SMTP/IMAP, domaines, réseaux autorisés et ports.

## 3. Production — Sécurité

Ne pas exposer de port avant configuration; sur Rocky, conserver SELinux enforcing.

## Validation et retour arrière

- **Validation** : Le paquet candidat et le plan de changement sont consignés.
- **Retour arrière** : Aucun changement; arrêter si provenance ou prérequis incertains.

## Si le problème n'est pas résolu

- [Installer](Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Installer.md)
- [Configurer](Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Configurer.md)
- [Sécuriser](Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Securiser.md)
- [Valider (recette)](Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Valider.md)
- [Sauvegarder / restaurer](Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Sauvegarder_Restaurer.md)
- [Mise à jour et retour arrière](Fiche_Simple_-_VM_Ubuntu_24.04_Postfix_Mise_A_Jour_Retour_Arriere.md)
- [Documentation officielle](https://www.postfix.org/documentation.html)
