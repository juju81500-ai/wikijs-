# Fiche_Simple_-_VM_Debian_13_KeePassXC_Valider_Coffre.md

- **Environnement** : KeePassXC 2.8.0 AppImage officielle sur Debian 13 amd64, coffre de test
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : gestionnaire de mots de passe / sauvegarde

---

## Problème précis à résoudre

Vérifier que l'application et un coffre KDBX de test démarrent, se verrouillent, se sauvegardent et se restaurent sans exposer de secrets.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler signature et digest de l'AppImage :
   ```bash
   gpg --verify KeePassXC-X.Y.Z-x86_64.AppImage.sig KeePassXC-X.Y.Z-x86_64.AppImage
   sha256sum -c KeePassXC-X.Y.Z-x86_64.AppImage.DIGEST
   ```
   👉 Explication : remplacer `X.Y.Z`; l'empreinte de la clé doit correspondre à la clé officielle et le digest afficher `OK`.

2. Lancer sous un compte standard et créer un coffre de test :
   ```bash
   chmod +x KeePassXC-X.Y.Z-x86_64.AppImage
   ./KeePassXC-X.Y.Z-x86_64.AppImage
   ```
   Puis **Database > New Database**, nom, mot de passe maître unique, fichier `.kdbx`.
   👉 Explication : ne pas utiliser root.

3. Vérifier le format : **Database > Database Settings > Encryption** : KDBX 4, KDF **Argon2id**. Créer une entrée : **Entries > New Entry** (titre et données fictifs).
   👉 Explication : aucun secret réutilisable.

4. Verrouiller : **Database > Lock Database**, rouvrir avec le mot de passe maître. Vérifier **Tools > Settings > Security** : verrouillage automatique et effacement du presse-papiers.
   👉 Explication : ces paramètres limitent l'exposition des secrets.

5. Sauvegarder : **Database > Save Database As...** vers un dossier temporaire :
   ```bash
   install -d -m 0700 /tmp/kp-test
   ls -l /tmp/kp-test
   ```
   👉 Explication : ouvrir la copie et vérifier l'entrée fictive; supprimer ensuite `/tmp/kp-test`.

## 2. Production — Contrôles

Avant usage métier, définir le propriétaire du coffre, la politique du mot de passe maître, l'emplacement du KDBX, les facteurs additionnels, les destinataires des sauvegardes et la fréquence du test de restauration. Garder la base active et la sauvegarde séparées; documenter comment récupérer un facteur perdu.

## 3. Production — Sécurité

- Ne jamais écrire le mot de passe maître en ligne de commande, dans un script, un ticket ou une capture.
- Protéger le poste et le profil utilisateur; verrouiller le coffre dès que la session est laissée sans surveillance.
- Ne pas exporter vers CSV sauf migration approuvée; contrôler puis supprimer les fichiers en clair et leurs copies connues.
- N'approuver que les associations navigateur attendues et les extensions installées depuis les magasins officiels.
- Une clé fichier additionnelle doit être sauvegardée séparément selon une procédure de récupération contrôlée.

## Validation et retour arrière

- **Validation** : coffre de test ouvert/fermé; sauvegarde restaurée depuis une copie; aucun export en clair laissé dans le répertoire de travail.
- **Retour arrière** : conserver le KDBX actif et la sauvegarde d'origine; tester toute restauration dans un répertoire distinct sans remplacer la base active.

## Si le problème n'est pas résolu

- [KeePassXC — guide utilisateur](https://keepassxc.org/docs/KeePassXC_UserGuide.html)
- [KeePassXC — vérification des signatures](https://keepassxc.org/verifying-signatures/)
- [Guide complet KeePassXC 2.8.0 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/79-deploiement-keepassxc-2-8-0-debian-13)