# Fiche_Simple_-_VM_Debian_13_draw_io_Valider_Diagramme.md

- **Environnement** : draw.io Desktop 32.6.1 hors ligne, fichiers locaux
- **OS / Version** : Debian 13 Trixie amd64
- **Catégorie** : documentation technique / schémas

---

## Problème précis à résoudre

Vérifier qu'un diagramme maître reste modifiable, que son export est lisible et qu'aucun contenu sensible ne fuit dans le livrable.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le digest de la release officielle puis lancer l'application :
   ```bash
   sha256sum drawio-amd64-X.Y.Z.deb
   sudo apt install ./drawio-amd64-X.Y.Z.deb
   drawio --version
   ```
   👉 Explication : remplacer `X.Y.Z`; comparer le digest à celui de la page de release GitHub officielle; lancer depuis le menu des applications.

2. Créer un diagramme fictif : **Fichier > Nouveau**, ajouter composants et flèches, puis **Fichier > Enregistrer sous...** :
   ```bash
   mkdir -p ~/schemas/source ~/schemas/exports
   ```
   👉 Explication : enregistrer le maître en `.drawio` dans `source/`.

3. Fermer puis rouvrir : **Fichier > Ouvrir**.
   👉 Explication : vérifier pages, libellés, limites de zones et flèches.

4. Exporter : **Fichier > Exporter en tant que > PDF** (ou **SVG**) vers `exports/`, puis ouvrir dans un lecteur distinct :
   ```bash
   xdg-open ~/schemas/exports/schema.pdf
   ```
   👉 Explication : la copie exportée n'est pas le fichier maître.

5. Contrôler les couches masquées : **Affichage > Calques**, **Modifier > Modifier les données**.
   👉 Explication : vérifier titres, dates, références, liens, notes; exclure identifiants, secrets et données classifiées.

## 2. Production — Contrôles

Attribuer un propriétaire et un numéro de révision; valider les zones, flux, interfaces et références avec les responsables techniques avant publication.

## 3. Production — Sécurité

- Utiliser la version Desktop hors ligne pour les dessins sensibles; les intégrations cloud ne sont pas incluses dans cette fiche.
- Garder le fichier `.drawio` maître dans un emplacement versionné et approuvé; limiter les accès.
- Traiter PDF/SVG/PNG comme des copies pouvant exposer le contenu du diagramme; inspecter aussi métadonnées et couches masquées.
- Téléchargements seulement depuis la release officielle, digest vérifié, mises à jour testées sur un poste pilote.

## Validation et retour arrière

- **Validation** : fichier maître rouvert, export lisible, contenu sensible absent, version et propriétaire consignés.
- **Retour arrière** : conserver une copie du fichier précédent et restaurer cette version si la nouvelle est corrompue.

## Si le problème n'est pas résolu

- [draw.io — format des exports](https://www.drawio.com/docs/manual/export/export-diagram/)
- [draw.io — documentation Desktop hors ligne](https://www.drawio.com/docs/security/diagrams-offline/)
- [Guide complet draw.io Desktop 32.6.1 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/76-deploiement-draw-io-desktop-32-6-1-debian-13)