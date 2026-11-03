# fiche-simple-truenas-core-13-0-deploiement-installer-laboratoire.md

- **Environnement** : Appliance TrueNAS CORE (FreeBSD) en [[Glossary:VM]] de laboratoire ou [[Glossary:NAS]] existant
- **OS / Version** : TrueNAS CORE, branche 13.0 (build exact à relever sur l'ISO)
- **Catégorie** : stockage NAS / installation
- **Tags** : `truenas-core`, `truenas`, `freebsd`, `zfs`, `smb`, `nas`

---

## Problème précis à résoudre

Installer TrueNAS CORE dans une VM de test.

## 1. Hors-Production (Lab / Test / POC)

1. Créer la VM, attacher l'ISO, démarrer et choisir **Install/Upgrade**.
   👉 Explication : lance l'installateur.

2. Sélectionner le disque de démarrage puis confirmer.
   👉 Explication : l'installateur efface le disque choisi : vérifier avant de confirmer.

3. Définir le mot de passe `root` (secret long, conservé dans le gestionnaire de secrets), choisir le mode de démarrage ([[Glossary:BIOS]] sous VMware).
   👉 Explication : le secret n'est jamais noté en clair dans un ticket.

4. Arrêter la VM, retirer l'ISO puis redémarrer.
   👉 Explication : évite de relancer l'installateur.

5. Dans le menu console, choisir **1) Configure Network Interfaces** pour une [[Glossary:IP]] fixe, puis ouvrir l'interface web en HTTPS depuis un poste d'administration.
   👉 Explication : l'adresse IP de l'interface web est affichée sur la console.

## 2. Production — Contrôles

Ne jamais exposer l'interface sur Internet.

## 3. Production — Sécurité

- Mot de passe `root` unique, interface limitée au réseau d'administration.

## Validation et retour arrière

- **Validation** : L'interface web répond en HTTPS.
- **Retour arrière** : En laboratoire, revenir au snapshot de VM pris avant l'installation.

## Si le problème n'est pas résolu

- [TrueNAS — documentation CORE 13.0](https://www.truenas.com/docs/core/13.0/)
- [TrueNAS — Software Status](https://www.truenas.com/docs/softwarestatus/)
- [Guide complet — 3. Installer (laboratoire)](../../../../../../02-fiches-completes/truenas/core-13-0/installation-deploiement/89-deploiement-truenas-core-13-0.md#3-installer-laboratoire)
