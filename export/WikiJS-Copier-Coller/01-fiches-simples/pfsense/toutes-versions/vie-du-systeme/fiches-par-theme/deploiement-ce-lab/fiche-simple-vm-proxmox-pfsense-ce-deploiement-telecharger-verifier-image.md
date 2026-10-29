# Fiche_Simple_-_VM_Proxmox_pfSense_CE_Deploiement_Telecharger_Verifier_Image.md

- **Environnement** : VM pfSense CE en laboratoire sur Proxmox VE, deux interfaces (WAN et LAN isolés)
- **OS / Version** : pfSense Community Edition 2.9.0 (VM x86-64 sur Proxmox VE)
- **Catégorie** : pare-feu et routage

---

## Problème précis à résoudre

Obtenir l'image officielle Netgate et contrôler son empreinte avant usage.

## 1. Hors-Production (Lab / Test / POC)

1. Se connecter au compte Netgate Store et télécharger l'image **AMD64 ISO** du Netgate Installer.
   👉 Explication : le téléchargement est gratuit mais nécessite un compte; ne jamais utiliser une image tierce préinstallée.

2. Repérer la somme SHA-256 correspondant exactement au fichier téléchargé sur la page officielle, puis calculer l'empreinte locale :
   ```bash
   sha256sum netgate-installer-amd64.iso.gz
   ```
   👉 Explication : Netgate publie les sommes des images compressées; comparer avant décompression (adapter le nom de fichier réel).

3. Si l'empreinte diffère, supprimer le fichier et le télécharger de nouveau.
   👉 Explication : un écart indique un fichier corrompu ou altéré.

4. Dans Proxmox : **Stockage ISO > Images ISO > Téléverser** (ou **Télécharger depuis une URL**) pour déposer l'ISO validée.
   👉 Explication : l'image doit être sur le stockage ISO pour être attachée à la VM.

## 2. Production — Contrôles

Archiver la somme SHA-256 contrôlée et la source de l'image dans le dossier de changement.

## 3. Production — Sécurité

- Comparer l'empreinte avant toute utilisation.
- N'utiliser que l'image officielle Netgate.

## Validation et retour arrière

- **Validation** : l'empreinte locale est identique à celle publiée et l'ISO est visible dans Proxmox.
- **Retour arrière** : supprimer l'image téléchargée et l'ISO du stockage Proxmox.

## Si le problème n'est pas résolu

- [Netgate — télécharger l'image](https://docs.netgate.com/pfsense/en/latest/install/download-installer-image.html)
- [Netgate — pfSense CE 2.9.0](https://docs.netgate.com/pfsense/en/latest/releases/2-9-0.html)
- [Guide complet](/02-fiches-completes/pfsense/toutes-versions/installation-deploiement/70-deploiement-pfsense-ce-2-9-0-proxmox-lab#2-telecharger-et-verifier-limage-ce)