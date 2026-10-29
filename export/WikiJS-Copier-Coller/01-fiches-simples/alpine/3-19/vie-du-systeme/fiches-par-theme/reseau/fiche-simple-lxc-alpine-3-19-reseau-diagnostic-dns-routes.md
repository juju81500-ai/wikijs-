# 📄 Fiche_Simple_-_LXC_Alpine_3.19_Reseau_Diagnostic_DNS_Routes.md

- **Environnement** : LXC Alpine administré depuis Proxmox VE
- **OS / Version** : Alpine Linux 3.19 avec BusyBox et OpenRC (version legacy)
- **Catégorie** : Réseau / Diagnostic

## 🎯 Problème précis à résoudre
Diagnostiquer une perte de connectivité ou de résolution DNS dans Alpine LXC, en distinguant les paramètres fournis par Proxmox de ceux du conteneur.

> Alpine 3.19 est une version ancienne : réserver cette fiche à un environnement existant ou de laboratoire et planifier une migration vers une branche maintenue.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever les interfaces et la route :
   ```sh
   ip -br addr
   ip route
   ```
2. Vérifier le fichier résolveur et tester successivement la passerelle puis un nom :
   ```sh
   ls -l /etc/resolv.conf
   cat /etc/resolv.conf
   ping -c 3 <passerelle>
   nslookup <nom-a-tester>
   ```
   👉 *Explication : si la passerelle répond mais que `nslookup` échoue, examiner le DNS; si la route manque, vérifier d'abord la configuration réseau du CT.*

## ⚡ 2. Production — Façon Simplifiée
1. Dans Proxmox, vérifier l'adresse, la passerelle, le bridge/VLAN et les paramètres DNS configurés pour le CT.
2. Dans Alpine, comparer l'état réellement fourni :
   ```sh
   ip -br addr
   ip route
   cat /etc/resolv.conf
   nslookup <nom-interne> <dns-interne>
   ```
3. Si la configuration est générée par Proxmox, corriger la source sur l'hôte et redémarrer ou réappliquer le réseau du CT selon la procédure du cluster.
   👉 *Explication : modifier `/etc/resolv.conf` ou les interfaces à l'intérieur du conteneur peut être écrasé par l'hôte.*

## 🔒 3. Production — Façon Sécurisée
1. Ne pas remplacer le résolveur interne par un DNS public lorsque le CT doit résoudre des noms privés.
2. Ne pas désactiver le filtrage de l'hôte ou ouvrir toutes les interfaces pour contourner un défaut DNS.
3. Garder une console Proxmox et noter la configuration initiale avant tout changement réseau.

## ✅ Validation et retour arrière
- Vérifier la route par défaut, résoudre un nom interne et tester le port du service depuis une source autorisée.
- Si l'accès est perdu, rétablir les paramètres précédents dans la configuration Proxmox du CT.
- Comparer les résultats `ip route`, `nslookup` et l'état réseau affiché par Proxmox.