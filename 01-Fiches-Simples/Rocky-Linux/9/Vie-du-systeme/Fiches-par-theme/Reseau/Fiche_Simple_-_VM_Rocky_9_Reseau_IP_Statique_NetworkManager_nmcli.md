# 📄 Fiche_Simple_-_VM_Rocky_9_Reseau_IP_Statique_NetworkManager_nmcli.md

- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9 - NetworkManager
- **Catégorie** : Réseau / Configuration IP
- **Tags** : `[rocky9]`, `[rhel9]`, `[networkmanager]`, `[nmcli]`, `[ip-statique]`, `[dns]`

## 🎯 Problème précis à résoudre
Configurer une adresse IPv4 statique persistante avec un profil NetworkManager sous Rocky Linux 9, sans modifier directement des fichiers générés par NetworkManager.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Identifier le profil actif, l'interface et l'état initial :
   ```bash
   nmcli -f NAME,DEVICE,TYPE connection show --active
   ip -br address
   ip route
   ```
2. Dans une console locale, définir le nom exact du profil et appliquer les paramètres d'exemple :
   ```bash
   CON="Wired connection 1"
   sudo nmcli connection modify "$CON" ipv4.method manual ipv4.addresses 192.0.2.50/24 ipv4.gateway 192.0.2.1 ipv4.dns "192.0.2.53" ipv4.ignore-auto-dns yes
   sudo nmcli connection up "$CON"
   ```
   👉 *Explication : Les adresses `192.0.2.0/24` sont réservées à la documentation; remplacer le profil et les paramètres par ceux du réseau de test.*

## ⚡ 2. Production — Façon Simplifiée
1. Depuis la console hyperviseur ou une fenêtre de maintenance, relever le profil actif et noter ses valeurs initiales. Vérifier l'adresse réservée dans le plan IP/DHCP.
2. Modifier le profil NetworkManager existant :
   ```bash
   CON="<nom-du-profil-actif>"
   sudo nmcli connection modify "$CON" ipv4.method manual ipv4.addresses "<IP>/<CIDR>" ipv4.gateway "<passerelle>" ipv4.dns "<DNS-interne>" ipv4.ignore-auto-dns yes
   sudo nmcli connection up "$CON"
   ```
3. Vérifier immédiatement la configuration :
   ```bash
   nmcli -f IP4.ADDRESS,IP4.GATEWAY,IP4.DNS device show
   ip route
   getent hosts <nom-interne-a-tester>
   ```
   👉 *Explication : `nmcli connection modify` persiste le profil; `connection up` le réactive et peut couper la session SSH.*

## 🔒 3. Production — Façon Sécurisée
1. Garder une console hors bande pendant le changement. Ne pas exécuter `connection up` à distance sans accès de secours.
2. Saisir uniquement les DNS internes de l'organisation si le serveur doit résoudre des noms internes; configurer les redirecteurs sur les résolveurs de l'infrastructure.
3. Ne pas supprimer ni recréer le profil réseau en production avant d'avoir vérifié les routes, les VLAN et les dépendances des services.

## ✅ Validation et retour arrière
- Confirmer l'adresse, la route par défaut et la résolution DNS; tester ensuite l'accès SSH dans une seconde session.
- En cas d'échec, rétablir les valeurs notées avant changement avec `nmcli connection modify`, puis réactiver le profil depuis la console.
- Vérifier l'état avec `nmcli connection show "$CON"` et les messages de `journalctl -u NetworkManager`.

## 🔗 Si le problème n'est pas résolu
- Vérifier la zone firewalld de l'interface, le VLAN côté hyperviseur/switch et les journaux NetworkManager.