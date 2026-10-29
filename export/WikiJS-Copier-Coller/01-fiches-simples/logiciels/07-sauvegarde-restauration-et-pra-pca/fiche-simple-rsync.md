# 📄 rsync

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : rsync 3.2.x fourni par les dépôts Debian 12, à vérifier avec `rsync --version` sur la version déployée
- **Catégorie** : Sauvegarde, restauration et PRA / PCA

## 🎯 Problème précis à résoudre
Copier un dossier de données vers un serveur de sauvegarde par SSH avec rsync, vérifier le résultat, tester une restauration, planifier la copie, puis durcir l'accès (clé SSH dédiée, commande forcée côté serveur). Cette fiche couvre Linux ; l'usage de rsync sous Windows n'est pas traité. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de rsync :
```bash
sudo apt update
sudo apt install -y rsync
rsync --version | head -n 1
```
👉 Explication : Installe rsync depuis les dépôts Debian 12 et affiche la version.

2. Données de test et simulation de copie locale :
```bash
mkdir -p /tmp/lab-source/compta /tmp/lab-cible
echo "facture test" > /tmp/lab-source/compta/facture-001.txt
rsync -avhn /tmp/lab-source/ /tmp/lab-cible/
```
👉 Explication : `-a` conserve droits, dates et liens, `-v` détaille, `-h` affiche les tailles lisibles, `-n` simule sans copier. La liste doit montrer `compta/facture-001.txt`.

3. Copie réelle et contrôle :
```bash
rsync -avh /tmp/lab-source/ /tmp/lab-cible/
diff -r /tmp/lab-source /tmp/lab-cible && echo "copie identique"
```
👉 Explication : La copie se fait réellement. `diff -r` ne retourne rien si les deux arborescences sont identiques, et `echo` confirme alors le résultat.

4. Copie vers le serveur de sauvegarde par SSH :
```bash
ssh-keygen -t ed25519 -f "$HOME/.ssh/cle_sauvegarde" -N ""
ssh-copy-id -i "$HOME/.ssh/cle_sauvegarde.pub" svc-sauv@srv-sauv01
rsync -avh -e "ssh -i $HOME/.ssh/cle_sauvegarde" /tmp/lab-source/ svc-sauv@srv-sauv01:/srv/sauvegardes/lab/
```
👉 Explication : Crée une paire de clés dédiée (sans phrase de passe, lab uniquement), installe la clé publique sur le serveur `srv-sauv01` pour le compte `svc-sauv`, puis copie les données. Le dossier distant `/srv/sauvegardes/lab/` doit exister et appartenir à `svc-sauv`.

5. Test de restauration :
```bash
mkdir -p /tmp/restauration-test
rsync -avh -e "ssh -i $HOME/.ssh/cle_sauvegarde" svc-sauv@srv-sauv01:/srv/sauvegardes/lab/compta/ /tmp/restauration-test/
diff -r /tmp/lab-source/compta /tmp/restauration-test && echo "restauration identique"
```
👉 Explication : Recopie le contenu depuis le serveur vers un dossier de test, puis compare avec la source. Le résultat attendu est `restauration identique`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Préparation du serveur de sauvegarde :
```bash
sudo useradd -m -s /bin/bash svc-sauv
sudo mkdir -p /srv/sauvegardes/donnees /srv/sauvegardes/corbeille
sudo chown -R svc-sauv:svc-sauv /srv/sauvegardes
```
👉 Explication : Crée le compte `svc-sauv` qui reçoit les copies, puis le dossier de destination et le dossier `corbeille` où rsync met les fichiers modifiés ou supprimés à la source.

2. Clé SSH dédiée de la machine source, exécutée par root :
```bash
sudo ssh-keygen -t ed25519 -f /root/.ssh/cle_sauvegarde -N ""
sudo ssh-copy-id -i /root/.ssh/cle_sauvegarde.pub svc-sauv@srv-sauv01
```
👉 Explication : La tâche planifiée s'exécute sous root, la clé appartient donc à root. Cette clé n'est pas réutilisée pour un autre usage.

3. Planification quotidienne à 02:30 :
```bash
sudo crontab -e
```
Ajouter cette ligne :
```
30 2 * * * rsync -aH --delete --backup --backup-dir=/srv/sauvegardes/corbeille -e "ssh -i /root/.ssh/cle_sauvegarde" /srv/donnees/ svc-sauv@srv-sauv01:/srv/sauvegardes/donnees/ --log-file=/var/log/rsync-donnees.log
```
👉 Explication : `--delete` aligne la destination sur la source, `--backup` déplace dans `corbeille` les fichiers supprimés ou remplacés plutôt que de les effacer définitivement. La corbeille doit être purgée régulièrement. Point à vérifier : `--backup-dir` est interprété côté serveur de sauvegarde.

4. Contrôle du journal et de la planification :
```bash
sudo crontab -l
sudo tail -n 30 /var/log/rsync-donnees.log
```
👉 Explication : Confirme que la tâche est enregistrée et affiche les dernières opérations de la copie.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restriction de la clé côté serveur, qui ne peut lancer que rsync sur le dossier de sauvegarde :
```bash
sudo ls /usr/share/doc/rsync/scripts/
sudo nano /home/svc-sauv/.ssh/authorized_keys
```
Ajouter au début de la ligne de la clé publique (contenu de `/root/.ssh/cle_sauvegarde.pub`) :
```
command="/usr/share/doc/rsync/scripts/rrsync /srv/sauvegardes/donnees",restrict
```
👉 Explication : `rrsync` limite la clé à des transferts rsync dans `/srv/sauvegardes/donnees`, sans shell interactif, sans redirection de port ni transfert d'agent. Point à vérifier : le script `rrsync` est fourni dans la documentation du paquet rsync et peut être compressé (`.gz`) ; le chemin exact se relève avec la première commande, à adapter.

2. Droits sur les clés :
```bash
sudo chmod 600 /root/.ssh/cle_sauvegarde
sudo ls -l /root/.ssh/
```
👉 Explication : La clé privée n'est lisible que par root. Une clé privée lisible par d'autres comptes doit être considérée comme compromise et remplacée.

3. Contrôle d'intégrité par somme de contrôle :
```bash
sudo rsync -avhn --checksum -e "ssh -i /root/.ssh/cle_sauvegarde" /srv/donnees/ svc-sauv@srv-sauv01:/srv/sauvegardes/donnees/
```
👉 Explication : `--checksum` compare le contenu réel et non seulement la taille et la date. `-n` simule : aucune liste de fichier à transférer signifie que les copies sont identiques.

4. Préservation des ACL et attributs étendus :
```bash
sudo rsync -aAXH --dry-run -e "ssh -i /root/.ssh/cle_sauvegarde" /srv/donnees/ svc-sauv@srv-sauv01:/srv/sauvegardes/donnees/
```
👉 Explication : `-A` et `-X` conservent les ACL et attributs étendus. Point à vérifier : le serveur de destination doit supporter ces attributs (système de fichiers ext4 ou XFS). Retirer `--dry-run` une fois le test validé, puis reporter les options dans la ligne cron.

---