# 📄 Fiche Q&A : Comment lire et décortiquer un script Bash (.sh) ligne par ligne ?

### ❓ Question
Comment comprendre la structure et le comportement d'un script Shell Linux ?

---

### 📋 Procédure Pas-à-Pas (1 Commande = 1 Explication Technique)

1. **Identifier l'entête Shebang (`#!/bin/bash`)** :
   ```bash
   head -n 1 script.sh
   ```
   👉 *Explication : Le Shebang indique au noyau Linux quel interpréteur binaire exécutera le fichier.*

2. **Vérifier les erreurs de syntaxe sans exécuter le script** :
   ```bash
   bash -n script.sh
   shellcheck script.sh
   ```
   👉 *Explication : `set -euo pipefail` peut être utile mais ne garantit pas la correction ; analyser le contexte et les codes de retour utilisés.*

3. **Lire les commandes et dépendances avant toute exécution**. Ne pas lancer un script reçu sans en comprendre les effets ; utiliser un environnement isolé et des données de test.

4. **Tracer uniquement dans un environnement de test avec des données expurgées** :
   ```bash
   bash -x script.sh
   ```
   👉 *Explication : Le mode `-x` exécute réellement les commandes et peut afficher des mots de passe, tokens ou données personnelles. Ne pas l'utiliser en production ni partager ses journaux sans nettoyage.*

---

### ⚙️ Matrice des 3 Modes d'Exécution

| Mode | Mode de Lecture / Exécution | Contrôle Qualité |
| :--- | :--- | :--- |
| **🧪 Hors-Prod** | Revue du code, `bash -n`, tests avec données factices. | Exécution en environnement isolé. |
| **⚡ Production** | Revue, `bash -n`, ShellCheck et permissions minimales. | Tester les erreurs et le retour arrière. |
| **🔒 Production renforcée** | Revue par pair, secrets externes au script et journaux expurgés. | Tracer uniquement sur données non sensibles. |