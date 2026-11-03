---
title: "Leçon — Réseau et stockage virtuels : bridges, VLAN, datastores, snapshots, templates"
description: "À la fin de cette leçon, tu sauras :"
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "lecon", "virtualisation", "reseau-virtuel", "vlan", "stockage", "snapshot", "sauvegarde"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Leçon — Réseau et stockage virtuels : bridges, VLAN, datastores, snapshots, templates

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `virtualisation`, `reseau-virtuel`, `vlan`, `stockage`, `snapshot`, `sauvegarde`
- **Niveau** : intermédiaire (technicien TSSR, administrateur systèmes en formation)
- **Durée estimée** : 3 h 30 (lecture 1 h 30, laboratoire 1 h, exercices et quiz 1 h)

---

## Objectifs pédagogiques

À la fin de cette leçon, tu sauras :

1. décrire le chemin d'un paquet entre une VM, un bridge ou vSwitch, une carte physique et le réseau réel ;
2. choisir entre mode ponté, NAT et réseau isolé, et configurer un VLAN (accès ou trunk) sans couper l'accès d'administration ;
3. expliquer ce qu'est un datastore et comparer stockage local, NFS, iSCSI, SAN et stockage distribué ;
4. distinguer disque fin et disque épais, et surveiller le surengagement de capacité ;
5. expliquer pourquoi un snapshot n'est pas une sauvegarde, et mettre en place une vraie stratégie de retour arrière ;
6. utiliser templates et clones (complets ou liés) en évitant les doublons d'identité ;
7. dresser la liste des risques et des contrôles associés.

## Prérequis et durée

- Avoir suivi la leçon [Hyperviseurs, machines virtuelles et ressources](/fr/00-cours-theoriques/tout-en-un/06-virtualisation-conteneurs-cloud/lecons/lecon-virtualisation-hyperviseurs), ou connaître hôte, invité, vCPU, disque virtuel.
- Notions de réseau : adresse IP, masque, passerelle, commutateur, VLAN.
- Laboratoire sur une **VM Linux jetable** (Debian 12) ou un hôte de laboratoire ; jamais sur une production.
- Adresses de documentation uniquement : 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24, 2001:db8::/32 ; domaines `example.com` et `example.test`.
- Durée : environ 3 h 30.

## L'essentiel en bref

- Un **bridge** (ou **vSwitch**) est un commutateur logiciel : il relie les cartes virtuelles des VM entre elles et à une carte physique.
- Un **VLAN** sépare des réseaux logiques sur le même câble grâce à une étiquette 802.1Q ; un lien **trunk** en transporte plusieurs.
- Un **datastore** est l'espace de stockage où vivent les disques des VM ; sa panne touche toutes les VM qu'il contient.
- **Fin** = alloué à la demande, économe mais risqué si le stockage se remplit ; **épais** = réservé d'avance, prévisible.
- Un **snapshot** est un point de retour **dépendant du stockage d'origine** ; une **sauvegarde** est une copie indépendante, restaurable après sinistre.
- **Template** = modèle ; **clone complet** = copie indépendante ; **clone lié** = dépend du disque du modèle. Un clone doit recevoir une **nouvelle identité**.
- Avant toute modification sensible : **snapshot ou sauvegarde, console de secours, test, retour arrière**.

---

## 1. Le réseau virtuel : un commutateur dans l'hôte

Une VM possède une ou plusieurs **cartes réseau virtuelles** (vNIC), chacune avec sa MAC. Elles se branchent sur un **commutateur virtuel** qui vit dans l'hôte : bridge Linux (`vmbr0` dans Proxmox VE), vSwitch (VMware), commutateur virtuel (Hyper-V). Comme un commutateur physique, il apprend les MAC et n'envoie la trame que vers le bon port. Analogie : une multiprise réseau dans l'hôte ; les VM sont les appareils, la carte physique est le câble qui sort vers le mur.

| Mode | Principe | Usage typique |
|---|---|---|
| **Ponté (bridged)** | La VM apparaît sur le réseau réel avec sa MAC et son IP. | Serveurs de production. |
| **NAT** | La VM sort par l'adresse de l'hôte, sans être joignable de l'extérieur. | Postes de laboratoire. |
| **Interne / isolé** | Réseau privé entre VM, sans carte physique. | Laboratoire fermé. |

Un hôte transporte des flux qu'il vaut mieux séparer, par cartes ou par VLAN : **gestion**, **VM**, **stockage** (sensible à la latence), **migration/réplication** (gros volumes ponctuels), **cluster/heartbeat** (faible volume, critique). On **agrège** les liens (LACP, bonding) pour la redondance. Ne mélange pas gestion et trafic saturable : une migration lourde ne doit pas rendre l'hôte injoignable.

## 2. Les VLAN dans un environnement virtualisé

![Trois VM sur un pont virtuel compatible VLAN, relié par un lien trunk à un commutateur physique](images/virtualisation-reseau-stockage-1.svg)
*Un pont virtuel étiquette le trafic de chaque VM (VLAN 10, 20, 30) et le transporte sur un trunk unique vers le commutateur physique. Création originale, adresses de documentation.*

Un **VLAN** (IEEE 802.1Q) découpe un réseau physique en réseaux logiques : deux machines de VLAN différents ne se voient pas, même sur le même commutateur et dans le même sous-réseau. L'étiquette est un identifiant de 1 à 4094 inséré dans la trame. Un port **d'accès** ne transporte qu'un VLAN ; un port **trunk** en transporte plusieurs, étiquetés (c'est le lien hôte → commutateur) ; le **VLAN natif** (non étiqueté sur un trunk) est une source classique de confusion si les deux extrémités ne sont pas d'accord.

| Plateforme | Où poser l'étiquette |
|---|---|
| Proxmox VE / Linux | Bridge compatible VLAN (`bridge-vlan-aware`) et champ « VLAN Tag » de la carte réseau de la VM. |
| VMware vSphere | **Groupe de ports** avec identifiant VLAN, sur un vSwitch dont les uplinks sont en trunk. |
| Hyper-V | Commutateur virtuel externe, identifiant VLAN par carte réseau de VM. |

Erreurs coûteuses :

- **Trunk incomplet** : le VLAN existe sur l'hôte mais n'est pas autorisé sur le port physique : la VM ne parle à personne.
- **Réseau de gestion modifié à distance** : la session coupe. **Console de secours (iLO, iDRAC, IPMI, console de l'hyperviseur) ouverte avant d'y toucher**, avec retour automatique si la plateforme en propose.
- **MTU incohérente** (9000 d'un côté, 1500 de l'autre) : les petits paquets passent, les gros disparaissent ; typique du stockage iSCSI/NFS.
- **Boucle** sans STP ni agrégation : tempête de diffusion.
- **MAC et promiscuité** : certains hyperviseurs bloquent par défaut les changements de MAC ; une VM de routage ou de capture doit être autorisée explicitement.

## 3. Le stockage virtuel : datastores et protocoles

Un **datastore** (« stockage », « pool ») est l'emplacement où l'hyperviseur place disques virtuels, ISO, parfois sauvegardes et templates.

| Type | Points forts | Points d'attention |
|---|---|---|
| **Local** (disques, RAID, ZFS) | Simple, rapide | Non partagé : pas de HA sans réplication. |
| **NFS / SMB** | Facile, souple | Latence réseau, verrouillage, serveur de fichiers. |
| **iSCSI / Fibre Channel** (SAN) | Performant, partagé | Dimensionnement, multipath, zonage. |
| **Distribué** (Ceph, vSAN, Storage Spaces Direct) | Pas de baie centrale, évolutif | Réseau dédié, nombre minimal de nœuds, complexité. |

Distingue **fichier** (l'hyperviseur voit des fichiers dans un partage) et **bloc** (il voit un disque brut). Trois indicateurs : la **capacité**, les **IOPS** (petites opérations aléatoires, typiques d'une base de données) et la **latence** (quelques millisecondes acceptables ; au-delà, les VM « ramollissent »). Une VM lente a souvent un problème de latence de stockage partagée avec une voisine gourmande (sauvegarde, réindexation), pas de CPU.

Le datastore est un **point unique de panne** : si dix VM en dépendent, sa panne les arrête toutes. Prévois redondance matérielle, réplication ou stockage distribué, supervision des disques et **sauvegardes hors de ce stockage**.

## 4. Disques fins et disques épais

![Datastore de 1 To contenant deux disques épais et trois disques fins, dont le total déclaré dépasse la capacité](images/virtualisation-reseau-stockage-2.svg)
*Surengagement de capacité : 1 800 Go promis pour 1 000 Go réels. Création originale du projet Pack Master.*

- **Épais** (thick) : tout l'espace est réservé à la création (chez VMware, *lazy zeroed* ou *eager zeroed*). Performance stable, pas de surprise de capacité, mais de la place immobilisée inutilement.
- **Fin** (thin) : l'espace est alloué au fil des écritures ; un disque de 400 Go contenant 100 Go de données occupe environ 100 Go. Économe, mais si tous les disques fins grossissent, le datastore se remplit et **les VM se bloquent ou passent en erreur**.

Le format compte : `raw` est épais par nature ; `qcow2`, `vmdk` fin et `vhdx` dynamique sont fins.

Bonnes pratiques :

1. Surveille l'**occupation réelle**, pas la taille déclarée : alerte à 70-80 %, action avant 90 %.
2. Garde une **marge libre** pour snapshots, consolidation et migrations.
3. Épais pour les charges critiques (bases de données), fin pour les VM ordinaires.
4. Active la **restitution d'espace** (TRIM/discard) de bout en bout quand c'est possible, sinon les fichiers supprimés dans l'invité occupent toujours de la place côté hôte.
5. Un disque fin ne rétrécit pas seul : libère l'espace dans l'invité, puis récupère-le côté hôte, hors heures de production.

## 5. Snapshots : un point de retour, pas une sauvegarde

![Chaîne de deltas de snapshot sur le même datastore comparée à une sauvegarde copiée vers un dépôt distinct](images/virtualisation-reseau-stockage-3.svg)
*Les deltas de snapshot partagent le sort du datastore ; la sauvegarde vit ailleurs. Création originale du projet Pack Master.*

À la prise du snapshot, l'état du disque est figé ; les écritures suivantes partent dans un **fichier delta** qui ne contient que les différences. Revenir en arrière revient à jeter le delta. Certains snapshots capturent aussi la **mémoire**, pour reprendre au même instant, au prix d'une création plus longue.

| Critère | Snapshot | Sauvegarde |
|---|---|---|
| Emplacement | Même stockage que la VM | Autre support, autre site |
| Panne du datastore | Perdu avec la VM | Restaurable ailleurs |
| Durée de vie | Heures ou jours | Semaines à années |
| Performance | Dégradation croissante avec la chaîne | Charge pendant la copie |
| Rançongiciel ou suppression | Faible protection | Forte si copie isolée et immuable |

Risques des snapshots : **chaîne trop longue** (lectures ralenties), **oubli** (un delta de plusieurs mois sature le datastore), **consolidation lourde** (espace, entrées-sorties, VM parfois figée), **incohérence** sur contrôleur de domaine ou serveur répliqué (suis la documentation de l'éditeur), et **cohérence limitée** : un snapshot à chaud est *cohérent après plantage* ; il n'est *cohérent applicativement* que si l'agent invité gèle le système de fichiers.

Règles d'usage : un snapshot **avant un changement**, nommé et daté, de quelques jours au plus ; **supprimé** une fois le changement validé ; pour toute donnée qui compte, une **sauvegarde 3-2-1** (trois copies, deux supports, une hors site, idéalement immuable ou hors ligne) ; et **une restauration testée** : une sauvegarde jamais restaurée est une hypothèse.

## 6. Templates et clones

Un **template** est une VM préparée une fois (système à jour, outils invités, configuration de base) qu'on duplique. Un **clone complet** est une copie indépendante, plus longue et gourmande en place. Un **clone lié** partage le disque de base du modèle et n'écrit que ses différences : rapide et économe, mais ce disque devient une dépendance critique : le perdre ou le modifier abîme tous les clones.

Préparer un bon modèle :

1. Installer système, correctifs et outils invités.
2. **Retirer l'identité** : `machine-id`, clés d'hôte SSH, nom d'hôte, journaux, historique, secrets. Sous Windows, généraliser avec `sysprep` ; sous Linux, réinitialiser le `machine-id` et régénérer les clés SSH au premier démarrage.
3. Utiliser si possible une initialisation au premier démarrage (cloud-init) pour nom, réseau et clés.
4. Verrouiller le modèle (nom explicite, version) et le mettre à jour de façon planifiée.

Le piège classique : un clone démarré sans nouvelle identité provoque **doublons d'IP, de nom, de MAC, de SID** (Windows dans un domaine), **clés SSH identiques**, jetons ou licences enregistrés. Pour un test de restauration, **démarre le clone sur un réseau isolé** ou avec une adresse différente avant toute connexion à la production.

## 7. Tableau des risques et contrôles

| Risque | Contrôle |
|---|---|
| Datastore plein (disques fins, snapshots) | Alertes d'occupation, marge, revue des snapshots. |
| Snapshot oublié | Étiquette de date, rapport automatique, suppression après validation. |
| Perte du datastore | Redondance, sauvegarde externe, test de restauration. |
| Trunk ou VLAN mal défini | Revue des VLAN, test de connectivité, schéma à jour. |
| Changement du réseau de gestion | Console de secours, retour arrière, fenêtre de maintenance. |
| Clone sans nouvelle identité | Généralisation, réseau isolé au premier démarrage. |

## Mise en pratique guidée

**Objectif** : simuler un bridge compatible VLAN avec des espaces de noms réseau, puis manipuler snapshots, disque lié et sauvegarde avec `qemu-img`.

**Règles** : exécute ceci **uniquement sur une VM Linux jetable** de laboratoire, depuis la **console** de l'hyperviseur (pas en SSH), après avoir pris un snapshot de cette VM jetable. Aucune machine de production, aucune adresse réelle.

### Partie A — Bridge et VLAN simulés

```bash
sudo ip link add br-lab type bridge vlan_filtering 1
sudo ip link set br-lab up
```
👉 Explication : crée un bridge Linux nommé `br-lab`, compatible VLAN (`vlan_filtering`), puis l'active ; il ne touche pas aux interfaces existantes.

```bash
for n in a b c; do
  sudo ip netns add vm-$n
  sudo ip link add v$n type veth peer name v$n-br
  sudo ip link set v$n netns vm-$n
  sudo ip link set v$n-br master br-lab up
  sudo ip netns exec vm-$n ip link set lo up
  sudo ip netns exec vm-$n ip link set v$n up
done
```
👉 Explication : crée trois « VM » simulées par des espaces de noms réseau, chacune reliée au bridge par un câble virtuel (paire `veth`).

```bash
sudo bridge vlan add dev va-br vid 10 pvid untagged
sudo bridge vlan add dev vb-br vid 10 pvid untagged
sudo bridge vlan add dev vc-br vid 20 pvid untagged
sudo bridge vlan del dev va-br vid 1
sudo bridge vlan del dev vb-br vid 1
sudo bridge vlan del dev vc-br vid 1
```
👉 Explication : place `vm-a` et `vm-b` dans le VLAN 10 et `vm-c` dans le VLAN 20 (ports d'accès), et retire le VLAN 1 par défaut de ces ports.

```bash
sudo ip netns exec vm-a ip addr add 192.0.2.11/24 dev va
sudo ip netns exec vm-b ip addr add 192.0.2.12/24 dev vb
sudo ip netns exec vm-c ip addr add 192.0.2.13/24 dev vc
```
👉 Explication : donne aux trois « VM » des adresses du même sous-réseau de documentation, pour montrer que le VLAN sépare même un sous-réseau commun.

```bash
sudo ip netns exec vm-a ping -c 2 192.0.2.12
sudo ip netns exec vm-a ping -c 2 -W 1 192.0.2.13
```
👉 Explication : le premier ping (même VLAN) doit réussir, le second (VLAN différent) doit échouer ; c'est la preuve de l'isolation.

```bash
bridge vlan show
```
👉 Explication : affiche la table des VLAN par port du bridge, en lecture seule.

### Partie B — Disques, snapshots, clone lié (`qemu-img`)

```bash
mkdir -p ~/lab-stock && cd ~/lab-stock
qemu-img create -f qcow2 base.qcow2 2G
qemu-img info base.qcow2
```
👉 Explication : crée un disque fin de 2 Go ; `info` compare la taille virtuelle (2 Go) et la taille réelle (quelques centaines de Ko).

```bash
qemu-img snapshot -c avant-changement base.qcow2
qemu-img snapshot -l base.qcow2
```
👉 Explication : crée un snapshot interne nommé `avant-changement` et liste les snapshots ; le point de retour vit **dans le même fichier**, donc sur le même stockage.

```bash
qemu-img create -f qcow2 -b base.qcow2 -F qcow2 clone-lie.qcow2
qemu-img info --backing-chain clone-lie.qcow2
```
👉 Explication : crée un clone lié qui dépend de `base.qcow2` ; la chaîne affichée montre la dépendance. Ne supprime ni ne modifie `base.qcow2` tant que le clone existe.

```bash
qemu-img convert -O qcow2 clone-lie.qcow2 clone-complet.qcow2
qemu-img info --backing-chain clone-complet.qcow2
```
👉 Explication : produit un clone **complet** et indépendant (aucun fichier de base listé) ; compare avec la chaîne précédente.

```bash
qemu-img check clone-complet.qcow2
```
👉 Explication : contrôle l'intégrité du disque copié, principe d'une vérification de sauvegarde.

### Partie C — Retour arrière du laboratoire

```bash
for n in a b c; do sudo ip netns del vm-$n; done
sudo ip link del br-lab
rm -rf ~/lab-stock
```
👉 Explication : supprime les espaces de noms (les paires `veth` disparaissent avec eux), le bridge et les fichiers du laboratoire ; vérifie le chemin avant `rm -rf`, l'opération est irréversible. En cas de doute sur la VM jetable, restaure son snapshot.

---

## Exercices

1. **(Vocabulaire)** Explique la différence entre un bridge et un VLAN, puis entre un port d'accès et un port trunk.
2. **(Réseau)** Une VM du VLAN 30 ne joint pas sa passerelle. Liste quatre vérifications, de l'invité vers le commutateur physique.
3. **(Sécurité de changement)** Tu dois changer le VLAN du réseau de gestion d'un hôte distant. Décris la procédure complète, avec snapshot ou sauvegarde de configuration, accès de secours, test et retour arrière.
4. **(Capacité)** Un datastore de 2 To contient 10 disques fins de 500 Go (occupés à 20 %) et 4 disques épais de 100 Go. Calcule capacité promise, occupation réelle, espace libre. Quel est ton diagnostic ?
5. **(Snapshots)** Un collègue laisse un snapshot « avant mise à jour » depuis trois mois sur un serveur de base de données. Quels risques ? Que fais-tu ?
6. **(Stratégie)** Propose une stratégie de protection pour un serveur de fichiers en VM : snapshots, sauvegarde (règle 3-2-1), fréquence, test de restauration.
7. **(Clones)** Tu clones un serveur Linux et un poste Windows pour des tests. Liste les éléments d'identité à renouveler dans chaque cas et la précaution réseau au premier démarrage.
8. **(Choix)** Une PME hésite entre un stockage NFS sur un NAS unique et un stockage distribué sur trois hôtes. Compare avantages, risques et prérequis.

## Corrigés des exercices

1. Un bridge relie des cartes virtuelles et physiques (commutation logicielle) ; un VLAN segmente logiquement un réseau avec une étiquette 802.1Q. Le port d'accès transporte un seul VLAN sans étiquette côté équipement ; le trunk transporte plusieurs VLAN étiquetés.
2. (1) Adresse, masque, passerelle dans l'invité ; (2) étiquette de VLAN sur la carte virtuelle ou le groupe de ports ; (3) bridge compatible VLAN et uplink de l'hôte ; (4) VLAN 30 autorisé sur le trunk du commutateur physique, route et pare-feu de la passerelle.
3. Fenêtre de maintenance annoncée ; sauvegarde de la configuration réseau ; console de secours testée ; si possible, changement avec délai de retour automatique ; appliquer sur un hôte à la fois ; tester l'accès sur la nouvelle configuration ; garder la configuration précédente pour revenir en arrière ; documenter.
4. Promis : 10 × 500 + 4 × 100 = 5 400 Go pour 2 000 Go (270 %). Réel : 10 × 100 + 400 = 1 400 Go, soit 70 % d'occupation et 600 Go libres. Diagnostic : surengagement de 270 % ; si les disques fins montent à 40 % d'occupation, ils représentent 2 000 Go et le datastore déborde. Mesures : alerte à 80 %, plafond de surengagement, migration de VM ou extension du stockage.
5. Risques : delta volumineux, performances dégradées, consolidation longue, espace saturé, incohérence si retour arrière. Action : vérifier l'espace, prévoir une fenêtre de maintenance, valider que la mise à jour est bonne, vérifier une sauvegarde récente, puis supprimer (fusionner) le snapshot.
6. Snapshots courts avant changements ; sauvegarde quotidienne cohérente (agent invité), 3 copies sur 2 supports dont une hors site ou immuable ; rétention adaptée ; restauration test planifiée (par exemple trimestrielle) sur un réseau isolé ; supervision des résultats.
7. Linux : `machine-id`, clés SSH, nom d'hôte, adresses, secrets. Windows : généralisation (`sysprep`), SID, nom, appartenance au domaine, licence. Précaution : démarrer sur un réseau isolé ou sans carte, ou avec une adresse unique, avant tout accès à la production.
8. Le NAS unique est simple et peu coûteux, mais c'est un point unique de panne. Le stockage distribué à trois nœuds survit à la perte d'un hôte, mais exige un réseau rapide dédié, une compétence d'exploitation, des disques adaptés et une marge de capacité pour la reconstruction. Dans les deux cas, une sauvegarde externe reste nécessaire.

## Quiz

**Question 1.** Un bridge virtuel sert principalement à :

- A. Chiffrer le trafic des VM.
- B. Relier les cartes virtuelles des VM entre elles et à une carte physique.
- C. Attribuer des adresses IP aux invités.

**Question 2.** Sur un lien hôte → commutateur portant les VLAN 10, 20 et 30, le port physique doit être en mode :

- A. Accès.
- B. Trunk.
- C. Miroir.

**Question 3.** Deux VM sont dans le même sous-réseau mais dans des VLAN différents. Que se passe-t-il ?

- A. Elles communiquent normalement.
- B. Elles ne se voient pas au niveau 2.
- C. Elles échangent uniquement en IPv6.

**Question 4.** Quel est le principal risque d'un disque fin ?

- A. Il ne peut pas être sauvegardé.
- B. Le datastore peut se remplir si le total des occupations réelles dépasse la capacité.
- C. Il ne supporte pas les snapshots.

**Question 5.** Un snapshot est-il une sauvegarde ?

- A. Oui, car il fige l'état de la VM.
- B. Non, car il dépend du stockage d'origine et disparaît avec lui.
- C. Oui, s'il est conservé un an.

**Question 6.** Que fais-tu avant de modifier le réseau de gestion d'un hôte distant ?

- A. Rien, une session SSH suffit.
- B. Je prépare la console de secours, une sauvegarde de configuration, un retour arrière.
- C. J'arrête les VM sans prévenir.

**Question 7.** Un clone lié :

- A. Est totalement indépendant du modèle.
- B. Dépend du disque de base, qui devient critique.
- C. Ne peut pas démarrer.

**Question 8.** Pourquoi démarrer un clone sur un réseau isolé ?

- A. Pour éviter doublons d'IP, de noms et d'identité avec la VM d'origine.
- B. Pour accélérer le disque.
- C. Pour supprimer les licences.

**Question 9.** Quelle règle résume une bonne stratégie de sauvegarde ?

- A. 1-1-1 : une copie, un support, un site.
- B. 3-2-1 : trois copies, deux supports, une copie hors site.
- C. 0-0-0 : rien, car les snapshots suffisent.

**Question 10.** Une MTU de 9000 d'un côté et de 1500 de l'autre provoque typiquement :

- A. Des échecs sur les gros paquets alors que les petits passent.
- B. Un doublement du débit.
- C. Une suppression des VLAN.

### Réponses justifiées

1. **B.** C'est un commutateur logiciel : il relie vNIC et carte physique. Il n'attribue pas d'IP (rôle du DHCP) ni ne chiffre.
2. **B.** Un trunk transporte plusieurs VLAN étiquetés ; un port d'accès n'en porte qu'un.
3. **B.** Les VLAN isolent au niveau 2, même avec le même sous-réseau IP.
4. **B.** L'allocation à la demande permet de promettre plus que la capacité ; si tout grossit, le datastore sature.
5. **B.** Un snapshot reste sur le même stockage ; la durée de conservation ne change pas cela.
6. **B.** On doit toujours pouvoir reprendre la main : console, sauvegarde, retour arrière.
7. **B.** Le clone lié ne contient que les différences ; sa base est donc critique.
8. **A.** Un clone démarré tel quel duplique l'identité réseau et système.
9. **B.** 3-2-1 : trois copies, deux supports, une hors site.
10. **A.** Les gros paquets ne passent pas la limite la plus basse (ou sont perdus s'ils sont non fragmentables), alors que les petits passent.

---

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Piste de résolution |
|---|---|---|
| VM sans réseau après ajout d'un VLAN | VLAN non autorisé sur le trunk physique ou bridge non compatible VLAN | Vérifier le trunk du commutateur et l'option de VLAN du bridge ; tester avec `bridge vlan show` côté Linux. |
| Perte d'accès à l'hôte après modification réseau | Bridge ou VLAN de gestion modifié | Console de secours, restauration de la configuration précédente, délai de retour automatique à l'avenir. |
| Gros transferts qui bloquent, petits paquets OK | MTU incohérente | Aligner la MTU de bout en bout ; tester avec `ping -M do -s <taille>`. |
| Datastore plein, VM en pause | Disques fins et snapshots qui ont grossi | Libérer ou étendre l'espace, supprimer les snapshots inutiles (après vérification), relancer les VM. |
| Deux machines avec la même IP après un clone | Identité non renouvelée | Arrêter le clone, régénérer identité et adresse, démarrer en réseau isolé. |
| Restauration impossible | Sauvegarde sur le même stockage que la VM, jamais testée | Copier hors du stockage de production, planifier des tests de restauration. |

Rappel : avant toute modification sensible, **snapshot ou sauvegarde, accès de secours, test, retour arrière**.

## À retenir

- Le commutateur virtuel fait partie de l'hôte : son état, ses VLAN et ses uplinks se traitent comme un équipement réseau.
- VLAN : étiquette 802.1Q, port d'accès pour un VLAN, trunk pour plusieurs ; le trunk physique doit correspondre.
- Le datastore est un point unique de panne : redondance, supervision, sauvegarde externe.
- Fin = économe mais dangereux sans alerte ; épais = prévisible mais coûteux.
- Un snapshot est un point de retour temporaire ; seule une sauvegarde isolée et testée protège d'un sinistre.
- Un clone sans nouvelle identité est un incident en attente.
- Console de secours avant toute modification du réseau de gestion.

## Pour aller plus loin

- IEEE 802.1Q (VLAN) : <https://1.ieee802.org/>
- Documentation du bridge Linux (noyau) : <https://docs.kernel.org/networking/bridge.html>
- Documentation de `qemu-img` : <https://www.qemu.org/docs/master/tools/qemu-img.html>
- Réseau et stockage dans Proxmox VE : <https://pve.proxmox.com/pve-docs/>
- Documentation Hyper-V (Microsoft Learn) : <https://learn.microsoft.com/windows-server/virtualization/hyper-v/hyper-v-technology-overview>
- Documentation VMware vSphere (Broadcom TechDocs) : <https://techdocs.broadcom.com/>
- Leçons voisines : [Hyperviseurs, machines virtuelles et ressources](/fr/00-cours-theoriques/tout-en-un/06-virtualisation-conteneurs-cloud/lecons/lecon-virtualisation-hyperviseurs) et [Panorama Proxmox VE, vSphere et Hyper-V](/fr/00-cours-theoriques/tout-en-un/06-virtualisation-conteneurs-cloud/lecons/lecon-virtualisation-panorama-plateformes).

## Crédits des images

| Fichier | Source (URL Commons) | Auteur | Licence | Modifications |
|---|---|---|---|---|
| `images/virtualisation-reseau-stockage-1.svg` | Création originale du projet Pack Master (pas de source Commons) | Projet Pack Master | Dédiée au domaine public (CC0) | Sans objet. |
| `images/virtualisation-reseau-stockage-2.svg` | Création originale du projet Pack Master (pas de source Commons) | Projet Pack Master | Dédiée au domaine public (CC0) | Sans objet. |
| `images/virtualisation-reseau-stockage-3.svg` | Création originale du projet Pack Master (pas de source Commons) | Projet Pack Master | Dédiée au domaine public (CC0) | Sans objet. |

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Contenu rédigé ; aucune commande de la leçon n'a été exécutée (les outils `ip`, `bridge` et `qemu-img` ne sont pas disponibles sur le poste de rédaction) | Rédacteur (assistant) | Non testé sur plateforme cible |
| 2026-11-01 | Debian 12 (VM jetable), `iproute2`, `qemu-utils` | — | Non testé sur plateforme cible |