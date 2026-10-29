# 📄 Fiche_Simple_-_VM_Ubuntu_26.04_Systeme_Test_Redemarrage

- **Environnement** : VM ou serveur Ubuntu en fin de mise en service
- **OS / Version** : Ubuntu Server 26.04 LTS (systemd 259)
- **Catégorie** : Système / Persistance au redémarrage

---

## 🎯 Problème précis à résoudre

Vérifier qu'un serveur Ubuntu 26.04 redémarre proprement et que tout ce qui a été configuré (disques, réseau, DNS, services) est rétabli automatiquement, sans intervention manuelle, avant sa mise en production.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Noter l'état avant redémarrage :
```bash
systemctl --failed --no-pager
systemctl is-system-running
findmnt -t ext4,xfs
ip -br address
ip route
```
👉 Explication : Ce relevé sert de référence. `is-system-running` doit afficher `running` ; `degraded` signale déjà une unité en échec.

2. Redémarrer la machine :
```bash
sudo reboot
```
👉 Explication : Déclenche un redémarrage propre. Sur un lab, prévoir l'accès à la console de l'hyperviseur au cas où le réseau ne revient pas.

3. Après reconnexion, contrôler l'état :
```bash
uptime -s
systemctl is-system-running
systemctl --failed --no-pager
```
👉 Explication : `uptime -s` confirme l'heure du redémarrage ; les deux autres commandes doivent donner le même résultat qu'avant redémarrage.

## ⚡ 2. Production — Façon Simplifiée

1. Comparer les montages avec le relevé initial :
```bash
findmnt --verify --verbose
findmnt -t ext4,xfs
```
👉 Explication : Vérifie les lignes de `/etc/fstab` et confirme que chaque disque de données est monté après redémarrage.

2. Vérifier la pile réseau et la résolution :
```bash
ip -br address
ip route
resolvectl status
```
👉 Explication : Les adresses, la route par défaut et les serveurs DNS doivent être identiques à ceux relevés avant le redémarrage.

3. Vérifier les services métier :
```bash
systemctl list-units --type=service --state=running --no-pager
```
👉 Explication : Compare la liste des services actifs à l'inventaire attendu. Un service absent sans erreur peut être désactivé par erreur.

## 🔒 3. Production — Façon Sécurisée

1. Analyser la durée et le chemin critique du démarrage :
```bash
systemd-analyze
systemd-analyze critical-chain
```
👉 Explication : Montre le temps de démarrage total et la chaîne de dépendances la plus longue. Un montage ou un service réseau qui bloque doit être corrigé avant la mise en production.

2. Contrôler qu'aucun service n'écoute sur une interface non prévue :
```bash
sudo ss -tulnp
```
👉 Explication : Après redémarrage, les services doivent écouter seulement sur les ports et adresses prévus. Un écart révèle une configuration par défaut non durcie.

3. Vérifier les pare-feu et l'état de sécurité après redémarrage :
```bash
sudo ufw status verbose
systemctl is-active fail2ban apparmor
```
👉 Explication : UFW, Fail2ban et AppArmor doivent être actifs, avec les règles attendues.

## ✅ Validation et retour arrière

- **Précontrôles** : relevé avant redémarrage archivé, console de secours accessible, sauvegarde ou snapshot de la VM réalisé.
- **Validation** : `systemctl is-system-running` affiche `running` ; les montages, l'IP, la route, le DNS et les services métier sont identiques au relevé initial.
- **Retour arrière** : si le démarrage échoue, utiliser la console pour restaurer `/etc/fstab` ou la configuration réseau depuis la copie sauvegardée, puis `sudo systemctl daemon-reload` ; à défaut, restaurer le snapshot.