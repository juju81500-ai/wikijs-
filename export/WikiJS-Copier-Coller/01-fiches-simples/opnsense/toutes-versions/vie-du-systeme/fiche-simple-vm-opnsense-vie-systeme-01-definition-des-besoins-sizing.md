# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_01_Definition_Des_Besoins_Sizing

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 01 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Dimensionner le pare-feu avant de créer la VM ou d'acheter le matériel.

## 1. Hors-Production (Lab / Test / POC)

1. Relever le débit WAN, le nombre de clients, de tunnels VPN et les services activés (IDS, proxy) :
   👉 Explication : le débit avec inspection (Suricata) et le chiffrement VPN dimensionnent le CPU, pas la RAM.

2. Sur un OPNsense existant, relever les ressources utilisées : Lobby > Tableau de bord (widgets Informations système et Trafic) ou, en shell (console option 8 ou SSH) :
   ```sh
   sysctl hw.ncpu hw.physmem
   df -h /
   zpool list 2>/dev/null
   vmstat 1 3
   ```
   👉 Explication : nombre de CPU, RAM, espace disque et charge; `zpool list` n'est utile qu'avec ZFS.

3. Compter les interfaces nécessaires (WAN, LAN, DMZ, HA) et choisir des cartes réseau compatibles FreeBSD (Intel de préférence).
   👉 Explication : une carte non reconnue interdit l'affectation de l'interface à l'installation.

4. Noter vCPU (2 minimum), RAM (4 Go conseillés avec IDS), disque (20 Go conseillés), nombre de ports et débit cible dans le dossier du projet.
   👉 Explication : ce tableau sert de référence pour l'hyperviseur et pour la recette.

## 2. Production — Contrôles

Ajouter 30 % de marge de débit; prévoir un second nœud si le pare-feu est un point unique de défaillance.

## 3. Production — Sécurité

Prévoir des interfaces physiques ou des VLAN distincts pour WAN, LAN et DMZ.

## Validation et retour arrière

- **Validation** : Tableau de sizing (CPU, RAM, disque, interfaces, débit) signé et conservé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)