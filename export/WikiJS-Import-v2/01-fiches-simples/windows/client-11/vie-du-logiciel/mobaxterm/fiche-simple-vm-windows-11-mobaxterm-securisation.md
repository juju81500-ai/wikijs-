---
title: "Fiche Simple - VM Windows 11 MobaXterm Securisation"
description: "Sécuriser MobaXterm : mot de passe maître, identifiants et clés privées."
published: true
date: 2026-10-29T20:39:58Z
tags: ["mobaxterm", "windows11", "securite", "credentials"]
editor: markdown
dateCreated: 2026-10-29T20:39:58Z
dateModified: 2026-10-29T20:39:58Z
---

# Fiche_Simple_-_VM_Windows_11_MobaXterm_Securisation

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; MobaXterm Home/Professional, version VERSION_MOBAXTERM (à remplacer)
- **Catégorie** : client SSH/RDP multi-sessions
- **Tags** : `mobaxterm`, `windows11`, `securite`, `credentials`

---

## Problème précis à résoudre

Sécuriser MobaXterm : mot de passe maître, identifiants et clés privées.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Settings > Configuration > Security** (libellé à vérifier selon la version).
   👉 Explication : emplacement des options de protection.

2. Activer l'option de **mot de passe maître** (master password) et saisir MOT_DE_PASSE_MAITRE (à remplacer, non noté dans la fiche).
   👉 Explication : MobaXterm indique protéger les mots de passe enregistrés ; le détail du chiffrement n'a pas été vérifié ici.

3. Protéger la clé privée par passphrase : `ssh-keygen -t ed25519 -f "$env:USERPROFILE\.ssh\CLE_PRIVEE"` (CLE_PRIVEE à remplacer).
   👉 Explication : la clé volée reste inutilisable sans la passphrase.

4. Restreindre les droits : `icacls "$env:USERPROFILE\.ssh\CLE_PRIVEE" /inheritance:r /grant:r "${env:USERNAME}:R"`.
   👉 Explication : seul l'utilisateur lit la clé.

5. Pour un compte de service ou mot de passe, utiliser le **Gestionnaire d'identifiants Windows** (`control /name Microsoft.CredentialManager`) ou le coffre d'entreprise, pas la session.
   👉 Explication : le secret est stocké hors du fichier de configuration.

## 2. Production — Contrôles

Documenter où est conservé le mot de passe maître et la clé privée (coffre distinct).

## 3. Production — Sécurité

- Clé privée et sa passphrase conservées dans deux emplacements séparés.
- Chiffrement SSH : n'accepter que les algorithmes modernes imposés par le serveur ; ne pas réactiver d'anciens protocoles.
- Pas de secret dans les exports de configuration partagés.

## Validation et retour arrière

- **Validation** : Redémarrer MobaXterm : le mot de passe maître est demandé avant l'usage d'un secret.
- **Retour arrière** : Retirer le mot de passe maître via le même écran (ancien mot de passe requis) et supprimer la clé de test.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [MobaXterm — documentation officielle](https://mobaxterm.mobatek.net/documentation.html)
- [MobaXterm — téléchargement](https://mobaxterm.mobatek.net/download.html)
- [MobaXterm — FAQ](https://mobaxterm.mobatek.net/faq.html)