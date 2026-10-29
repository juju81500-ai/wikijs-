# Mise en situation professionnelle : Services réseau

## Serveurs

## 🚀 Ajout et configuration des serveurs

Dans cette étape, nous allons ajouter trois serveurs à l’infrastructure virtuelle, en respectant une convention de nommage, un plan d’adressage cohérent et une configuration réseau stable.

---

## 📁 Serveurs à déployer

|Nom de la machine|OS|Adresse IP|Rôle(s) prévus|VMNet|
|---|---|---|---|---|
|SRV-AD-MD|Windows Server|192.168.55.101|Contrôleur de domaine AD, DNS|VMNet2|
|SRV-SVC-MD|Windows Server|192.168.55.102|DHCP, serveur de fichiers, DNS|VMNet2|
|SRV-LNX-MD|Debian (minimal)|192.168.55.111|DHCP, DNS (selon parité), tests|VMNet2|

> **Convention de nommage** :
> 
> - `SRV-AD-MD` : serveur Active Directory (MD pour tes initiales)
> - `SRV-SVC-MD` : serveur de services
> - `SRV-LNX-MD` : serveur GNU/Linux

---

## 🔧 Création des VMs

### Pour chaque VM :

- **Réseau** : Custom > VMNet2
- **Disque** : 60 Go pour les Windows, 20 Go pour Debian
- **RAM** : 4 Go pour les Windows, 1 Go pour Debian
- **Nombre de CPU** : 1
- **Nom de la VM** : selon le tableau ci-dessus

> Utilisation des images "sysprep" pour accélérer la déploiement.

---

## 🔌 Configuration réseau des serveurs

Sur chaque machine, configuration d'une adresse IP statique (pas de DHCP à ce stade).

### Exemple pour SRV-AD-MD (Windows) :

1. **Panneau de configuration > Centre Réseau et partage**.
2. **Modifier les paramètres de la carte**.
3. Interface Ethernet > **Propriétés**.
4. **Protocole Internet version 4 (TCP/IPv4)**.
5. **Utiliser l’adresse IP suivante** :
    - IP : `192.168.55.101`
    - Masque : `255.255.255.0`
    - Passerelle : `192.168.55.254`
    - DNS (temporaire) : `192.168.55.254` (pfSense) ou DNS ENI
6. OK > Fermer.

> Répétition de l’opération pour SRV-SVC-MD  avec leurs adresses respectives.

### Pour Debian (SRV-LNX-MD) :

1. Connexion en root.
2. Fichier `/etc/network/interfaces` :

```bash
auto ens33
iface ens33 inet static
  address 192.168.55.111
  netmask 255.255.255.0
  gateway 192.168.55.254
  dns-nameservers 192.168.55.254
```

3. Redémarrage du service :

```bash
sudo systemctl restart networking
```

---

## 🛡️ Vérifications

- Depuis chaque serveur, **ping** vers :
    - `192.168.55.254` (pfSense)
    - Les autres serveurs
- Depuis pfSense, utilise **Diagnostics > Ping** vers :
    - `192.168.55.101`, `102`, `111`

> Si un serveur ne répond pas, vérifie :
> - la configuration IP (erreur de syntaxe)
> - que le pare-feu Windows autorise les ICMP (ou le désactiver temporairement)
> - que la carte réseau est bien connectée à VMNet2

---

## 📄 Synthèse

|Serveur|Adresse IP|OS|Rôles techniques|
|---|---|---|---|
|SRV-AD-MD|192.168.55.101|Windows Server|Contrôleur AD, DNS de domaine|
|SRV-SVC-MD|192.168.55.102|Windows Server|DHCP, partage de fichiers, DNS secondaire|
|SRV-LNX-MD|192.168.55.111|Debian sans GUI|DHCP ou DNS selon parité|