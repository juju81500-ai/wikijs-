# Fiche_Simple_-_VM_Debian_13_tcpdump_Prerequis_Limites

- **Environnement** : VM Debian 13 dédiée à tcpdump
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : tcpdump / prérequis et limites

---

## Problème précis à résoudre

Cadrer une capture réseau limitée à un périmètre autorisé et à une durée définie.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer OS et paquet candidat :
   ```bash
   cat /etc/os-release
   apt-cache policy tcpdump
   ```
   👉 Explication : La version disponible dépend des dépôts Debian activés.

2. Identifier interfaces et adresses :
   ```bash
   ip -br address
   ip -br link
   ```
   👉 Explication : Sélectionner uniquement l’interface autorisée, distincte de l’administration si possible.

3. Obtenir autorisation écrite, filtre, durée, rétention et stockage.
   👉 Explication : Les captures peuvent contenir identifiants, métadonnées ou contenu privé; ne jamais capturer un tiers sans autorisation.

## 2. Production — Contrôles

Fixer durée et volume maximum; préférer filtre ciblé et capture tronquée si suffisante.

## 3. Production — Sécurité

- Ne pas utiliser tcpdump comme surveillance persistante non approuvée; limiter les droits de lecture des pcap.

## Validation et retour arrière

- **Validation** : Interface, filtre, durée et stockage approuvés avant capture.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [tcpdump — documentation officielle](https://www.tcpdump.org/manpages/tcpdump.1.html)
- [Étape suivante du guide](/01-fiches-simples/debian/13/vie-du-logiciel/tcpdump/fiche-simple-vm-debian-13-tcpdump-installer)