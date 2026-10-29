# Fiche_Simple_-_TrueNAS_SCALE_25.10_Deploiement_Telecharger_Installer.md

- **Environnement** : NAS autonome pilote (matériel x86-64 ou VM de laboratoire)
- **OS / Version** : TrueNAS SCALE 25.10 Community Edition
- **Catégorie** : stockage NAS / installation
- **Tags** : `truenas`, `scale2510`, `zfs`, `nas`, `smb`, `sauvegarde`

---

## Problème précis à résoudre

Installer SCALE 25.10 à partir d'une ISO vérifiée.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'ISO depuis **https://www.truenas.com/download/** puis calculer son SHA-256 (Linux) :
   ```bash
   sha256sum truenas-scale-25.10.iso
   ```
   👉 Explication : (nom de fichier d'exemple à remplacer) à comparer avec l'empreinte publiée.

2. Équivalent Windows :
   ```powershell
   Get-FileHash .\truenas-scale-25.10.iso -Algorithm SHA256
   ```
   👉 Explication : même contrôle sous PowerShell.

3. Démarrer l'ISO en UEFI et choisir le périphérique de boot.
   👉 Explication : l'installateur efface le disque choisi.

4. Après redémarrage, ouvrir l'adresse de la console, définir un compte admin dédié, un mot de passe unique, le nom d'hôte, une IP statique, DNS et NTP.
   👉 Explication : configuration minimale de gestion.

5. Passer l'interface en HTTPS avec un certificat approuvé.
   👉 Explication : protège les identifiants d'administration.

## 2. Production — Contrôles

Ne jamais exposer l'interface d'administration à Internet.

## 3. Production — Sécurité

- Empreinte ou signature vérifiée avant création du média.

## Validation et retour arrière

- **Validation** : L'interface répond en HTTPS avec l'IP prévue.
- **Retour arrière** : Réinstaller depuis l'ISO vérifiée en cas d'échec (lab).

## Si le problème n'est pas résolu

- [TrueNAS SCALE 25.10 — installation](https://www.truenas.com/docs/scale/25.10/gettingstarted/install/installingscale/)
- [TrueNAS SCALE 25.10 — guide matériel](https://www.truenas.com/docs/scale/25.10/gettingstarted/scalehardwareguide/)
- [Guide complet — 2. Télécharger, vérifier et installer](../../../../../../02-Fiches-Completes/TrueNAS/SCALE-25.10/Installation-Deploiement/60_Deploiement_TrueNAS_SCALE_25.10.md#2-telecharger-verifier-et-installer)
