# Bash

## 📌 Présentation

Bash (Bourne Again SHell) est l’interpréteur de commandes principal sur les systèmes GNU/Linux. Il permet d’exécuter des commandes, de manipuler des fichiers, d’automatiser des tâches via des scripts et d’interagir avec le système de manière fine.

---

## 🧰 Commandes essentielles

| Commande | Description | Arguments utiles | Exemple |
|---------|-------------|------------------|---------|
| `ls` | Liste le contenu d’un répertoire | `-l` (long), `-a` (fichiers cachés), `-h` (tailles lisibles) | `ls -lah` |
| `cd` | Change de répertoire | chemin relatif ou absolu | `cd /etc` |
| `pwd` | Affiche le chemin du répertoire courant | Aucun | `pwd` |
| `mkdir` | Crée un répertoire | `-p` (crée arborescence) | `mkdir -p dossier/test` |
| `touch` | Crée un fichier vide | Aucun | `touch fichier.txt` |
| `rm` | Supprime un fichier ou dossier | `-r` (récursif), `-f` (forcer) | `rm -rf /tmp/test` |
| `cp` | Copie un fichier ou répertoire | `-r`, `-v` | `cp -rv source/ cible/` |
| `mv` | Déplace ou renomme | Aucun | `mv ancien.txt nouveau.txt` |
| `cat` | Affiche le contenu d’un fichier | Aucun | `cat fichier.txt` |
| `less` / `more` | Pagination de fichiers longs | Aucun | `less /etc/passwd` |
| `echo` | Affiche du texte | `"texte"`, `$VARIABLE` | `echo "Bonjour $USER"` |
| `man` | Affiche le manuel d’une commande | commande | `man ls` |
| `chmod` | Modifie les permissions | `+x`, `755`, etc. | `chmod +x script.sh` |
| `chown` | Change le propriétaire | `utilisateur:groupe` | `chown user:user fichier.txt` |
| `grep` | Recherche dans du texte | `-i`, `-r`, `--color` | `grep -i "erreur" /var/log/syslog` |
| `find` | Recherche de fichiers | `-name`, `-type` | `find /etc -name "*.conf"` |
| `ps` | Liste les processus actifs | `aux`, `-ef` | `ps aux` |
| `kill` | Termine un processus | PID ou nom | `kill -9 1234` |
| `top` / `htop` | Vue dynamique des processus | Aucun | `htop` |
| `df` | Espace disque | `-h` | `df -h` |
| `du` | Taille d’un dossier | `-sh`, `-h` | `du -sh /var` |
| `tar` | Archivage | `-cvf`, `-xvf` | `tar -cvf archive.tar dossier/` |
| `nano` / `vim` | Éditeurs de texte CLI | Aucun | `vim script.sh` |

---
## 🔎 Cas d’usage courant

- Maintenance de système (création, déplacement, suppression de fichiers)
- Supervision des ressources et des processus
- Analyse de logs avec `grep`, `less`, `tail`
- Automatisation de tâches via des scripts `.sh`
- Configuration réseau et système via scripts

---

## ⚠️ Erreurs fréquentes

- **Utilisation de `rm -rf /` sans précaution** → peut supprimer tout le système
- Oubli des guillemets pour les noms de fichiers contenant des espaces
- Mauvaises permissions empêchant l’exécution des scripts
- Confusion entre `>` (écrase) et `>>` (ajoute)

---

## ✅ Bonnes pratiques

- Toujours utiliser `man` pour comprendre une commande inconnue
- Ajouter `#!/bin/bash` en début de script
- Tester les commandes dangereuses avec `echo` ou en mode sec (`--dry-run` si disponible)
- Écrire des scripts modulaires avec des fonctions
- Utiliser `set -euo pipefail` dans les scripts pour une meilleure gestion des erreurs
- Sauvegarder régulièrement les fichiers `.bashrc` ou `.bash_profile`

---

## 📚 Ressources complémentaires
- [Explainshell – Décortique les commandes bash](https://explainshell.com)
- [The Bash Guide](https://guide.bash.academy/)
- `man bash` : la bible de bash intégrée à Linux