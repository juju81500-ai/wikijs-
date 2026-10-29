# Déployer draw.io Desktop 32.6.1 sur Debian 13

- **OS / Version** : Debian 13 Trixie amd64; draw.io Desktop 32.6.1
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : paquet `.deb` officiel, création et export de diagrammes locaux hors ligne
- **Catégorie** : documentation technique / schémas
- **Tags** : `drawio`, `diagramsnet`, `debian13`, `diagramme`, `offline`, `documentation`

## 1. Choix et périmètre

Fiche simple : [cadrer le choix draw.io Desktop](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/draw.io/Fiche_Simple_-_VM_Debian_13_draw_io_Cadrer.md).

Au 27 octobre 2026, la release stable la plus récente consultée est draw.io Desktop 32.6.1. Le projet fournit un paquet `.deb` amd64 et l'API GitHub de la release publie son digest SHA-256. Cette procédure ne couvre pas Microsoft Visio, les intégrations Cloud, la collaboration en ligne, l'IA ou les plugins tiers.

La version Desktop est conçue pour créer, ouvrir et enregistrer des diagrammes sur le poste, y compris sans connexion Internet. Pour un environnement sensible, télécharger et contrôler le paquet depuis un poste connecté approuvé, puis transférer l'artefact vérifié selon la procédure de l'organisation. Ne pas placer dans un dessin des mots de passe, tokens ou données sans classification connue.

## 2. Télécharger et vérifier le paquet

Fiche simple : [télécharger et vérifier le paquet draw.io](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/draw.io/Fiche_Simple_-_VM_Debian_13_draw_io_Telecharger.md).

Utiliser le paquet de release GitHub officiel, et non un miroir ou un paquet trouvé sur un site tiers :

```bash
cd /tmp
curl --fail --location --proto '=https' --tlsv1.2 -o drawio-amd64-32.6.1.deb https://github.com/jgraph/drawio-desktop/releases/download/v32.6.1/drawio-amd64-32.6.1.deb
echo '515a975fbdb982e0d736b6f99248dbbb856a8b07bb72d6d3648a54b850fa33db  drawio-amd64-32.6.1.deb' | sha256sum --check
```

L'empreinte doit afficher `OK`. Elle correspond au champ `digest` de l'asset dans l'API GitHub de la release 32.6.1. Si le contrôle échoue, supprimer le fichier téléchargé et ne pas installer.

## 3. Installer l'application

Fiche simple : [installer draw.io Desktop](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/draw.io/Fiche_Simple_-_VM_Debian_13_draw_io_Installer.md).

Vérifier l'architecture et les métadonnées du paquet, puis laisser APT résoudre ses dépendances :

```bash
dpkg --print-architecture
dpkg-deb --info /tmp/drawio-amd64-32.6.1.deb
sudo apt install /tmp/drawio-amd64-32.6.1.deb
```

Lancer draw.io depuis le menu de l'environnement graphique. Lors de la première ouverture, créer un fichier de test dans un dossier utilisateur approuvé, le fermer puis le rouvrir. Une installation Desktop peut tourner hors ligne; les intégrations Cloud et fonctions en ligne ne sont pas disponibles.

## 4. Créer un diagramme technique exploitable

Fiche simple : [créer un diagramme technique draw.io](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/draw.io/Fiche_Simple_-_VM_Debian_13_draw_io_Creer_Diagramme.md).

1. Créer le dossier du livrable avec les sous-dossiers `source/` et `exports/`.
2. Créer un diagramme vierge, choisir la taille de page et donner au fichier source un nom explicite avec date ou version de révision.
3. Séparer visuellement zones, composants, interfaces, flux et responsabilités; distinguer les flux autorisés des flux à valider.
4. Ajouter une légende, un titre, la date, le propriétaire et les références documentaires utiles. Garder les valeurs de secrets et données personnelles hors du dessin.
5. Enregistrer le document maître en `.drawio` ou `.xml`; ces formats conservent le diagramme modifiable.
6. Exporter une copie PDF pour diffusion ou PNG/SVG pour insertion dans une documentation. L'export est une copie de présentation, pas le fichier source modifiable.

Pour un schéma d'architecture, nommer clairement les limites de confiance, les composants externes, la segmentation réseau et les dépendances. Les flèches doivent indiquer le sens du flux; ajouter les ports ou protocoles seulement lorsqu'ils sont confirmés par une source approuvée.

## 5. Contrôler le fichier et l'export

Fiche simple : [contrôler et exporter un diagramme draw.io](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/draw.io/Fiche_Simple_-_VM_Debian_13_draw_io_Controler_Export.md).

- Fermer et rouvrir le `.drawio`; vérifier les pages, les libellés, les connecteurs et l'absence de contenu coupé.
- Exporter en PDF ou SVG vers `exports/`, puis ouvrir l'export avec un lecteur distinct pour vérifier polices, multipages et lisibilité.
- Si l'export doit rester rééditable, préférer le `.drawio` original. Les exports PNG ou SVG peuvent intégrer une copie du XML selon l'option choisie; traiter ces exports comme contenant le diagramme complet.
- Vérifier qu'aucune donnée classifiée ne figure dans les métadonnées, notes, liens, commentaires ou couches masquées.
- Stocker et sauvegarder le fichier maître dans l'espace approuvé avec gestion des versions et contrôle d'accès; n'envoyer les exports qu'aux destinataires autorisés.

## 6. Mises à jour et dépannage

Fiche simple : [mettre à jour et dépanner draw.io](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/draw.io/Fiche_Simple_-_VM_Debian_13_draw_io_Maj_Depannage.md).

Contrôler la page des releases et le digest de chaque nouvel asset avant mise à jour. Pour remplacer la version, fermer l'application, sauvegarder les diagrammes, installer le `.deb` approuvé avec APT, puis ouvrir et contrôler une copie représentative avant de supprimer l'ancienne version.

Si APT signale une dépendance manquante, confirmer d'abord Debian 13 amd64 et la disponibilité des bibliothèques prévues pour cette release. Ne pas installer des dépendances provenant de distributions différentes pour contourner l'erreur. En cas de problème sur un diagramme précis, travailler sur une copie et préserver le fichier original.

## Sources

- [draw.io Desktop — releases officielles et assets](https://github.com/jgraph/drawio-desktop/releases)
- [draw.io Desktop 32.6.1 — notes de release](https://github.com/jgraph/drawio-desktop/releases/tag/v32.6.1)
- [GitHub API — digest SHA-256 de l'asset](https://api.github.com/repos/jgraph/drawio-desktop/releases/tags/v32.6.1)
- [draw.io — travail hors ligne et emplacements locaux](https://www.drawio.com/docs/security/diagrams-offline/)
- [draw.io — formats source et export](https://www.drawio.com/docs/manual/export/export-diagram/)
- [draw.io — sécurité et confidentialité des diagrammes](https://www.drawio.com/docs/security/)

La version Debian 13 amd64 n'a pas été installée ni exécutée par cette fiche. Valider le paquet sur un poste pilote, vérifier le lancement graphique et tester la réouverture et l'export avant déploiement.