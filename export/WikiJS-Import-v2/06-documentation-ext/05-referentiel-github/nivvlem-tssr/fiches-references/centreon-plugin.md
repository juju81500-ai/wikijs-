---
title: "Créer un plugin personnalisé pour Centreon"
description: "Les plugins personnalisés permettent d’étendre les capacités de supervision de Centreon (et Nagios) pour surveiller des applications ou métriques spécifiques. Ils sont des scripts exécutables (Bash, Python, Perl…) qui retournent un code d’état Nagios et un message interprétable par Centreon."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Créer un plugin personnalisé pour Centreon

## 📌 Présentation

Les plugins personnalisés permettent d’étendre les capacités de supervision de Centreon (et Nagios) pour surveiller des applications ou métriques spécifiques. Ils sont des **scripts exécutables** (Bash, Python, Perl…) qui retournent un **code d’état Nagios** et un **message interprétable par Centreon**.

---

## ✅ Format attendu d’un plugin

Un plugin doit :
- retourner l’un de ces codes de sortie :
  - `0` → OK
  - `1` → WARNING
  - `2` → CRITICAL
  - `3` → UNKNOWN
- afficher une sortie standard du type :
```bash
STATUT - Message utilisateur | perfdata
```

---

## 🐚 Exemple en Bash

```bash
#!/bin/bash
usage=$(df / | awk 'NR==2 {print $5}' | tr -d '%')

if [ "$usage" -ge 90 ]; then
  echo "CRITICAL - Disk usage at ${usage}% | usage=${usage}%"
  exit 2
elif [ "$usage" -ge 75 ]; then
  echo "WARNING - Disk usage at ${usage}% | usage=${usage}%"
  exit 1
else
  echo "OK - Disk usage at ${usage}% | usage=${usage}%"
  exit 0
fi
```

---

## 🐍 Exemple en Python

```python
#!/usr/bin/env python3
import shutil

total, used, free = shutil.disk_usage("/")
usage = used / total * 100

if usage > 90:
    print(f"CRITICAL - Disk usage: {usage:.2f}% | usage={usage:.2f}%")
    exit(2)
elif usage > 75:
    print(f"WARNING - Disk usage: {usage:.2f}% | usage={usage:.2f}%")
    exit(1)
else:
    print(f"OK - Disk usage: {usage:.2f}% | usage={usage:.2f}%")
    exit(0)
```

---

## 🧙 Exemple en Perl (héritage Nagios)

```perl
#!/usr/bin/perl
use strict;
use warnings;

my $cpu = `top -bn1 | grep 'Cpu(s)' | awk '{print \$2 + \$4}'`;
chomp($cpu);

if ($cpu > 90) {
  print "CRITICAL - CPU usage at $cpu% | cpu=$cpu%\n";
  exit 2;
} elsif ($cpu > 75) {
  print "WARNING - CPU usage at $cpu% | cpu=$cpu%\n";
  exit 1;
} else {
  print "OK - CPU usage at $cpu% | cpu=$cpu%\n";
  exit 0;
}
```

---

## 📂 Emplacement recommandé

Copier le plugin dans l’un des répertoires suivants selon la distribution :

```bash
/usr/lib/nagios/plugins/
/usr/lib/centreon/plugins/
```
Et le rendre exécutable :
```bash
chmod +x check_custom_disk.sh
```

---

## 🧪 Test local avant intégration

```bash
./check_custom_disk.sh
```

## 📎 Intégration dans Centreon

1. Configuration > Modèles > Services : créer un **template personnalisé**
2. Commande à utiliser : `/usr/lib/nagios/plugins/check_custom_disk.sh`
3. Ajouter le service à un hôte depuis la configuration

---

## ✅ Bonnes pratiques

- Toujours tester le plugin **en local** avant ajout dans Centreon
- Ajouter une section `--help` pour faciliter l’utilisation
- Respecter la convention Nagios (code retour + sortie formatée)
- Ajouter des **données de performance** (`| nom=valeur;warn;crit`) si possible
- Utiliser des noms explicites : `check_custom_XXX.sh`

---

## 📚 Ressources complémentaires
- [Nagios Plugin Development Guidelines](https://nagios-plugins.org/doc/guidelines.html)