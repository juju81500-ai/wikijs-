# Fiche_Simple_-_VM_Debian_13_PuTTY_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 (Trixie), poste d'administration en ligne de commande
- **OS / Version** : Debian 13 (Trixie) — paquet putty-tools
- **Catégorie** : outils d'administration / SSH

---

## Problème précis à résoudre

Sauvegarder et restaurer les clés `.ppk` et la configuration PuTTY de l'utilisateur.

## 1. Hors-Production (Lab / Test / POC)

1. Archiver les clés dans un dossier chiffré :
   ```bash
   tar czf - -C ~ .ssh | gpg -c -o SAUVEGARDE_A_REMPLACER.tar.gz.gpg
   ```
   👉 Explication : la phrase de passe GPG se saisit à l'invite.
2. Si l'interface graphique est utilisée, sauvegarder `~/.putty` (sessions et clés d'hôtes).
   👉 Explication : `plink` lit aussi ces sessions enregistrées.
3. Restaurer :
   ```bash
   gpg -d SAUVEGARDE_A_REMPLACER.tar.gz.gpg | tar xzf - -C ~
   chmod 600 ~/.ssh/CLE_A_REMPLACER.ppk
   ```
   👉 Explication : rétablir les droits.

## 2. Production — Contrôles

- Tester la restauration sur un poste de test.

## 3. Production — Sécurité

- Stocker la sauvegarde hors du poste, chiffrée.

## Validation et retour arrière

- **Validation** : connexion fonctionnelle après restauration. **Retour arrière** : supprimer les fichiers restaurés.

## Si le problème n'est pas résolu

- [Fiche d'entrée PuTTY](/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-putty)
- [Documentation officielle PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html)
- [Documentation officielle PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html)