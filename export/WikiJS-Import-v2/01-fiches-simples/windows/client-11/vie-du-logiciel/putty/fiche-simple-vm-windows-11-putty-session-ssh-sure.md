---
title: "Fiche Simple - VM Windows 11 PuTTY Session SSH Sure"
description: "Se connecter en vérifiant l'empreinte de la clé d'hôte."
published: true
date: 2026-10-29T20:14:10Z
tags: ["putty", "windows11", "ssh", "puttygen", "host-key"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Windows_11_PuTTY_Session_SSH_Sure.md

- **Environnement** : Poste Windows 11 x64 d'administration
- **OS / Version** : Windows 11 x64; PuTTY 0.85 Stable
- **Catégorie** : client SSH / connexion
- **Tags** : `putty`, `windows11`, `ssh`, `puttygen`, `host-key`

---

## Problème précis à résoudre

Se connecter en vérifiant l'empreinte de la clé d'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Obtenir adresse, port, compte et empreinte de la clé d'hôte auprès de l'administrateur par un canal indépendant.
   👉 Explication : référence de comparaison.

2. Dans PuTTY, choisir **Session > Connection type : SSH**, saisir le nom d'hôte et le port approuvés, puis **Save** sous un nom descriptif non sensible.
   👉 Explication : crée une session réutilisable.

3. Cliquer **Open** et comparer l'empreinte affichée à la première connexion avec celle reçue hors bande.
   👉 Explication : n'accepter que si algorithme et empreinte correspondent.

4. En cas de différence ou de changement de clé signalé : annuler et contacter l'administrateur.
   👉 Explication : ne pas effacer l'ancienne clé avant d'avoir compris le changement.

5. Se connecter avec le compte nominatif autorisé.
   👉 Explication : aucune connexion partagée.

## 2. Production — Contrôles

Protéger le profil Windows (les sessions et clés d'hôte sont dans le registre de l'utilisateur) et l'inclure dans les procédures de sauvegarde.

## 3. Production — Sécurité

- Ne jamais accepter automatiquement les clés d'hôte ni désactiver les vérifications SSH.

## Validation et retour arrière

- **Validation** : Connexion établie, empreinte conforme.
- **Retour arrière** : Supprimer la session enregistrée depuis **Session > Saved Sessions > Delete**.

## Si le problème n'est pas résolu

- [PuTTY — page officielle](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
- [PuTTY — clés de signature](https://www.chiark.greenend.org.uk/~sgtatham/putty/keys.html)
- [Guide complet — 5. Créer une session SSH sûre](/02-fiches-completes/windows/client-11/installation-deploiement/84-deploiement-putty-0-85-windows-11#5-creer-une-session-ssh-sure)