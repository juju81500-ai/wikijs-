---
title: "Fiche Simple - VM Windows 11 mRemoteNG Sessions Connexions"
description: "Créer des connexions mRemoteNG organisées et sans mot de passe en clair."
published: true
date: 2026-10-29T20:39:58Z
tags: ["mremoteng", "windows11", "session", "connexions"]
editor: markdown
dateCreated: 2026-10-29T20:39:58Z
dateModified: 2026-10-29T20:39:58Z
---

# Fiche_Simple_-_VM_Windows_11_mRemoteNG_Sessions_Connexions

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; mRemoteNG VERSION_MREMOTENG (à remplacer)
- **Catégorie** : gestionnaire de connexions distantes
- **Tags** : `mremoteng`, `windows11`, `session`, `connexions`

---

## Problème précis à résoudre

Créer des connexions mRemoteNG organisées et sans mot de passe en clair.

## 1. Hors-Production (Lab / Test / POC)

1. Clic droit sur **Connections** > **New Folder** ; nommer DOSSIER_LAB (à remplacer).
   👉 Explication : classement logique.

2. Clic droit sur le dossier > **New Connection** ; renseigner **Hostname/IP** = HOTE_CIBLE, **Protocol** = SSH version 2 ou RDP.
   👉 Explication : définit la cible et le protocole.

3. Laisser le champ **Password** vide ; renseigner **Username** = UTILISATEUR_CIBLE (à remplacer).
   👉 Explication : le mot de passe sera saisi à la demande.

4. Pour RDP : définir **Domain** = DOMAINE (à remplacer) et vérifier la sécurité NLA dans les options du protocole.
   👉 Explication : protège l'authentification RDP.

5. Double-clic sur la connexion pour tester.
   👉 Explication : valide la cible.

## 2. Production — Contrôles

Définir une convention de nommage et un propriétaire du fichier de connexions.

## 3. Production — Sécurité

- Pas de mot de passe stocké dans les champs de connexion.
- Utiliser des comptes nominatifs.

## Validation et retour arrière

- **Validation** : La connexion s'ouvre avec le compte attendu.
- **Retour arrière** : Clic droit > **Delete** sur la connexion ou le dossier.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [mRemoteNG — documentation officielle](https://mremoteng.readthedocs.io/en/latest/)
- [mRemoteNG — dépôt et releases](https://github.com/mRemoteNG/mRemoteNG/releases)
- [mRemoteNG — site officiel](https://mremoteng.org/)