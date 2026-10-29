# Fiche_Simple_-_DMZ_Valider_Flux_Zone_Lab.md

- **Environnement** : Pare-feu virtuel et VMs de test sur réseaux isolés; aucun raccord à un réseau tiers ou de production
- **OS / Version** : Pare-feu de lab, version consignée dans le compte rendu
- **Catégorie** : Réseau / segmentation / validation

## Problème précis à résoudre

Vérifier qu'une DMZ de laboratoire n'autorise que les flux nécessaires entre WAN simulé, DMZ, LAN de test et administration.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier interfaces et sous-réseaux : **Interfaces > Assignments**, puis **Diagnostics > Command Prompt** :
   ```sh
   ifconfig -a | grep -E '^[a-z]|inet '
   netstat -rn
   ```
   👉 Explication : le lab est isolé; aucune plage ne chevauche le poste, le VPN ou le LAN.

2. Préparer la matrice des flux (tableau ci-dessous) : origine, destination, protocole/port, propriétaire.
   👉 Explication : chaque test cible un résultat attendu précis.

3. Tester le service publié depuis le WAN simulé :
   ```bash
   nc -zv IP_DMZ PORT_PUBLIE
   curl -fsSI http://IP_DMZ:PORT_PUBLIE/
   ```
   👉 Explication : remplacer IP et port; seul le port prévu doit répondre.

4. Vérifier les refus WAN→LAN/administration et DMZ→LAN depuis les machines concernées :
   ```bash
   nc -zv -w 3 IP_LAN 22
   nc -zv -w 3 IP_LAN 445
   ```
   👉 Explication : le résultat attendu est un échec (timeout ou refus), hors exceptions documentées.

5. Tester les flux sortants minimaux depuis la DMZ, puis chaque exception :
   ```bash
   nc -zv -w 3 IP_DEPENDANCE PORT
   curl -fsSI --max-time 5 https://example.net/
   ```
   👉 Explication : seules les dépendances nécessaires doivent passer; le reste est bloqué par défaut.

6. Répéter en IPv6 et contrôler les journaux : **Status > System Logs > Firewall**, **Diagnostics > States** et **Firewall > Rules** (compteurs).
   ```bash
   nc -6zv -w 3 ADRESSE_IPV6 PORT
   ```
   👉 Explication : les compteurs de règles confirment le chemin réellement suivi.

7. Sauvegarder avant toute modification : **Diagnostics > Backup & Restore > Download configuration as XML** (cocher le chiffrement), puis tester la restauration sur le lab.
   👉 Explication : le retour arrière doit être prouvé avant la production.

| Origine | Destination | Résultat attendu |
|---|---|---|
| WAN simulé | Service public en DMZ | Autorisé uniquement sur les ports documentés |
| WAN simulé | LAN et administration | Bloqué |
| DMZ | LAN | Bloqué, sauf exception précise approuvée |
| DMZ | Internet | Bloqué par défaut; seules les dépendances nécessaires passent |
| Réseau d'administration | Équipement/service DMZ | Autorisé seulement depuis les sources de gestion approuvées |

## 2. Production — Contrôles

Ne pas appliquer directement une configuration de lab. Faire valider la matrice de flux, le propriétaire de chaque exception, les règles implicites, le routage IPv4/IPv6, la journalisation, les sauvegardes et le plan de retour arrière par les responsables réseau et applicatifs.

## 3. Production — Sécurité

- Refus interzone par défaut et exceptions limitées à une source, une destination et un service nécessaires.
- Administration séparée des flux utilisateurs et jamais exposée directement à Internet.
- Aucun serveur DMZ à double interface permettant un pont ou routage non prévu vers le LAN.
- Journaliser les refus et autorisations sensibles sans collecter plus de données que nécessaire.
- Revoir et supprimer les règles temporaires à leur échéance.

## Validation et retour arrière

- **Validation** : les flux métier autorisés passent; les chemins interdits échouent; règles et journaux correspondent aux tests; résultat confirmé en IPv4 et IPv6.
- **Retour arrière** : conserver une sauvegarde restaurable et un accès console/hors bande; arrêter la mise en service si l'administration ou les flux essentiels sont perturbés.

## Si le problème n'est pas résolu

- [Guide complet de conception et validation DMZ](/02-fiches-completes/transverses/multi-os/autres/86-conception-dmz-segmentation-flux-multi-os)
- [Référence pédagogique TSSR sur les DMZ](https://github.com/kipit/nivvlem-TSSR/blob/main/fiches-r%C3%A9f%C3%A9rences/dmz.md)
- [NIST — Firewalls and Firewall Policy](https://csrc.nist.gov/pubs/sp/800/41/r1/final)
- [OPNsense — règles de pare-feu](https://docs.opnsense.org/manual/firewall.html)