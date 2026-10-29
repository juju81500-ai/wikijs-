# 📄 Fiche_Simple_-_LXC_Alpine_3.19_Systeme_Test_Redemarrage.md

- **Environnement** : LXC (Proxmox VE)
- **OS / Version** : Alpine Linux 3.19 - Famille Alpine (OpenRC, apk)
- **Catégorie** : Système & Services / Validation de la persistance

## 🎯 Problème précis à résoudre
Vérifier qu'un conteneur Alpine Linux redémarre proprement : montages, réseau et services OpenRC doivent revenir dans l'état attendu sans intervention manuelle.

> Alpine 3.19 est en fin de support : valider cette procédure sur une branche maintenue avant tout usage en production.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever l'état de référence avant le redémarrage :
   ```sh
   rc-status -a
   ip -br addr
   ip route
   ss -lntup
   ```
   👉 Explication : Ces sorties servent de référence : services dans leurs runlevels, adresses IP, route par défaut et ports en écoute.

2. Redémarrer le conteneur depuis l'hôte Proxmox :
   ```sh
   pct reboot <vmid>
   ```
   👉 Explication : `pct reboot` redémarre le CT proprement depuis l'hôte. Depuis le conteneur, la commande `reboot` produit le même effet.

3. Relever à nouveau l'état et comparer avec la référence :
   ```sh
   rc-status --crashed
   rc-status -a
   ip -br addr
   ss -lntup
   ```
   👉 Explication : Aucun service ne doit apparaître dans `--crashed`, et les ports attendus doivent être de nouveau en écoute.

---

## ⚡ 2. Production — Façon Simplifiée
1. Contrôler les services activés au démarrage :
   ```sh
   rc-update show -v
   ```
   👉 Explication : Chaque service attendu doit figurer dans le runlevel `default`, ou `boot` pour les services système; aucun service inutile ne doit y être présent.

2. Contrôler les montages et l'espace disque après redémarrage :
   ```sh
   mount
   df -h
   ```
   👉 Explication : Les points de montage déclarés dans `/etc/fstab` ou dans la configuration Proxmox doivent apparaître avec la bonne taille.

3. Contrôler la connectivité réseau :
   ```sh
   ip route
   ping -c 3 <ip_passerelle>
   ```
   👉 Explication : La route par défaut doit pointer vers la passerelle attendue, et la passerelle doit répondre.

---

## 🔒 3. Production — Façon Sécurisée
1. Effectuer le test pendant une fenêtre de maintenance, avec la console Proxmox ouverte :
   ```sh
   pct console <vmid>
   ```
   👉 Explication : Si le réseau ou SSH ne revient pas, la console de l'hôte reste le seul moyen d'accès. Ne pas tester un redémarrage à distance sans cette console.

2. Vérifier l'absence d'erreurs de démarrage dans les journaux après le redémarrage :
   ```sh
   grep -iE 'error|fail' /var/log/messages | tail -n 30
   ```
   👉 Explication : Les erreurs de montage ou de service apparaissent dans ces lignes. Corriger la cause avant de déclarer le conteneur conforme.