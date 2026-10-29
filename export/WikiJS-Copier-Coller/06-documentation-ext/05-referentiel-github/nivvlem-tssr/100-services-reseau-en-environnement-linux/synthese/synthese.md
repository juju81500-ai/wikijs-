# Synthèse – Services réseau en environnement Linux

## 📦 Services abordés et rôle

|Service|Rôle principal|
|---|---|
|Routage|Interconnecter plusieurs réseaux|
|NAT (pfSense)|Fournir un accès Internet via translation d’adresse|
|SSH|Administration distante sécurisée|
|DNS Résolveur|Résolution des noms publics via forwarder|
|DNS Autoritaire|Répondre pour un domaine donné, gérer zones directe/inverse|
|DHCP|Attribuer dynamiquement des IP aux postes clients|

---

## ⚙️ Commandes clés à retenir

### 🔹 Routage (Debian)

```bash
ip route add default via <IP_gateway>
sysctl -w net.ipv4.ip_forward=1
```

Fichier persistant : `/etc/sysctl.conf` → `net.ipv4.ip_forward=1`

### 🔹 DHCP (isc-dhcp-server)

```bash
apt install isc-dhcp-server
nano /etc/dhcp/dhcpd.conf
systemctl restart isc-dhcp-server
```

Validation : `dhcpd -t`

### 🔹 DNS (BIND9)

```bash
apt install bind9 bind9-utils
named-checkconf
named-checkzone domaine fichier_zone
rndc reload
```

### 🔹 SSH

```bash
apt install openssh-server
ssh user@ip_serveur
ssh-keygen && ssh-copy-id user@ip_serveur
```

### 🔹 Debug / outils réseau

```bash
ping, traceroute, dig, nslookup, ip a, ip r
```

---

## 🔍 Pièges courants à éviter

|Piège|Correction recommandée|
|---|---|
|Routage non actif entre interfaces|`sysctl -w net.ipv4.ip_forward=1` + redémarrage|
|BIND9 plante au démarrage|Vérifier les fichiers avec `named-checkconf` / `checkzone`|
|DHCP ne démarre pas|Mauvaise interface déclarée ou conflit sur la plage IP|
|Fichier `/etc/resolv.conf` écrasé par DHCP|Configurer DNS via NetworkManager ou le relancer après fix|
|Serial de zone DNS non incrémenté|Toujours incrémenter le `serial` dans les fichiers de zone|

---

## ✅ À retenir pour les révisions

- **Routage** : une passerelle par défaut et `ip_forward` actif sont nécessaires
- **NAT** (via pfSense) : indispensable pour accéder à Internet depuis un réseau privé
- **SSH** : permet l’accès distant sécurisé, utiliser les **clés publiques** plutôt que les mots de passe
- **DHCP** : fichier principal = `/etc/dhcp/dhcpd.conf`, attention à la **séparation IP fixe/DHCP**
- **DNS Résolveur** : utiliser des **redirecteurs fiables** (9.9.9.9, 1.1.1.1) dans `named.conf.options`
- **DNS Autoritaire** : bien séparer **zone directe/inverse**, et configurer un **secondaire** pour la redondance

---

## 📌 Bonnes pratiques professionnelles

|Pratique|Pourquoi ?|
|---|---|
|Toujours documenter les IP, routes, noms d’hôte|Permet une maintenance efficace et évite les conflits|
|Redémarrer les services proprement (`systemctl`)|Assurer le fonctionnement attendu après changement de conf|
|Tester la conf avant lancement (DHCP/DNS)|Prévenir les pannes au redémarrage|
|Surveiller les logs `/var/log/syslog`|Identifier les problèmes rapidement|
|Séparer les rôles (DHCP, DNS, NAT) entre machines|Meilleure sécurité et robustesse|