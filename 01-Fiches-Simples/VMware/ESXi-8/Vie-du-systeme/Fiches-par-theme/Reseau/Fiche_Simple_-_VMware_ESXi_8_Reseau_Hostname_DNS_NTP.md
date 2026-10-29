# 📄 Fiche_Simple_-_VMware_ESXi_8_Reseau_Hostname_DNS_NTP.md

- **Environnement** : Hôte physique VMware ESXi 8 (ESXi Shell ou SSH, Host Client, vSphere Client)
- **OS / Version** : VMware ESXi 8.0 - Hyperviseur bare-metal
- **Catégorie** : Virtualisation / Réseau et identité de l'hôte
- **Tags** : `[vmware-esxi-8]`, `[esxcli]`, `[reseau]`, `[dns]`, `[ntp]`, `[hardening]`

---

## 🎯 Problème précis à résoudre
Définir le nom d'hôte complet (FQDN), les serveurs DNS et la synchronisation NTP d'un hôte ESXi 8 avec `esxcli`, puis restreindre le client NTP aux seuls serveurs autorisés.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lire la configuration actuelle de l'hôte :
```bash
esxcli system hostname get
esxcli network ip dns server list
esxcli system ntp get
```
👉 Explication : affiche le nom d'hôte et le domaine, les serveurs DNS configurés et l'état du client NTP avant toute modification.

2. Définir le nom d'hôte et le domaine :
```bash
esxcli system hostname set --host=<nom_de_l_hote> --domain=<domaine_dns>
```
👉 Explication : fixe le nom court et le domaine ; le FQDN `<nom_de_l_hote>.<domaine_dns>` doit correspondre à l'enregistrement DNS direct et inverse.

3. Ajouter le serveur DNS et le domaine de recherche :
```bash
esxcli network ip dns server add --server=<ip_dns_primaire>
esxcli network ip dns search add --domain=<domaine_dns>
```
👉 Explication : déclare le résolveur DNS utilisé par l'hôte et le domaine ajouté automatiquement aux noms courts.

4. Configurer le serveur NTP et démarrer le service :
```bash
esxcli system ntp set --server=<ip_serveur_ntp> --enabled=true
/etc/init.d/ntpd restart
esxcli system ntp get
```
👉 Explication : active le client NTP vers `<ip_serveur_ntp>`, redémarre le service `ntpd` et affiche la configuration appliquée. Un décalage d'horloge fausse les certificats TLS et l'authentification Kerberos.

5. Tester la connectivité depuis le VMkernel de management :
```bash
vmkping -I vmk0 <ip_passerelle>
```
👉 Explication : envoie un ping depuis l'interface `vmk0` (pile réseau VMkernel) vers la passerelle ; la réponse confirme que l'adresse, le masque et la route sont valides.

---

## ⚡ 2. Production — Façon Simplifiée
1. Passer l'adresse de management en IPv4 statique :
```bash
esxcli network ip interface ipv4 set --interface-name=vmk0 --type=static --ipv4=<ip_management> --netmask=<masque_reseau>
```
👉 Explication : remplace l'adresse DHCP par l'adresse fixe définitive de l'hôte ; à exécuter depuis la console DCUI ou une session SSH ouverte hors de `vmk0`, pour éviter une coupure.

2. Déclarer la route par défaut :
```bash
esxcli network ip route ipv4 add --network=default --gateway=<ip_passerelle>
```
👉 Explication : ajoute la passerelle par défaut utilisée par `vmk0` pour joindre DNS, NTP et les équipements distants.

3. Valider la résolution DNS et la liste des serveurs :
```bash
esxcli network ip dns server list
vmkping -I vmk0 <ip_dns_primaire>
```
👉 Explication : confirme que le serveur DNS configuré répond bien depuis le réseau de management.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restreindre le pare-feu du client NTP à la seule source autorisée :
```bash
esxcli network firewall ruleset set --ruleset-id=ntpClient --allowed-all=false
esxcli network firewall ruleset allowedip add --ruleset-id=ntpClient --ip-address=<ip_serveur_ntp>
```
👉 Explication : désactive l'autorisation de toutes les adresses pour la règle `ntpClient` puis n'autorise que `<ip_serveur_ntp>` ; les réponses NTP provenant d'autres sources sont bloquées.

2. Vérifier les règles appliquées :
```bash
esxcli network firewall ruleset list --ruleset-id=ntpClient
esxcli network firewall ruleset allowedip list --ruleset-id=ntpClient
```
👉 Explication : confirme que la règle est active et ne contient que l'adresse du serveur NTP approuvé.

3. Documenter la configuration réseau de l'hôte :
```bash
esxcli network ip interface list
esxcli network ip route ipv4 list
```
👉 Explication : exporte l'état réel des interfaces VMkernel et des routes pour l'inventaire et le dossier d'exploitation (étape CMDB et documentation).
