# 📄 Fiche_Simple_-_Proxmox_VE_8_Systeme_Test_Redemarrage.md

- **Environnement** : Hyperviseur Proxmox VE 8 (nœud autonome ou membre de cluster)
- **OS / Version** : Proxmox VE 8.x - Debian 12 Bookworm
- **Catégorie** : Système & Services / Persistance au redémarrage
- **Tags** : `[proxmox-ve-8]`, `[debian-bookworm]`, `[reboot-test]`, `[zfs]`, `[pve-guests]`, `[production]`

---

## 🎯 Problème précis à résoudre
Vérifier que l'hyperviseur Proxmox VE 8 redémarre proprement : montages, stockages, réseau, cluster et démarrage automatique des VM et conteneurs, avant sa mise en production ou après une maintenance.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Inventorier l'état avant redémarrage :
```bash
qm list
pct list
pvesm status
```
👉 Explication : `qm list` et `pct list` listent les VM et conteneurs avec leur état ; `pvesm status` vérifie que chaque stockage est actif avant l'arrêt.

2. Contrôler les montages et les services en échec :
```bash
systemctl --failed
findmnt --verify --verbose
```
👉 Explication : `systemctl --failed` doit renvoyer aucune unité ; `findmnt --verify` valide le contenu de `/etc/fstab` pour éviter un montage bloquant au démarrage.

3. Redémarrer le nœud :
```bash
shutdown -r +2 "Test de redemarrage planifie Proxmox VE"
```
👉 Explication : programme un redémarrage dans deux minutes et notifie les utilisateurs connectés ; `shutdown -c` annule la demande si besoin.

4. Contrôler l'état après retour du nœud :
```bash
uptime
systemctl --failed
qm list
pct list
```
👉 Explication : confirme le nouveau démarrage, l'absence d'unités en échec et le démarrage des VM et conteneurs configurés.

---

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier le quorum du cluster avant maintenance :
```bash
pvecm status | grep -E 'Quorate|Nodes'
```
👉 Explication : confirme que le cluster est quorate avant d'arrêter un nœud ; sur un nœud autonome, la commande signale l'absence de cluster et ne bloque pas le test.

2. Configurer le démarrage automatique et l'ordre de démarrage des invités :
```bash
qm set <vmid> --onboot 1 --startup order=1,up=60
pct set <ctid> --onboot 1 --startup order=2,up=30
```
👉 Explication : démarre automatiquement la VM `<vmid>` en premier puis le conteneur `<ctid>` ; `up` définit le délai en secondes avant de passer à l'invité suivant.

3. Vérifier la santé des pools ZFS avant redémarrage (si ZFS est utilisé) :
```bash
zpool status -x
```
👉 Explication : affiche `all pools are healthy` si aucun pool n'est dégradé ; ne pas redémarrer un nœud dont un pool est en état DEGRADED ou FAULTED.

4. Redémarrer et vérifier le démarrage automatique :
```bash
shutdown -r +2 "Test de redemarrage avec demarrage automatique"
```
👉 Explication : après le retour du nœud, `qm list` et `pct list` doivent montrer les invités configurés en `running` sans intervention manuelle ; `pvesm status` doit confirmer les stockages actifs.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérifier les sauvegardes récentes avant tout redémarrage :
```bash
ls -lt /var/lib/vz/dump/ | head -n 10
```
👉 Explication : confirme qu'une sauvegarde VZDump récente existe pour chaque VM critique ; sans sauvegarde valide, le redémarrage est reporté.

2. Contrôler la cohérence du montage et du démarrage avec les journaux :
```bash
findmnt --verify --verbose
journalctl --list-boots | tail -n 3
```
👉 Explication : valide `/etc/fstab` puis liste les derniers démarrages enregistrés ; la présence d'un historique de boot confirme que le journal persistant est actif.

3. Analyser les erreurs du démarrage précédent après redémarrage :
```bash
journalctl -b -1 -p err --no-pager | tail -n 50
```
👉 Explication : affiche les erreurs survenues pendant le démarrage précédent (`-b -1`), afin de documenter les anomalies avant de clore le test.

4. Vérifier que le service de démarrage des invités est actif :
```bash
systemctl status pve-guests --no-pager
```
👉 Explication : `pve-guests` lance les VM et conteneurs marqués `onboot` selon l'ordre défini ; un service inactif ou en échec explique un invité resté arrêté.
