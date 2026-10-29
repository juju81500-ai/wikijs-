# 📄 Fiche_Simple_-_VM_Rocky_9_Sauvegarde_Test_Restauration.md

- **Environnement** : VM ou serveur Rocky Linux dans un environnement isolé de test
- **OS / Version** : Rocky Linux 9 / RHEL 9 avec Restic (EPEL)
- **Catégorie** : Sauvegarde / Test de restauration PRA

## 🎯 Problème précis à résoudre
Vérifier qu'une sauvegarde Restic est réellement restaurable, dans un répertoire isolé, et que les fichiers restaurés sont identiques aux originaux sur Rocky Linux 9.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lister les instantanés disponibles dans le dépôt :
   ```bash
   sudo env RESTIC_PASSWORD_FILE=/root/.restic_pass restic -r /srv/restic/<nom_du_serveur> snapshots
   ```
   👉 Explication : Chaque ligne représente un instantané avec son identifiant, sa date et les chemins sauvegardés. Noter l'identifiant à tester.

2. Restaurer le dernier instantané dans un répertoire de test :
   ```bash
   sudo mkdir -p /srv/restore-test
   sudo env RESTIC_PASSWORD_FILE=/root/.restic_pass restic -r /srv/restic/<nom_du_serveur> restore latest --target /srv/restore-test
   ```
   👉 Explication : Restic recrée l'arborescence complète sous `/srv/restore-test`. Par exemple, `/etc/hostname` est restauré dans `/srv/restore-test/etc/hostname`. Le répertoire d'origine n'est pas modifié.

---

## ⚡ 2. Production — Façon Simplifiée
1. Restaurer un fichier précis pour un test rapide :
   ```bash
   sudo env RESTIC_PASSWORD_FILE=/root/.restic_pass restic -r /srv/restic/<nom_du_serveur> restore latest --target /srv/restore-test --include /etc/hostname
   ```
   👉 Explication : `--include` limite la restauration au chemin indiqué. Le chemin doit être celui enregistré dans l'instantané, donc absolu.

2. Comparer le fichier restauré avec l'original :
   ```bash
   diff /etc/hostname /srv/restore-test/etc/hostname && echo "Fichier identique"
   ```
   👉 Explication : Aucune sortie et le message `Fichier identique` confirment que le contenu est strictement identique. Un écart signale une sauvegarde incomplète ou un fichier modifié depuis la sauvegarde.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérifier l'intégrité du dépôt, en lisant un sous-ensemble des données :
   ```bash
   sudo env RESTIC_PASSWORD_FILE=/root/.restic_pass restic -r /srv/restic/<nom_du_serveur> check --read-data-subset=1/10
   ```
   👉 Explication : Confirme que les blocs lus sont déchiffrables et non corrompus. Cette lecture est distincte de la restauration et la complète.

2. Restreindre l'accès au répertoire de test, car il contient des données de production :
   ```bash
   sudo chmod 700 /srv/restore-test
   ls -ld /srv/restore-test
   ```
   👉 Explication : Seul `root` peut lire les données restaurées. Le test doit être réalisé sur une VM sans route vers le réseau de production.

3. Mesurer le temps de restauration pour valider le RTO, puis supprimer les données de test :
   ```bash
   date
   sudo env RESTIC_PASSWORD_FILE=/root/.restic_pass restic -r /srv/restic/<nom_du_serveur> restore latest --target /srv/restore-test
   date
   sudo rm -rf /srv/restore-test
   ```
   👉 Explication : La différence entre les deux dates donne la durée réelle de restauration, à comparer au RTO défini. Vérifier le chemin avant `rm -rf`, car la commande est irréversible.

---

## ✅ Contrôle
```bash
sudo env RESTIC_PASSWORD_FILE=/root/.restic_pass restic -r /srv/restic/<nom_du_serveur> restore latest --target /srv/restore-test --include /etc/hostname
```
👉 Explication : La restauration doit se terminer sans erreur. Consigner la date, l'identifiant de l'instantané et le résultat du `diff` dans le dossier d'exploitation.