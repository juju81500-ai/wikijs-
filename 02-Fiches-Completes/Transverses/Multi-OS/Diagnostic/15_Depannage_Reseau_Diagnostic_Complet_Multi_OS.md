# Dépanner un réseau : diagnostic complet multi-OS

- **Environnement** : VM, poste, serveur, LXC Proxmox ou hôte/conteneur Docker
- **OS / Version** : Debian 12/13, Ubuntu 24.04/26.04, Rocky Linux 9, Alpine Linux, Windows 10/11, Windows Server 2022/2025
- **Catégorie** : Réseau / Diagnostic / Dépannage
- **Tags** : `reseau`, `diagnostic`, `debian`, `ubuntu`, `rocky`, `alpine`, `windows`, `docker`, `dns`, `routage`

## 1. Objectif et périmètre

Fiche simple : [cadrer l'objectif et le périmètre](../../../../01-Fiches-Simples/Transverses/Multi-OS/Diagnostic-Reseau/Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Cadrer_Perimetre.md).

Isoler une panne réseau sans appliquer de changement au hasard. Le parcours va de l'interface au service : **Lien → Adresse → Passerelle → Route → DNS → Port → Application**.

Cette fiche concerne le diagnostic d'un poste ou serveur. La configuration persistante se fait ensuite avec le gestionnaire propre à l'OS : Netplan, NetworkManager, systemd-networkd, OpenRC, paramètres Windows ou configuration Proxmox/Docker.

## 2. Sécuriser le diagnostic

Fiche simple : [sécuriser le diagnostic](../../../../01-Fiches-Simples/Transverses/Multi-OS/Diagnostic-Reseau/Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Securiser_Diagnostic.md).

1. Noter l'heure, la machine, l'interface, le VLAN, l'adresse source, la destination et le port concerné.
2. Comparer avec une machine fonctionnelle du même segment et avec les changements récents (IP, DHCP, DNS, firewall, switch, hyperviseur).
3. Garder une console/hyperviseur ou un accès hors bande avant une modification réseau distante.
4. Ne pas vider les règles firewall, désactiver le pare-feu, remplacer tous les DNS ou redémarrer toute la pile réseau pour « tester ».
5. Tester uniquement une adresse et un port autorisés, pas un balayage réseau.

## 3. Étape 1 — Vérifier le lien et l'interface

Fiche simple : [vérifier le lien et l'interface](../../../../01-Fiches-Simples/Transverses/Multi-OS/Diagnostic-Reseau/Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Lien_Interface.md).

### Linux : Debian, Ubuntu, Rocky

```bash
ip -br link
ip -br address
```

Pour identifier le gestionnaire actif :

```bash
systemctl is-active NetworkManager systemd-networkd
nmcli -f NAME,DEVICE,TYPE connection show --active
networkctl list
```

L'absence de `NetworkManager` ou `systemd-networkd` peut être normale si l'autre gestionnaire est utilisé. Ne pas en activer un second avant d'avoir identifié le propriétaire de l'interface.

### Alpine Linux

```sh
ip -br link
ip -br addr
ip route
rc-status
```

Pour un LXC Proxmox, vérifier aussi la configuration réseau du CT sur l'hôte; l'adresse, la passerelle, le bridge et le VLAN sont souvent gérés par Proxmox.

### Windows 10/11 et Windows Server

```powershell
Get-NetAdapter | Format-Table Name, Status, LinkSpeed, MacAddress
Get-NetIPConfiguration
```

En GUI, ouvrir `ncpa.cpl` et vérifier que la bonne carte est activée. Ne pas supprimer/recréer la carte virtuelle avant d'avoir noté ses paramètres.

### Interprétation

| Observation | Vérification suivante |
|---|---|
| Interface `DOWN` ou `Disconnected` | Câble, carte, port switch, état de la vNIC/bridge et VLAN |
| Interface active mais sans adresse attendue | DHCP, réservation, configuration du gestionnaire réseau ou configuration PVE |
| Plusieurs interfaces/routes inattendues | VPN, bridge, bonding, VLAN, Docker ou routes statiques |

## 4. Étape 2 — Vérifier adresse, masque et passerelle

Fiche simple : [vérifier adresse, masque et passerelle](../../../../01-Fiches-Simples/Transverses/Multi-OS/Diagnostic-Reseau/Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Adresse_Passerelle.md).

### Linux

```bash
ip -br address
ip route
ip route get <IP_DESTINATION>
```

### Windows

```powershell
Get-NetIPConfiguration
Get-NetRoute -DestinationPrefix 0.0.0.0/0
```

Vérifier que l'adresse et le préfixe correspondent au plan réseau, qu'il n'y a pas de conflit IP et qu'une route permet d'atteindre la destination. Ne pas attribuer une IP de documentation (`192.0.2.0/24`) à une machine de production.

Tester la passerelle si ICMP est autorisé :

```bash
ping -c 3 <IP_PASSERELLE>
```

```powershell
Test-Connection <IP_PASSERELLE> -Count 3
```

Un échec ping n'est pas une preuve suffisante : ICMP peut être filtré alors que le service fonctionne.

## 5. Étape 3 — Vérifier le chemin vers la destination

Fiche simple : [vérifier le chemin vers la destination](../../../../01-Fiches-Simples/Transverses/Multi-OS/Diagnostic-Reseau/Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Chemin_Destination.md).

1. Comparer la route choisie par le système avec la destination et l'interface attendue.
2. Tester un saut réseau si l'outil est installé et autorisé :
   ```bash
   tracepath <IP_DESTINATION>
   ```
   Sous Windows :
   ```powershell
   tracert -d <IP_DESTINATION>
   ```
3. Si la passerelle locale est joignable mais pas le réseau distant, vérifier routage, ACL, VPN, VLAN et routes de retour auprès du propriétaire du réseau.

Ne pas conclure qu'un routeur est en panne uniquement parce qu'un saut intermédiaire ne répond pas; les équipements peuvent filtrer les sondes de traceroute.

## 6. Étape 4 — Vérifier le DNS

Fiche simple : [vérifier le DNS](../../../../01-Fiches-Simples/Transverses/Multi-OS/Diagnostic-Reseau/Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_DNS.md).

Tester d'abord l'adresse IP connue, puis le nom. Cela sépare une panne de routage d'une panne de résolution.

### Debian/Ubuntu avec systemd-resolved

```bash
resolvectl status
resolvectl query <NOM_DNS>
getent ahosts <NOM_DNS>
```

### Rocky Linux

```bash
nmcli device show
cat /etc/resolv.conf
getent ahosts <NOM_DNS>
```

### Alpine Linux

```sh
cat /etc/resolv.conf
nslookup <NOM_DNS>
```

Dans un LXC, confirmer si `/etc/resolv.conf` est géré par Proxmox avant toute édition.

### Windows

```powershell
Get-DnsClientServerAddress
Resolve-DnsName <NOM_DNS>
```

Vérifier que les DNS configurés sont ceux du réseau attendu. Un poste joint à Active Directory doit utiliser les DNS AD internes; ne pas ajouter un DNS public comme secours pour un domaine privé.

## 7. Étape 5 — Vérifier le port et le service

Fiche simple : [vérifier le port et le service](../../../../01-Fiches-Simples/Transverses/Multi-OS/Diagnostic-Reseau/Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Port_Service.md).

Tester le port précis depuis le client concerné; adapter cible et port aux flux autorisés.

### Linux

```bash
nc -vz -w 3 <HOTE_CIBLE> <PORT>
```

Vérifier l'écoute locale côté serveur :

```bash
sudo ss -lntup
systemctl --failed
```

### Windows

```powershell
Test-NetConnection <HOTE_CIBLE> -Port <PORT>
Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction
```

Vérifier ensuite le service et ses journaux; une connexion TCP réussie ne valide pas à elle seule l'application ou son authentification.

## 8. Cas particuliers des conteneurs

Fiche simple : [traiter les cas particuliers des conteneurs](../../../../01-Fiches-Simples/Transverses/Multi-OS/Diagnostic-Reseau/Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Conteneurs.md).

### Docker Compose

```bash
docker compose ps
 docker network ls
```

Inspecter le réseau, puis tester le nom du service et le port depuis le réseau Compose :

```bash
docker network inspect <RESEAU_COMPOSE>
docker compose exec <SERVICE_CLIENT> getent hosts <SERVICE_CIBLE>
docker compose logs --tail 100 <SERVICE_CIBLE>
```

Les noms de service sont résolus dans le réseau Compose; un port interne n'est pas nécessairement publié sur l'hôte. Ne pas exécuter `iptables -F` ou `nft flush ruleset` pour dépanner Docker.

### LXC Proxmox

Contrôler le bridge, le VLAN tag, l'adresse, la passerelle et le firewall dans la configuration Proxmox du CT, puis comparer avec `ip -br addr` et `ip route` dans le conteneur. Conserver la console Proxmox pendant toute correction réseau.

## 9. Réparer sans aggraver la panne

Fiche simple : [réparer sans aggraver la panne](../../../../01-Fiches-Simples/Transverses/Multi-OS/Diagnostic-Reseau/Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Reparer_Sans_Aggraver.md).

1. **Lien/VLAN :** corriger le port switch, bridge ou VLAN à la source; ne pas changer simultanément la configuration IP du CT.
2. **Adresse/route :** modifier uniquement le profil ou fichier possédé par le gestionnaire réseau actif; sauvegarder la configuration avant modification.
3. **DNS :** corriger le résolveur prévu par l'organisation; ne pas figer `/etc/resolv.conf` ni contourner le DNS d'entreprise par un résolveur public.
4. **Pare-feu :** ajouter une règle minimale pour une source, une destination, un protocole et un port; vérifier d'abord les règles existantes et la politique de l'hôte.
5. Après chaque modification, refaire seulement le test qui avait échoué et garder une session de secours ouverte.

## 10. Validation et retour arrière

Fiche simple : [valider et revenir en arrière](../../../../01-Fiches-Simples/Transverses/Multi-OS/Diagnostic-Reseau/Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Validation_Retour_Arriere.md).

- Refaire la chaîne **Lien → Adresse → Passerelle → Route → DNS → Port → Application** depuis le client touché.
- Tester aussi depuis une machine qui ne doit pas être autorisée pour confirmer le filtrage attendu.
- Comparer les résultats avant/après, noter le changement et surveiller le service.
- Si l'accès est perdu, restaurer le profil/fichier ou la configuration réseau Proxmox précédente depuis la console; ne pas enchaîner d'autres changements à l'aveugle.

## 11. Informations à transmettre pour escalade

Fiche simple : [préparer l'escalade](../../../../01-Fiches-Simples/Transverses/Multi-OS/Diagnostic-Reseau/Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_Escalade.md).

- Nom/OS/version de la machine, interface, adresse/préfixe, VLAN et passerelle.
- Destination, port, heure du test et message d'erreur exact.
- Résultats des commandes pertinentes, changements récents et tests réalisés depuis un poste fonctionnel.
- Règles firewall/ACL modifiées et méthode de retour arrière utilisée.

## Fiches simples complémentaires

- [[Fiche_Simple_-_VM_Debian_13_IP_Statique_systemd-networkd]]
- [[Fiche_Simple_-_VM_Ubuntu_24.04_LTS_Reseau_Netplan_IP_et_DNS]]
- [[Fiche_Simple_-_VM_Rocky_9_Reseau_IP_Statique_NetworkManager_nmcli]]
- [[Fiche_Simple_-_LXC_Alpine_3.19_Reseau_Diagnostic_DNS_Routes]]
- [[Fiche_Simple_-_Docker_Reseau_Diagnostic_Reseaux_Compose]]
- [[Reparation_DNS_Linux_Resolution_Echec]]
- [[Reparation_SSH_Acces_Distant_Impossible]]
