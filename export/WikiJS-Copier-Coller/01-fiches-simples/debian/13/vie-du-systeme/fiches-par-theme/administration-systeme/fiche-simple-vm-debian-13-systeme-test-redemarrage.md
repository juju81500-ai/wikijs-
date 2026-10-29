# 📄 Fiche_Simple_-_VM_Debian_13_Systeme_Test_Redemarrage

- **Environnement** : VM ou serveur Debian 13 avant mise en production
- **OS / Version** : Debian 13 (Trixie) avec systemd - Famille Debian
- **Catégorie** : Système & Services / Test de persistance au redémarrage

## 🎯 Problème précis à résoudre
Vérifier qu'une VM ou un serveur Debian 13 redémarre proprement : montages, pile réseau, résolution DNS, pare-feu et services métier doivent revenir automatiquement, sans intervention manuelle.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever l'état avant le redémarrage :
   ```bash
   systemctl --failed --no-pager
   findmnt --verify
   ip -br address
   ```
   👉 Explication : Ces sorties servent de référence. Une unité déjà en échec, un montage invalide ou une interface absente avant le reboot ne doivent pas être attribués au redémarrage.

2. Redémarrer la VM de test :
   ```bash
   sudo reboot
   ```
   👉 Explication : Le redémarrage complet suit la séquence réelle de démarrage (fsck, montages, réseau, services). Une console hyperviseur doit rester disponible pour observer le boot.

3. Contrôler l'état après le démarrage :
   ```bash
   uptime -s
   systemctl --failed --no-pager
   findmnt --verify
   journalctl -b -p err --no-pager
   ```
   👉 Explication : `uptime -s` confirme l'heure du démarrage récent. Aucune unité en échec et aucune erreur de montage ou de niveau `err` ne doit apparaître pour le démarrage courant.

---

## ⚡ 2. Production — Façon Simplifiée
1. Planifier le redémarrage dans une fenêtre validée et prévenir les utilisateurs. Vérifier au préalable que les services sont configurés pour démarrer automatiquement :
   ```bash
   systemctl list-unit-files --state=enabled --no-pager | grep -E "<service_1>|<service_2>"
   ```
   👉 Explication : Chaque service métier doit apparaître comme `enabled`. Un service non activé ne redémarre pas seul et demande une intervention manuelle.

2. Redémarrer puis contrôler la pile réseau et la résolution DNS :
   ```bash
   sudo reboot
   ip route
   resolvectl status
   ```
   👉 Explication : La route par défaut doit être présente, et le DNS doit répondre. Sous Debian 13 en ifupdown, `resolvectl` peut être absent ; dans ce cas, contrôler `cat /etc/resolv.conf`.

3. Vérifier les services métier et les ports attendus :
   ```bash
   systemctl is-active <service_1> <service_2>
   sudo ss -tulnp
   ```
   👉 Explication : Chaque service doit répondre `active`, et les ports attendus doivent être en écoute, comme avant le redémarrage.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérifier que le pare-feu est restauré au démarrage et que les règles sont identiques :
   ```bash
   sudo nft list ruleset | head -n 40
   systemctl is-enabled nftables
   ```
   👉 Explication : Le service `nftables` doit être `enabled`, sinon le serveur redémarre sans filtrage. Comparer le résultat avec la configuration validée.

2. Contrôler la synchronisation horaire, le fuseau et les erreurs de montage après le boot :
   ```bash
   timedatectl status
   sudo findmnt --verify --verbose
   ```
   👉 Explication : Une horloge non synchronisée fausse les journaux et les certificats. Un montage fstab invalide peut bloquer le démarrage en mode de secours.

3. Vérifier l'arrêt puis le redémarrage propres depuis l'invité, en fenêtre de maintenance :
   ```bash
   sudo systemctl poweroff
   ```
   👉 Explication : L'arrêt propre arrête les services dans l'ordre inverse de leurs dépendances. Une coupure brutale (arrêt forcé depuis l'hyperviseur) ne se teste que sur une VM de lab, jamais sur un serveur de production sans sauvegarde restaurable.