---
title: "TP 1 & 2 – Configurer un service DNS faisant autorité et secondaire (BIND9)"
description: "1. Déclaration de la zone dans /etc/bind/named.conf.local"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP 1 & 2 – Configurer un service DNS faisant autorité et secondaire (BIND9)

## ✅ TP 1 – Configurer un service DNS faisant autorité

### 🔹 Étape 1 – Héberger une zone directe sur `DEB-S2`

1. **Déclaration de la zone dans `/etc/bind/named.conf.local`**

```bash
zone "tssr.eni" {
  type master;
  file "/var/cache/bind/db.tssr.eni";
};
```

2. **Création du fichier de zone directe `/var/cache/bind/db.tssr.eni`**

```bash
$ORIGIN tssr.eni.
$TTL 86400
@  IN SOA deb-s2.tssr.eni. admin.tssr.eni. (
    1 86400 7200 3600000 3600 )

@     IN NS deb-s2.tssr.eni.

# Enregistrements
ns1     IN A 192.168.100.12
pfsense IN A 172.30.100.1
deb-s1  IN A 192.168.100.11
deb-s2  IN A 192.168.100.12
routux  IN A 192.168.100.254
routux  IN A 172.18.100.254
test    IN CNAME ns1.tssr.eni.
```

3. **Contrôle de syntaxe et rechargement**

```bash
named-checkzone tssr.eni /var/cache/bind/db.tssr.eni
rndc reload
```

### 🔹 Étape 2 – Résolution depuis `cli-db-12`

1. **Configurer `/etc/resolv.conf`**

```bash
nameserver 192.168.100.12
```

2. **Tester avec `dig`**

```bash
dig soa tssr.eni
dig ns tssr.eni
dig deb-s1.tssr.eni
dig test.tssr.eni
dig pfsense.tssr.eni
```

3. **Configurer le DHCP pour inclure le domaine**

```bash
option domain-name "tssr.eni";
```

Permet une résolution par nom court sans FQDN.

### 🔹 Étape 3 – Zone inverse

1. **Ajout dans `named.conf.local`**

```bash
zone "100.18.172.in-addr.arpa" {
  type master;
  file "/var/cache/bind/db.inv.172.18.100";
};

zone "100.168.192.in-addr.arpa" {
  type master;
  file "/var/cache/bind/db.inv.192.168.100";
};
```

2. **Fichiers de zones inverses**

```bash
# /var/cache/bind/db.inv.172.18.100
$TTL 86400
@ IN SOA deb-s2.tssr.eni. admin.tssr.eni. (1 86400 7200 3600000 3600)
@ IN NS deb-s2.tssr.eni.
254 IN PTR routux.tssr.eni.

# /var/cache/bind/db.inv.192.168.100
254 IN PTR routux.tssr.eni.
11  IN PTR deb-s1.tssr.eni.
12  IN PTR deb-s2.tssr.eni.
```

3. **Tests depuis `cli-db-12`**

```bash
dig -x 172.18.100.254
dig -x 192.168.100.254
```

✔️ Résolution inverse confirmée

---

## ✅ TP 2 – Configurer un service DNS secondaire (DEB-S1)

### 🔹 Étape 1 – Autoriser les transferts

Dans `named.conf.local` sur DEB-S2 :

```bash
zone "tssr.eni" {
  type master;
  file "/var/cache/bind/db.tssr.eni";
  allow-transfer { 192.168.100.11; };
};
```

Tester :

```bash
# Depuis cli-db-12 : dig axfr tssr.eni @192.168.100.12 → refusé
# Depuis deb-s1 : dig axfr tssr.eni @192.168.100.12 → OK
```

### 🔹 Étape 2 – Déclarer le DNS secondaire

1. Sur `db.tssr.eni` (zone primaire), ajouter :

```bash
@ IN NS deb-s1.tssr.eni.
```

2. Sur DEB-S1 : `/etc/bind/named.conf.local`

```bash
zone "tssr.eni" {
  type slave;
  file "/var/cache/bind/db.tssr.eni";
  masters { 192.168.100.12; };
};
```

```bash
named-checkconf -z
rndc reload
```

### 🔹 Étape 3 – Tests de redondance

- Tester la résolution via `dig` avec `@192.168.100.11`
- Stopper Bind sur DEB-S2
- Ping des FQDN depuis `cli-db-12` → OK

### 🔹 Étape 4 – Analyse logs & extension DNS

1. Suivi DNS

```bash
rndc querylog
journalctl -fu bind9.service
```

2. Ajouter un enregistrement sur DEB-S2 + `rndc reload`
3. Observer l’échange IXFR → DEB-S1 récupère le diff
4. Configurer `DEB-S1` pour forwarding en cas de requête externe

```bash
options {
  recursion yes;
  allow-query { 172.18.100.0/24; 192.168.100.0/24; };
  forwarders {
    9.9.9.9;
  };
  dnssec-validation no;
};
```

📌 Limitation actuelle : **pas de redondance sur la zone inverse**. À corriger en la déclarant aussi en zone secondaire sur DEB-S1.

---

## 📌 Bonnes pratiques professionnelles

|Pratique|Pourquoi ?|
|---|---|
|Incrémenter le serial après chaque modification|Permet la réplication correcte vers les serveurs secondaires|
|Tester la syntaxe (`named-checkzone`, `checkconf`)|Prévenir les erreurs de démarrage de Bind9|
|Surveiller les transferts (IXFR/AXFR)|Vérifier la cohérence et la mise à jour entre maîtres/esclaves|
|Configurer le DNS secondaire pour cache/forward|Continuité de service si le maître tombe|
|Étendre la redondance aux zones inverses|Garantir la résolution IP → nom en cas de panne|