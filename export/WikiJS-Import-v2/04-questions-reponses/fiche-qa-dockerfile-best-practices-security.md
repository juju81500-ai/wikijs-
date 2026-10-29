---
title: "Fiche Q&A : Quelles sont les bonnes pratiques pour sécuriser la création d'un Dockerfile ?"
description: "Comment rédiger un Dockerfile sécurisé et optimisé pour la production ?"
published: true
date: 2026-10-27T11:22:58Z
tags: ["docker", "dockerfile", "securite", "conteneurs", "ci-cd"]
editor: markdown
dateCreated: 2026-10-27T11:22:58Z
dateModified: 2026-10-27T11:22:58Z
---

# 📄 Fiche Q&A : Quelles sont les bonnes pratiques pour sécuriser la création d'un Dockerfile ?

- **Tags** : `docker`, `dockerfile`, `securite`, `conteneurs`, `ci-cd`

### ❓ Question
Comment rédiger un Dockerfile sécurisé et optimisé pour la production ?

---

### 📋 Procédure Pas-à-Pas (1 Instruction = 1 Explication Technique)

1. **Utiliser une image officielle maintenue et versionnée** :
   ```dockerfile
   FROM alpine:<VERSION_SUPPORTÉE>
   ```
   👉 *Explication : Vérifier la période de support et les mises à jour de sécurité avant de l'adopter ; une image minimale n'est pas automatiquement plus sûre.*

2. **Créer et utiliser un utilisateur non-privilégié (Non-Root)** :
   ```dockerfile
   RUN addgroup -S appgroup && adduser -S appuser -G appgroup
   USER appuser
   ```
   👉 *Explication : Tu réduis les privilèges dans le conteneur, sans en faire une frontière garantissant l'absence d'accès à l'hôte.*

3. **Copier uniquement les fichiers nécessaires en restreignant les droits** :
   ```dockerfile
   COPY --chown=appuser:appgroup ./app /app
   ```
   👉 *Explication : Tu attribues directement la propriété des fichiers à l'utilisateur non-root lors de la copie.*

4. **Éviter le stockage de secrets dans les variables d'environnement (`ENV`)** :
   ```dockerfile
   # NE PAS FAIRE : ENV DB_PASSWORD=<SECRET>
   ```
   👉 *Explication : Tu empêches la fuite de mots de passe ou clés API dans l'historique des calques (`docker history`).*

5. **Définir un Check de Santé natif (`HEALTHCHECK`)** :
   ```dockerfile
   HEALTHCHECK --interval=30s --timeout=3s --start-period=20s --retries=3 CMD ["/app/healthcheck"]
   ```
   👉 *Explication : Le healthcheck marque le conteneur `unhealthy` mais ne le redémarre pas à lui seul. Le programme doit exister dans l'image et vérifier réellement le service.*

---

### ⚙️ Matrice des 3 Modes d'Exécution

| Mode | Configuration Dockerfile | Niveau de Sécurité |
| :--- | :--- | :--- |
| **🧪 Hors-Prod** | Image de test versionnée et secrets factices. | Pas de privilèges hôte. |
| **⚡ Production** | Image maintenue, utilisateur non-root et contexte `.dockerignore` minimal. | Scans et mises à jour régulières. |
| **🔒 Production renforcée** | Image épinglée par digest, build reproductible, secrets BuildKit/runtime et SBOM. | Scan CI, signature/provenance et healthcheck adapté. |