# Fiche_Simple_-_VM_Multi-OS_Reseau_Diagnostic_DNS.md

- **Environnement** : VM, poste, serveur, LXC Proxmox ou hôte Docker (Linux ou Windows)
- **OS / Version** : Debian 12/13, Ubuntu 24.04/26.04, Rocky Linux 9, Alpine Linux, Windows 10/11, Windows Server 2022/2025
- **Catégorie** : réseau / résolution de noms
- **Tags** : `reseau`, `diagnostic`, `multi-os`, `depannage`

---

## Problème précis à résoudre

Distinguer une panne de routage d'une panne de résolution de noms.

## 1. Hors-Production (Lab / Test / POC)

1. Tester d'abord l'IP connue (exemple à remplacer), puis le nom :
   ```bash
   ping -c 2 192.0.2.10
   ```
   👉 Explication : si l'IP répond mais pas le nom, le problème est le DNS.

2. Debian/Ubuntu (systemd-resolved) — remplacer `srv1.example.test` par le nom testé :
   ```bash
   resolvectl status
   resolvectl query srv1.example.test
   getent ahosts srv1.example.test
   ```
   👉 Explication : montre les serveurs DNS utilisés et le résultat de la résolution par le système.

3. Rocky Linux :
   ```bash
   nmcli device show
   cat /etc/resolv.conf
   getent ahosts srv1.example.test
   ```
   👉 Explication : NetworkManager gère le DNS; on lit la configuration effective.

4. Alpine Linux :
   ```sh
   cat /etc/resolv.conf
   nslookup srv1.example.test
   ```
   👉 Explication : dans un LXC, vérifier d'abord si Proxmox gère `/etc/resolv.conf`.

5. Windows :
   ```powershell
   Get-DnsClientServerAddress
   Resolve-DnsName srv1.example.test
   ```
   👉 Explication : un poste joint à Active Directory doit utiliser les DNS AD internes.

## 2. Production — Contrôles

Utiliser les DNS de l'organisation; ne pas ajouter un DNS public pour un domaine privé.

## 3. Production — Sécurité

- Ne pas contourner le DNS d'entreprise par un résolveur public.
- Ne pas figer `/etc/resolv.conf`.

## Validation et retour arrière

- **Validation** : Le nom est résolu par le serveur DNS attendu.
- **Retour arrière** : Aucune modification ici; ne pas figer `/etc/resolv.conf`.

## Si le problème n'est pas résolu

- [Netplan — documentation](https://netplan.readthedocs.io/)
- [Microsoft — cmdlets NetTCPIP](https://learn.microsoft.com/en-us/powershell/module/nettcpip/)
- [Guide complet — 6. Étape 4 — Vérifier le DNS](../../../../02-Fiches-Completes/Transverses/Multi-OS/Diagnostic/15_Depannage_Reseau_Diagnostic_Complet_Multi_OS.md#6-etape-4-verifier-le-dns)
