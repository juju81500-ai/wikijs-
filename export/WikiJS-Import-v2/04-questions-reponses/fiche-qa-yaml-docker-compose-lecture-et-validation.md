---
title: "Fiche Q&A : Comment lire, rédiger et valider un fichier YAML (Docker Compose) ?"
description: "Comment structurer et vérifier la syntaxe d'un fichier docker-compose.yml sans erreur d'indentation ?"
published: true
date: 2026-10-27T11:12:47Z
tags: ["yaml", "docker", "compose", "validation", "conteneurs"]
editor: markdown
dateCreated: 2026-10-27T11:12:47Z
dateModified: 2026-10-27T11:12:47Z
---

# 📄 Fiche Q&A : Comment lire, rédiger et valider un fichier YAML (Docker Compose) ?

- **Tags** : `yaml`, `docker`, `compose`, `validation`, `conteneurs`

### ❓ Question
Comment structurer et vérifier la syntaxe d'un fichier `docker-compose.yml` sans erreur d'indentation ?

---

### 📋 Procédure Pas-à-Pas (1 Commande = 1 Explication Technique)

1. **Vérifier une indentation cohérente (espaces, pas de tabulations)** :
   ```yaml
   services:
     web:
       image: nginx:alpine
       ports:
             - "127.0.0.1:8080:80"
   ```
    👉 *Explication : YAML n'impose pas partout exactement deux espaces, mais les tabulations ne doivent pas servir à l'indentation. Compose moderne n'a pas besoin de la clé `version`.*

2. **Valider la configuration Compose sans démarrer le service** :
   ```bash
   docker compose config
   ```
   👉 *Explication : La commande peut afficher les variables résolues et des secrets. Ne pas publier ni joindre sa sortie sans l'avoir expurgée.*

3. **Protéger séparément les fichiers qui contiennent des secrets** :
   ```bash
   chmod 600 .env
   ```
   👉 *Explication : Restreindre les fichiers de secrets et les exclure du dépôt. Le fichier Compose seul n'est pas nécessairement secret.*

4. **Lancer les services définis en arrière-plan (Mode Detached)** :
   ```bash
   docker compose up -d
   ```
   👉 *Explication : Tu créées les réseaux, volumes et conteneurs décrits dans le fichier YAML et les exécutes en tâche de fond.*

---

### ⚙️ Matrice des 3 Modes d'Exécution

| Mode | Utilisation YAML | Sécurité Réseau & Fichier |
| :--- | :--- | :--- |
| **🧪 Hors-Prod** | Bind sur loopback, données et secrets factices. | Vérifier les logs sans données sensibles. |
| **⚡ Production** | Valider avec `docker compose config`, secrets hors dépôt et ports limités. | Accès au socket Docker réservé au besoin. |
| **🔒 Production renforcée** | Réseaux dédiés, secrets gérés par l'environnement et images versionnées. | Scans CI et contrôle d'accès minimal. |