---
title: "Fiche Simple - VM Windows 11 mRemoteNG Securisation"
description: "Protéger le fichier de connexions et les identifiants mRemoteNG."
published: true
date: 2026-10-29T20:39:58Z
tags: ["mremoteng", "windows11", "securite", "credentials"]
editor: markdown
dateCreated: 2026-10-29T20:39:58Z
dateModified: 2026-10-29T20:39:58Z
---

# Fiche_Simple_-_VM_Windows_11_mRemoteNG_Securisation

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; mRemoteNG VERSION_MREMOTENG (à remplacer)
- **Catégorie** : gestionnaire de connexions distantes
- **Tags** : `mremoteng`, `windows11`, `securite`, `credentials`

---

## Problème précis à résoudre

Protéger le fichier de connexions et les identifiants mRemoteNG.

## 1. Hors-Production (Lab / Test / POC)

1. Clic droit sur **Connections** > **Properties** (racine) puis définir un mot de passe de protection MOT_DE_PASSE_FICHIER (à remplacer ; non noté).
   👉 Explication : chiffre le fichier avec un secret choisi par vous ; libellé exact à vérifier dans la version.

2. **Tools > Options > Advanced/Security** : examiner moteur de chiffrement et nombre d'itérations KDF (noms à vérifier).
   👉 Explication : les paramètres de chiffrement sont documentés par l'éditeur ; le détail n'est pas repris ici faute de vérification.

3. Décocher l'enregistrement des mots de passe dans les connexions ; utiliser le **Gestionnaire d'identifiants Windows** : `cmdkey /list`.
   👉 Explication : les secrets restent hors du fichier.

4. Restreindre le dossier : `icacls "$env:APPDATA\mRemoteNG" /inheritance:r /grant:r "${env:USERNAME}:(OI)(CI)F"`.
   👉 Explication : seul l'utilisateur accède au fichier.

5. Pour SSH, utiliser une clé privée protégée par passphrase, conservée séparément du mot de passe du fichier.
   👉 Explication : un vol de fichier ne livre pas les deux secrets.

## 2. Production — Contrôles

Documenter où est stocké MOT_DE_PASSE_FICHIER (coffre d'entreprise).

## 3. Production — Sécurité

- Le chiffrement du fichier par défaut peut utiliser un mot de passe par défaut : changer ce comportement (à vérifier dans la documentation).
- TLS/RDP : exiger NLA ; SSH : version 2 uniquement.

## Validation et retour arrière

- **Validation** : Redémarrer l'application : le mot de passe du fichier est demandé.
- **Retour arrière** : Restaurer la sauvegarde du fichier de connexions (voir fiche Sauvegarde_Restauration).

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [mRemoteNG — documentation officielle](https://mremoteng.readthedocs.io/en/latest/)
- [mRemoteNG — dépôt et releases](https://github.com/mRemoteNG/mRemoteNG/releases)
- [mRemoteNG — site officiel](https://mremoteng.org/)