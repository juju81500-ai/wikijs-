---
title: "TP – Enchaînement conditionnel dans un script Bash"
description: "- Prendre un nom d'utilisateur en argument :"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Enchaînement conditionnel dans un script Bash

## 📄 Énoncé

### Fonctionnalités attendues du script :

- Prendre un **nom d'utilisateur** en argument :
	- Si **plus d’un argument** : afficher un message d’utilisation et quitter.
    - Si **aucun argument** : demander une saisie clavier.
        - Si **aucun nom saisi** : utiliser le nom "invité".
- Si le nom est **root** :
    - Afficher un message rouge gras sur fond noir.  
    - Quitter avec le code retour `4`. 
- Si le nom est **invité** : afficher une redirection explicite.
- Afficher un message de bienvenue avec le nom de la machine (`hostname`).
- En cas de bon déroulement : afficher "fin du script".

---

## 🧪 Script complet

```bash
#!/bin/bash

# Vérification du nombre d’arguments
if [ "$#" -gt 1 ]; then
  echo "Utilisation : $0 [nom_utilisateur]"
  exit 1
fi

# Gestion de l'entrée
if [ -z "$1" ]; then
  read -p "Entrez votre nom : " nom
  [ -z "$nom" ] && nom="invité"
else
  nom="$1"
fi

# Blocage de root
if [ "$nom" = "root" ]; then
  echo -e "\033[1;31;40mInterdit de se connecter en root\033[0m"
  exit 4
fi

# Message si redirigé sur 'invité'
[ "$nom" = "invité" ] && echo "Vous avez été redirigé sur le compte \"invité\"."

# Message de bienvenue
echo "Bonjour $nom, bienvenue sur la machine $(hostname)."

# Fin du script
echo "fin du script"
```

---

## 🧠 Explication des points-clés

| Élément               | Fonction                                                          |
| --------------------- | ----------------------------------------------------------------- |
| `$#`                  | Nombre d’arguments passés au script                               |
| `-gt`                 | Opérateur arithmétique : "greater than" (supérieur strict)        |
| `read -p`             | Saisie utilisateur                                                |
| `[ -z "$var" ]`       | Teste si la variable est vide                                     |
| `&&`                  | Exécute la commande suivante uniquement si la précédente a réussi |
| `[ "$nom" = "root" ]` | Condition spécifique pour interdire l’utilisateur "root"          |
| `\033[1;31;40m...`    | Couleur : rouge gras sur fond noir                                |

---

## ✅ À retenir pour les révisions

- Utiliser `&&` et `||` pour des conditions claires.
- Utiliser `read` avec fallback par défaut (`invité`). 
- Toujours tester les arguments (`$#`, `$1`, etc.).
- Utiliser `hostname` pour personnaliser les messages système.
- Coloriser les messages importants pour les rendre visibles.