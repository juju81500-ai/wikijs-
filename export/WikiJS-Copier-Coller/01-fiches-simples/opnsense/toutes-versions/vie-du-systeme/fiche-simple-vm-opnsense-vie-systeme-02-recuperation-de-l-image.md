# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_02_Recuperation_De_L_Image

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 02 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Obtenir l'image officielle d'OPNsense.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'image `dvd` (ISO) ou `vga`/`serial` (clé USB) depuis la page officielle https://opnsense.org/download/ (Architecture amd64, Type dvd, Miroir au choix). En shell :
   ```sh
   mkdir -p ~/iso && cd ~/iso
   curl -fLO https://MIROIR/releases/VERSION/OPNsense-VERSION-dvd-amd64.iso.bz2
   curl -fLO https://MIROIR/releases/VERSION/OPNsense-VERSION-checksums-amd64.sha256
   ```
   👉 Explication : `MIROIR` est l'adresse d'un miroir listé sur opnsense.org et `VERSION` la version publiée (ex. 25.1); l'image est compressée en bzip2 et le fichier de sommes de contrôle accompagne la version.

2. Décompresser l'image :
   ```sh
   bunzip2 -k OPNsense-VERSION-dvd-amd64.iso.bz2
   ```
   👉 Explication : produit l'`.iso` utilisable par l'hyperviseur (`-k` conserve l'archive pour la vérification).

3. Ranger l'ISO dans le stockage de l'hyperviseur (Proxmox : Datacenter > Stockage > ISO Images > Upload).
   👉 Explication : l'image devient sélectionnable à la création de la VM.

## 2. Production — Contrôles

Utiliser un dépôt d'images interne contrôlé et tracer la version retenue.

## 3. Production — Sécurité

Télécharger uniquement depuis un miroir listé sur opnsense.org, en HTTPS.

## Validation et retour arrière

- **Validation** : Fichiers `.iso.bz2` et `.sha256` présents, taille cohérente (`ls -lh`).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)