# Fiche_Simple_-_VM_Rocky_9_Postfix_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Rocky Linux 9; Postfix depuis les dépôts de la distribution
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Vie du logiciel / Postfix — Mise à jour et retour arrière

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

- [Prérequis et limites](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-prerequis-limites)
- [Installer](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-installer)
- [Configurer](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-configurer)
- [Sécuriser](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-securiser)
- [Valider (recette)](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/postfix/fiche-simple-vm-rocky-9-postfix-sauvegarder-restaurer)
- [Documentation officielle](https://www.postfix.org/documentation.html)