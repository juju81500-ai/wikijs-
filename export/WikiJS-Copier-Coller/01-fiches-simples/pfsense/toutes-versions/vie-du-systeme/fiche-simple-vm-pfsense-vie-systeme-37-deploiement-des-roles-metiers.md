# Fiche_Simple_-_VM_pfSense_Vie_Systeme_37_Deploiement_Des_Roles_Metiers

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 37 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Activer les rôles du pare-feu : DHCP, NAT, VPN.

## 1. Hors-Production (Lab / Test / POC)

1. DHCP : Services > DHCP Server > LAN > Enable, plage `IP_DEBUT` à `IP_FIN`, passerelle `IP_LAN`, Save.
   👉 Explication : `IP_DEBUT` et `IP_FIN` délimitent la plage distribuée.

2. NAT : Firewall > NAT > Outbound (mode automatique pour le LAN vers le WAN) et Firewall > NAT > Port Forward pour publier un service.
   👉 Explication : traduit les adresses internes vers l'adresse WAN et publie un service si besoin.

3. VPN : VPN > OpenVPN > Wizards (ou VPN > IPsec), puis Firewall > Rules > WAN pour autoriser UDP 1194.
   👉 Explication : crée un accès distant chiffré.

4. Vérifier en shell :
   ```sh
   pfctl -sn | head
   sockstat -4 -l | grep -E 'dhcpd|kea|openvpn'
   ```
   👉 Explication : affiche les règles NAT et les services DHCP/VPN en écoute.

## 2. Production — Contrôles

Documenter chaque redirection de port et son propriétaire.

## 3. Production — Sécurité

Limiter la publication de services; préférer un VPN à une redirection directe.

## Validation et retour arrière

- **Validation** : Un client reçoit une adresse, sort sur Internet et le VPN se monte.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)