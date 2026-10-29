# Fiche_Simple_-_LXC_Alpine_Proxmox_Securiser_Exposition.md

- **Environnement** : LXC Alpine sur Proxmox avec filtrage défini par l'architecture
- **OS / Version** : branche Alpine maintenue; noyau partagé avec l'hôte Proxmox
- **Catégorie** : virtualisation / réseau et sécurité

---

## Problème précis à résoudre

Exposer uniquement les services indispensables et appliquer les contrôles au niveau qui possède effectivement les capacités réseau requises.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les ports à l'écoute dans le CT :
   ```sh
   apk add iproute2
   ss -lntup
   ```
   👉 Explication : ne laisser que les ports du service.

2. Désactiver les services inutiles :
   ```sh
   rc-status
   rc-update del SERVICE default
   rc-service SERVICE stop
   ```
   👉 Explication : remplacer `SERVICE`; un LXC non privilégié ne peut pas charger ses propres règles noyau.

3. Filtrer côté Proxmox : **Datacenter > Firewall** ou **CT > Firewall > Add** (Direction `in`, Action `ACCEPT`, Source = réseau autorisé, Dest. port = port du service), puis **CT > Firewall > Options** : **Firewall = yes**.
   👉 Explication : une politique d'entrée `DROP` par défaut, puis des règles minimales par source et port.

4. Vérifier les capacités et la configuration du CT :
   ```bash
   pct config CTID
   ```
   👉 Explication : contrôler `unprivileged: 1`, `features`; documenter l'adresse et le rôle dans DNS, supervision, inventaire.

## 2. Production — Contrôles

Valider les règles, leur persistance, les sources et destinations, les capacités LXC, l'identité DNS, l'inventaire et la supervision.

## 3. Production — Sécurité

- N'ouvrir que les ports et sources strictement nécessaires.
- Ne pas exposer une interface d'administration sur un réseau utilisateur ou Internet.
- Ne pas modifier le filtrage de l'hôte sans fenêtre et accès de secours validés.
- Ne pas publier des secrets dans l'inventaire ou la documentation.

## Validation et retour arrière

- **Validation** : test positif depuis le réseau autorisé, test négatif depuis une source non autorisée et règles documentées.
- **Retour arrière** : retirer uniquement les règles ajoutées au CT/bridge concerné et confirmer que l'administration reste accessible.

## Si le problème n'est pas résolu

- [Proxmox VE — documentation](https://pve.proxmox.com/pve-docs/)
- [Alpine Linux — documentation](https://docs.alpinelinux.org/)
- [Guide complet LXC Alpine sur Proxmox](/02-fiches-completes/alpine/toutes-versions/installation-deploiement/16-installation-lxc-alpine-proxmox#5-securiser-et-exposer-le-service)