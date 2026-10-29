# Mise en situation professionnelle : Services réseau

## Redondance

## 🛠️ 1. DHCP redondant

### 🔁 Rappel :

Premier DHCP hébergé sur : `SRV-LNX-MD` (192.168.55.111)

### ➕ Ajouter un second serveur DHCP

Sur `SRV-SVC-MD` (192.168.55.102) :

```powershell
Install-WindowsFeature DHCP -IncludeManagementTools
```

Configurer une **plage DHCP complémentaire** :

```text
Plage : 192.168.52.200 - 192.168.52.250
Passerelle : 192.168.52.254
DNS : 192.168.55.102, 192.168.55.111
```

### 🔁 Activer le relais DHCP sur pfSense

1. Interface Web > **Services > DHCP Relay**
2. Activer sur l’interface LAN Clients
3. Ajouter les deux IP : `192.168.55.111`, `192.168.55.102`
4. Sauvegarder et redémarrer le service relay

### ✅ Tests DHCP

- Arrêter l’un des deux serveurs DHCP → vérifier l’attribution d’adresses IP par l’autre
- Observer dans `/var/log/syslog` (Debian) ou via l'observateur d'événements (Windows)

---

## 🌐 2. DNS secondaire avec zone répliquée

### 📍 Contexte :

Zone principale `melvin13.infra.tld` hébergée sur : `SRV-SVC-MD`

### ➕ Ajouter le rôle DNS sur `SRV-LNX-MD`

```bash
sudo apt install bind9 -y
```

### 🛠️ Créer une **zone secondaire** sur SRV-LNX-MD

Dans `/etc/bind/named.conf.local` :

```bash
zone "melvin13.infra.tld" IN {
    type slave;
    masters { 192.168.55.102; };
    file "/var/cache/bind/melvin13.infra.tld.zone";
};
```

Puis :

```bash
sudo systemctl restart bind9
```

> Sur le DNS principal (SRV-SVC-MD), autoriser le transfert de zone vers `192.168.55.111` dans les propriétés de la zone.

### 🔍 Vérification

```bash
dig @192.168.55.111 srv-ad-md.melvin13.infra.tld
```

---

## 🏢 3. Second contrôleur de domaine

### ➕ Promouvoir SRV-SVC-MD comme second DC

Sur `SRV-SVC-MD` (déjà membre du domaine) :

```powershell
Install-WindowsFeature AD-Domain-Services -IncludeManagementTools
```

Puis lancer : **Gestionnaire de serveur > Notifications > Promouvoir en contrôleur de domaine**

- Ajouter à une **forêt existante** : `melvin13.domaine.tssr`
- Choisir : DNS + Global Catalog (par défaut)
- Réplication depuis : `SRV-AD-MD`

### 🔁 Vérifier la réplication

```powershell
repadmin /replsummary
```

### 🔁 Vérifier les enregistrements DNS liés au nouveau DC

Dans la zone DNS intégrée, tu devrais voir :

- `_ldap._tcp.dc._msdcs.melvin13.domaine.tssr` → avec les deux serveurs

### 🔄 Test de redondance AD

1. Éteindre `SRV-AD-MD`
2. Depuis `CLT-WIN-MD`, ouvrir une session avec un utilisateur du domaine
3. Vérifie que la connexion fonctionne malgré la coupure du premier DC

---

## 📄 Synthèse

|Service|Serveur principal|Serveur secondaire|Testé ?|
|---|---|---|---|
|DHCP|SRV-LNX-MD (Debian)|SRV-SVC-MD (Windows)|✅|
|DNS|SRV-SVC-MD (Windows)|SRV-LNX-MD (Debian)|✅|
|Active Directory|SRV-AD-MD (Windows)|SRV-SVC-MD (Windows)|✅|