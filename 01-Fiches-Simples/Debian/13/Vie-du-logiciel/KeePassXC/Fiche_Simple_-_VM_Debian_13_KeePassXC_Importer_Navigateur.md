# Fiche_Simple_-_VM_Debian_13_KeePassXC_Importer_Navigateur.md

- **Environnement** : Poste Debian 13 amd64, KeePassXC AppImage en compte utilisateur
- **OS / Version** : Debian 13 Trixie amd64; KeePassXC 2.8.0
- **Catégorie** : gestionnaire de mots de passe local
- **Tags** : `debian13`, `keepassxc`, `kdbx`, `argon2id`, `appimage`

---

## Problème précis à résoudre

Importer des mots de passe sans fuite et activer l'intégration navigateur de façon contrôlée.

## 1. Hors-Production (Lab / Test / POC)

1. Préférer l'import direct d'un format chiffré pris en charge; sinon, utiliser **Database > Import > CSV File...** avec un CSV créé dans un emplacement protégé.
   👉 Explication : un CSV contient les mots de passe en clair.

2. Après contrôle des entrées, supprimer le CSV puis vider la corbeille :
   ```bash
   shred -u "$HOME/export-a-supprimer.csv"
   ```
   👉 Explication : `export-a-supprimer.csv` est un exemple à remplacer; la suppression ne garantit pas l'effacement sur SSD ou snapshots.

3. Intégration navigateur optionnelle : installer KeePassXC-Browser depuis le magasin officiel du navigateur, puis activer le navigateur dans **Tools > Settings > Browser Integration**.
   👉 Explication : limite la surface au navigateur choisi.

4. Approuver chaque association en vérifiant domaine et entrée.
   👉 Explication : ne pas approuver une demande inattendue; les navigateurs Snap ou Flatpak peuvent ne pas supporter le canal natif.

## 2. Production — Contrôles

Documenter qui peut importer et quels navigateurs sont autorisés.

## 3. Production — Sécurité

- Ne pas importer de base legacy de source non fiable.
- Ne laisser aucun CSV en clair dans un répertoire partagé.

## Validation et retour arrière

- **Validation** : Entrées importées contrôlées, CSV supprimé, associations navigateur connues.
- **Retour arrière** : Supprimer les entrées importées par erreur, retirer l'extension et révoquer les associations dans les paramètres.

## Si le problème n'est pas résolu

- [KeePassXC — import CSV](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_importing_csv_file)
- [Guide complet KeePassXC 2.8.0 Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/79_Deploiement_KeePassXC_2.8.0_Debian_13.md#6-importer-des-donnees-et-utiliser-lextension-navigateur)
