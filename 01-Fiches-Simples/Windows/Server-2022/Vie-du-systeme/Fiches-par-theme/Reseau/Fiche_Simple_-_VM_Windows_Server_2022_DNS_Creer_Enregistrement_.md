# 📄 VM_WinSrv_2022_DNS_Creer-Enregistrement-A-Et-CNAME.md

- **Environnement** : VM / Serveur DNS Windows
- **OS / Version** : Windows Server 2022 Standard / Datacenter
- **Catégorie** : Services Réseau / DNS
- **Tags** : `[winsrv2022]`, `[dns]`, `[enregistrement-a]`, `[cname]`, `[gui]`, `[powershell]`, `[hardening]`

---

## 🎯 Problème précis à résoudre
Créer un enregistrement DNS hôte (A) pour associer un nom à une adresse IP, et créer un alias (CNAME) dans une zone DNS principale (`lab.local`).

---

## 🖥️ Méthode Interface Graphique (GUI Pas-à-Pas - "Clic-Clic")

1. **Ouvrir la console DNS** :
   - Appuyer sur `Win + R`.
   - Saisir `dnsmgmt.msc` puis appuyer sur `Entrée`.
   - Dérouler le serveur ➔ **Zones de recherche directe** ➔ Cliquer sur la zone (ex: `lab.local`).
   - 👉 *Explication : Ouvre la console de gestion des enregistrements DNS du domaine.*

2. **Créer un enregistrement A (Hôte)** :
   - Faire un **clic droit** dans l'espace vide de la zone ➔ **Nouvel hôte (A ou AAAA)...**.
   - *Nom* : `srv-web`
   - *Adresse IP* : `192.168.1.80`
   - Cocher la case **Créer un enregistrement de pointeur (PTR) associé** (si la zone inversée existe).
   - Cliquer sur **Ajouter un hôte**.
   - 👉 *Explication : Associe le nom `srv-web.lab.local` à l'IP `192.168.1.80`.*

3. **Créer un enregistrement CNAME (Alias)** :
   - Faire un **clic droit** dans la zone ➔ **Nouvel alias (CNAME)...**.
   - *Nom de l'alias* : `wiki`
   - *Nom de domaine pleinement qualifié (FQDN) pour l'hôte cible* : cliquer sur **Parcourir...** et cibler `srv-web.lab.local` (ou saisir directement `srv-web.lab.local.`)
   - Cliquer sur **OK**.
   - 👉 *Explication : Permet de joindre le serveur via l'adresse conviviale `wiki.lab.local`.*

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. **Ajout d'un enregistrement A et CNAME en PowerShell** :
   ```powershell
   Add-DnsServerResourceRecordA -Name "srv-web" -ZoneName "lab.local" -IPv4Address "192.168.1.80"
   Add-DnsServerResourceRecordCName -Name "wiki" -ZoneName "lab.local" -HostNameAlias "srv-web.lab.local"
   ```
   👉 *Explication : Tu fais ça, l'hôte et l'alias sont immédiatement enregistrés dans le serveur DNS.*