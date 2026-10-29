# Fiche_Simple_-_VM_Debian_13_GNS3_Deploiement_Sauvegarde_MAJ.md

- **Environnement** : Poste Debian 13 avec GNS3
- **OS / Version** : Debian 13 Trixie amd64; GNS3 2.2.61 stable
- **Catégorie** : simulation reseau / maintenance
- **Tags** : `gns3`, `debian13`, `sauvegarde`, `pipx`

---

## Problème précis à résoudre

Sauvegarder les projets, mettre à niveau et nettoyer.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder les projets (la licence doit permettre la copie des images) :
   ```bash
   tar -czf "$HOME/gns3-projets-$(date +%F).tar.gz" "$HOME/GNS3/projects"
   ```
   👉 Explication : on archive les fichiers projet; les images ne se sauvegardent que si leur licence le permet.

2. Noter les versions avant mise à niveau :
   ```bash
   gns3 --version
   gns3server --version
   ```
   👉 Explication : on consigne les versions GUI et serveur.

3. Mettre à niveau les deux composants vers la même stable (remplacer `2.2.61` par la nouvelle version stable) :
   ```bash
   pipx install --force gns3-server==2.2.61
   pipx install --force gns3-gui==2.2.61
   pipx inject gns3-gui gns3-server==2.2.61 PyQt6
   ```
   👉 Explication : on ouvre ensuite une copie d'un projet représentatif avant reprise.

4. Nettoyer les disques temporaires identifiés après un exercice :
   ```bash
   virsh list --all
   virsh vol-list default
   ```
   👉 Explication : on repère les ressources libvirt à supprimer; ne pas effacer ce qui appartient à d'autres personnes.

## 2. Production — Contrôles

Planifier sauvegardes, mises à niveau et ouverture d'une copie de projet sur un second poste.

## 3. Production — Sécurité

- Ne pas sauvegarder d'images non redistribuables.
- Ne pas effacer les projets d'autres utilisateurs.

## Validation et retour arrière

- **Validation** : Copie du projet ouverte avec succès après sauvegarde ou mise à niveau.
- **Retour arrière** : Restaurer l'archive des projets et réinstaller la version précédente avec `pipx install --force`.

## Si le problème n'est pas résolu

- [GNS3 — installation Linux](https://docs.gns3.com/docs/getting-started/installation/linux)
- [GNS3 — releases serveur](https://github.com/GNS3/gns3-server/releases)
- [Guide complet GNS3 Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/77_Deploiement_GNS3_2.2.61_Debian_13.md#7-sauvegarder-mettre-a-jour-et-nettoyer)
