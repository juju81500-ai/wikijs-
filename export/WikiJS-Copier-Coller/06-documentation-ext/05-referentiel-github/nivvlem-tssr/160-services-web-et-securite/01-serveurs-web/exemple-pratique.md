# TP – Installation de l’infrastructure

> **Objectif :** Mettre en place l’infrastructure de maquettage pour les TP de la semaine.

---

## 🔧 Objectifs

- Définir le sous-réseau de maquettage
- Découper les sous-réseaux pour chaque zone (Utilisateurs, Serveurs, DMZ)
- Définir l’adressage IP pour chaque machine
- Installer et configurer les VMs nécessaires
- Déployer un contrôleur de domaine avec le rôle ADDS

---

## 🧼 Étape 1 : Calcul du sous-réseau principal

- Réseau attribué : `192.168.128.0/17`
- On divise en 32 sous-réseaux → besoin de **5 bits supplémentaires** (`/22`)
- Huitième sous-réseau : valeur binaire `00111` = **28**
- → Adresse du sous-réseau : **`192.168.156.0/22`**

---

## 🗽 Étape 2 : Sous-réseaux dédiés à l'infrastructure

|Zone|Sous-réseau|Taille|
|---|---|---|
|Utilisateurs|`192.168.157.128/26`|64 IPs|
|Serveurs|`192.168.159.120/29`|8 IPs|
|DMZ|`192.168.159.232/29`|8 IPs|

---

## 🧑‍💻 Étape 3 : Plan d'adressage IP

### Réseau Utilisateurs (`192.168.157.128/26`)

|Machine|IP|
|---|---|
|Client Debian|`192.168.157.129`|
|Client Windows|`192.168.157.130`|
|Routeur (pfSense)|`192.168.157.190`|
|Broadcast|`192.168.157.191`|

### Réseau Serveurs (`192.168.159.120/29`)

| Machine                        | IP                |
| ------------------------------ | ----------------- |
| Contrôleur de domaine (CD-DNS) | `192.168.159.120` |
| Serveur Web IIS                | `192.168.159.125` |
| Routeur (pfSense)              | `192.168.159.126` |
| Broadcast                      | `192.168.159.127` |

### Réseau DMZ (`192.168.159.232/29`)

| Machine           | IP                |
| ----------------- | ----------------- |
| Serveur Apache    | `192.168.159.233` |
| Routeur (pfSense) | `192.168.159.238` |
| Broadcast         | `192.168.159.239` |

---

## 💻 Étape 4 : Configuration des VMs

|VM|OS|Rôle|Réseau (VMnet)|
|---|---|---|---|
|CD-DNS|Windows Server 2019|Contrôleur de domaine|LAN_Srv (VMNet10)|
|SRV-IIS|Windows Server 2019|Serveur IIS|LAN_Srv (VMNet10)|
|DEB-SRV|Debian (CLI)|Serveur Apache|DMZ (VMNet12)|
|Debian Client|Debian (GUI)|Client utilisateur|LAN_Users (VMNet11)|
|Windows Client|Windows 10|Client utilisateur|LAN_Users (VMNet11)|
|pfSense|pfSense|Firewall/Routeur|WAN (Bridged), +3 OPTs|

- **pfSense WAN** : DHCP / Bridged
- **pfSense LAN_Srv** : VMNet10
- **pfSense LAN_Users** : VMNet11
- **pfSense DMZ** : VMNet12

---

## 🧱 Étape 5 : Installation et configuration du rôle ADDS

### 1. Configuration du nom d'hôte

Sur la VM `CD-DNS`, nommer la machine :

```
Nom : CD-DNS
```

### 2. Attribuer une IP statique

```
IP : 192.168.159.120
Masque : 255.255.255.248
Passerelle : 192.168.159.126
DNS : 127.0.0.1
```

### 3. Installer le rôle ADDS

```powershell
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
```

### 4. Promotion en tant que DC

Utiliser l'assistant graphique pour :

- Créer une nouvelle forêt
- Nom du domaine : **nivvlem.md**

### 5. Redémarrer et valider l'intégration du domaine

---

## 🌐 Étape 6 : Configuration initiale de pfSense

### Interfaces réseau

Depuis la console :

- `WAN` → interface bridged (DHCP)
- `LAN` → VMNet10 (LAN_Srv)
- `OPT1` → VMNet11 (LAN_Users)
- `OPT2` → VMNet12 (DMZ)

### Attribution des IP

- `LAN (LAN_Srv)` : `192.168.159.126`
- `OPT1 (LAN_Users)` : `192.168.157.190`
- `OPT2 (DMZ)` : `192.168.159.238`

### Activer le NAT

- Par défaut, le NAT est activé en mode automatique (recommended).
- Vérifier via : **Firewall > NAT > Outbound**

### DNS Resolver

- Aller dans **Services > DNS Resolver**
- Activer l’écoute sur toutes les interfaces (All).
- S’assurer que les clients obtiennent le DNS de pfSense dans leur configuration IP.

### DHCP (optionnel)

- Peut être activé uniquement sur les interfaces clients (ex : LAN_Users) si besoin de simplifier.
- Déconseillé sur le LAN_Srv : préférer les IP fixes côté serveur.

---

## ✅ Bonnes pratiques à retenir

- Toujours réserver les premières et dernières adresses pour les routeurs et services critiques
- Attribuer des noms explicites aux VMs
- Documenter rigoureusement votre plan d’adressage
- Isoler la DMZ sur un réseau dédié avec un accès restreint via pfSense
- Tester chaque communication inter-réseau une fois l’infrastructure déployée

---

## ⚠️ Pièges à éviter

- Oublier de définir des IP statiques avant l'intégration au domaine
- Configurer les mauvaises interfaces dans pfSense (attention à l'ordre des cartes)
- Ne pas installer les outils RSAT après l’installation d’ADDS