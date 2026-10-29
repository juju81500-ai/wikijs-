# Fiche_Simple_-_VM_Debian_13_KeePassXC_Creer_Coffre.md

- **Environnement** : Poste Debian 13 amd64, KeePassXC AppImage en compte utilisateur
- **OS / Version** : Debian 13 Trixie amd64; KeePassXC 2.8.0
- **Catégorie** : gestionnaire de mots de passe local
- **Tags** : `debian13`, `keepassxc`, `kdbx`, `argon2id`, `appimage`

---

## Problème précis à résoudre

Créer un coffre KDBX 4 chiffré (Argon2id) avec un mot de passe maître solide.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer l'assistant : **Database > New Database**, choisir un emplacement dans le profil ou un volume chiffré, extension `.kdbx`.
   👉 Explication : le fichier reste sous contrôle de l'utilisateur.

2. Conserver KDBX 4 et le chiffrement recommandé; ne modifier Argon2id que selon la compatibilité et le temps de déverrouillage mesuré.
   👉 Explication : les réglages par défaut sont adaptés dans la plupart des cas.

3. Définir un mot de passe maître long, unique et aléatoire, mémorisé ou conservé selon une procédure de récupération approuvée, séparée du fichier.
   👉 Explication : sa perte rend le coffre irrécupérable.

4. N'ajouter un fichier-clé ou une clé matérielle que si sa sauvegarde et sa récupération sont maîtrisées.
   👉 Explication : un facteur manquant bloque aussi l'accès.

5. Organiser les entrées en groupes, générer des mots de passe uniques et activer le verrouillage automatique dans **Tools > Settings > Security**.
   👉 Explication : réduit l'exposition quand le poste est laissé sans surveillance.

## 2. Production — Contrôles

Définir la procédure de récupération du mot de passe maître et des facteurs supplémentaires.

## 3. Production — Sécurité

- Protéger la session de bureau; le contenu est déchiffré en mémoire quand le coffre est ouvert.
- Éviter de stocker le secret TOTP dans la même base que le mot de passe, sauf choix de risque explicite.

## Validation et retour arrière

- **Validation** : Le coffre se ferme, se rouvre avec le mot de passe maître et se verrouille automatiquement.
- **Retour arrière** : Supprimer le fichier `.kdbx` de test (jamais un coffre actif sans sauvegarde).

## Si le problème n'est pas résolu

- [KeePassXC — créer sa première base](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_creating_your_first_database)
- [Guide complet KeePassXC 2.8.0 Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/79_Deploiement_KeePassXC_2.8.0_Debian_13.md#4-creer-un-coffre-kdbx)
