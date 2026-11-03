---
title: "Leçon — Panorama Proxmox VE, VMware vSphere et Hyper-V : concepts, haute disponibilité, migration à chaud, licences, exploitation"
description: "À la fin de cette leçon, tu sauras :"
published: true
date: 2026-11-03T14:22:28Z
tags: ["transverse", "tout-en-un", "lecon", "virtualisation", "proxmox", "vsphere", "hyper-v", "haute-disponibilite", "migration", "licences"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Leçon — Panorama Proxmox VE, VMware vSphere et Hyper-V : concepts, haute disponibilité, migration à chaud, licences, exploitation

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `virtualisation`, `proxmox`, `vsphere`, `hyper-v`, `haute-disponibilite`, `migration`, `licences`
- **Niveau** : intermédiaire (technicien [[Glossary:TSSR]], administrateur systèmes en formation)
- **Durée estimée** : 3 h 30 (lecture 1 h 30, laboratoire 1 h, exercices et quiz 1 h)

---

## Objectifs pédagogiques

À la fin de cette leçon, tu sauras :

1. décrire l'architecture de Proxmox VE, de VMware vSphere et de Microsoft Hyper-V, et relier leurs vocabulaires ;
2. expliquer ce qu'est un cluster, un quorum, un fencing, et ce que la haute disponibilité garantit réellement (et ne garantit pas) ;
3. expliquer la migration à chaud, ses prérequis et ses limites, et la distinguer de la migration à froid et de la migration de stockage ;
4. aborder la gestion des licences avec méthode, sans citer de prix ni se fier à des idées reçues ;
5. appliquer des bonnes pratiques d'exploitation : mises à jour, supervision, sauvegarde, sécurité, cycle de vie ;
6. construire une grille de choix argumentée pour un contexte donné.

## Prérequis et durée

- Avoir suivi les leçons [Hyperviseurs, machines virtuelles et ressources](/fr/00-cours-theoriques/tout-en-un/06-virtualisation-conteneurs-cloud/lecons/lecon-virtualisation-hyperviseurs) et [Réseau et stockage virtuels](/fr/00-cours-theoriques/tout-en-un/06-virtualisation-conteneurs-cloud/lecons/lecon-virtualisation-reseau-stockage), ou en maîtriser les notions.
- Laboratoire : plateforme **jetable** (Proxmox VE à deux ou trois nœuds virtuels imbriqués, ou environnement d'évaluation officiel) ; **jamais** de production. Domaines `example.com` / `example.test` et adresses de documentation (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24).
- Durée : environ 3 h 30.

## L'essentiel en bref

- Les trois plateformes répondent aux mêmes besoins (exécuter des [[Glossary:VM]], les gérer en cluster, les déplacer, les protéger) avec des **vocabulaires différents**.
- **Proxmox VE** : Debian + [[Glossary:KVM]]/LXC + cluster intégré, logiciel libre, support par abonnement. **vSphere** : ESXi (hôte) + vCenter (gestion), écosystème commercial riche. **Hyper-V** : rôle de Windows Server, clustering de basculement Windows.
- La **haute disponibilité** redémarre les VM d'un hôte en panne ailleurs : c'est une **reprise rapide**, pas une continuité sans coupure.
- La **migration à chaud** déplace une VM allumée entre hôtes ; elle exige [[Glossary:CPU]] compatibles, réseau cohérent et stockage accessible (ou copie de stockage).
- Les **licences** changent selon l'éditeur et le temps : inventorie, lis les conditions en vigueur, anticipe les échéances.
- L'exploitation compte plus que le produit : correctifs en rotation, supervision, sauvegarde testée, accès de gestion protégés.
- Avant toute modification sensible : **snapshot ou sauvegarde, console de secours, test, retour arrière**.

---

## 1. Les trois plateformes en une page

### 1.1 Proxmox VE

Proxmox VE est une distribution basée sur **Debian** qui associe **KVM/QEMU** (machines virtuelles) et **[[Glossary:LXC]]** (conteneurs), une interface web, une [[Glossary:API]] et des outils en ligne de commande (`qm` pour les VM, `pct` pour les conteneurs, `pvesm` pour le stockage, `pvecm` pour le cluster, `ha-manager` pour la HA). Le cluster repose sur **Corosync** (communication et quorum) et un système de fichiers de configuration partagé (`pmxcfs`, monté sous `/etc/pve`). Les stockages possibles : local ([[Glossary:LVM]], [[Glossary:ZFS]]), [[Glossary:NFS]], iSCSI, **Ceph** intégré, etc. **Proxmox Backup Server** complète l'ensemble (déduplication, sauvegardes incrémentales).

Le code est sous licence libre (AGPLv3) ; l'éditeur vend des **abonnements** qui donnent accès au dépôt « entreprise » (mises à jour testées) et à un support.

### 1.2 VMware vSphere

vSphere associe **ESXi**, l'hyperviseur de type 1 installé sur chaque hôte, et **vCenter Server**, le serveur de gestion centralisée. Les fonctions de cluster (HA, [[Glossary:DRS]] pour l'équilibrage de charge, vMotion pour la migration à chaud) passent par vCenter. Le réseau s'appuie sur des vSwitch standard ou **distribués**, le stockage sur des datastores VMFS, NFS, vSAN (stockage distribué) ou vVols.

Côté commercial, VMware appartient désormais à Broadcom, qui a profondément remanié les offres, les éditions et les conditions de licence ces dernières années. Les informations de cette leçon sur ce point restent volontairement générales : **vérifie les conditions en vigueur auprès de l'éditeur ou de son revendeur**.

### 1.3 Microsoft Hyper-V

Hyper-V est un **rôle de Windows Server** (aussi disponible sur certains postes Windows). Il s'administre avec le Gestionnaire Hyper-V, PowerShell, Windows Admin Center, et à plus grande échelle System Center Virtual Machine Manager (SCVMM) ou d'autres outils. La haute disponibilité s'appuie sur le **clustering de basculement Windows** (WSFC) et sur les **volumes partagés de cluster** (CSV) ; le stockage distribué se fait avec **Storage Spaces Direct**. La migration à chaud s'appelle **Live Migration**. Hyper-V s'intègre naturellement à Active Directory ; sa licence est liée à Windows Server.

## 2. Les concepts comparés

![Tableau comparant, pour Proxmox VE, VMware vSphere et Hyper-V, la gestion, le cluster, la haute disponibilité, la migration à chaud et le modèle économique](images/virtualisation-panorama-plateformes-2.svg)
*Mêmes besoins, vocabulaires différents. Création originale du projet Pack Master ; les noms de produits sont cités à titre descriptif, sans logo.*

Quelques correspondances utiles :

| Besoin | Proxmox VE | vSphere | Hyper-V |
|---|---|---|---|
| Hôte | Nœud | Hôte ESXi | Nœud / hôte Hyper-V |
| Gestion centrale | Cluster (pas de serveur dédié) | vCenter Server | WSFC + SCVMM / WAC |
| Équilibrage | Planification manuelle ou règles | DRS | Optimisation dynamique (SCVMM) |
| Disque virtuel | qcow2, raw, volume ZFS/Ceph | VMDK | VHDX |
| Pilotes invités | virtio, `qemu-guest-agent` | VMware Tools / `open-vm-tools` | Services d'intégration |

Un point d'architecture mérite d'être noté : **vSphere sépare** l'hôte (ESXi) et la gestion (vCenter, qui est lui-même une VM ou une appliance à protéger), alors que **Proxmox VE** distribue la gestion sur tous les nœuds du cluster (pas de serveur central, mais un quorum à maintenir). **Hyper-V** place la gestion du cluster dans Windows, avec Active Directory comme dépendance fréquente (attention aux démarrages « à froid » où le contrôleur de domaine est lui-même une VM).

## 3. Cluster, quorum, fencing et haute disponibilité

![Trois hôtes partageant un stockage : migration à chaud d'une VM de l'hôte 1 vers l'hôte 2, et redémarrage des VM d'un hôte en panne par la haute disponibilité](images/virtualisation-panorama-plateformes-1.svg)
*Migration à chaud (planifiée) et haute disponibilité (après panne) reposent sur le même socle : réseau de gestion fiable, stockage accessible, quorum. Création originale du projet Pack Master.*

**Cluster et quorum.** Un cluster regroupe plusieurs hôtes administrés ensemble. Pour qu'un cluster coupé en deux ne produise pas deux « cerveaux » aux décisions contradictoires (*split-brain*), on exige un **quorum** : une majorité de votes. Avec trois nœuds, deux suffisent ; avec deux nœuds, la perte de l'un fait perdre la majorité, d'où un **témoin** (QDevice sous Proxmox VE, témoin de disque, de partage ou cloud sous Windows, datastore de battement de cœur sous vSphere). Vise un nombre **impair** de votes et des liens de cluster **redondants**, séparés du trafic de VM.

**Fencing.** Quand un hôte ne répond plus, le cluster ignore s'il est éteint ou seulement injoignable. Redémarrer ses VM ailleurs alors qu'il fonctionne encore corromprait les disques (deux instances écrivent au même endroit). Le **fencing** garantit que l'hôte fautif ne peut plus écrire : chien de garde (*watchdog*), coupure électrique via la carte de gestion, verrous de stockage. Pas de HA sérieuse sans fencing.

| La HA fait | La HA ne fait pas |
|---|---|
| Détecter la panne d'un hôte et **redémarrer** ses VM ailleurs | Éviter la coupure : les VM redémarrent (quelques minutes) |
| Respecter des priorités de redémarrage | Protéger d'une erreur humaine ou d'une corruption |
| Fonctionner avec un stockage partagé (ou répliqué) | Réparer un stockage ou un réseau défaillant |
| | Garantir l'état applicatif : un redémarrage ressemble à une coupure de courant |

- **Capacité N+1** : il faut assez de ressources libres pour absorber la perte d'un hôte (*contrôle d'admission* chez VMware).
- **Continuité réelle** : certains produits exécutent la VM en parallèle (Fault Tolerance chez VMware), avec des contraintes fortes ; c'est un autre mécanisme.
- **Stockage répliqué** (par exemple réplication ZFS asynchrone sous Proxmox VE) : la VM redémarre sur la dernière réplication, avec une **perte de données possible**.
- **Ordre de démarrage** : annuaire, [[Glossary:DNS]], base de données avant les applications ; méfie-toi des dépendances circulaires (contrôleur de domaine nécessaire au démarrage du cluster).

## 4. Migration à chaud

La **migration à chaud** (vMotion, Live Migration, migration en ligne de Proxmox) déplace une VM allumée d'un hôte à un autre. Déroulé simplifié : l'hôte de destination prépare une VM vide ; la mémoire est copiée **par passes successives** pendant que la VM tourne, les pages modifiées étant recopiées ; quand le reste est petit, la VM est **suspendue une fraction de seconde** et l'état final est transféré ; elle reprend sur la destination, généralement sans rupture des connexions. Une VM qui modifie sa mémoire très vite (base chargée, calcul intensif) retarde la convergence : la plateforme peut la ralentir ou échouer.

| Prérequis | Pourquoi |
|---|---|
| **CPU compatibles** | L'invité a vu certaines instructions ; elles doivent exister sur la destination. Même génération, ou masque de compatibilité (EVC chez VMware, type de CPU générique sous Proxmox VE, compatibilité de processeur sous Hyper-V). |
| **Réseau de migration** dédié et rapide | La mémoire transite par le réseau ; un lien saturé fragilise l'opération. |
| **Mêmes réseaux et [[Glossary:VLAN]]** sur la destination | Sinon la VM perd sa connectivité. |
| **Stockage accessible** aux deux hôtes | Sinon, migration avec copie de stockage, plus longue. |
| **Pas de périphérique local lié** | Passthrough PCI, disque local, ISO de l'hôte : à détacher. |

À ne pas confondre : la **migration à froid** (VM éteinte), la **migration de stockage** (la VM reste sur son hôte, ses disques changent de datastore) et la migration entre clusters ou sites (latence, bande passante, sécurité, licences). Teste d'abord avec une VM de test, vérifie la connectivité après migration, planifie hors des pics et prépare un retour. La migration n'est **pas** une sauvegarde.

## 5. Gestion des licences

Les conditions commerciales évoluent : retiens une **méthode** plutôt que des chiffres.

- **Licence de l'hyperviseur** : par processeur, cœur, nœud ou abonnement selon l'éditeur. Proxmox VE est libre (l'abonnement achète support et dépôts stables) ; VMware propose des offres commerciales par abonnement aux conditions changeantes ; Hyper-V dépend de Windows Server et de ses éditions.
- **Licence des invités** : chaque Windows Server ou poste virtuel doit être licencié ; avec Windows Server, le nombre de VM autorisées dépend de l'édition et des cœurs couverts.
- **Licence des applications** : certains éditeurs facturent par cœur, socket ou hôte du cluster, avec des règles de **mobilité** : la migration à chaud ou la HA peuvent élargir le périmètre à licencier.
- **Outils périphériques** : sauvegarde, supervision, gestion centralisée.

Méthode : (1) inventorier hôtes, cœurs, éditions, versions, VM et OS invités ; (2) relever contrats, échéances et support ; (3) identifier les applications à licence liée au matériel ; (4) rapprocher inventaire et droits, documenter et corriger les écarts ; (5) prévoir la **réversibilité** (formats exportables, coût d'une migration) ; (6) réviser chaque année et avant tout changement d'architecture. Conserve les preuves de conformité ; n'utilise jamais de clé trouvée en ligne et ne contourne aucun mécanisme de licence.

## 6. Bonnes pratiques d'exploitation

**Accès de gestion.** Réseau de gestion dédié, non exposé à Internet ([[Glossary:VPN]] ou bastion) ; comptes nominatifs, **[[Glossary:MFA]]** quand c'est possible, droits par rôle, comptes d'urgence en coffre ; services inutiles désactivés, journaux centralisés. Protège vCenter, la gestion de cluster et les sauvegardes comme des actifs critiques : qui contrôle l'hyperviseur contrôle toutes les VM.

**Mises à jour.** Hôte par hôte, en vidant d'abord l'hôte (mode maintenance, migration des VM), avec contrôle du cluster avant et après ; notes de version lues, test en laboratoire ; versions **homogènes** entre hôtes ; firmware, [[Glossary:BIOS]] et pilotes conformes à la matrice de compatibilité ; fins de support anticipées.

**Supervision et capacité.** CPU, `steal`/ready, mémoire (balloon, swap), latence et occupation des datastores, réseau, santé du quorum, sauvegardes, matériel. Alertes sur seuils utiles, tendances, **N+1** dans les calculs.

**Sauvegarde et reprise.** Sauvegardes hors du stockage de production, règle **3-2-1**, restauration testée en réseau isolé ; sauvegarde de la **configuration** des hôtes et de la gestion ; snapshots courts ; plan de reprise avec ordre de redémarrage et exercice périodique.

**Changement et documentation.** Pour chaque changement sensible : **fenêtre annoncée, snapshot ou sauvegarde, console de secours, test sur clone ou laboratoire, retour arrière écrit**. Conventions de nommage, propriétaires, schémas réseau et stockage à jour (VLAN, [[Glossary:MTU]], chemins).

**Choisir.** Pose les bonnes questions : compétences de l'équipe, budget complet (licences, support, matériel, formation, sauvegarde), besoins de HA et de migration, règles de licence des applications, écosystème, réversibilité. Il n'existe pas de meilleur choix absolu : une petite structure à compétences Linux peut s'orienter vers Proxmox VE, un environnement Windows et Active Directory vers Hyper-V, une organisation très outillée vers vSphere. Ce sont des tendances, pas des règles.

## Mise en pratique guidée

**Objectif** : inspecter un cluster de laboratoire (lecture seule), puis réaliser une migration à chaud et un test de HA sur une VM jetable.

**Règles** : plateforme jetable uniquement (par exemple trois VM Proxmox VE imbriquées, noms `pve1.example.test` à `pve3.example.test`) ; sauvegarde ou snapshot de la VM de test ; console de secours disponible ; aucune VM de production ; aucun accès à une machine réelle. Remplace chaque identifiant (`9001`, nœuds) par ceux de ton laboratoire.

### Partie A — Proxmox VE : état du cluster (lecture seule)

```bash
pveversion -v | head -n 5
```
👉 Explication : affiche la version de Proxmox VE et des principaux paquets, utile pour vérifier l'homogénéité des nœuds.

```bash
pvecm status
```
👉 Explication : montre le quorum, le nombre de votes attendus et l'état du cluster ; vérifie que « Quorate » vaut `Yes`.

```bash
pvesm status
```
👉 Explication : liste les stockages avec leur type, état et occupation ; permet de repérer un stockage saturé ou non partagé avant une migration.

```bash
ha-manager status
qm list
```
👉 Explication : affiche l'état du gestionnaire de HA et les VM du nœud local ; ne modifie rien.

### Partie B — Migration à chaud d'une VM de test

```bash
qm migrate 9001 pve2 --online
```
👉 Explication : migre à chaud la VM de test `9001` vers le nœud `pve2` ; à lancer seulement si le stockage est partagé (sinon ajoute l'option `--with-local-disks`, plus longue) et après avoir pris un snapshot de la VM de test. Pendant l'opération, un `ping` continu vers la VM montre la brève pause éventuelle.

```bash
qm status 9001
```
👉 Explication : vérifie que la VM tourne bien et, avec `pvecm nodes` / l'interface, sur quel nœud ; retour arrière : relance la migration vers le nœud d'origine.

### Partie C — Test de haute disponibilité (laboratoire uniquement)

```bash
ha-manager add vm:9001 --state started
ha-manager status
```
👉 Explication : place la VM de test sous le contrôle de la HA et l'affiche dans l'état du gestionnaire ; la VM sera redémarrée ailleurs si son nœud tombe.

Simule ensuite la panne de **ce nœud de laboratoire uniquement** en l'éteignant depuis l'hyperviseur parent (arrêt forcé de la VM imbriquée), puis observe le redémarrage de `9001` sur un autre nœud et mesure le délai.

```bash
ha-manager remove vm:9001
```
👉 Explication : retire la VM de la HA une fois le test terminé ; remets ensuite le nœud arrêté en service et vérifie `pvecm status`.

### Partie D — Équivalents en lecture seule sur les autres plateformes

```powershell
Get-ClusterNode
Get-VM | Select-Object Name, State, ProcessorCount, MemoryAssigned
Get-VMHost | Select-Object VirtualMachineMigrationEnabled, VirtualMachineMigrationAuthenticationType
```
👉 Explication : sur un hôte Hyper-V d'un cluster de laboratoire, liste les nœuds, les VM et la configuration de migration ; aucune modification.

```powershell
Move-ClusterVirtualMachineRole -Name "vm-test01" -Node "HV02" -MigrationType Live
```
👉 Explication : déclenche une Live Migration de la VM de test `vm-test01` vers `HV02` dans un cluster de laboratoire ; à n'exécuter qu'après snapshot ou sauvegarde de cette VM.

```powershell
Connect-VIServer -Server vcenter.example.test
Get-Cluster | Select-Object Name, HAEnabled, DrsEnabled
Get-VMHost | Select-Object Name, ConnectionState, Version
```
👉 Explication : avec PowerCLI sur un vCenter d'évaluation, liste les clusters (HA, DRS) et les hôtes (état, version) ; lecture seule.

---

## Exercices

1. **(Vocabulaire)** Pour chacun des termes suivants, donne l'équivalent sous Proxmox VE, vSphere et Hyper-V : migration à chaud ; gestion centralisée ; pilotes invités.
2. **(Quorum)** Un cluster de deux nœuds perd l'un d'eux. Que se passe-t-il pour le quorum ? Quelle solution proposes-tu ?
3. **(HA)** Un client attend de la HA qu'elle « évite toute coupure ». Rédige une explication claire de ce qu'elle garantit et de ce qu'elle ne garantit pas, avec un exemple.
4. **(Capacité)** Un cluster de 4 hôtes de 256 Go de [[Glossary:RAM]] porte 640 Go de VM. Peut-il absorber la perte d'un hôte en HA ? Justifie par un calcul.
5. **(Migration)** Une migration à chaud échoue : « CPU incompatible ». Liste trois causes possibles et les corrections associées.
6. **(Licences)** Tu reprends un cluster de 3 hôtes sans documentation de licences. Établis un plan en 6 étapes pour évaluer la conformité.
7. **(Exploitation)** Rédige la procédure de mise à jour d'un cluster de 3 hôtes, hôte par hôte, avec contrôles avant/après et retour arrière.
8. **(Choix)** Une association de 20 postes dispose d'un administrateur à temps partiel et d'un budget limité. Propose un choix de plateforme argumenté, en indiquant les risques et les mesures.

## Corrigés des exercices

1. Migration à chaud : migration en ligne (Proxmox), vMotion (vSphere), Live Migration (Hyper-V). Gestion centralisée : cluster et interface web des nœuds, vCenter Server, WSFC avec SCVMM ou Windows Admin Center. Pilotes invités : virtio et `qemu-guest-agent`, VMware Tools ou `open-vm-tools`, services d'intégration.
2. Avec deux votes, perdre un nœud laisse un vote sur deux, soit pas la majorité : le quorum est perdu et les opérations de gestion ou de HA sont bloquées. Solution : un témoin tiers (QDevice, témoin de cluster Windows, datastore de battement de cœur) ou un troisième nœud.
3. La HA détecte la panne d'un hôte et **redémarre** les VM ailleurs, en quelques minutes ; l'état est celui d'une coupure de courant. Elle ne supprime pas la coupure, ne protège pas des erreurs humaines ni des corruptions, et ne remplace pas la sauvegarde. Exemple : un hôte tombe, la base de données redémarre, avec reprise après récupération du journal.
4. Capacité totale : 4 × 256 = 1 024 Go ; après perte d'un hôte : 768 Go. Les VM prennent 640 Go : cela tient en mémoire (83 %), mais sans marge pour l'hôte lui-même ni pour la croissance, et il faut vérifier que la mémoire est réservable. Conclusion : possible, mais limite ; viser N+1 avec marge (sur 3 hôtes, rester sous 66 % d'utilisation).
5. Hôtes de générations de CPU différentes → utiliser un mode de compatibilité (EVC, type de CPU générique, compatibilité de processeur) ; VM configurée avec un type de CPU « natif de l'hôte » → passer à un type compatible lors d'un arrêt planifié ; microcode ou paramètres BIOS différents (virtualisation, options CPU) → aligner les hôtes.
6. Inventaire matériel et logiciel ; contrats et abonnements ; liste des VM, OS invités et applications ; rapprochement droits/usages ; écarts et règles de mobilité ; plan de régularisation, preuves conservées, revue annuelle.
7. Vérifier cluster et sauvegarde ; lire les notes de version ; hôte 1 : mode maintenance, VM migrées, mise à jour, redémarrage, contrôle, retour en service ; répéter pour les hôtes 2 et 3 ; contrôles finaux. Retour arrière : arrêter au premier problème, remettre les VM sur les hôtes sains, restaurer la configuration sauvegardée.
8. Un hôte unique ou deux hôtes avec réplication, une plateforme bien documentée et maîtrisée (Proxmox VE, ou Hyper-V si l'environnement est Windows), sauvegarde externe testée, supervision simple, accès de gestion protégés, documentation. Risques : compétence unique (prévoir une procédure et un contrat de support), pas de HA sur un seul hôte (accepter le délai de restauration ou ajouter un second hôte).

## Quiz

**Question 1.** Quelle est la fonction principale d'un quorum dans un cluster ?

- A. Accélérer les migrations.
- B. Empêcher deux parties isolées de prendre des décisions contradictoires (split-brain).
- C. Chiffrer le trafic de gestion.

**Question 2.** Que fait la haute disponibilité lorsqu'un hôte tombe ?

- A. Elle migre à chaud les VM sans coupure.
- B. Elle redémarre les VM sur d'autres hôtes après avoir isolé l'hôte défaillant.
- C. Elle restaure les VM depuis la sauvegarde.

**Question 3.** Pourquoi le fencing est-il nécessaire ?

- A. Pour éviter que deux instances de la même VM écrivent sur les mêmes disques.
- B. Pour augmenter la mémoire disponible.
- C. Pour supprimer les snapshots.

**Question 4.** Quel est l'équivalent Hyper-V de vMotion ?

- A. Live Migration.
- B. Storage Spaces.
- C. Sysprep.

**Question 5.** Quel prérequis d'une migration à chaud est le plus souvent oublié ?

- A. Les mêmes réseaux et VLAN sur l'hôte de destination.
- B. Un fond d'écran identique.
- C. Un nom de VM court.

**Question 6.** Sous Proxmox VE, où trouve-t-on la configuration partagée du cluster ?

- A. Dans `/etc/pve`, via le système de fichiers de cluster `pmxcfs`.
- B. Dans un serveur vCenter.
- C. Uniquement dans le registre Windows.

**Question 7.** Quelle affirmation sur les licences est la plus prudente ?

- A. Les conditions ne changent jamais.
- B. Il faut inventorier, lire les conditions en vigueur et tenir compte des règles de mobilité des applications.
- C. Les clés trouvées en ligne conviennent pour un test.

**Question 8.** Pour la mise à jour d'un cluster, on procède :

- A. Sur tous les hôtes en même temps pour gagner du temps.
- B. Hôte par hôte, en mode maintenance, avec contrôles avant et après.
- C. Uniquement la nuit sans vérifier la sauvegarde.

**Question 9.** Un cluster de 3 hôtes à 80 % de mémoire utilisée sur chacun : que se passe-t-il à la perte d'un hôte ?

- A. Les VM restantes tiennent sans difficulté.
- B. Il manque de la capacité : les VM de l'hôte perdu ne pourront pas toutes redémarrer.
- C. Le cluster crée de la mémoire.

**Question 10.** Une migration est-elle une sauvegarde ?

- A. Oui, car la VM existe sur un autre hôte.
- B. Non : elle déplace la VM ; en cas de corruption ou de suppression, les données sont perdues.
- C. Oui, si elle est faite chaque jour.

### Réponses justifiées

1. **B.** Le quorum fixe qui a le droit de décider ; c'est la défense contre le split-brain.
2. **B.** La HA est une reprise, pas une continuité ; elle isole d'abord, puis redémarre ailleurs.
3. **A.** Sans isolement, une VM pourrait tourner en double et corrompre ses disques.
4. **A.** Live Migration est le terme Microsoft ; Storage Spaces est du stockage, Sysprep de la généralisation.
5. **A.** Sans les mêmes réseaux et VLAN, la VM perd sa connectivité après la migration.
6. **A.** `pmxcfs` expose la configuration du cluster sous `/etc/pve`.
7. **B.** Les conditions évoluent ; la méthode d'inventaire et la vérification sont la seule approche fiable.
8. **B.** Rotation en maintenance avec contrôles ; la sauvegarde doit être vérifiée avant.
9. **B.** Il reste 2 × 20 % = 40 % d'un hôte de mémoire libre pour absorber les 80 % de l'hôte perdu : c'est insuffisant.
10. **B.** Migrer n'ajoute aucune copie indépendante.

---

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Piste de résolution |
|---|---|---|
| Cluster « sans quorum », opérations bloquées | Perte de nœuds ou de liaison, pas de témoin | Rétablir les liens ou nœuds ; ajouter un témoin ; ne forcer le quorum qu'en connaissance de cause et dans les règles de l'éditeur. |
| HA qui ne redémarre pas toutes les VM | Capacité insuffisante, stockage non partagé | Recalculer N+1 ; vérifier le stockage ; hiérarchiser les VM. |
| Migration à chaud échouée | CPU incompatibles, réseau absent sur la destination, périphérique local | Mode de compatibilité CPU ; aligner réseaux/VLAN ; détacher les ressources locales. |
| VM injoignable après migration | VLAN ou groupe de ports différent | Aligner les noms et VLAN sur tous les hôtes. |
| Gestion injoignable après changement réseau | Changement du réseau de gestion sans accès de secours | Console de secours ; retour de la configuration ; délai de retour automatique. |

Rappel : avant toute modification sensible, **snapshot ou sauvegarde, accès console de secours, test, retour arrière**.

## À retenir

- Les trois plateformes couvrent les mêmes besoins ; apprends les **concepts** (cluster, quorum, fencing, HA, migration) avant les menus.
- HA = redémarrage rapide après panne, avec fencing, capacité N+1 et stockage accessible ; ce n'est pas une sauvegarde ni une continuité.
- Migration à chaud : CPU compatibles, réseau cohérent, stockage accessible, lien rapide.
- Licences : méthode, inventaire, lecture des conditions en vigueur, règles de mobilité des applications, réversibilité.
- Exploitation : accès de gestion protégés, mises à jour en rotation, supervision, sauvegarde testée, documentation à jour.
- Il n'y a pas de meilleur choix absolu : un choix se fait selon compétences, budget, besoins et réversibilité.

## Pour aller plus loin

- Documentation Proxmox VE (cluster, HA, migration, stockage) : <https://pve.proxmox.com/pve-docs/>
- Documentation Proxmox Backup Server : <https://pbs.proxmox.com/docs/>
- Documentation VMware vSphere (Broadcom TechDocs) : <https://techdocs.broadcom.com/>
- Hyper-V et clustering de basculement (Microsoft Learn) : <https://learn.microsoft.com/windows-server/virtualization/hyper-v/hyper-v-technology-overview> et <https://learn.microsoft.com/windows-server/failover-clustering/failover-clustering-overview>
- Documentation de Corosync : <https://corosync.github.io/corosync/>
- Leçons voisines : [Hyperviseurs, machines virtuelles et ressources](/fr/00-cours-theoriques/tout-en-un/06-virtualisation-conteneurs-cloud/lecons/lecon-virtualisation-hyperviseurs) et [Réseau et stockage virtuels](/fr/00-cours-theoriques/tout-en-un/06-virtualisation-conteneurs-cloud/lecons/lecon-virtualisation-reseau-stockage).

## Crédits des images

| Fichier | Source (URL Commons) | Auteur | Licence | Modifications |
|---|---|---|---|---|
| `images/virtualisation-panorama-plateformes-1.svg` | Création originale du projet Pack Master (pas de source Commons) | Projet Pack Master | Dédiée au domaine public (CC0) | Sans objet. |
| `images/virtualisation-panorama-plateformes-2.svg` | Création originale du projet Pack Master (pas de source Commons) | Projet Pack Master | Dédiée au domaine public (CC0) | Sans objet. |

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Contenu rédigé ; aucune commande de la leçon n'a été exécutée (pas de Proxmox VE, Hyper-V ni vSphere sur le poste de rédaction) | Rédacteur (assistant) | Non testé sur plateforme cible |
| 2026-11-01 | Proxmox VE (cluster de laboratoire), Windows Server (Hyper-V), VMware vSphere (PowerCLI) | — | Non testé sur plateforme cible |