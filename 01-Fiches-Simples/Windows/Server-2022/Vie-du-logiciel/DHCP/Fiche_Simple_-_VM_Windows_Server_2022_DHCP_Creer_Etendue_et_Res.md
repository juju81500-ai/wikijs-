# 📄 VM_WinSrv_2022_DHCP_Creer-Etendue-Et-Reservation-IP.md

- **Environnement** : VM / Serveur DHCP Windows
- **OS / Version** : Windows Server 2022 Standard / Datacenter
- **Catégorie** : Services Réseau / DHCP
- **Tags** : `[winsrv2022]`, `[dhcp]`, `[etendue]`, `[reservation-ip]`, `[gui]`, `[powershell]`, `[hardening]`

---

## 🎯 Problème précis à résoudre
Créer une étendue DHCP IPv4 (plage d'adresses dynamiques, masque, passerelle, DNS) et attribuer une réservation d'adresse IP fixe basée sur la carte adresse MAC d'un équipement.

---

## 🖥️ Méthode Interface Graphique (GUI pas-à-pas)

### Prérequis
- Le serveur DHCP a une adresse IP statique et le rôle DHCP est installé.
- En environnement AD, le serveur DHCP doit être autorisé dans Active Directory avant de distribuer des baux.
- Valider le sous-réseau, la plage dynamique, les exclusions, la passerelle, les DNS, le suffixe DNS et les adresses réservées avec le responsable réseau.

1. **Ouvrir la console et contrôler l'autorisation** :
   - Appuyer sur `Win + R`, saisir `dhcpmgmt.msc` et appuyer sur `Entrée`.
   - Dérouler le serveur DHCP. En domaine, clic droit sur son nom > **Autoriser** si l'action est disponible, puis actualiser et vérifier son état avant de continuer.
   - Clic droit sur **IPv4** > **Nouvelle étendue...**.
   - 👉 *Explication : Les serveurs DHCP non autorisés dans AD ne doivent pas fournir d'adresses sur le réseau du domaine.*

2. **Créer une étendue cohérente avec le plan IP** :
   - Dans l'assistant, donner le nom `Etendue_LAN_TSSR`.
   - Pour l'exemple `192.168.1.0/24`, saisir `192.168.1.100` à `192.168.1.200`, masque `255.255.255.0`.
   - Ajouter l'exclusion `192.168.1.100` à `192.168.1.110` seulement si ces adresses sont configurées statiquement ; elles ne seront alors pas attribuées par DHCP.
   - Choisir une durée de bail conforme au réseau. Dans les options, renseigner la passerelle (`192.168.1.1`), le DNS interne (`192.168.1.10`) et le suffixe DNS si nécessaire.
   - Activer l'étendue uniquement après validation des options ; sinon choisir de l'activer plus tard.
   - 👉 *Explication : Les options sont propres au sous-réseau. Les clients d'un domaine AD doivent utiliser les DNS capables de résoudre la zone AD.*

3. **Créer une réservation dans l'étendue** :
   - Dérouler l'étendue > **Réservations** > clic droit > **Nouvelle réservation...**.
   - Saisir `Imprimante_RH`, `192.168.1.150` (adresse située dans l'étendue et hors exclusions), et la MAC réelle de l'interface réseau.
   - Choisir **DHCP** comme type pris en charge, cliquer sur **Ajouter**, puis **Fermer**.
   - 👉 *Explication : La réservation est liée à l'identifiant client/MAC. L'équipement doit être configuré pour obtenir son adresse via DHCP.*

4. **Vérifier le bail** :
   - Dans l'étendue, ouvrir **Baux d'adresses** et confirmer qu'un client de test reçoit une adresse dans la plage attendue.
   - Vérifier la réservation dans **Réservations** et, lorsque le client de test renouvelle son bail, confirmer que l'adresse prévue lui est attribuée.
   - Tester sur un client de laboratoire ou pendant une fenêtre approuvée ; ne pas renouveler le bail d'un serveur de production sans autorisation.
   - 👉 *Explication : La présence d'une étendue activée ne valide pas à elle seule le relais DHCP, le VLAN ni les options reçues par le client.*

Référence : [Microsoft Learn — Installer et configurer DHCP Server](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/quickstart-install-configure-dhcp-server).

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. **Création d'une étendue DHCP de test en PowerShell** :
   ```powershell
   Add-DhcpServerv4Scope -Name "TestScope" -StartRange 192.168.1.100 -EndRange 192.168.1.200 -SubnetMask 255.255.255.0 -State Active
   ```
   👉 *Explication : Tu fais ça, l'étendue DHCP est créée et active immédiatement.*

---

## ⚡ 2. Production — Façon Simplifiée
1. **Création d'une réservation IP statique par adresse MAC** :
   ```powershell
   Add-DhcpServerv4Reservation -ScopeId 192.168.1.0 -IPAddress 192.168.1.50 -ClientId "00-11-22-33-44-55" -Name "Srv-Print" -Description "Reservation Imprimante RH"
   ```
   👉 *Explication : Tu associes l'adresse IP 192.168.1.50 à la carte réseau physique MAC correspondante.*