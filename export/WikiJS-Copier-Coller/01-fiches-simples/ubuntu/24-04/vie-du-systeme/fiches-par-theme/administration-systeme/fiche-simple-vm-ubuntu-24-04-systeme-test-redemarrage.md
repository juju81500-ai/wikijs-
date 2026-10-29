# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Systeme_Test_Redemarrage

- **Environnement** : VM Ubuntu Server (production après validation en fenêtre de maintenance)
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat)
- **Catégorie** : Système / Test de persistance au redémarrage

## 🎯 Problème précis à résoudre
Vérifier qu'un serveur Ubuntu Server 24.04 LTS redémarre sans intervention : montages, réseau, DNS, horloge et services métier doivent revenir à l'état attendu, avant toute mise en production définitive.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever l'état de référence avant le redémarrage :
   ```bash
   systemctl --failed --no-pager
   findmnt --verify
   ip -br address
   ip route
   systemctl list-unit-files --state=enabled --no-pager
   ```
   👉 *Explication : Ces sorties servent de comparaison après redémarrage ; noter l'adresse IP, la passerelle et la liste des services activés.*
2. Redémarrer dans la VM de test :
   ```bash
   sudo systemctl reboot
   ```
   👉 *Explication : Déclenche un arrêt propre puis un démarrage complet de la machine.*

## ⚡ 2. Production — Façon Simplifiée
1. Après redémarrage, vérifier le temps de démarrage et l'absence de services en échec :
   ```bash
   systemd-analyze
   systemctl --failed --no-pager
   who -b
   ```
   👉 *Explication : `systemd-analyze` affiche la durée du démarrage ; `who -b` indique l'heure du dernier démarrage pour la traçabilité.*
2. Contrôler les montages, le réseau et le DNS :
   ```bash
   findmnt --verify
   ip -br address
   ip route
   resolvectl status | grep -i 'DNS Servers'
   timedatectl status | grep -E 'Time zone|synchronized'
   ```
   👉 *Explication : Les montages doivent apparaître comme attendus, l'adresse IP et la passerelle doivent correspondre à la fiche Netplan, et l'horloge doit être synchronisée.*

## 🔒 3. Production — Façon Sécurisée
1. Vérifier que les services métier sont actifs et écoutent sur les ports prévus :
   ```bash
   systemctl is-active <nom_du_service>
   sudo ss -tulnp
   ```
   👉 *Explication : `is-active` doit renvoyer `active` ; `ss -tulnp` confirme que les ports attendus sont en écoute et qu'aucun port inattendu n'apparaît.*
2. Comparer l'état de référence et l'état après redémarrage :
   ```bash
   systemctl list-unit-files --state=enabled --no-pager
   sudo journalctl -b -p err --no-pager
   ```
   👉 *Explication : Toute différence dans les services activés doit être justifiée ; les erreurs du démarrage courant doivent être analysées avant de déclarer le test réussi.*

## ✅ Validation et retour arrière
- Le test est réussi si : aucune unité en échec, montages présents, IP et passerelle identiques, services métier actifs et journal sans erreur bloquante.
- En cas d'échec d'un montage, lancer une console (hyperviseur) puis corriger `/etc/fstab` (voir la fiche Stockage_Fstab_Options) ; en cas d'échec réseau, revoir la configuration Netplan dans `/etc/netplan/`.
- Retour arrière d'une configuration récente : restaurer la sauvegarde du fichier modifié, lancer `sudo netplan try` ou `sudo findmnt --verify`, puis redémarrer une seule fois.