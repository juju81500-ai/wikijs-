# Fiche_Simple_-_pfSense_CE_2.9.0_Valider_Flux_Lab.md

- **Environnement** : pfSense CE 2.9.0 en VM Proxmox VE, réseaux WAN/LAN de laboratoire
- **OS / Version** : pfSense CE 2.9.0
- **Catégorie** : Pare-feu / validation de configuration

---

## Problème précis à résoudre

Valider la séparation WAN/LAN et prouver qu'un backup de configuration chiffré peut être restauré sans raccorder la VM de test à la production.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer WAN et LAN sur deux bridges Proxmox distincts, isolés de la production : sur le nœud Proxmox :
   ```bash
   qm config VMID | grep net
   ip -br link show type bridge
   ```
   👉 Explication : remplacer `VMID`; chaque `netX` doit pointer vers un bridge de lab différent.

2. Vérifier l'assignation `vtnet0` WAN / `vtnet1` LAN et l'absence de chevauchement : **Interfaces > Assignments**, puis **Interfaces > WAN** et **Interfaces > LAN**.
   👉 Explication : les sous-réseaux WAN et LAN doivent être distincts.

3. Changer les identifiants initiaux : **System > User Manager > admin > Edit** (nouveau mot de passe fort). Limiter le GUI au LAN : **System > Advanced > Admin Access** et **Firewall > Rules > WAN** (aucune règle autorisant 443/22).
   👉 Explication : le mot de passe par défaut `pfsense` doit être remplacé dès la première connexion.

4. Tester un flux LAN autorisé, un flux non autorisé et l'accès entrant GUI/SSH depuis WAN :
   ```bash
   curl -fsSI --max-time 5 https://example.net/
   nc -zv -w 3 IP_WAN_PFSENSE 443
   nc -zv -w 3 IP_WAN_PFSENSE 22
   ```
   👉 Explication : le premier passe depuis le LAN; les deux autres, depuis le WAN, doivent échouer. Vérifier **Status > System Logs > Firewall** et les règles correspondantes.

5. Exporter la configuration chiffrée : **Diagnostics > Backup & Restore > Backup Configuration** (cocher **Encrypt this configuration file**, saisir la phrase de passe) > **Download configuration as XML**.
   👉 Explication : ranger fichier et phrase de passe séparément.

6. Restaurer dans un clone déconnecté du WAN et de la production : **Diagnostics > Backup & Restore > Restore Configuration**, choisir le fichier, saisir la phrase de passe, **Restore Configuration**.
   👉 Explication : vérifier ensuite interfaces, règles et accès GUI.

## 2. Production — Contrôles

Avant toute mise en service réelle, faire revoir le plan d'adressage, le routage, les règles, les sauvegardes, l'accès console hors bande et le plan de retour arrière. Le simple fonctionnement du lab ne valide ni le débit, ni la haute disponibilité, ni une politique de production.

## 3. Production — Sécurité

- Aucune interface d'administration sur WAN; accès GUI limité au réseau de gestion.
- Refus par défaut et règles d'autorisation minimales documentées; pas de règle WAN générale.
- Images issues du portail Netgate avec SHA-256 vérifié; backups de configuration chiffrés et conservés hors hôte.
- Ne pas restaurer une configuration partielle entre révisions différentes.

## Validation et retour arrière

- **Validation** : flux autorisés et bloqués conformes, logs cohérents, restauration de clone réussie.
- **Retour arrière** : conserver le backup précédant tout changement; isoler le clone restauré jusqu'à vérification complète.

## Si le problème n'est pas résolu

- [Netgate — notes pfSense CE 2.9.0](https://docs.netgate.com/pfsense/en/latest/releases/2-9-0.html)
- [Netgate — virtualiser sur Proxmox VE](https://docs.netgate.com/pfsense/en/latest/recipes/virtualize-proxmox-ve.html)
- [Netgate — restaurer une configuration](https://docs.netgate.com/pfsense/en/latest/backup/restore.html)
- [Guide complet pfSense CE sur Proxmox VE](/02-fiches-completes/pfsense/toutes-versions/installation-deploiement/70-deploiement-pfsense-ce-2-9-0-proxmox-lab)