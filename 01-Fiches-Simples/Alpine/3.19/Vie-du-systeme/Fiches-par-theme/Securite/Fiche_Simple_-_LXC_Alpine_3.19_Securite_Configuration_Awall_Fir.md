# Filtrer un conteneur LXC Alpine sur Proxmox

- **Environnement** : Conteneur LXC Alpine Linux sur Proxmox VE
- **Catégorie** : Réseau / Pare-feu
- **Tags** : `alpine`, `lxc`, `proxmox`, `firewall`, `awall`, `reseau`

## 🎯 Objectif et limite LXC

Filtrer les flux entrants d'un conteneur sans casser sa connectivité. Dans un LXC, le pare-feu s'appuie sur le noyau de l'hôte et les capacités accordées au conteneur. Le filtrage Proxmox est généralement le point de contrôle adapté ; ne pas supposer qu'Awall/iptables peut charger des règles dans un conteneur non privilégié.

## 🧪 1. Diagnostic

Dans le conteneur, relever les services et interfaces :

```sh
ip addr
ip route
ss -lntup
```
   👉 Explication : relève adresses, routes et ports en écoute du conteneur avant toute règle.

Depuis l'hôte Proxmox, vérifier l'état du pare-feu au niveau Datacenter, nœud et conteneur, ainsi que l'interface et l'adresse du CT. Ne pas modifier le pare-feu depuis le CT avant d'avoir confirmé les capacités et la politique de l'hôte.

## ⚡ 2. Configurer le filtrage sur Proxmox

Dans l'interface Proxmox, activer le pare-feu aux niveaux requis, puis créer des règles entrantes explicites sur le conteneur :

1. Autoriser SSH uniquement depuis le réseau d'administration réellement utilisé.
2. Autoriser les ports applicatifs strictement nécessaires depuis les réseaux clients attendus.
3. Vérifier les flux DNS, DHCP, supervision et sauvegarde nécessaires au rôle du conteneur.
4. Appliquer une politique entrante restrictive après avoir confirmé les règles et gardé la console Proxmox accessible.

Les règles sont gérées sur l'hôte et doivent être persistantes via la configuration Proxmox. Ne pas copier une règle `iptables` ou `nft add rule` dans le CT : elle peut être interdite, non persistante ou agir sur le mauvais namespace.

## 🔒 3. Vérifier sans se couper

Depuis un second poste, tester SSH depuis le réseau d'administration, puis tester le service applicatif autorisé et confirmer le refus d'un flux non prévu. Dans le CT :

```sh
ss -lntup
ip route
```
   👉 Explication : confirme que SSH et le service restent en écoute et que la route est intacte.

En cas de perte d'accès, utiliser la console Proxmox et corriger ou désactiver la dernière règle au niveau CT. Ne pas activer un profil Awall nommé `ssh`/`http` sans vérifier qu'il existe et qu'il est configuré pour cette installation.

## Cas d'une VM Alpine

Cette fiche concerne LXC. Pour une VM Alpine dédiée, Awall peut convenir si la version installée le prend en charge ; définir d'abord les politiques selon la documentation Alpine locale, valider le ruleset et garder un accès console. Ne pas appliquer ces étapes LXC à une VM.