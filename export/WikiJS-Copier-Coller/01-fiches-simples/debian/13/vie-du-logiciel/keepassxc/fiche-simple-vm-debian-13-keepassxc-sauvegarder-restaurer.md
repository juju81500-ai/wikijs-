# Fiche_Simple_-_VM_Debian_13_KeePassXC_Sauvegarder_Restaurer.md

- **Environnement** : Poste Debian 13 amd64, KeePassXC AppImage en compte utilisateur
- **OS / Version** : Debian 13 Trixie amd64; KeePassXC 2.8.0
- **Catégorie** : gestionnaire de mots de passe local

---

## Problème précis à résoudre

Protéger le coffre contre la corruption et la perte, et prouver que la restauration fonctionne.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Tools > Settings > File Operations** et conserver les sauvegardes sûres par défaut.
   👉 Explication : KeePassXC écrit un fichier temporaire avant remplacement; éviter l'écriture directe qui expose à la corruption.

2. Produire une copie à la demande avec **Database > Save Database Backup**.
   👉 Explication : crée une sauvegarde chiffrée du `.kdbx`.

3. Conserver plusieurs générations dans un emplacement chiffré et contrôlé, avec au moins une copie hors du poste.
   👉 Explication : protège de la suppression et de la perte du poste.

4. Tester la restauration : copier une sauvegarde dans un répertoire de test, l'ouvrir avec les facteurs requis, contrôler quelques entrées, puis refermer sans écraser la base active.
   👉 Explication : prouve que la sauvegarde est exploitable.

## 2. Production — Contrôles

Planifier la sauvegarde, la rétention et un test de restauration périodique; sauvegarder séparément fichier-clé ou clé matérielle et documenter leur remplacement.

## 3. Production — Sécurité

- Ne pas synchroniser simultanément plusieurs copies ouvertes du même coffre.
- Protéger les sauvegardes contre suppression, remplacement et accès non autorisé.

## Validation et retour arrière

- **Validation** : La copie de test s'ouvre et les entrées contrôlées sont correctes.
- **Retour arrière** : Conserver la base active; comparer dates et versions avant toute restauration.

## Si le problème n'est pas résolu

- [KeePassXC — options de sauvegarde](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_database_backup_options)
- [Guide complet KeePassXC 2.8.0 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/79-deploiement-keepassxc-2-8-0-debian-13#5-sauvegarder-et-restaurer-le-coffre)