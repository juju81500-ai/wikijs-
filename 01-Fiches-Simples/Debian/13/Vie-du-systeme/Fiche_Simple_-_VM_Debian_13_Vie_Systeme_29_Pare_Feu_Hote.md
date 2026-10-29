# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_29_Pare_Feu_Hote

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 29 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian13`, `vie-du-systeme`, `cycle-de-vie`, `etape-29`

---

## Problème précis à résoudre

Filtrer les flux entrants.

## 1. Hors-Production (Lab / Test / POC)

1. Installer et charger une politique nftables minimale :
   ```bash
   sudo apt install nftables
   sudoedit /etc/nftables.conf
   sudo nft -c -f /etc/nftables.conf
   ```
   👉 Explication : `-c` vérifie la syntaxe sans appliquer.

2. Appliquer puis activer au démarrage :
   ```bash
   sudo nft -f /etc/nftables.conf
   sudo systemctl enable --now nftables
   sudo nft list ruleset
   ```
   👉 Explication : politique `drop` en entrée avec SSH autorisé depuis le réseau d'administration.

## 2. Production — Contrôles

Journaliser les refus et conserver la console ouverte pendant l'application.

## 3. Production — Sécurité

Ne jamais appliquer une politique `drop` sans règle SSH testée.

## Validation et retour arrière

- **Validation** : `nft list ruleset` correspond au plan.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Debian 13](./Sommaire_-_Vie_du_systeme_Debian_13.md)
- [Documentation officielle](https://www.debian.org/doc/)
