---
title: "GPO (Group Policy Objects)"
description: "Les GPO (Stratégies de groupe) sont des règles administratives utilisées dans les environnements Active Directory pour configurer de façon centralisée les systèmes, utilisateurs et applications. Elles permettent de gérer la sécurité, les scripts, les déploiements logiciels, les restrictions utilisat"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# GPO (Group Policy Objects)

## 📌 Présentation

Les GPO (Stratégies de groupe) sont des règles administratives utilisées dans les environnements Active Directory pour configurer de façon centralisée les systèmes, utilisateurs et applications. Elles permettent de gérer la sécurité, les scripts, les déploiements logiciels, les restrictions utilisateurs et bien plus.

---

## 🧰 Outils de gestion

| Outil | Description | Exemple d'utilisation |
|-------|-------------|------------------------|
| `GPMC.msc` | Console de gestion des GPO | Création et liaison de GPO à une OU |
| `gpedit.msc` | Éditeur de stratégie locale | Test de GPO sur poste non lié à AD |
| `gpupdate` | Applique les GPO manuellement | `gpupdate /force` |
| `rsop.msc` | Résultat des stratégies effectives | Diagnostic de conflits ou héritage |
| `gpresult` | Affiche les GPO appliquées | `gpresult /r` ou `/h rapport.html` |
| `Get-GPO` | Cmdlet PowerShell (module GPMC) | `Get-GPO -All` |
| `New-GPO`, `Set-GPLink` | Crée et lie une GPO | `New-GPO -Name "Sécurité"` |

---

## 🗂️ Types de stratégies

- **Stratégies d’ordinateur** : appliquées au démarrage (services, registres, scripts, restrictions système)
- **Stratégies d’utilisateur** : appliquées à l’ouverture de session (bureau, menus, restriction accès)

---

## 🔑 Paramètres courants

- 🔐 Sécurité : interdiction de l’USB, force du mot de passe
- 🖥️ Interface : désactiver le panneau de configuration, rediriger les dossiers utilisateurs
- 💡 Scripts : exécuter des scripts au démarrage / fermeture / connexion / déconnexion
- 📦 Déploiement de logiciels : installation automatique via MSI
- 🔄 Redirection de dossiers : Documents, Bureau, AppData vers serveur

---

## 🔎 Cas d’usage courant

- Uniformiser les postes utilisateurs (fond d’écran, restrictions, imprimantes)
- Appliquer des règles de sécurité (firewall, antivirus, contrôle des périphériques)
- Déploiement automatisé de logiciels
- Gérer des scripts d’ouverture de session

---

## ⚠️ Erreurs fréquentes

- Mauvaise hiérarchie OU → GPO appliquée au mauvais groupe
- Conflits entre GPO liées à différents niveaux (site, domaine, OU)
- Oublier d’utiliser le filtrage de sécurité ou WMI
- GPO créée mais non liée (`Set-GPLink` manquant)
- Scripts en .bat ou .ps1 mal référencés ou non accessibles en réseau

---

## ✅ Bonnes pratiques

- Toujours documenter les GPO créées (nom, but, date)
- Privilégier des GPO **thématiques et ciblées** plutôt qu’une unique GPO massive
- Utiliser des filtres de sécurité pour cibler les utilisateurs/machines spécifiques
- Tester d’abord sur une OU de test avant déploiement global
- Utiliser `gpupdate /force` pour vérifier la bonne application

---

## 📚 Ressources complémentaires

- [Docs GPMC PowerShell](https://learn.microsoft.com/en-us/powershell/module/grouppolicy/)
- `gpresult`, `rsop.msc`, `gpedit.msc`, `GPMC.msc`