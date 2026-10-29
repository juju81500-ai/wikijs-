# Fiche_Simple_-_VM_Debian_13_Vault_Architecture.md

- **Environnement** : Cluster Vault trois nœuds Raft sur Debian 13
- **OS / Version** : Debian 13 Trixie x86-64; Vault Community ou Enterprise selon canal validé
- **Catégorie** : coffre de secrets / architecture
- **Tags** : `debian13`, `vault`, `raft`, `architecture`

---

## Problème précis à résoudre

Décider de l'édition, du nombre de nœuds et des règles d'exploitation avant d'installer Vault.

## 1. Hors-Production (Lab / Test / POC)

1. Relever le système et les ressources de chaque futur nœud :
   ```bash
   cat /etc/os-release | head -3
   nproc && free -h && df -h /opt
   ```
   👉 Explication : on vérifie Debian 13 et la capacité disponible; trois nœuds dans des domaines de panne distincts sont visés pour la production.

2. Vérifier la résolution DNS et l'heure (exemple de nom à remplacer par le vôtre) :
   ```bash
   getent hosts vault1.example.invalid
   timedatectl status | grep -E 'synchronized|NTP'
   ```
   👉 Explication : chaque nœud doit avoir un nom DNS stable et une heure synchronisée, nécessaires aux certificats TLS et au quorum Raft.

3. Rédiger sur papier ou dans le dossier de projet : édition Community ou Enterprise, propriétaires, méthodes d'authentification, engines, politiques, TTL, audit et plan de reprise.
   👉 Explication : ces décisions doivent exister avant le premier secret; une instance unique n'est qu'un lab, pas un service HA.

## 2. Production — Contrôles

Valider licence, trois nœuds Raft, DNS, NTP, certificats TLS par nœud, supervision, sauvegarde des snapshots et propriétaires.

## 3. Production — Sécurité

- Ne stocker aucun secret réel pendant la phase de lab.
- Prévoir dès maintenant l'audit et la séparation des détenteurs de clés.

## Validation et retour arrière

- **Validation** : architecture écrite et validée, prérequis DNS/NTP/ressources confirmés.
- **Retour arrière** : aucun changement système à annuler; reprendre la décision documentée.

## Si le problème n'est pas résolu

- [HashiCorp — Installer Vault](https://developer.hashicorp.com/vault/install)
- [HashiCorp — Déployer Vault avec Integrated Storage/Raft](https://developer.hashicorp.com/vault/tutorials/day-one-raft/raft-deployment-guide)
- [HashiCorp — Durcissement production](https://developer.hashicorp.com/vault/docs/concepts/production-hardening)
- [Guide complet — étape 1](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/61_Deploiement_Hashicorp_Vault_Raft_Debian_13.md#1-choisir-larchitecture)
