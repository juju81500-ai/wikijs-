# DNS autoritaire sur zone (Linux / BIND9)

## 🌐 Rôle d’un DNS faisant autorité

Un serveur DNS **faisant autorité** est :

- la **source officielle des informations** pour un ou plusieurs domaines
- consulté par des **résolveurs DNS** pour obtenir des réponses valides
- capable de gérer une **zone primaire** (modifiable localement)
- ou de **répliquer une zone secondaire** (en lecture seule, synchronisée avec un maître)

### 🔹 Types de zones

|Type de zone|Description|
|---|---|
|Zone directe|Association FQDN → IP (ex : `www → 192.168.0.10`)|
|Zone inverse|Association IP → FQDN (ex : `192.168.0.10 → www`)|

> 📌 Les zones inverses utilisent le format `in-addr.arpa`

---

## 🧩 Types d’enregistrements dans une zone

|Type|Rôle|
|---|---|
|SOA|Paramètres globaux de la zone (nom du serveur maître…)|
|NS|Serveur(s) DNS faisant autorité pour cette zone|
|A|FQDN vers adresse IPv4|
|AAAA|FQDN vers adresse IPv6|
|MX|Serveur de messagerie associé au domaine|
|CNAME|Alias d’un nom (redirection vers un autre FQDN)|
|PTR|Résolution inverse (IP → nom)|
|SRV|Référencement de services (ex : LDAP, SIP, etc.)|

---

## 🛠️ Création d’une zone primaire avec BIND9

### 🔹 Fichier : `/etc/bind/named.conf.local`

```bash
zone "demo.eni" {
  type master;
  file "/etc/bind/db.demo.eni";
};

zone "42.168.192.in-addr.arpa" {
  type master;
  file "/etc/bind/db.192.168.42";
};
```

### 🔹 Exemple de fichier de zone directe `/etc/bind/db.demo.eni`

```bash
$TTL 86400
@   IN  SOA demo.eni. admin.demo.eni. (
            2025041001 ; serial
            3600       ; refresh
            1800       ; retry
            604800     ; expire
            86400 )    ; minimum

    IN  NS  ns1.demo.eni.

DB10-FS1      IN  A     10.9.9.5
DB10-FS2      IN  A     10.9.9.10
DB10-INFRA1   IN  A     10.9.9.9
DB10-INFRA1   IN  AAAA  2001:DBB::EC01:e
```

### 🔹 Exemple de zone inverse `/etc/bind/db.192.168.42`

```bash
$TTL 86400
@   IN  SOA demo.eni. admin.demo.eni. (
            2025041001 ; serial
            3600       ; refresh
            1800       ; retry
            604800     ; expire
            86400 )    ; minimum

    IN  NS  ns1.demo.eni.

103 IN PTR SPX.PE.JO.
104 IN PTR GLS.PE.JO.
205 IN PTR GTI.PE.JO.
```

> ✅ Ne pas oublier d’incrémenter le **serial** à chaque modification

---

## 🔁 Zone secondaire (slave)

### 🔹 Configuration sur le serveur secondaire

```bash
zone "demo.eni" {
  type slave;
  masters { 10.9.9.1; };
  file "/var/cache/bind/demo.eni.zone";
};
```

- Le serveur secondaire télécharge la zone depuis le maître à l’aide de l’adresse IP indiquée.

---

## ✅ À retenir pour les révisions

- Un DNS faisant autorité **répond directement** pour une zone définie
- Les zones doivent être déclarées dans `named.conf.local`
- Le fichier de zone doit toujours commencer par un **SOA + NS**
- Les zones inverses utilisent un format inversé `in-addr.arpa`
- Les **zones secondaires** sont en lecture seule, synchronisées automatiquement

---

## 📌 Bonnes pratiques professionnelles

|Pratique|Pourquoi ?|
|---|---|
|Utiliser des noms cohérents et explicites|Facilite le support et la maintenance|
|Incrémenter le serial après chaque modif|Permet la réplication correcte vers les serveurs secondaires|
|Tester chaque zone avec `named-checkzone`|Valider la cohérence syntaxique avant relance|
|Limiter les requêtes autorisées (ACL, `allow-query`)|Sécuriser l’exposition du service|
|Distinguer zone directe et zone inverse|Permet la résolution dans les deux sens (nom ↔ IP)|