# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_23_Outils_D_Administration_Fondamentaux

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 23 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-23`

---

## Problème précis à résoudre

Disposer des outils de diagnostic usuels (BusyBox est limité).

## 1. Hors-Production (Lab / Test / POC)

1. Installer les outils courants :
   ```sh
   doas apk add curl vim htop bind-tools tcpdump lsof iproute2 util-linux
   ```
   👉 Explication : ajoute le client HTTP, l'éditeur, le moniteur, DNS, capture, fichiers ouverts, `ip` complet et les outils système (`lsblk`, `dmesg`).

2. Installer l'aide en ligne :
   ```sh
   doas apk add mandoc man-pages docs
   man apk
   ```
   👉 Explication : fournit les pages de manuel; sans elles `man` est absent.

3. Contrôler les versions :
   ```sh
   curl --version | head -1
   vim --version | head -1
   ```
   👉 Explication : confirme que les outils répondent.

## 2. Production — Contrôles

Limiter la liste aux outils utiles et la tenir à jour dans le runbook.

## 3. Production — Sécurité

Supprimer les outils de capture (`tcpdump`) si la politique l'interdit.

## Validation et retour arrière

- **Validation** : Les commandes s'exécutent sans erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Alpine Linux 3.19](./Sommaire_-_Vie_du_systeme_Alpine_3.19.md)
- [Documentation officielle](https://docs.alpinelinux.org/)
