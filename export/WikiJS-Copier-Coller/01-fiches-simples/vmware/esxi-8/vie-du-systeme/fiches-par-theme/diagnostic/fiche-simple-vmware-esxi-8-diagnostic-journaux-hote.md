# 📄 Fiche_Simple_-_VMware_ESXi_8_Diagnostic_Journaux_Hote.md

- **Environnement** : Hôte physique VMware ESXi 8 (ESXi Shell ou SSH, serveur syslog distant)
- **OS / Version** : VMware ESXi 8.0 - Journaux et diagnostic
- **Catégorie** : Diagnostic / Journaux et tâches de l'hôte

---

## 🎯 Problème précis à résoudre
Diagnostiquer un hôte ESXi 8 à partir de ses journaux (`hostd`, `vmkernel`, `vobd`), suivre les tâches en cours, puis centraliser les journaux vers un serveur syslog avec une rotation maîtrisée.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lire les dernières erreurs du service de gestion `hostd` :
```bash
tail -n 100 /var/log/hostd.log
grep -iE "error|warn|fail" /var/log/hostd.log | tail -n 50
```
👉 Explication : `hostd` gère l'API de l'hôte et les opérations vSphere ; les lignes filtrées par `error`, `warn` ou `fail` concentrent les anomalies récentes.

2. Consulter les erreurs du noyau VMkernel :
```bash
grep -iE "error|fail|warn" /var/log/vmkernel.log | tail -n 50
```
👉 Explication : `vmkernel.log` trace le stockage, le réseau et les pilotes matériels ; une erreur de chemin d'accès ou de carte réseau y apparaît en premier.

3. Consulter les événements de haut niveau (VOBD) :
```bash
tail -n 50 /var/log/vobd.log
```
👉 Explication : `vobd.log` enregistre les événements de santé (perte de chemin, bascule HA, état du stockage) comme ceux affichés dans vSphere.

4. Lister les tâches en cours sur l'hôte :
```bash
vim-cmd vimsvc/task_list
```
👉 Explication : affiche les tâches vSphere en cours d'exécution (migration, snapshot, création de VM) avec leur état, utile avant un redémarrage ou une maintenance.

**Équivalent interface graphique :**

- **Host Client > Monitor > Logs**, puis choisir `hostd.log`, `vmkernel.log` ou `vobd.log`.
  👉 Explication : même lecture des journaux depuis le navigateur, sans SSH.
- **Host Client > Monitor > Tasks** pour les tâches en cours.
  👉 Explication : équivalent de `vim-cmd vimsvc/task_list`.

## ⚡ 2. Production — Façon Simplifiée
1. Configurer la transmission des journaux vers un serveur syslog distant :
```bash
esxcli system syslog config set --loghost=tcp://<ip_serveur_syslog>:514
esxcli system syslog reload
esxcli system syslog config get
```
👉 Explication : envoie les journaux de l'hôte en TCP vers `<ip_serveur_syslog>`, recharge la configuration puis affiche les paramètres actifs (`Remote Host`, `Log Dir`, `Log to Persistent Disk`).

2. Valider la chaîne de transmission par un message de test :
```bash
esxcli system syslog mark --message="Test de transmission syslog ESXi <nom_de_l_hote>"
```
👉 Explication : insère un marqueur dans les journaux locaux et distants ; le message doit apparaître sur le serveur syslog.

3. Contrôler l'espace disponible pour les journaux :
```bash
df -h /scratch
```
👉 Explication : vérifie que la partition `/scratch`, qui stocke les journaux persistants, n'est pas saturée ; une partition pleine interrompt la journalisation locale.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Définir une rotation stricte des journaux locaux :
```bash
esxcli system syslog config set --default-rotate=8 --default-size=1024
esxcli system syslog reload
```
👉 Explication : conserve 8 fichiers de 1 Mo par journal sur le stockage local, ce qui garantit un historique local même si le serveur distant est injoignable.

2. Vérifier la configuration de journalisation de chaque composant :
```bash
esxcli system syslog config logger list
```
👉 Explication : liste les journalisateurs (`hostd`, `vmkernel`, `vobd`, etc.) avec leur taille maximale et leur nombre de rotations, pour vérifier qu'aucun composant n'est oublié.

3. Vérifier la configuration de la capture de dumps mémoire :
```bash
esxcli system coredump partition get
```
👉 Explication : affiche la partition utilisée pour les dumps noyau ; un dump correct est indispensable à l'analyse d'un plantage PSOD (Purple Screen of Death).

4. Générer un bundle de support pour l'éditeur :
```bash
vm-support -w /vmfs/volumes/<datastore_securise>
```
👉 Explication : crée une archive complète des journaux et de la configuration dans le datastore indiqué ; le bundle contient des informations sensibles et doit être transmis uniquement au support autorisé.

5. Contrôler la santé matérielle lorsque le BMC est présent :
```bash
esxcli hardware ipmi sdr list
```
👉 Explication : affiche les capteurs de température, tension et ventilation remontés par le BMC (IPMI) ; sur un matériel sans BMC, la commande ne renvoie rien et la supervision matérielle passe par l'IPMI ou l'outil constructeur.