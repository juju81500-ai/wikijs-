---
title: "Leçon — Hyperviseurs, machines virtuelles et ressources : comprendre la virtualisation"
description: "À la fin de cette leçon, tu sauras :"
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "lecon", "virtualisation", "hyperviseur", "vm", "kvm", "overcommit"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Leçon — Hyperviseurs, machines virtuelles et ressources : comprendre la virtualisation

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `virtualisation`, `hyperviseur`, `vm`, `kvm`, `overcommit`
- **Niveau** : débutant à intermédiaire (technicien TSSR, administrateur systèmes en formation)
- **Durée estimée** : 3 h 30 (lecture 1 h 30, laboratoire 1 h, exercices et quiz 1 h)

---

## Objectifs pédagogiques

À la fin de cette leçon, tu sauras :

1. expliquer pourquoi la virtualisation a remplacé « un serveur physique par application » ;
2. distinguer hyperviseurs de type 1 et de type 2, avec leurs nuances (KVM, Hyper-V) ;
3. décrire une VM : configuration, disque virtuel, mémoire, vCPU, carte réseau ;
4. dimensionner une VM sans la sur-doter ni la sous-doter ;
5. expliquer l'overcommit CPU et mémoire, et en mesurer les effets ;
6. vérifier la virtualisation matérielle d'un hôte Linux ;
7. justifier les pilotes invités (virtio, outils de l'invité) ;
8. monter une VM jetable et l'observer de l'intérieur comme de l'extérieur.

## Prérequis et durée

- Notions sur processeur, mémoire, disque, carte réseau ; aisance minimale en ligne de commande Linux.
- Aucune production : le laboratoire se fait sur un poste personnel ou une VM jetable (Debian 12, processeur Intel ou AMD récent, 8 Go de RAM) ou sur un hôte Proxmox VE jetable.
- Adresses de documentation uniquement (192.0.2.0/24, 198.51.100.0/24).
- Durée : environ 3 h (lecture 1 h 15, laboratoire 1 h, exercices et quiz 45 min).

## L'essentiel en bref

- Virtualiser, c'est faire croire à un système qu'il possède sa propre machine, alors qu'il partage le matériel d'un **hôte**.
- L'**hyperviseur** découpe le matériel et arbitre entre les **VM** (« invités »). **Type 1** : au plus près du matériel (serveurs). **Type 2** : application dans un OS classique (postes).
- Une VM est surtout **une configuration, des disques virtuels, de la mémoire et des vCPU prêtés**.
- La **virtualisation matérielle** (VT-x, AMD-V, EPT/NPT) rend le tout rapide.
- L'**overcommit** est acceptable pour le CPU, dangereux pour la mémoire.
- Les **pilotes invités** remplacent des périphériques émulés lents et apportent arrêt propre et sauvegardes cohérentes.

## 1. Pourquoi virtualiser : l'idée de départ

Imagine un immeuble. Autrefois, chaque service (messagerie, annuaire, base de données) vivait dans sa propre maison : un serveur par application, souvent occupé à 5 ou 10 %, mais à alimenter, climatiser et maintenir. Virtualiser, c'est construire un immeuble : un seul bâtiment (l'hôte), des logements isolés (les VM), un syndic qui répartit eau et électricité (l'hyperviseur).

Bénéfices : **consolidation** (moins de machines, d'énergie, de place), **isolation** (un plantage reste dans sa VM), **souplesse** (créer, cloner, redimensionner en minutes), **portabilité** (une VM est un ensemble de fichiers), **reprise après sinistre** plus simple.

Contreparties : l'hôte devient un **point de concentration des risques** (d'où les clusters), les VM **prolifèrent** si on ne les inventorie pas, une VM bruyante peut gêner ses voisines, et l'on ajoute une couche à superviser et à patcher.

## 2. Vocabulaire indispensable

L'**hôte** fournit les ressources ; l'**invité** est le système qui tourne dans la VM ; l'**hyperviseur** (VMM) crée et arbitre les VM ; un **vCPU** est un processeur virtuel, vu par l'hôte comme un fil d'exécution à placer sur un cœur ; l'**overcommit** alloue au total plus que l'hôte ne possède. Ici, « virtualisation » désigne celle de **machines complètes** ; les conteneurs partagent le noyau de l'hôte et sont traités ailleurs dans le pack.

## 3. Hyperviseur de type 1 et de type 2

![Schéma comparant l'hyperviseur de type 1, posé directement sur le matériel, et l'hyperviseur de type 2, exécuté au-dessus d'un système d'exploitation hôte](images/virtualisation-hyperviseurs-1.svg)
*Hyperviseurs de type 1 (natif, « bare metal ») et de type 2 (hébergé). Libellés en anglais : HARDWARE = matériel, OS = système d'exploitation.*

**Type 1.** Il s'installe directement sur le matériel, comme un système minimal dédié aux VM. C'est le modèle des datacenters : VMware ESXi, Microsoft Hyper-V, Xen, et KVM dans Proxmox VE. Avantages : performances, surface d'attaque réduite, conception pour la disponibilité (clusters, migration à chaud). Inconvénient : la machine est dédiée et demande des compétences d'administration.

**Type 2.** Application installée sur Windows, macOS ou Linux : Oracle VirtualBox, VMware Workstation, Parallels. Idéal pour tester ou se former ; moins prévisible (mises à jour, veille de l'hôte), non conçu pour une production exigeante.

**Les nuances.** La classification est pédagogique :

- **KVM** est un module du noyau Linux : le noyau devient hyperviseur et QEMU fournit les périphériques. On le range en type 1, mais l'hôte est un Linux complet.
- **Hyper-V**, même activé sur un Windows de poste, démarre **avant** Windows, qui tourne alors dans une « partition parente ».
- Un type 2 accéléré par le matériel exécute le code invité presque nativement : l'écart se réduit.

**Autres techniques.** L'*émulation* imite un autre processeur (très lent) ; la *paravirtualisation* fait coopérer l'invité et l'hyperviseur (virtio) ; la *virtualisation assistée par le matériel* est le cas général aujourd'hui. Règle pratique : un type 1 en production, un type 2 en poste et en formation.

## 4. Anatomie d'une machine virtuelle

Pour l'invité, la VM ressemble à un PC (UEFI, processeur, RAM, disque, carte réseau). Pour l'hôte, c'est :

- **un fichier de description** (`.conf`, `.vmx`, `.xml`, `.vmcx`) : vCPU, RAM, disques, réseaux ;
- **un ou plusieurs disques virtuels** : `raw` (brut), `qcow2` (QEMU, allocation à la demande, snapshots), `vmdk` (VMware), `vhdx` (Hyper-V) ;
- **un processus** : avec KVM/QEMU, une VM est un processus Linux dont chaque vCPU est un thread ;
- **un espace mémoire** et, éventuellement, un état sauvegardé.

On peut donc voir une VM dans la liste des processus, la limiter et la surveiller avec les outils habituels. Et comme tout se résume à des fichiers, perdre une VM revient à perdre des fichiers : d'où la sauvegarde. La conversion entre formats (`qemu-img convert`) se fait sur une copie, VM arrêtée, avec contrôle d'intégrité.

## 5. Dimensionner une VM : vCPU, RAM, disque

**vCPU.** Un vCPU n'est pas un cœur réservé : c'est un fil que l'hyperviseur place sur un cœur libre. Commence petit (1 à 2 vCPU pour un service léger) : une VM de 8 vCPU qui en utilise 20 % complique l'ordonnancement de tout l'hôte, et un second vCPU ne sert à rien à une application mono-thread. Le total des vCPU rapporté aux cœurs physiques donne le ratio d'overcommit CPU.

**RAM.** Le CPU se partage dans le temps, la mémoire dans l'espace. L'allocation *statique* réserve la quantité configurée (prévisible, gaspilleuse) ; l'allocation *dynamique* ajuste entre un minimum et un maximum (ballooning, mémoire dynamique Hyper-V : économe, moins prévisible). Linux utilise la mémoire libre comme cache disque : regarde « disponible », pas « libre ». Garde une marge pour l'hôte lui-même (et pour ZFS ou Ceph).

**Disque.** La taille déclarée n'est pas l'espace occupé (voir la leçon sur le stockage). Pense aux **IOPS** et à la **latence** : dix VM sur un disque lent se gênent, quelle que soit la capacité. Utilise un contrôleur paravirtualisé (virtio-scsi, virtio-blk).

**Exemple.** Petit serveur web de test : 1 à 2 vCPU, 1 à 2 Go, 20 Go de disque, carte réseau paravirtualisée, outils invités. Une base de production se dimensionne sur des mesures. Règle d'or : **mesurer, ajuster, recontrôler**.

## 6. L'overcommit : promettre plus que ce qu'on possède

![Schéma d'un hôte de 8 cœurs et 64 Go de RAM hébergeant quatre VM qui totalisent 16 vCPU et 80 Go de mémoire promis](images/virtualisation-hyperviseurs-2.svg)
*Exemple chiffré : le CPU surengagé de 2 pour 1 est généralement acceptable, la mémoire à 125 % ne l'est pas.*

Une compagnie aérienne vend plus de billets que de sièges, en pariant que tous les passagers ne viendront pas ; si tout le monde se présente, c'est la crise. L'overcommit repose sur le même pari.

**CPU.** Si une VM n'a rien à faire, elle libère son créneau. Un ratio de 2 à 4 vCPU par cœur est courant pour des charges légères ; pour des bases de données ou du calcul, on reste proche de 1 pour 1. Symptômes d'un surengagement : charge élevée de l'hôte et, dans l'invité, la métrique **`steal`** (colonne `st` de `top` ou `vmstat`), temps pendant lequel la VM voulait tourner mais où l'hyperviseur donnait la main à une autre. Chez VMware, le « CPU ready » joue ce rôle.

**Mémoire.** Plus délicate : à l'instant T, chaque page appartient à quelqu'un. Les hyperviseurs ont des techniques : le **partage de pages** (KSM : pages identiques stockées une fois), le **ballooning** (un pilote invité occupe de la mémoire pour que l'hôte la récupère), la **compression**, et en dernier recours le **swap de l'hôte**, qui fait s'effondrer les performances. Quand cela déraille : swap massif, toutes les VM ralentissent, ou l'OOM killer tue des processus, voire une VM. En production on évite le surengagement mémoire, on **réserve** la RAM des VM critiques et on garde une marge pour absorber la panne d'un hôte.

| Ressource | Stratégie raisonnable |
|---|---|
| CPU | Surengagement modéré et mesuré ; ratio plus bas pour les VM sensibles. |
| RAM | Aucun surengagement en production ; modéré et supervisé en test. |
| Disque (capacité) | Possible (disques fins) avec alerte sur l'espace réel. |

## 7. La virtualisation matérielle : VT-x, AMD-V, EPT, IOMMU

Virtualiser un x86 sans aide était pénible : certaines instructions sensibles ne s'interceptaient pas proprement. Les fabricants ont ajouté :

- **Intel VT-x** (indicateur `vmx`) et **AMD-V** (`svm`) : un mode d'exécution dédié, avec une transition « sortie de VM » (VM exit) ;
- **EPT** (Intel) et **NPT/RVI** (AMD), dits SLAT : traduction d'adresses assistée, qui réduit le coût de la mémoire des invités ;
- **IOMMU** (VT-d, AMD-Vi) : isole les accès directs des périphériques à la mémoire, indispensable au **passthrough** (donner une carte PCI à une VM).

Ces fonctions doivent souvent être **activées** dans le BIOS/UEFI. La **virtualisation imbriquée** (un hyperviseur dans une VM) n'est pas activée partout par défaut ; elle sert à tester Proxmox VE ou ESXi dans une VM de laboratoire, avec des performances réduites. Dans un invité Linux, l'indicateur `hypervisor` de `/proc/cpuinfo` et `systemd-detect-virt` révèlent la virtualisation.

## 8. Les pilotes invités : pourquoi les installer

![Schéma comparant le chemin d'un accès disque ou réseau avec un périphérique émulé et avec un pilote virtio paravirtualisé](images/virtualisation-hyperviseurs-3.svg)
*Un périphérique émulé impose une sortie de VM à chaque accès ; virtio échange par files partagées et par lots.*

Par défaut, une VM peut présenter du matériel **émulé** ancien et répandu (carte Intel e1000, disque IDE ou SATA) : l'installation se passe sans surprise, mais chaque opération coûte cher. Les **pilotes paravirtualisés** font mieux : **virtio** (disque, réseau, ballon mémoire, console) est inclus dans les noyaux Linux récents ; sous Windows on charge les pilotes depuis une image dédiée.

Les **outils invités** (`qemu-guest-agent`, `open-vm-tools`, services d'intégration Hyper-V) apportent l'**arrêt propre**, la **synchronisation de l'heure** (sans conflit avec NTP), la **remontée d'informations** (IP, nom, état) et le **gel du système de fichiers** pour des sauvegardes cohérentes. Sans eux : disque et réseau lents, arrêt « à la prise » après délai, sauvegardes incohérentes, IP invisible dans la console.

Attention : changer le contrôleur disque d'une VM installée peut l'empêcher de démarrer si l'invité n'a pas le pilote dans son image de démarrage. On teste sur un clone, avec un instantané préalable.

## 9. Observer et gouverner

Confronte toujours les deux vues. Si l'invité manque de CPU alors que l'hôte est calme, regarde le plafond configuré, le `steal` et les files de disque ; si l'hôte est saturé alors que l'invité est tranquille, cherche l'overcommit, le swap de l'hôte ou un voisin bruyant. Côté gouvernance : nomme les VM selon une convention, renseigne un propriétaire, mets les invités à jour, sauvegarde et teste la restauration, supprime les VM oubliées après sauvegarde, cloisonne les réseaux. Avant toute opération sensible : snapshot ou sauvegarde, console de secours, test, retour arrière.

## Mise en pratique guidée

**Objectif** : vérifier la virtualisation matérielle de ton poste, créer une VM jetable avec QEMU/KVM, observer ses ressources de l'intérieur et de l'extérieur.

**Règles du laboratoire** : poste personnel ou VM jetable ; aucun accès à des machines de production ; pas de données réelles ; adresses de documentation uniquement ; un instantané ou une copie de ce que tu modifies ; une console de secours ouverte avant toute action réseau.

### Étape 1 — Vérifier les extensions du processeur

```bash
grep -m1 -o -E 'vmx|svm' /proc/cpuinfo
```
👉 Explication : affiche `vmx` (Intel VT-x) ou `svm` (AMD-V) si le processeur expose la virtualisation matérielle ; aucune sortie signifie qu'elle est absente ou désactivée dans le BIOS/UEFI.

```bash
ls -l /dev/kvm
```
👉 Explication : vérifie que le noyau expose le périphérique KVM ; s'il est absent, le module n'est pas chargé ou la virtualisation est désactivée. Les droits d'accès dépendent du groupe `kvm` ; ne change pas les droits du système sans comprendre pourquoi.

```bash
lscpu | grep -Ei 'virtualisation|virtualization|hypervisor'
```
👉 Explication : montre le type de virtualisation matérielle du processeur et, si tu es toi-même dans une VM, le fournisseur d'hyperviseur détecté.

### Étape 2 — Installer les outils de laboratoire (poste Debian)

```bash
sudo apt update && sudo apt install --yes qemu-system-x86 qemu-utils
```
👉 Explication : installe l'émulateur QEMU et l'outil `qemu-img` ; à exécuter sur un poste de laboratoire où tu as les droits d'administration, jamais sur un serveur de production.

### Étape 3 — Créer un disque virtuel fin

```bash
mkdir -p ~/lab-virt && cd ~/lab-virt
qemu-img create -f qcow2 lab-vm.qcow2 10G
qemu-img info lab-vm.qcow2
```
👉 Explication : crée un disque qcow2 de 10 Go qui n'occupe presque rien sur le disque hôte tant que rien n'y est écrit ; `qemu-img info` affiche la taille virtuelle et la taille réellement occupée, ce qui illustre l'allocation à la demande.

### Étape 4 — Démarrer une VM d'installation avec des pilotes virtio

Télécharge d'abord une image d'installation Debian depuis le site officiel (ou utilise celle dont tu disposes), puis :

```bash
qemu-system-x86_64 -enable-kvm -cpu host -smp 2 -m 2048 \
  -drive file=lab-vm.qcow2,if=virtio,format=qcow2 \
  -cdrom debian-netinst.iso -boot d \
  -nic user,model=virtio-net-pci \
  -vnc 127.0.0.1:1
```
👉 Explication : démarre une VM avec 2 vCPU, 2 Go de RAM, un disque et une carte réseau virtio, accessible par VNC uniquement sur l'interface locale (`127.0.0.1`, port 5901) ; `-enable-kvm` demande l'accélération matérielle, `-nic user` fournit un réseau de laboratoire isolé en traduction d'adresses.

Connecte-toi avec un client VNC sur `127.0.0.1:5901` et installe Debian avec les choix par défaut. À la fin, arrête la VM proprement, puis relance-la sans `-cdrom` ni `-boot d`.

### Étape 5 — Observer l'invité de l'intérieur

Dans la VM :

```bash
systemd-detect-virt
```
👉 Explication : indique le type de virtualisation détecté (par exemple `kvm`).

```bash
lscpu | grep -E '^CPU\(s\)|Model name'
free -h
```
👉 Explication : confirme que l'invité voit 2 processeurs et environ 2 Go de mémoire, c'est-à-dire exactement ce que tu as demandé à QEMU.

```bash
lspci | grep -i virtio
```
👉 Explication : liste les périphériques virtio vus par l'invité (réseau, disque…), preuve que le pilote paravirtualisé est utilisé.

```bash
vmstat 1 5
```
👉 Explication : affiche cinq mesures d'activité à une seconde d'intervalle ; la dernière colonne `st` est le temps « volé » par l'hyperviseur, proche de 0 dans un laboratoire tranquille.

### Étape 6 — Observer la VM de l'extérieur

Sur l'hôte, dans un autre terminal :

```bash
ps -eo pid,nlwp,pcpu,pmem,cmd | grep '[q]emu-system'
```
👉 Explication : montre la VM comme un simple processus Linux ; `nlwp` indique le nombre de threads, qui inclut les vCPU. Aucune modification n'est faite.

```bash
du -h ~/lab-virt/lab-vm.qcow2
```
👉 Explication : compare la taille réelle du fichier à la taille virtuelle de 10 Go déclarée.

### Étape 7 — Retour arrière

```bash
rm -rf ~/lab-virt
```
👉 Explication : supprime le dossier de laboratoire et la VM jetable ; vérifie le chemin avant d'exécuter, cette commande est irréversible.

---

## Exercices

1. **(Vocabulaire)** Définis en une phrase : hôte, invité, hyperviseur, vCPU. Donne un exemple de logiciel pour chacun des deux types d'hyperviseur.
2. **(Classification)** Classe VirtualBox, VMware ESXi, KVM et Hyper-V en type 1 ou type 2, et explique en deux lignes pourquoi KVM et Hyper-V peuvent prêter à discussion.
3. **(Calcul)** Un hôte a 16 cœurs physiques et 128 Go de RAM. On veut y placer 12 VM de 4 vCPU et 16 Go chacune. Calcule le ratio vCPU/cœur et le taux d'engagement mémoire. Quelles sont tes conclusions ?
4. **(Diagnostic)** Dans une VM Linux, `vmstat` montre `st` à 25 % de façon prolongée, alors que la VM n'exécute presque rien de coûteux. Propose trois hypothèses et les vérifications côté hôte.
5. **(Matériel)** Un collègue affirme que sa VM Proxmox ne démarre pas « avec KVM » et affiche une erreur sur l'accélération. Quelle liste de contrôles proposes-tu, de la plus simple à la plus technique ?
6. **(Pilotes)** Explique pourquoi une VM Windows installée avec disque IDE émulé est plus lente qu'avec virtio, et décris une procédure prudente pour passer au pilote virtio sur une VM existante.
7. **(Dimensionnement)** Propose un dimensionnement initial (vCPU, RAM, disque) pour : un serveur de fichiers de 15 utilisateurs, un contrôleur de domaine de laboratoire, un serveur de supervision. Justifie et indique comment tu vérifierais ensuite.
8. **(Gouvernance)** Rédige une checklist de 6 points à valider avant de supprimer une VM « qui semble inutilisée ».

## Corrigés des exercices

1. Hôte : machine qui fournit les ressources ; invité : système dans la VM ; hyperviseur : logiciel qui crée et arbitre les VM ; vCPU : fil d'exécution placé sur un cœur. Type 1 : ESXi, Hyper-V, Xen, KVM. Type 2 : VirtualBox, VMware Workstation.
2. VirtualBox : type 2 ; ESXi : type 1. KVM : type 1 en pratique (le noyau Linux est l'hyperviseur) mais l'hôte est un Linux complet. Hyper-V : type 1 ; activé sur Windows, l'OS d'administration tourne dans la partition parente.
3. 48 vCPU pour 16 cœurs : **3 : 1**, acceptable pour des charges légères, risqué pour des charges soutenues. 192 Go pour 128 Go : **150 %**, surengagement mémoire à éviter en production (réduire après mesure, ajouter de la RAM ou répartir sur plus d'hôtes).
4. Hypothèses : surengagement CPU de l'hôte, voisin bruyant, fréquence ou énergie bridée. Côté hôte : charge, utilisation par VM, VM à nombreux vCPU, limites de CPU configurées.
5. (1) `vmx`/`svm` présent ? (2) virtualisation activée dans le BIOS/UEFI ? (3) `/dev/kvm` et modules `kvm`, `kvm_intel` ou `kvm_amd` ? (4) si l'hôte est une VM, imbrication activée chez son hyperviseur ? (5) type de CPU configuré compatible ? (6) journaux de l'hôte.
6. L'IDE émulé impose beaucoup de sorties de VM et une file courte ; virtio échange par files partagées. Procédure : sauvegarde ou instantané, charger le pilote virtio dans Windows via un petit disque virtio temporaire, vérifier sa détection, arrêter la VM, changer le contrôleur du disque système, redémarrer ; sinon revenir à l'ancien contrôleur ou restaurer. D'abord sur un clone.
7. Exemples : serveur de fichiers (2 vCPU, 4 Go, 40 Go + données) ; contrôleur de domaine de labo (2 vCPU, 4 Go, 60 Go) ; supervision (2–4 vCPU, 4–8 Go, disque selon la rétention). On mesure ensuite la charge sur une période représentative et on ajuste.
8. Propriétaire prévenu ; activité réseau et connexions vérifiées ; dépendances (DNS, tâches planifiées) examinées ; sauvegarde testée ; arrêt d'observation avant suppression ; inventaire et supervision mis à jour.

## Quiz

**Question 1.** Quelle affirmation décrit le mieux un hyperviseur de type 2 ?

- A. Il remplace entièrement le système d'exploitation de l'hôte.
- B. Il s'exécute comme une application au-dessus d'un système d'exploitation classique.
- C. Il ne permet jamais d'exécuter plus d'une VM.

**Question 2.** Quel indicateur de `/proc/cpuinfo` signale la virtualisation matérielle d'un processeur Intel ?

- A. `svm`
- B. `vmx`
- C. `hypervisor`

**Question 3.** Un hôte a 8 cœurs et héberge des VM totalisant 24 vCPU. Le ratio est :

- A. 3 : 1
- B. 1 : 3
- C. 8 : 24 sans signification

**Question 4.** Pourquoi l'overcommit mémoire est-il plus dangereux que celui du CPU ?

- A. La mémoire est plus chère.
- B. Le CPU se partage dans le temps alors que la mémoire occupée ne peut pas être « prêtée » sans lenteur ou perte (swap, OOM).
- C. Il n'y a aucune différence.

**Question 5.** Que mesure la colonne `st` (steal) de `vmstat` dans un invité ?

- A. Le temps passé à attendre le disque.
- B. Le temps pendant lequel l'invité voulait le CPU mais l'hyperviseur l'a donné à un autre.
- C. Le temps de démarrage de l'invité.

**Question 6.** Quel est l'effet principal d'un pilote virtio par rapport à une carte e1000 émulée ?

- A. Il réduit les sorties de VM et améliore le débit et la latence.
- B. Il chiffre automatiquement le trafic.
- C. Il permet de se passer de l'hyperviseur.

**Question 7.** À quoi sert l'agent invité (qemu-guest-agent, open-vm-tools) ?

- A. À remplacer le pare-feu de l'hôte.
- B. À permettre arrêt propre, remontée d'informations et sauvegardes cohérentes.
- C. À augmenter la capacité du disque.

**Question 8.** Quelle bonne pratique de dimensionnement est recommandée ?

- A. Donner le maximum de vCPU à toutes les VM par précaution.
- B. Commencer modestement, mesurer, puis ajuster.
- C. Ne jamais redimensionner une VM après sa création.

**Question 9.** Qu'est-ce que l'IOMMU permet en particulier ?

- A. De donner de façon sûre un périphérique PCI à une VM (passthrough).
- B. De doubler la mémoire de l'hôte.
- C. De convertir les disques qcow2 en VMDK.

**Question 10.** Avant de modifier le contrôleur disque d'une VM de production, que fais-tu ?

- A. Rien, c'est transparent pour l'invité.
- B. Instantané ou sauvegarde, test sur un clone, accès console de secours, plan de retour.
- C. J'arrête l'hôte entier.

### Réponses justifiées

1. **B.** Le type 2 est une application dans un OS hôte (VirtualBox, VMware Workstation). A décrit le type 1 ; C est faux.
2. **B.** `vmx` pour Intel VT-x, `svm` pour AMD-V ; `hypervisor` indique que l'on tourne déjà dans une VM.
3. **A.** 24 vCPU / 8 cœurs = 3 vCPU par cœur, soit 3 : 1.
4. **B.** Le CPU alterne dans le temps ; la mémoire occupée doit exister quelque part, sinon on swappe, on compresse, ou le noyau tue des processus.
5. **B.** C'est la définition du temps « volé » ; l'attente disque se lit dans `wa`.
6. **A.** Les files partagées de virtio évitent une sortie de VM par accès aux registres, d'où de meilleures performances.
7. **B.** L'agent invité fournit arrêt propre, informations IP, gel du système de fichiers pour sauvegarde ; il n'agit ni sur le pare-feu ni sur la capacité.
8. **B.** Les VM sur-dimensionnées pénalisent l'ordonnancement ; on mesure et on ajuste.
9. **A.** L'IOMMU (VT-d, AMD-Vi) isole les accès DMA et permet le passthrough sûr.
10. **B.** Toute modification sensible demande instantané ou sauvegarde, test sur clone, console de secours et retour arrière.

---

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Piste de résolution |
|---|---|---|
| `/dev/kvm` introuvable ou « KVM not available » | Virtualisation désactivée dans le BIOS/UEFI, modules non chargés, hôte lui-même virtualisé sans imbrication | Contrôler `vmx`/`svm`, activer l'option du BIOS/UEFI, vérifier l'imbrication. |
| VM très lente sans cause visible | Émulation sans accélération (pas de KVM), périphériques émulés, overcommit | Vérifier l'accélération, passer à virtio, regarder le `steal` et la charge de l'hôte. |
| `st` élevé dans l'invité | CPU de l'hôte surengagé ou voisin bruyant | Réduire le nombre de vCPU, déplacer des VM, limiter les voisins. |
| L'hôte swappe, tout ralentit | Surengagement mémoire | Réduire la mémoire attribuée, réserver pour les VM critiques, ajouter de la RAM. |
| Arrêt « brutal » depuis la console de gestion | Agent invité absent ou arrêté, ACPI non géré | Installer et démarrer l'agent, vérifier la configuration ACPI de la VM. |
| VM qui ne démarre plus après changement de contrôleur | Pilote absent de l'image de démarrage | Revenir au contrôleur précédent, préparer l'invité (pilote, initramfs) puis retenter sur un clone. |

Rappel de méthode : avant toute modification sensible, **snapshot ou sauvegarde, console de secours, test sur une copie, retour arrière écrit**.

## À retenir

- Un hyperviseur partage le matériel entre des VM isolées ; type 1 pour la production, type 2 pour le poste de travail et l'apprentissage.
- Une VM est un ensemble de configuration, disques et ressources prêtées : traite-la comme des données à protéger.
- Dimensionne par la mesure : commence petit, observe, ajuste.
- Le CPU se surengage avec modération ; la mémoire de production, presque jamais.
- Active la virtualisation matérielle et installe les pilotes et agents invités.
- Observe toujours l'hôte et l'invité ensemble : le `steal` est le pont entre les deux vues.
- Toute opération sensible s'entoure de : snapshot ou sauvegarde, accès de secours, test, retour arrière.

## Pour aller plus loin

- Documentation de QEMU : <https://www.qemu.org/docs/master/>
- Site du projet KVM : <https://linux-kvm.org/>
- Spécification virtio (OASIS) : <https://docs.oasis-open.org/virtio/virtio/v1.2/virtio-v1.2.html>
- Documentation de Proxmox VE : <https://pve.proxmox.com/pve-docs/>
- Présentation d'Hyper-V (Microsoft Learn) : <https://learn.microsoft.com/windows-server/virtualization/hyper-v/hyper-v-technology-overview>
- Documentation VMware vSphere (Broadcom TechDocs) : <https://techdocs.broadcom.com/>
- Leçons suivantes de ce dossier : [Réseau et stockage virtuels](/fr/00-cours-theoriques/tout-en-un/06-virtualisation-conteneurs-cloud/lecons/lecon-virtualisation-reseau-stockage) et [Panorama Proxmox VE, vSphere et Hyper-V](/fr/00-cours-theoriques/tout-en-un/06-virtualisation-conteneurs-cloud/lecons/lecon-virtualisation-panorama-plateformes).

## Crédits des images

| Fichier | Source (URL Commons) | Auteur | Licence | Modifications |
|---|---|---|---|---|
| `images/virtualisation-hyperviseurs-1.svg` | <https://commons.wikimedia.org/wiki/File:Hyperviseur.svg> | Scsami | CC0 1.0, <https://creativecommons.org/publicdomain/zero/1.0/> | Aucune (fichier SVG d'origine renommé). |
| `images/virtualisation-hyperviseurs-2.svg` | Création originale du projet Pack Master | Projet Pack Master | Dédiée au domaine public (CC0) | Sans objet. |
| `images/virtualisation-hyperviseurs-3.svg` | Création originale du projet Pack Master | Projet Pack Master | Dédiée au domaine public (CC0) | Sans objet. |

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Contenu rédigé ; seules les lectures `grep -m1 -o -E 'vmx\|svm' /proc/cpuinfo` (résultat : `vmx`) et `ls -l /dev/kvm` (présent) ont été exécutées, sur le poste de rédaction, en lecture seule | Rédacteur (assistant) | Non testé sur plateforme cible |
| 2026-11-01 | QEMU/KVM sur Debian 12, installation d'une VM jetable, mesure du steal | — | Non testé sur plateforme cible |