# Mise en situation professionnelle : Services réseau

## Architecture

## 🗺️ Conception de l'architecture réseau

Dans cette partie, nous allons concevoir l'architecture réseau en détaillant la **topologie**, le **plan d'adressage IPv4**, l'installation de **pfSense** en tant que routeur, et la **configuration du routage et du NAT**.

---

## 🌐 Topologie réseau

L'infrastructure est divisée en **trois réseaux distincts** :

|Réseau|Rôle|
|---|---|
|**LAN Clients**|Réseau des postes utilisateurs|
|**LAN Serveurs**|Réseau des serveurs internes (AD, DNS, DHCP, fichiers...)|
|**WAN**|Accès vers Internet et dépôts externes via proxy ENI (ou simulé)|

> Les interfaces réseau seront associées dans VMware comme suit :
> - **VMNet3** : LAN Clients
> - **VMNet2** : LAN Serveurs
> - **VMNet0 (Bridged)** : WAN (vers le réseau ENI)

---

## 🔢 Plan d'adressage IPv4

Données personnelles :

- Adresse IP de poste ENI : dernier octet `13`
- Calcul : `13 x 4 = 52` → réseau : `192.168.52.0/22`

Découpage en /24 :

|Réseau|Adresse|Masque|VMNet|
|---|---|---|---|
|LAN Clients|192.168.52.0|255.255.255.0|VMNet3|
|LAN Serveurs|192.168.55.0|255.255.255.0|VMNet2|
|WAN (ENI)|10.107.0.0|255.255.0.0|Bridged (VMNet0)|

---

## 🛠️ Installation et configuration de pfSense

### Création de la VM pfSense

- **Nom de la VM** : `ROUTEUR-MD`
- **ISO** : pfSense
- **Disques & ressources** : 1 vCPU, 1 Go RAM, 10 Go HDD
- **Réseaux à attacher** :
    - `vmnet0` (mode Bridged) → WAN
    - `vmnet2` → LAN Serveurs
    - `vmnet3` → LAN Clients

### Interface pfSense → correspondance

|Interface pfSense|VMware|Adresse IP attribuée|
|---|---|---|
|WAN (`em0`)|VMNet0|10.107.42.13|
|LAN Serveurs (`em1`)|VMNet2|192.168.55.254|
|LAN Clients (`em2`)|VMNet3|192.168.52.254|

> Les adresses utilisées sont les **dernières de chaque sous-réseau utilisable**.

---

## 🔒 Configuration des règles de pare-feu pfSense

### Pourquoi une règle "Allow All" (any) ?

Par défaut, pfSense **bloque tout** le trafic entrant sur ses interfaces LAN. Pour autoriser la circulation du trafic (ping, accès SSH, AD, etc.), il est nécessaire de créer une règle "any to any" sur chaque interface interne.

### Étapes :

1. Accès à l’interface web de pfSense (`https://192.168.55.254` depuis un serveur).
2. **Firewall > Rules**.
3. Onglet correspondant à l’interface (LAN Clients ou LAN Serveurs).
4. **Add (flèche vers le haut)**.
5. Paramétrage de la règle :
    - **Action** : Pass
    - **Interface** : (celle en cours)
    - **Address Family** : IPv4
    - **Protocol** : Any
    - **Source** : any
    - **Destination** : any
6. **Save**, puis **Apply Changes**.
7. Répétition de cette opération pour chaque interface interne.

---

## 🌍 Activer le NAT (Accès Internet)

1. Dans pfSense, **Firewall > NAT > Outbound**.
2. Mode : **Hybrid Outbound NAT rule generation**.
3. **Save**, puis **Apply Changes**.
4. **Add** et créer une règle de NAT automatique pour chaque interface interne (LAN Clients et LAN Serveurs) vers l’interface WAN.

- Interface : LAN
- Source : `192.168.52.0/24` ou `192.168.55.0/24`
- Translation address : Interface Address (WAN)

---

## 🧪 Vérifications essentielles

- Depuis pfSense → **Diagnostics > Ping** vers :
    - `9.9.9.9` (vérifier accès Internet)
    - `192.168.52.1` et `192.168.55.1` (machines clientes)
- Depuis une VM cliente (Windows ou Debian), tester le ping vers :
    - `192.168.52.254` ou `192.168.55.254` (pfSense)

> Si ping KO : vérifier que la VM est sur le bon réseau (VMNet), que la carte réseau est activée, et que la configuration IP est correcte.

---

## ⚠️ Bonnes pratiques à respecter

- **Conserver une copie exportée de la config pfSense (.xml)** via **Diagnostics > Backup & Restore**
- Toujours **attribuer une IP fixe** à pfSense sur chaque interface (évite les conflits DHCP)
- Créer un fichier de documentation listant :
    - les interfaces VMware
    - les IPs associées
    - le rôle des interfaces
    - les correspondances internes pfSense