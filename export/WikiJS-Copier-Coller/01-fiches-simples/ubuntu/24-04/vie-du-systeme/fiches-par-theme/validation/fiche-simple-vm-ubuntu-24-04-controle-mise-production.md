# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Controle_Mise_Production.md

- **Environnement** : VM ou serveur Ubuntu Server
- **OS / Version** : Ubuntu Server 24.04 LTS
- **Catégorie** : Production / Validation / Exploitation

## 🎯 Problème précis à résoudre
Valider un serveur Ubuntu avant sa mise en production : réseau, cloud-init, mises à jour, SSH, AppArmor, pare-feu, sauvegarde et supervision.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Identité, mises à jour, unités en échec :
   ```bash
   lsb_release -a
   apt list --upgradable
   systemctl --failed
   cloud-init status --long
   ```
   👉 Explication : aucune unité en échec; mises à jour en attente documentées.

2. Réseau et sécurité :
   ```bash
   sudo netplan generate
   resolvectl status
   sudo ufw status verbose
   sudo aa-status
   ```
   👉 Explication : `netplan generate` valide la configuration; UFW et AppArmor actifs.

3. Tester les ports applicatifs depuis un client autorisé :
   ```bash
   nc -zv IP_SERVEUR PORT
   ```
   👉 Explication : remplacer IP et port; puis restaurer en environnement isolé.

## ⚡ 2. Production — Façon Simplifiée
1. Système et réseau :
   ```bash
   lsb_release -d; ip -br a; ip route
   resolvectl query example.net
   ls /etc/netplan /etc/cloud/cloud.cfg.d
   ```
   👉 Explication : IP/DNS/routage persistants; identifier la source cloud-init.

2. Accès et sécurité :
   ```bash
   sudo sshd -T | grep -E 'passwordauthentication|permitrootlogin'
   sudo ufw status
   sudo aa-status | head -3
   ```
   👉 Explication : SSH par clé, root interdit, ports limités.

3. Exploitation et continuité :
   ```bash
   df -h
   sudo journalctl -p err -b --no-pager | tail
   ```
   👉 Explication : journaux collectés, espace surveillé; sauvegarde récente et restauration testée consignées.

## 🔒 3. Production — Façon Sécurisée
- Ne pas ouvrir le service si le pare-feu est désactivé, si la sauvegarde est inexploitable ou si cloud-init réécrit le réseau de façon imprévue.
- Contrôler la conformité après redémarrage et après installation des mises à jour.
- Conserver console hyperviseur et accès de secours jusqu'à validation externe.

## ✅ Validation et retour arrière
- Tester service, SSH, DNS, réseau et alertes depuis les postes autorisés; conserver les preuves de validation.
- Restaurer une sauvegarde représentative dans une VM isolée.
- En cas d'échec, suspendre la bascule, restaurer la configuration précédente ou reconstruire depuis l'ISO vérifié.