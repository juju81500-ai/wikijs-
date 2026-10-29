# Fiche_Simple_-_VM_Debian_13_draw_io_Controler_Export.md

- **Environnement** : draw.io Desktop sur poste Debian 13
- **OS / Version** : Debian 13 Trixie amd64; draw.io Desktop 32.6.1
- **Catégorie** : documentation / export

---

## Problème précis à résoudre

Exporter et contrôler le fichier avant diffusion.

## 1. Hors-Production (Lab / Test / POC)

1. Exporter via **Fichier > Exporter en tant que > PDF** (ou **SVG/PNG**) vers le dossier `exports/`.
   👉 Explication : l'export est une copie de présentation; le `.drawio` reste le fichier maître.

2. Contrôler le type et la présence des fichiers :
   ```bash
   ls -l "$HOME/Documents/schema-exemple/source" "$HOME/Documents/schema-exemple/exports"
   file "$HOME/Documents/schema-exemple/exports/"*
   ```
   👉 Explication : on vérifie que les formats sont les attendus.

3. Ouvrir l'export avec un lecteur distinct pour contrôler polices, pages et lisibilité.
   👉 Explication : un autre lecteur révèle les défauts d'affichage.

4. Vérifier métadonnées, notes, liens, commentaires et calques masqués.
   👉 Explication : aucune donnée classifiée ne doit y figurer; un export SVG/PNG peut embarquer le XML complet.

## 2. Production — Contrôles

Stocker le fichier maître avec gestion des versions et droits d'accès; envoyer les exports aux seuls destinataires autorisés.

## 3. Production — Sécurité

- Traiter un PNG/SVG avec XML intégré comme contenant tout le diagramme.

## Validation et retour arrière

- **Validation** : export lisible, complet et sans donnée interdite.
- **Retour arrière** : supprimer l'export fautif et refaire l'export depuis le `.drawio`.

## Si le problème n'est pas résolu

- [draw.io Desktop — releases officielles](https://github.com/jgraph/drawio-desktop/releases)
- [draw.io — travail hors ligne](https://www.drawio.com/docs/security/diagrams-offline/)
- [draw.io — formats et export](https://www.drawio.com/docs/manual/export/export-diagram/)
- [Guide complet — étape 5](/02-fiches-completes/debian/13/installation-deploiement/76-deploiement-draw-io-desktop-32-6-1-debian-13#5-controler-le-fichier-et-lexport)