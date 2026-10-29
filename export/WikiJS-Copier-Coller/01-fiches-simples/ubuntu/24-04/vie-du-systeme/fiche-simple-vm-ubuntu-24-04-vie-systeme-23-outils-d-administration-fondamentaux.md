# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_23_Outils_D_Administration_Fondamentaux

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 23 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Installer la boîte à outils.

## 1. Hors-Production (Lab / Test / POC)

1. Installer :
   ```bash
   sudo apt install -y vim curl wget htop tmux git lsof tcpdump dnsutils net-tools
   ```
   👉 Explication : outils d'édition, réseau et diagnostic de base.

## 2. Production — Contrôles

Limiter à la liste approuvée.

## 3. Production — Sécurité

Retirer `tcpdump` des serveurs exposés si la politique l'impose.

## Validation et retour arrière

- **Validation** : `dig -v` et `htop --version` répondent.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 24.04](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-24-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)