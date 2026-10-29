---
title: "Fiche Simple - VM Windows 11 mRemoteNG Validation"
description: "Valider l'installation et la configuration mRemoteNG."
published: true
date: 2026-10-29T20:39:58Z
tags: ["mremoteng", "windows11", "validation"]
editor: markdown
dateCreated: 2026-10-29T20:39:58Z
dateModified: 2026-10-29T20:39:58Z
---

# Fiche_Simple_-_VM_Windows_11_mRemoteNG_Validation

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; mRemoteNG VERSION_MREMOTENG (à remplacer)
- **Catégorie** : gestionnaire de connexions distantes
- **Tags** : `mremoteng`, `windows11`, `validation`

---

## Problème précis à résoudre

Valider l'installation et la configuration mRemoteNG.

## 1. Hors-Production (Lab / Test / POC)

1. `Get-Process mRemoteNG | Select Name,Id,Path`.
   👉 Explication : confirme le binaire exécuté.

2. Ouvrir une connexion SSH de test puis `whoami`.
   👉 Explication : test fonctionnel.

3. Ouvrir une connexion RDP de test vers HOTE_RDP (à remplacer).
   👉 Explication : test du second protocole.

4. Vérifier l'emplacement du fichier : `Get-ChildItem "$env:APPDATA\mRemoteNG"`.
   👉 Explication : preuve que la configuration est persistée.

5. Fermer/rouvrir l'application.
   👉 Explication : vérifie la protection par mot de passe.

## 2. Production — Contrôles

Archiver les preuves sans secret dans le ticket.

## 3. Production — Sécurité

- Masquer les noms d'hôtes sensibles dans les captures.

## Validation et retour arrière

- **Validation** : Connexions fonctionnelles et fichier protégé.
- **Retour arrière** : Restaurer la configuration précédente.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [mRemoteNG — documentation officielle](https://mremoteng.readthedocs.io/en/latest/)
- [mRemoteNG — dépôt et releases](https://github.com/mRemoteNG/mRemoteNG/releases)
- [mRemoteNG — site officiel](https://mremoteng.org/)