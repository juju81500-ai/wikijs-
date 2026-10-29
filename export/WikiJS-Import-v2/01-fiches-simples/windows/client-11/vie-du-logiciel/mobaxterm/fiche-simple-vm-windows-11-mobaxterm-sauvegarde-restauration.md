---
title: "Fiche Simple - VM Windows 11 MobaXterm Sauvegarde Restauration"
description: "Sauvegarder et restaurer la configuration MobaXterm (sessions et paramètres)."
published: true
date: 2026-10-29T20:39:58Z
tags: ["mobaxterm", "windows11", "sauvegarde", "restauration"]
editor: markdown
dateCreated: 2026-10-29T20:39:58Z
dateModified: 2026-10-29T20:39:58Z
---

# Fiche_Simple_-_VM_Windows_11_MobaXterm_Sauvegarde_Restauration

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; MobaXterm Home/Professional, version VERSION_MOBAXTERM (à remplacer)
- **Catégorie** : client SSH/RDP multi-sessions
- **Tags** : `mobaxterm`, `windows11`, `sauvegarde`, `restauration`

---

## Problème précis à résoudre

Sauvegarder et restaurer la configuration MobaXterm (sessions et paramètres).

## 1. Hors-Production (Lab / Test / POC)

1. GUI : **Settings > Configuration > General**, noter l'emplacement du **Persistent home directory** et le chemin de sauvegarde des sessions.
   👉 Explication : la fiche ne suppose pas de chemin fixe : à vérifier dans l'interface selon la version.

2. Exporter : clic droit dans le panneau Sessions > **Export sessions** (libellé à vérifier) vers `C:\Sauvegardes\MobaXterm\`.
   👉 Explication : produit un fichier de sessions.

3. Copier le fichier de configuration : `Copy-Item "$env:APPDATA\MobaXterm\MobaXterm.ini" "C:\Sauvegardes\MobaXterm\MobaXterm_DATE.ini"` (DATE à remplacer ; chemin `MobaXterm.ini` à vérifier).
   👉 Explication : copie rapide des paramètres si le fichier existe à cet endroit.

4. Restaurer : fermer MobaXterm, recopier le fichier avec `Copy-Item` inverse, puis relancer.
   👉 Explication : évite l'écrasement pendant l'exécution.

5. Importer des sessions : **Import sessions** puis choisir le fichier.
   👉 Explication : réinjecte les sessions.

## 2. Production — Contrôles

Planifier la sauvegarde et tester la restauration sur une VM vierge.

## 3. Production — Sécurité

- Chiffrer le dossier de sauvegarde (BitLocker ou archive chiffrée).
- Vérifier qu'aucun mot de passe en clair n'est contenu dans l'export avant de le partager.

## Validation et retour arrière

- **Validation** : Après restauration, les sessions et la version attendue réapparaissent.
- **Retour arrière** : Remettre le fichier .ini précédent depuis `C:\Sauvegardes\MobaXterm\`.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [MobaXterm — documentation officielle](https://mobaxterm.mobatek.net/documentation.html)
- [MobaXterm — téléchargement](https://mobaxterm.mobatek.net/download.html)
- [MobaXterm — FAQ](https://mobaxterm.mobatek.net/faq.html)