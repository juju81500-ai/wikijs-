# Fiche_Simple_-_VM_Debian_13_draw_io_Telecharger.md

- **Environnement** : draw.io Desktop sur poste Debian 13
- **OS / Version** : Debian 13 Trixie amd64; draw.io Desktop 32.6.1
- **Catégorie** : documentation / téléchargement
- **Tags** : `debian13`, `drawio`, `deb`, `sha256`, `verification`

---

## Problème précis à résoudre

Télécharger le .deb officiel et contrôler son empreinte SHA-256.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger depuis la release GitHub officielle, dans un dossier de travail utilisateur :
   ```bash
   mkdir -p "$HOME/drawio-install" && cd "$HOME/drawio-install"
   curl --fail --location --proto '=https' --tlsv1.2 -o drawio-amd64-32.6.1.deb https://github.com/jgraph/drawio-desktop/releases/download/v32.6.1/drawio-amd64-32.6.1.deb
   ```
   👉 Explication : le fichier vient du dépôt officiel, jamais d'un miroir tiers.

2. Contrôler l'empreinte :
   ```bash
   echo '515a975fbdb982e0d736b6f99248dbbb856a8b07bb72d6d3648a54b850fa33db  drawio-amd64-32.6.1.deb' | sha256sum --check
   ```
   👉 Explication : `OK` confirme que le paquet correspond au `digest` publié par l'API GitHub de la release.

3. En cas d'échec, supprimer le fichier :
   ```bash
   rm -f drawio-amd64-32.6.1.deb
   ```
   👉 Explication : on n'installe jamais un paquet dont l'empreinte diffère.

## 2. Production — Contrôles

Si le poste est hors ligne, conserver l'empreinte avec l'artefact transféré.

## 3. Production — Sécurité

- Ne jamais installer un paquet dont le contrôle échoue.

## Validation et retour arrière

- **Validation** : `sha256sum --check` affiche `OK`.
- **Retour arrière** : supprimer le dossier `drawio-install`.

## Si le problème n'est pas résolu

- [draw.io Desktop — releases officielles](https://github.com/jgraph/drawio-desktop/releases)
- [draw.io — travail hors ligne](https://www.drawio.com/docs/security/diagrams-offline/)
- [draw.io — formats et export](https://www.drawio.com/docs/manual/export/export-diagram/)
- [Guide complet — étape 2](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/76_Deploiement_draw_io_Desktop_32.6.1_Debian_13.md#2-telecharger-et-verifier-le-paquet)
