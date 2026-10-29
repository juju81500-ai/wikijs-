# Fiche_Simple_-_VM_pfSense_Vie_Systeme_02_Recuperation_De_L_Image

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 02 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Obtenir l'image officielle de pfSense CE.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'ISO depuis https://www.pfsense.org/download/ (Architecture AMD64, Installer = DVD Image (ISO), miroir au choix) puis sa somme de contrôle. En shell :
   ```sh
   mkdir -p ~/iso && cd ~/iso
   curl -fLO https://MIROIR/pfSense-CE-VERSION-RELEASE-amd64.iso.gz
   curl -fLO https://MIROIR/pfSense-CE-VERSION-RELEASE-amd64.iso.gz.sha256
   ```
   👉 Explication : `MIROIR` est l'adresse du miroir proposé par le site officiel et `VERSION` la version publiée (ex. 2.8.0); l'archive est compressée en gzip.

2. Décompresser l'image :
   ```sh
   gunzip -k pfSense-CE-VERSION-RELEASE-amd64.iso.gz
   ```
   👉 Explication : produit l'`.iso` utilisable par l'hyperviseur (`-k` conserve l'archive pour la vérification).

3. Ranger l'ISO dans le stockage de l'hyperviseur (Proxmox : Datacenter > Stockage > ISO Images > Upload).
   👉 Explication : l'image devient sélectionnable à la création de la VM.

## 2. Production — Contrôles

Utiliser un dépôt d'images interne contrôlé et tracer la version retenue.

## 3. Production — Sécurité

Télécharger uniquement depuis le site officiel de Netgate, en HTTPS.

## Validation et retour arrière

- **Validation** : Fichiers `.iso.gz` et `.sha256` présents, taille cohérente (`ls -lh`).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)