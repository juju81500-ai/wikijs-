# Fiche_Simple_-_VM_Rocky_9_Postfix_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Rocky Linux 9; Postfix depuis les dépôts de la distribution
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Vie du logiciel / Postfix — Mise à jour et retour arrière
- **Tags** : `postfix`, `serveur`, `vie-du-logiciel`, `mise_a_jour_retour_arriere`

---

## Problème précis à résoudre

Mettre à jour Postfix depuis dépôts configurés.

## 1. Hors-Production (Lab / Test / POC)

1. Mise à jour et retour arrière :
   ```bash
   sudo dnf check-update postfix || test "$?" -eq 100
sudo dnf upgrade -y postfix
sudo systemctl restart postfix
sudo postfix check
   ```
   👉 Explication : Liste les paquets puis met à jour en lab; contrôler les notes de version et la syntaxe après redémarrage.


## 2. Production — Contrôles

Préparer sauvegarde restaurable, fenêtre, espace disque et compatibilité clients.

## 3. Production — Sécurité

Utiliser paquets signés des dépôts autorisés.

## Validation et retour arrière

- **Validation** : Version mise à jour consignée, service actif et contrôle syntaxique réussi.
- **Retour arrière** : Restaurer un snapshot cohérent plutôt qu’un downgrade de paquet isolé.

## Si le problème n'est pas résolu

- [Prérequis et limites](Fiche_Simple_-_VM_Rocky_9_Postfix_Prerequis_Limites.md)
- [Installer](Fiche_Simple_-_VM_Rocky_9_Postfix_Installer.md)
- [Configurer](Fiche_Simple_-_VM_Rocky_9_Postfix_Configurer.md)
- [Sécuriser](Fiche_Simple_-_VM_Rocky_9_Postfix_Securiser.md)
- [Valider (recette)](Fiche_Simple_-_VM_Rocky_9_Postfix_Valider.md)
- [Sauvegarder / restaurer](Fiche_Simple_-_VM_Rocky_9_Postfix_Sauvegarder_Restaurer.md)
- [Documentation officielle](https://www.postfix.org/documentation.html)
