# Fiche_Simple_-_VM_Rocky_9_Postfix_Valider

- **Environnement** : VM Rocky Linux 9; Postfix depuis les dépôts de la distribution
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Vie du logiciel / Postfix — Valider (recette)
- **Tags** : `postfix`, `serveur`, `vie-du-logiciel`, `valider`

---

## Problème précis à résoudre

Réaliser une recette locale contrôlée de Postfix.

## 1. Hors-Production (Lab / Test / POC)

1. Valider (recette) :
   ```bash
   sudo postfix check
systemctl is-active postfix
sudo ss -lntup
sudo journalctl -u postfix -n 80 --no-pager
   ```
   👉 Explication : Contrôle syntaxe, service, sockets et journaux; compléter par un client de recette autorisé.


## 2. Production — Contrôles

Tester depuis compte et réseau dédiés, puis consigner résultat et certificat.

## 3. Production — Sécurité

Ne pas utiliser de vrais secrets dans les commandes ou captures.

## Validation et retour arrière

- **Validation** : La syntaxe passe, service actif, ports et journaux cohérents.
- **Retour arrière** : Si échec, ne pas augmenter l’exposition; revenir à la configuration précédente.

## Si le problème n'est pas résolu

- [Prérequis et limites](fiche-simple-vm-rocky-9-postfix-prerequis-limites.md)
- [Installer](fiche-simple-vm-rocky-9-postfix-installer.md)
- [Configurer](fiche-simple-vm-rocky-9-postfix-configurer.md)
- [Sécuriser](fiche-simple-vm-rocky-9-postfix-securiser.md)
- [Sauvegarder / restaurer](fiche-simple-vm-rocky-9-postfix-sauvegarder-restaurer.md)
- [Mise à jour et retour arrière](fiche-simple-vm-rocky-9-postfix-mise-a-jour-retour-arriere.md)
- [Documentation officielle](https://www.postfix.org/documentation.html)
