---
title: "Diagnostiquer un LXC Alpine : réseau et services OpenRC"
description: "Fiche simple : [préparer l'intervention](../../../../01-Fiches-Simples/Alpine/Toutes-versions/Vie-du-systeme/Fiches-par-theme/Diagnostic/FicheSimple-LXCAlpineDiagnosticPreparerIntervention.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["alpine", "proxmox", "lxc", "diagnostic", "openrc", "reseau"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Diagnostiquer un LXC Alpine : réseau et services OpenRC

- **Type de fiche** : Diagnostic
- **Environnement** : LXC Alpine sur Proxmox VE
- **OS / Version** : Branche Alpine maintenue; noter la version réelle avant intervention
- **Rôle** : Isoler les pannes de lien, IP, route, DNS, pare-feu et service
- **Tags** : `alpine`, `proxmox`, `lxc`, `diagnostic`, `openrc`, `reseau`

## 1. Objectif et précautions

Fiche simple : [préparer l'intervention](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/diagnostic/fiche-simple-lxc-alpine-diagnostic-preparer-intervention).

Suivre la chaîne **hôte/bridge → interface → IP → passerelle → route → DNS → port → service**. Un LXC partage le noyau de l'hôte et peut recevoir sa configuration réseau de Proxmox; ne pas appliquer à l'intérieur du CT une réparation conçue pour une VM.

Avant tout changement, noter l'heure, l'IP, l'interface, le bridge/VLAN, la destination et le port. Garder la console Proxmox ouverte. Ne pas vider les règles firewall ni redémarrer tout le nœud.

## 2. Relever l'état Proxmox et Alpine

Fiche simple : [relever l'état Proxmox et Alpine](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/diagnostic/fiche-simple-lxc-alpine-diagnostic-relever-etat).

Sur l'hôte Proxmox :

```bash
pct config <CTID>
pct status <CTID>
```

Dans le conteneur :

```sh
cat /etc/alpine-release
ip -br link
ip -br addr
ip route
cat /etc/resolv.conf
rc-status
```

Comparer le bridge, le VLAN tag, l'adresse, la passerelle et le DNS du CT avec le plan réseau et une machine fonctionnelle du même segment.

## 3. Isoler la couche en panne

Fiche simple : [isoler la couche en panne](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/diagnostic/fiche-simple-lxc-alpine-diagnostic-isoler-couche).

1. **Lien/bridge/VLAN** : vérifier que l'interface est `UP`, le CT démarré, le bridge existe et le VLAN est permis sur le switch.
2. **IP et route** : confirmer que l'adresse/prefixe attendus apparaissent et qu'une route existe vers la destination.
3. **Passerelle** : tester ICMP si autorisé; un ping bloqué ne prouve pas une panne.
4. **DNS** : tester l'IP de destination puis `nslookup <nom>`; lire le résolveur fourni à `/etc/resolv.conf`.
5. **Port/service** : confirmer que le service écoute et tester uniquement le port requis depuis un client autorisé.

Exemples dans Alpine :

```sh
ping -c 3 <IP_PASSERELLE>
nslookup <NOM_CIBLE>
ss -lntup
rc-service <service> status
```

Si `ss` ou `nslookup` n'est pas installé, relever le résultat avec les outils BusyBox disponibles ou installer le paquet nécessaire lors d'une maintenance approuvée.

## 4. Réparer selon le propriétaire de la configuration

Fiche simple : [corriger selon le propriétaire](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/diagnostic/fiche-simple-lxc-alpine-diagnostic-corriger-proprietaire).

- **Adresse/DNS gérés par Proxmox** : corriger l'interface CT sur l'hôte puis réappliquer selon la procédure du cluster; ne pas éditer un fichier que Proxmox régénère.
- **Profil géré dans Alpine VM** : vérifier le gestionnaire actif et utiliser OpenRC/configuration Alpine appropriés; ne pas appliquer les commandes de VM à un LXC.
- **Service arrêté** : examiner `rc-service <service> status`, corriger sa configuration et relancer ce service seulement.
- **Firewall** : identifier la règle effective au niveau Proxmox, routeur ou hôte; tester une règle minimale et réversible.

## 5. Validation

Fiche simple : [valider la correction](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/diagnostic/fiche-simple-lxc-alpine-diagnostic-valider).

Après une correction, vérifier IP, route, DNS, port et fonction applicative dans cet ordre. Tester depuis un second terminal et depuis une source non autorisée pour confirmer le filtrage.

## 6. Retour arrière

Fiche simple : [préparer le retour arrière](/01-fiches-simples/alpine/toutes-versions/vie-du-systeme/fiches-par-theme/diagnostic/fiche-simple-lxc-alpine-diagnostic-retour-arriere).

Restaurer la configuration précédente dans Proxmox ou Alpine depuis la console. Si l'accès est toujours perdu, arrêter les écritures, conserver le CT et ses journaux, puis restaurer une sauvegarde dans un ID/réseau isolé avant toute bascule.

## Sources

- [Proxmox VE — Documentation](https://pve.proxmox.com/pve-docs/)
- [Alpine Linux — Documentation réseau](https://docs.alpinelinux.org/)