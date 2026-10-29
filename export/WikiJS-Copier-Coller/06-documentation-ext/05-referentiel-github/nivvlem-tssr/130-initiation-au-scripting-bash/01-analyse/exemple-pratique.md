# TP 1 – Préparation d’un café : de l’énoncé à l’algorithme

## 📄 Énoncé du TP

Nous devons modéliser le processus de **préparation d’un café** à l’aide d’un **algorithme**.

### 🔧 Cahier des charges

Pour faire du café, il faut :
- De l’eau
- Du café moulu
- Un filtre
- Une cafetière
- De l’électricité

La quantité de café et d’eau varie selon le **nombre de tasses** souhaitées. Ce nombre (`n`) doit être **connu avant le début de la préparation**.

---

## 💡 Résolution – Pseudo-code

Voici une proposition d’algorithme, rédigée en pseudo-code :
```
Si j’ai de l’eau Je continue Sinon Fin du script
finSI

Si j’ai du café Je continue Sinon Fin du script
finSI

Si j’ai un filtre Je continue Sinon Fin du script
finSI

Si j’ai une cafetière Je continue Sinon Fin du script
finSI

Si j’ai de l’électricité Je continue Sinon Fin du script
finSI

Je dois faire n tasses d est le nombre de doses ajoutées d commence à 0

Tant que d est différent de n Ajouter une dose de café Ajouter une dose d’eau Incrémenter d de 1
finTantQue

Allumer la cafetière
```

---

## 🧭 Représentation par organigramme (description)

Voici une transcription simplifiée de l’organigramme (sans image) :

- **Début**
- Vérifier la présence :
  - d’eau
  - de café
  - de filtre
  - de cafetière
  - d’électricité
  → Si un seul élément manque → **Fin**
- Initialiser : `n = nombre de tasses`, `d = 0`
- **Tant que** `d ≠ n` :
  - Ajouter une dose de café
  - Ajouter une dose d’eau
  - `d = d + 1`
- Allumer la cafetière
- **Fin**

> ✅ **Bonne pratique** : toujours valider les prérequis avant d’exécuter des actions répétées.

---

# TP 2 – Script Bash : automatiser la préparation d’un café ☕

## 🖥️ Script Bash complet

```bash
#!/bin/bash

# Vérifications des prérequis
if [ "$eau" != "oui" ]; then
  echo "Pas d'eau disponible, arrêt du script."
  exit 1
fi

if [ "$cafe" != "oui" ]; then
  echo "Pas de café disponible, arrêt du script."
  exit 1
fi

if [ "$filtre" != "oui" ]; then
  echo "Pas de filtre, arrêt du script."
  exit 1
fi

if [ "$cafetière" != "oui" ]; then
  echo "Pas de cafetière, arrêt du script."
  exit 1
fi

if [ "$electricite" != "oui" ]; then
  echo "Pas d'électricité, arrêt du script."
  exit 1
fi

# Préparation du café
read -p "Combien de tasses de café souhaitez-vous ? " n
d=0

while [ "$d" -lt "$n" ]; do
  echo "Ajout d'une dose de café..."
  echo "Ajout d'une dose d'eau..."
  d=$((d + 1))
done

echo "Allumage de la cafetière... ☕"
```

---

## 🧠 Explication pas à pas

**Ligne(s)** : Fonction  
`#!/bin/bash` : Spécifie l’interpréteur Bash à utiliser  
`if [...]` : Vérifie si les ressources nécessaires sont disponibles  
`exit 1` : Termine le script avec une erreur si une ressource est manquante  
`read -p ...` : Demande à l'utilisateur combien de tasses il veut  
`while [ "$d" -lt "$n" ]` : Boucle de préparation selon le nombre de tasses demandé  
`echo ...` : Affiche les étapes de la préparation  
`d=$((d + 1))` : Incrémente le nombre de doses versées  

> ⚠️ **Important** : ici, on suppose que les variables `eau`, `cafe`, `filtre`, etc., sont définies dans l’environnement ou en début de script. Tu peux les ajouter avec `read` ou les fixer en haut du script pour tester.

---

## ✅ Bonnes pratiques

- Toujours utiliser `#!/bin/bash` en première ligne.
- Utiliser `exit 1` en cas d’erreur pour que les appels externes (ex: cron) sachent que ça a échoué.
- Ajouter des commentaires pour clarifier chaque bloc.
- Prévoir un comportement **par défaut** en cas de saisie invalide (`read -p` avec validation par exemple).