# Le service DNS

## 🌐 Qu’est-ce que le DNS ?

Le **DNS** (Domain Name System) permet de traduire les noms de machines (FQDN) en adresses IP, et inversement.

### 🔹 Exemples :

- [www.google.com](http://www.google.com) → 142.250.74.68
- \SRVFIC01\Partage → 192.168.10.1

Il remplace la gestion manuelle par le fichier `hosts` local, tout en permettant un **espace de noms hiérarchique et distribué**.

---

## 📖 Types de serveurs DNS

|Rôle|Fonction principale|
|---|---|
|DNS hébergeur|Fait autorité sur un ou plusieurs espaces de noms|
|DNS résolveur|Interroge d'autres serveurs pour résoudre des noms|

> Un même serveur peut être **hébergeur et résolveur** à la fois.

### 🔹 Types de requêtes

|Type de requête|Fonctionnement|
|---|---|
|Récursive|Le serveur DNS **doit** répondre à la question|
|Itérative|Le serveur DNS **suggère un autre serveur** à interroger|

---

## 🛠️ Installation du rôle DNS

### 🔹 Via l’interface graphique

- **Server Manager** > `Add Roles and Features` > `DNS Server`

### 🔹 Via PowerShell

```powershell
Install-WindowsFeature -Name DNS -IncludeManagementTools
```

### 🔹 Ajout de zones (GUI ou PowerShell)

```powershell
Add-DnsServerPrimaryZone -Name "mondomaine.lcl" -ZoneFile "mondomaine.lcl.dns" -DynamicUpdate Secure
```

---

## 🗺️ Zones DNS et enregistrements

|Type de zone|Description|
|---|---|
|Zone directe|Associe un nom à une adresse IP (`A`, `CNAME`, `MX`...)|
|Zone inverse|Associe une adresse IP à un nom (`PTR`)|
|Zone secondaire|Copie en lecture seule d’une zone primaire|

### 🔹 Exemples d’enregistrements :

```powershell
Add-DnsServerResourceRecordA -Name "SRVFILE" -ZoneName "mondomaine.lcl" -IPv4Address "192.168.0.10"
```

```powershell
Add-DnsServerResourceRecordPtr -Name "10" -ZoneName "0.168.192.in-addr.arpa" -PtrDomainName "SRVFILE.mondomaine.lcl"
```

---

## 🔄 Mise à jour dynamique et transfert de zone

### 🔹 Enregistrements dynamiques

- Active Directory permet l’enregistrement automatique des postes membres du domaine
- Sinon : `ipconfig /registerdns` à la main

### 🔹 Transfert de zone

- Autoriser sur le maître : onglet `Transfert de zone`
- Créer une **zone secondaire** sur l’esclave avec l’IP du maître
- Type de transfert : `AXFR` (complet) ou `IXFR` (incrémental)

> ⚠️ Zones secondaires = lecture seule

---

## 🧩 Sous-domaines et délégations

### 🔹 Sous-domaine intégré

- Ajout d’enregistrements dans la **même zone principale**
- Exemple : `srv1.rennes.mondomaine.lcl` dans la zone `mondomaine.lcl`

### 🔹 Délégation de zone

- La gestion du sous-domaine est déléguée à un **autre serveur DNS**
- Exemple :
    - `rennes.mondomaine.lcl` délégué vers le serveur DNS `10.2.0.1`
    - Création d’une zone principale sur ce serveur
    - Sur le maître, clic droit > Nouvelle délégation > IP cible

---

## 🔁 Redirections et cache

### 🔹 Redirection non conditionnelle

- Toutes les requêtes externes passent par un DNS spécifique (ex : celui de l’opérateur)

### 🔹 Redirection conditionnelle

- Par domaine (ex : pour `enigme.lcl`, aller vers 10.0.0.254)
- Optimise les résolutions fréquentes ou privées

### 🔹 Mise en cache DNS

- TTL propre à chaque enregistrement
- Visible via :

```powershell
Clear-DnsClientCache
```

---

## 🧠 À retenir pour les révisions

- Le DNS est **indispensable à Active Directory**
- Il permet la **résolution directe et inverse**
- Il gère **SOA, NS, A, CNAME, PTR, MX, SRV...**
- Les zones secondaires sont en lecture seule
- Le DNS est un service critique → **superviser les journaux** et **sécuriser** son usage

---

## 📌 Bonnes pratiques professionnelles

|Pratique|Pourquoi ?|
|---|---|
|Toujours créer une zone inverse|Pour que les outils (nslookup, monitoring...) fonctionnent|
|Activer les mises à jour sécurisées|Empêche des enregistrements DNS non autorisés|
|Utiliser des noms de zones cohérents|Pour maintenir une arborescence propre et compréhensible|
|Créer des redirecteurs conditionnels|Pour la performance et la gestion de domaines multiples|
|Sauvegarder la configuration DNS|Zone files + paramètres DNS à sauvegarder régulièrement|