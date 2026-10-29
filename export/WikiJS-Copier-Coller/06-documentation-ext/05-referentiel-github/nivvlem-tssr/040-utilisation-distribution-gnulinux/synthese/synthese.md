# 🌐 Synthèse – Utilisation de distributions GNU/Linux

## 🧱 Notions fondamentales

### ✅ À connaître absolument

- **Structure Unix/Linux** : arborescence unique (`/`), tout est fichier.
- **Noyau** = `kernel` : cœur du système, gère mémoire, périphériques, utilisateurs.
- **Shell (Bash)** : interpréteur de commandes.
- **OS Linux ≠ logiciel libre**, mais **souvent** associé au mouvement libre GNU (licences GPL, etc.).
- Distributions principales : Debian, Ubuntu, RedHat, CentOS, Kali, Arch, etc.

### 📁 Répertoires importants

|Répertoire|Usage|
|---|---|
|`/etc`|Fichiers de configuration|
|`/home`|Répertoires utilisateurs|
|`/var`|Logs, fichiers temporaires|
|`/bin`, `/sbin`, `/usr/bin`|Commandes essentielles|
|`/dev`, `/proc`, `/sys`|Interfaces avec le noyau et le matériel|

---

## 💻 Commandes essentielles à maîtriser

### 📂 Fichiers et dossiers

```bash
pwd         # Affiche le répertoire courant
cd ..       # Remonte d’un niveau
mkdir -p    # Crée dossier (arborescence)
rm -r       # Supprime récursivement
cp -r       # Copie récursive
mv          # Déplace ou renomme
ls -lhA     # Liste détaillée et fichiers cachés
```

### 🧠 Informations système et utilisateur

```bash
who, whoami, id, logname     # Infos sur les utilisateurs
passwd                       # Changement de mot de passe
uname -a                     # Infos noyau et distribution
```

### 🕵️ Recherches et filtres

```bash
grep -i, -v, -n "motif" fichier   # Rechercher dans un fichier
find / -name "*.conf"             # Recherche récursive
locate fichier                    # Recherche rapide (base indexée)
updatedb                          # Met à jour la base locate
```

### 🔁 Redirections et pipes

```bash
commande > fichier      # Redirige stdout
commande 2> erreur.txt  # Redirige stderr
commande &> tout.txt    # Redirige stdout + stderr
commande | tee fichier  # Affiche + écrit dans fichier
commande | autre_commande  # Pipe entre commandes
```

### 🧰 Processus et gestion des tâches

```bash
ps -ef | grep nom      # Lister les processus
kill -9 PID            # Terminer un processus
nohup commande &       # Exécuter en arrière-plan même si déconnexion
jobs / fg / bg         # Gérer les tâches en cours
```

### 📦 Archivage et compression

```bash
tar -cvf archive.tar dossier/     # Création
-tf, -xvf, -czf, -cjvf            # Listing, extraction, compression gzip/bzip2
```

### 📐 Variables d’environnement

```bash
VAR="valeur"      # Déclaration locale
echo $VAR         # Lecture
export VAR        # Disponible dans sous-shells
unset VAR         # Suppression
```

---

## 📝 Éditeurs de texte en terminal

### ✏️ Vim (à privilégier en usage pro)

|Mode|Touche d’accès|
|---|---|
|Insertion|`i`, `a`, `o`|
|Commande|`Échap`|
|Ligne de commande|`:`|

#### Commandes utiles

```vim
:w     # enregistrer
:q     # quitter
:wq    # enregistrer et quitter
:n     # ligne suivante pour recherche
:g/pattern/d       # supprimer lignes contenant motif
:g/foo/s/bar/baz/g # remplacer dans lignes contenant foo
```

### 📁 Fins de lignes : Windows ≠ Linux

- Linux = LF (`\n`) ; Windows = CRLF (`\r\n`)
- Conversion avec : `unix2dos`, `dos2unix`, ou `:set fileformat=unix`

---

## 📌 Bonnes pratiques professionnelles

### 🔐 Sécurité & manipulation

- **Ne jamais exécuter un `rm -rf` sans vérifier** le chemin.
- Toujours tester une regex ou une commande avec `ls` ou `echo` avant de la rendre destructive.
- Ne jamais laisser de **session root** ouverte inutilement.

### 🗂️ Organisation

- Créer des arborescences claires et cohérentes (`~/scripts`, `~/backups`, etc.).
- Utiliser des noms explicites pour les fichiers, scripts, variables.

### 🧩 Scripting et automatisation

- Documenter chaque script.
- Utiliser `tee` pour tracer les exécutions dans des logs.
- Modulariser : préférer plusieurs petits scripts à un script monolithique.

### ⚙️ Personnalisation & ergonomie

- Configurer `.bashrc` ou `.vimrc` pour gagner du temps :

```bash
alias ll='ls -lhA'
export PATH="$PATH:$HOME/scripts"
```

---

## 🧠 Erreurs fréquentes à éviter

- Oublier les guillemets dans les chemins avec espaces : `"fichier avec espaces.txt"`
- Confondre `>` et `>>` (écrasement vs ajout)
- Utiliser = au lieu de == dans les scripts
- Oublier d’exporter une variable qui doit être visible dans un sous-shell
- Ne pas vérifier les droits d’exécution d’un script (`chmod +x script.sh`)

---

## ✅ À retenir pour les révisions

- Le **shell est un langage** à part entière : il permet d’automatiser, diagnostiquer, configurer.
- La **ligne de commande est incontournable** dans le monde pro Linux.
- **Savoir lire, interpréter, tester une commande** avant de l’exécuter est plus important que la mémorisation brute.

---

## 🔗 Liens utiles pour aller plus loin

- [TLDP Bash Beginner Guide](https://tldp.org/LDP/Bash-Beginners-Guide/html/)
- [Explainshell (décompose les commandes)](https://explainshell.com/)
- [Cheat.sh](https://cheat.sh/)