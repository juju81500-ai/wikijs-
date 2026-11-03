---
title: "TP – Mécanismes avancés de Linux et Bash"
description: "mkdir -p $HOME/process"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Mécanismes avancés de Linux et Bash 
# 🧱 TP 1 – Utilisation des systèmes

### 🔍 1. Lister les processus finissant par « d » dans un fichier dédié

```bash
mkdir -p $HOME/process
ps -e | grep d$ > $HOME/process/daemons.txt
```

### 🧾 2. Rechercher les fichiers .conf sur le système de fichiers racine

```bash
mkdir -p $HOME/resultats
find / -mount -type f -name "*.conf" 2>/dev/null | tee $HOME/resultats/fichiers.conf
```

### ⏱️ 3. Mesurer le temps d'exécution de la commande précédente

```bash
time find / -mount -type f -name "*.conf" 2>/dev/null | tee $HOME/resultats/fichiers.conf
```

### 🔢 4. Enregistrer le nombre total de fichiers trouvés

```bash
find / -mount -type f -name "*.conf" 2>/dev/null | wc -l > $HOME/resultats/compteur.txt
```

---

# 🧱 TP 2 – Archivage et compression

### 📤 1. Sauvegarder le répertoire personnel non compressé

```bash
tar cvf /tmp/$LOGNAME.tar $HOME
ls -lh /tmp/$LOGNAME.tar
```

### 🗜️ 2. Compression gzip en une seule commande

```bash
tar czvf /tmp/$LOGNAME.tar.gz $HOME
```

### 🗜️ 3. Compression bzip2

```bash
tar cjvf /tmp/$LOGNAME.tar.bz2 $HOME
```

### 📊 4. Comparaison des tailles

```bash
ls -lh /tmp/$LOGNAME.tar*
```

### ♻️ 5. Restauration dans un répertoire dédié

```bash
mkdir -p $HOME/Restaurations
tar xzvf /tmp/$LOGNAME.tar.gz -C $HOME/Restaurations
```

### 🧾 6. Nouvelle archive en excluant « Restaurations »

```bash
tar cvf /tmp/$LOGNAME-v2.tar --exclude=Restaurations $HOME
```

### ➕ 7. Mise à jour d’archive après ajout de fichier

```bash
touch $HOME/new_fichier.txt
tar uvf /tmp/$LOGNAME-v2.tar --exclude=Restaurations $HOME
```

---

# 🧱 TP 3 – Manipuler des variables

### 🏠 1. Afficher le contenu du répertoire personnel

```bash
ls $HOME
```

### 🧭 2. Afficher la variable contenant les chemins système

```bash
echo $PATH
```

### 📁 3. Créer un dossier scripts et l’ajouter au PATH (de manière pérenne)

```bash
mkdir -p $HOME/scripts
PATH="$PATH:$HOME/scripts"
echo 'export PATH="$PATH:$HOME/scripts"' >> ~/.bashrc
```

### 🙋 4. Créer une variable contenant son login

```bash
monnom="$LOGNAME"
```

### 🧮 5. Afficher toutes les variables d’environnement

```bash
env
```

### 🔄 6. Vérifier que « monnom » est vide dans un sous-shell

```bash
bash
echo $monnom  # vide
exit
```

### 🔗 7. Transformer en variable d’environnement

```bash
export monnom
```

### ✅ 8. Vérification dans un nouveau sous-shell

```bash
bash
echo $monnom  # devrait afficher le login
exit
```

---

# 🧱 TP 4 – Redirections

### 🗂️ 1. Lister les processus finissant par « d » dans daemons.txt

```bash
mkdir -p $HOME/process
ps -e | grep d$ > $HOME/process/daemons.txt
```

### 🔎 2. Trouver tous les fichiers .conf depuis la racine (stockage + affichage)

```bash
mkdir -p $HOME/resultats
find / -mount -type f -name "*.conf" 2>/dev/null | tee $HOME/resultats/fichiers.conf
```

### ⏱️ 3. Connaître le temps d’exécution de la commande précédente

```bash
time find / -mount -type f -name "*.conf" 2>/dev/null | tee $HOME/resultats/fichiers.conf
```

### 🧮 4. Compter les résultats sans passer par le fichier intermédiaire

```bash
find / -mount -type f -name "*.conf" 2>/dev/null | wc -l > $HOME/resultats/compteur.txt
```

---

## ✅ À retenir pour les révisions

- `ps`, `grep`, `find`, `tar`, `tee`, `wc`, `time`, `export` sont des commandes clés du shell avancé
- `tar` permet des sauvegardes et restaurations efficaces
- `$PATH`, `$HOME`, variables d’environnement : base de la personnalisation
- Redirections `>`, `>>`, `2>`, `&>` indispensables pour scripts pro

---

## 📌 Bonnes pratiques professionnelles

- Toujours rediriger proprement stdout et stderr dans les scripts
- Exclure les répertoires inutiles ou sensibles des sauvegardes
- S’assurer de la pérennité des chemins en modifiant `.bashrc` avec prudence
- Utiliser `tee` pour debug ou journalisation
- Valider la cohérence des archives avant suppression