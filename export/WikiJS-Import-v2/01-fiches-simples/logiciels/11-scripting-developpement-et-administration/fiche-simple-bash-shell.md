---
title: "Bash / Shell"
description: "Vérifier la version de Bash et installer l'analyseur shellcheck sur une VM Debian 12, écrire un script d'administration qui s'arrête à la première erreur (set -euo pipefail), le valider par analyse statique, puis le déployer avec des droits restreints. Les tests ne se font que sur votre propre VM."
published: true
date: 2026-10-29T12:24:41Z
tags: ["[debian-12]", "[bash]", "[shell]", "[scripting]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:24:41Z
dateModified: 2026-10-29T12:24:41Z
---

# 📄 Bash / Shell

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : GNU Bash 5.2.x (paquet des dépôts Debian 12, à vérifier sur la version déployée)
- **Catégorie** : Scripting, développement et administration
- **Tags** : `[debian-12]`, `[bash]`, `[shell]`, `[scripting]`, `[hardening]`

## 🎯 Problème précis à résoudre
Vérifier la version de Bash et installer l'analyseur `shellcheck` sur une VM Debian 12, écrire un script d'administration qui s'arrête à la première erreur (`set -euo pipefail`), le valider par analyse statique, puis le déployer avec des droits restreints. Les tests ne se font que sur votre propre VM.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Contrôle de la version de Bash et installation de `shellcheck` :
```bash
bash --version
sudo apt update
sudo apt install -y shellcheck
shellcheck --version
```
👉 Explication : `bash --version` affiche le shell par défaut de Debian 12 (Bash 5.2). `shellcheck` est l'analyseur statique qui signale les erreurs courantes dans les scripts.

2. Création d'un script de test dans le dossier personnel :
```bash
mkdir -p ~/scripts-lab
nano ~/scripts-lab/verif_espace.sh
```
Contenu à saisir :
```bash
#!/usr/bin/env bash
set -euo pipefail

seuil=80
usage=$(df --output=pcent / | tail -n 1 | tr -dc '0-9')
if [ "$usage" -ge "$seuil" ]; then
    echo "Alerte : partition racine utilisée à ${usage} %" >&2
    exit 1
fi
echo "OK : partition racine utilisée à ${usage} %"
```
👉 Explication : `set -euo pipefail` arrête le script à la première erreur, à une variable non définie ou à une erreur dans un pipeline. Le code de sortie `1` permet à une supervision de détecter le dépassement du seuil.

3. Contrôle de la syntaxe, analyse statique puis exécution :
```bash
bash -n ~/scripts-lab/verif_espace.sh
shellcheck ~/scripts-lab/verif_espace.sh
chmod 750 ~/scripts-lab/verif_espace.sh
~/scripts-lab/verif_espace.sh
echo "Code de retour : $?"
```
👉 Explication : `bash -n` vérifie la syntaxe sans exécuter le script. `shellcheck` ne doit remonter aucun avertissement bloquant. `chmod 750` limite l'accès au propriétaire et à son groupe. Le code de retour vaut `0` si l'espace est sous le seuil.

---

## ⚡ 2. Production — Façon Simplifiée
1. Installation du script dans un dossier système :
```bash
sudo install -o root -g root -m 755 ~/scripts-lab/verif_espace.sh /usr/local/sbin/verif_espace.sh
ls -l /usr/local/sbin/verif_espace.sh
```
👉 Explication : `install` copie le fichier en fixant propriétaire et droits. Le script est placé dans `/usr/local/sbin`, hors de tout dossier personnel.

2. Planification avec la crontab de root :
```bash
sudo crontab -l
sudo crontab -e
```
Ligne à ajouter :
```
*/15 * * * * /usr/local/sbin/verif_espace.sh >> /var/log/verif_espace.log 2>&1
```
👉 Explication : `crontab -l` liste les tâches existantes avant modification. La ligne lance le contrôle toutes les 15 minutes et journalise la sortie et les erreurs.

3. Contrôle manuel de l'exécution :
```bash
sudo /usr/local/sbin/verif_espace.sh; echo "Code : $?"
sudo tail -n 5 /var/log/verif_espace.log
```
👉 Explication : Lance le script à la main pour vérifier son code de retour, puis lit les dernières lignes du journal. Le fichier `/var/log/verif_espace.log` n'existe qu'après le premier passage de cron.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restriction des droits du journal :
```bash
sudo touch /var/log/verif_espace.log
sudo chown root:adm /var/log/verif_espace.log
sudo chmod 640 /var/log/verif_espace.log
ls -l /var/log/verif_espace.log
```
👉 Explication : Seul `root` écrit dans le journal, le groupe `adm` (groupe standard de Debian pour la lecture des journaux) peut le lire. Les autres comptes n'y ont pas accès.

2. Contrôle qu'aucun utilisateur ordinaire ne peut modifier le script exécuté en root :
```bash
ls -l /usr/local/sbin/verif_espace.sh
sudo find /usr/local/sbin -maxdepth 1 -name verif_espace.sh -perm -o+w
```
👉 Explication : La seconde commande ne doit rien afficher. Un script exécuté par root et modifiable par un autre compte permettrait une élévation de privilèges.

3. Recherche de secrets en clair dans les scripts :
```bash
sudo grep -rniE "password|passwd|secret|token" /usr/local/sbin/ || echo "Aucune occurrence"
```
👉 Explication : Liste les lignes qui pourraient contenir un mot de passe ou un jeton. Les identifiants doivent être lus depuis un coffre-fort (voir les fiches Passbolt ou Vaultwarden du pack), jamais écrits dans le script.

4. Empreinte du script pour détecter une modification :
```bash
sudo sha256sum /usr/local/sbin/verif_espace.sh | sudo tee -a /root/empreintes_scripts.sha256
sudo sha256sum -c /root/empreintes_scripts.sha256
```
👉 Explication : La première commande enregistre l'empreinte SHA-256 du script dans un fichier réservé à root. La seconde recalcule l'empreinte et répond `OK` tant que le script n'a pas été modifié. Un `FAILED` signale une modification non prévue.

---

**Point à vérifier** : `df --output` dépend de GNU coreutils (présent sur Debian 12) ; le groupe `adm` et le chemin `/var/log` sont ceux de la configuration Debian par défaut, à confirmer sur la machine déployée.