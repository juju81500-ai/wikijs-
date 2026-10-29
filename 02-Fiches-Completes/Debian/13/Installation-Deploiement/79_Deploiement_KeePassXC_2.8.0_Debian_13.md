# Déployer KeePassXC 2.8.0 sur Debian 13

- **OS / Version** : Debian 13 Trixie amd64; KeePassXC 2.8.0 stable
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : AppImage x86-64 officiel, création de coffre KDBX, sauvegarde et restauration
- **Catégorie** : gestionnaire de mots de passe local
- **Tags** : `keepassxc`, `debian13`, `gestionnaire-mots-de-passe`, `kdbx`, `argon2id`, `sauvegarde`

## 1. Version et périmètre

Fiche simple : [vérifier version et périmètre](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/KeePassXC/Fiche_Simple_-_VM_Debian_13_KeePassXC_Version_Perimetre.md).

Au 27 octobre 2026, KeePassXC 2.8.0 est la version stable publiée par le projet. Cette procédure utilise l'AppImage x86-64 officielle, distribuée avec une signature PGP et un digest SHA-256. L'application fonctionne comme un poste de travail local; aucun serveur de coffre n'est déployé.

La release 2.8.0 inclut des correctifs de sécurité, notamment pour l'import de bases KDB legacy construites de façon malveillante et l'intégration navigateur. Garder l'application à jour et ne jamais importer une base legacy ou activer une extension provenant d'une source non fiable. Ce guide n'a pas été testé sur une machine Debian 13.

## 2. Télécharger et vérifier l'AppImage

Fiche simple : [télécharger et vérifier l'AppImage](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/KeePassXC/Fiche_Simple_-_VM_Debian_13_KeePassXC_Telecharger_Verifier.md).

Télécharger les trois fichiers depuis les assets de la release officielle, dans un répertoire utilisateur dédié :

```bash
mkdir -p "$HOME/Téléchargements/keepassxc-2.8.0"
cd "$HOME/Téléchargements/keepassxc-2.8.0"
curl --fail --location --proto '=https' --tlsv1.2 -O https://github.com/keepassxreboot/keepassxc/releases/download/2.8.0/KeePassXC-2.8.0-1-x86_64.AppImage
curl --fail --location --proto '=https' --tlsv1.2 -O https://github.com/keepassxreboot/keepassxc/releases/download/2.8.0/KeePassXC-2.8.0-1-x86_64.AppImage.sig
curl --fail --location --proto '=https' --tlsv1.2 -O https://github.com/keepassxreboot/keepassxc/releases/download/2.8.0/KeePassXC-2.8.0-1-x86_64.AppImage.DIGEST
```

Importer la clé de publication depuis le serveur de clés indiqué par KeePassXC, puis vérifier que son empreinte primaire correspond à celle publiée par le projet : `BF5A 669F 2272 CF43 24C1 FDA8 CFB4 C216 6397 D0D2`.

```bash
gpg --keyserver keys.openpgp.org --recv-keys BF5A669F2272CF4324C1FDA8CFB4C2166397D0D2
gpg --fingerprint BF5A669F2272CF4324C1FDA8CFB4C2166397D0D2
gpg --verify KeePassXC-2.8.0-1-x86_64.AppImage.sig KeePassXC-2.8.0-1-x86_64.AppImage
shasum -a 256 -c KeePassXC-2.8.0-1-x86_64.AppImage.DIGEST
```

Ne pas exécuter le fichier si la signature est invalide, si l'empreinte ne correspond pas à la documentation officielle ou si le digest ne confirme pas `OK`. Un avertissement GPG sur le niveau de confiance n'est acceptable que si l'empreinte vérifiée est exactement celle publiée par le projet.

## 3. Lancer l'application sans privilèges

Fiche simple : [lancer l'application sans privilèges](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/KeePassXC/Fiche_Simple_-_VM_Debian_13_KeePassXC_Lancer.md).

Rendre l'AppImage exécutable et la lancer avec le compte utilisateur, jamais avec `sudo` :

```bash
chmod 700 KeePassXC-2.8.0-1-x86_64.AppImage
./KeePassXC-2.8.0-1-x86_64.AppImage
```

Confirmer la version affichée par l'application. Si le démarrage échoue à cause du montage AppImage/FUSE, installer uniquement la dépendance FUSE disponible dans les dépôts Debian 13, puis réessayer; ne pas lancer le binaire en root ni désactiver les contrôles du système.

## 4. Créer un coffre KDBX

Fiche simple : [créer un coffre KDBX](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/KeePassXC/Fiche_Simple_-_VM_Debian_13_KeePassXC_Creer_Coffre.md).

1. Dans l'assistant, créer une nouvelle base et choisir un emplacement dans le profil utilisateur ou un volume chiffré contrôlé. Utiliser l'extension `.kdbx`.
2. Conserver le format KDBX 4 et le réglage de chiffrement recommandé par l'application. Dans les paramètres avancés, KeePassXC recommande Argon2id; ne modifier ses paramètres qu'en fonction de la compatibilité requise et du temps de déverrouillage mesuré.
3. Créer un mot de passe maître long, unique et généré aléatoirement. Le mémoriser ou le conserver dans une procédure de récupération approuvée, séparée du fichier KDBX. La perte du mot de passe ou d'un facteur additionnel peut rendre le coffre irrécupérable.
4. N'ajouter un fichier-clé ou une clé matérielle que si la procédure de récupération et ses copies de secours sont maîtrisées. Un facteur supplémentaire manquant bloque aussi l'accès.
5. Organiser les entrées en groupes; générer des mots de passe uniques avec le générateur. Verrouiller le coffre lorsque le poste est laissé sans surveillance et définir un verrouillage automatique dans les paramètres de sécurité.

Le contenu KDBX est chiffré sur disque, mais les informations sont déchiffrées en mémoire lorsque la base est ouverte. Protéger la session de bureau, limiter les logiciels exécutés dans le profil et éviter les captures d'écran ou le presse-papiers partagé dans les environnements sensibles. Stocker un secret TOTP dans la même base que le mot de passe réduit la séparation entre facteurs; réserver cette configuration à un choix de risque explicite.

## 5. Sauvegarder et restaurer le coffre

Fiche simple : [sauvegarder et restaurer le coffre](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/KeePassXC/Fiche_Simple_-_VM_Debian_13_KeePassXC_Sauvegarder_Restaurer.md).

Dans **Tools > Settings > File Operations**, conserver les sauvegardes sûres par défaut. KeePassXC écrit un fichier temporaire à côté du coffre avant son remplacement; éviter le mode d'écriture directe, qui expose la base à la corruption en cas d'interruption. Configurer une destination de sauvegarde protégée et distincte, ou produire une copie à la demande via **Database > Save Database Backup**.

Conserver plusieurs générations du `.kdbx` dans un emplacement chiffré et contrôlé, avec au moins une copie hors du poste. La sauvegarde reste chiffrée, mais doit être protégée contre suppression, remplacement et accès non autorisé. Si un fichier-clé ou une clé matérielle protège le coffre, sauvegarder/récupérer ce facteur séparément et documenter le plan de remplacement.

Pour tester une restauration, copier une sauvegarde dans un répertoire temporaire, ouvrir cette copie dans KeePassXC avec les facteurs requis, contrôler quelques entrées de test et refermer le coffre sans écraser la base active. En cas de divergence, conserver la base active et comparer les dates/version de sauvegarde avant toute restauration. Ne pas synchroniser simultanément plusieurs copies ouvertes du même coffre : cela peut produire des conflits ou écraser des modifications.

## 6. Importer des données et utiliser l'extension navigateur

Fiche simple : [importer des données et extension navigateur](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/KeePassXC/Fiche_Simple_-_VM_Debian_13_KeePassXC_Importer_Navigateur.md).

Préférer l'import direct d'un format chiffré pris en charge lorsque c'est possible. Un CSV ou export équivalent peut contenir tous les mots de passe en clair : créer ce fichier uniquement dans un emplacement protégé, l'importer, contrôler les entrées, puis supprimer les copies et vider la corbeille selon la politique du système. La suppression simple ne garantit pas l'effacement physique sur SSD, snapshots ou sauvegardes.

L'intégration navigateur est optionnelle. Installer KeePassXC-Browser uniquement depuis le magasin officiel du navigateur, activer explicitement les navigateurs concernés dans KeePassXC, puis approuver chaque association présentée. Vérifier le domaine et l'entrée avant autorisation; ne pas approuver une demande inattendue. Sur Linux, certains navigateurs distribués en Snap ou Flatpak peuvent ne pas prendre en charge le canal natif de communication.

## 7. Vérifications et mise à jour

Fiche simple : [vérifier et mettre à jour](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/KeePassXC/Fiche_Simple_-_VM_Debian_13_KeePassXC_Verifier_Mise_A_Jour.md).

- L'empreinte de la clé, la signature PGP et le digest SHA-256 sont valides avant exécution.
- KeePassXC démarre sous l'utilisateur standard et affiche la version attendue.
- Un coffre de test s'ouvre, se verrouille, se sauvegarde et sa copie de sauvegarde se restaure.
- La sauvegarde et les éventuels facteurs supplémentaires sont accessibles par la procédure de reprise approuvée.
- Aucun CSV, export en clair, secret ou fichier-clé n'est laissé dans un répertoire temporaire partagé.

À chaque mise à jour, télécharger les nouveaux artefacts depuis le site ou les releases officielles, revérifier signature et digest, puis ouvrir une copie de sauvegarde avant d'utiliser la nouvelle version avec le coffre actif.

## Sources

- [KeePassXC — téléchargements Linux et AppImage 2.8.0](https://keepassxc.org/download/)
- [KeePassXC — release 2.8.0 et correctifs](https://github.com/keepassxreboot/keepassxc/releases/tag/2.8.0)
- [KeePassXC — vérification des signatures, clé et empreinte](https://keepassxc.org/verifying-signatures/)
- [KeePassXC — guide utilisateur, création de base et Argon2id](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_creating_your_first_database)
- [KeePassXC — sauvegardes et écritures sûres](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_database_backup_options)
- [KeePassXC — import CSV et données non chiffrées](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_importing_csv_file)

L'installation, la compatibilité AppImage/FUSE, la création et la restauration n'ont pas été testées sur Debian 13. Conserver les statuts **À revoir** et **À tester** jusqu'à validation sur un poste pilote.