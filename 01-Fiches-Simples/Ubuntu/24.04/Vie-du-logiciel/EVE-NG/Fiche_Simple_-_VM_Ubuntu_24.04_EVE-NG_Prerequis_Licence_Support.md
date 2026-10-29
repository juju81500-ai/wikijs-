# Fiche_Simple_-_VM_Ubuntu_24.04_EVE-NG_Prerequis_Licence_Support

- **Environnement** : VM EVE-NG (appliance basée sur Ubuntu Server 24.04 LTS) hébergée sur un poste ou serveur de virtualisation
- **OS / Version** : EVE-NG 7.x (7.2.0-18 au contrôle du 29/10/2026), Ubuntu 24.04 LTS embarqué; Community 6.2.0-4 (Ubuntu 22.04) en fin de support juin 2026
- **Catégorie** : simulation réseau / prérequis
- **Tags** : `ubuntu24.04`, `eve-ng`, `prerequis`, `licence`, `freemium`, `support`

---

## Problème précis à résoudre

Savoir si EVE-NG peut être déployé sur l'hôte disponible, quelle édition choisir et quelles limites de licence s'appliquent, avant toute installation.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la virtualisation matérielle sur l'hôte Linux (commandes en lecture seule) :
   ```bash
   lscpu | grep -iE 'model name|virtualization|^cpu\(s\)'
   egrep -c '(vmx|svm)' /proc/cpuinfo
   free -h
   df -h
   ```
   👉 Explication : un résultat `vmx` (Intel VT-x/EPT) ou `svm` (AMD-V) supérieur à 0 est nécessaire, car les nœuds QEMU d'EVE-NG requièrent la virtualisation imbriquée; la doc officielle donne comme priorités le CPU, un disque local rapide, puis la RAM.

2. Confronter l'hôte à la matrice officielle : ouvrir **Supported Hardware and Software Systems** et **Not Supported Systems or HW** sur eve-ng.net.
   👉 Explication : supportés : VMware Workstation/Player 16+, ESXi 6.7+, Ubuntu Server 24.04 LTS (bare-metal), Google Cloud; non supportés : Hyper-V, VirtualBox, Citrix XenServer, AWS, Mac à puce ARM, disques NAS/SAN/DAS ou externes. Proxmox VE est cité comme supporté sur la page publique mais le cookbook 7.9 ne le liste pas en 2.2 : ⚠️ point à confirmer auprès de l'éditeur avant tout usage.

3. Choisir l'édition : ouvrir **Download** sur eve-ng.net et relever la version courante (BASE/RBL 7.2.0-18 au 29/10/2026) et l'état de l'édition Community.
   👉 Explication : la page affiche l'édition Community 6.2.0-4 « EOS-EOL, juin 2026 » (donc sans support à la date du contrôle) : ne pas démarrer un nouveau déploiement sur Community 6.x; privilégier l'édition courante en mode Freemium (7 nœuds, VPCS illimités, comptes admin uniquement selon les notes de version) ou une licence payante.

4. Dimensionner la VM : ouvrir le **Resource Calculator** (page Download) puis noter vCPU, RAM et disque.
   👉 Explication : minimum cookbook pour un poste : CPU 8 vCPU, 16 Go RAM, 120 Go disque (200 Go conseillés dans l'assistant VMware); recommandé : 16 vCPU, 32 Go, 300 Go. Ces valeurs sont indicatives : le calculateur reste la référence.

5. Vérifier l'absence de conflit réseau avec les sous-réseaux internes d'EVE-NG : `172.29.129.0/24` (NAT), `172.29.130.0/24` (VPN cluster) et `172.17.0.0/16` (consoles Docker).
   ```bash
   ip -4 route show | grep -E '172\.(17|29)\.' || echo 'Aucun conflit visible'
   ```
   👉 Explication : un recoupement avec le LAN existant casserait les consoles ou l'accès Internet des labs.

6. Lire la licence : **Documentation > EULA** et **EVE Licensing Model**.
   👉 Explication : les licences Pro/Learning Centre sont annuelles et comptées par sessions simultanées; le mode Freemium est limité. Vérifier que l'usage visé (formation, entreprise) est couvert. Toute image éditeur (Cisco, Juniper, etc.) doit être obtenue légalement par vos soins : EVE-NG n'en fournit pas.

## 2. Production — Contrôles

- Valider la compatibilité de l'hôte (hyperviseur supporté, disque local, VT-x/EPT) et conserver la référence de page consultée avec la date.
- Prévoir un accès Internet et DNS sortants depuis la VM : requis pour les mises à jour et la validation de licence.
- Prévoir un hôte unique par licence Pro : ne jamais allumer deux EVE avec la même licence en même temps.

## 3. Production — Sécurité

- Ne pas utiliser de licence ni d'image d'origine douteuse : seules des images autorisées par un contrat ou une licence valide sont acceptables.
- Ne pas publier d'identifiants de licence dans un ticket ou un dépôt.
- Placer EVE-NG sur un VLAN de lab isolé du réseau de production.

## Validation et retour arrière

- **Validation** : la matrice hôte est documentée, l'édition est choisie (version et date relevées) et la taille de la VM est arrêtée.
- **Retour arrière** : aucune modification n'a été faite : rien à annuler.

## Si le problème n'est pas résolu

- [EVE-NG — matériel et logiciels supportés](https://www.eve-ng.net/index.php/supported-hardware-and-software-systems/)
- [EVE-NG — systèmes non supportés](https://www.eve-ng.net/index.php/not-supported-systems-or-hw/)
- [EVE-NG — téléchargements et version courante](https://www.eve-ng.net/index.php/download/)
- [EVE-NG — modèle de licence](https://www.eve-ng.net/index.php/documentation/eve-licensing-model/)
- [EVE-NG — EULA](https://www.eve-ng.net/index.php/documentation/eula/)
[EVE-NG — documentation officielle](https://www.eve-ng.net/index.php/documentation/)
- [Fiche logiciel EVE-NG](../../../../Logiciels/15-Topologie-IPAM-et-outils-metiers/Fiche_Logiciel_-_EVE-NG.md)
- [Installer EVE-NG depuis l'ISO officiel](./Fiche_Simple_-_VM_Ubuntu_24.04_EVE-NG_Installer_ISO_VM.md)
