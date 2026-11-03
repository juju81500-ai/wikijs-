# Nutanix AHV : cluster, Prism et première VM

- **Environnement** : Cluster Nutanix (AOS + AHV) sur matériel compatible ou environnement d'évaluation
- **Tags** : `nutanix`, `ahv`, `hyperviseur`, `hci`, `prism`
- **Statut de validation** : **Verdict : Non testé sur plateforme cible.** Les procédures ci-dessous sont issues de la méthode documentaire et doivent être rejouées en laboratoire avant toute production.

## 1. Périmètre et prérequis

- Périmètre : création d'un cluster AHV, accès Prism, réseau, stockage, première VM, sauvegarde et retour arrière. Hors périmètre : Nutanix Cloud Clusters, Flow, DR multi-sites.
- Matériel/HCL : vérifier la compatibilité nœuds, disques, cartes réseau et firmware dans la matrice de compatibilité du portail éditeur.
- Réseau : plan d'adressage pour hyperviseur (AHV), CVM et IPMI/BMC ; VLAN, DNS, NTP, passerelle ; commutateurs avec MTU et LACP/active-backup décidés.
- Minimum de nœuds, facteur de réplication (RF2/RF3) et capacité tolérée en cas de panne : à valider selon la documentation éditeur de la version retenue.
- Comptes : accès au portail support, licences ou évaluation, clés API/téléchargement.

## 2. Exigences de version et licence

- **Version à figer avant déploiement** : couple AOS / AHV / Prism Central / firmware, choisi dans les notes de version et la matrice de compatibilité éditeur. Ne pas mélanger les versions hors matrice.
- Licences : le niveau de licence (édition, durée, fonctions) conditionne les fonctions disponibles ; l'édition Community n'est pas destinée à la production. Confirmer les conditions actuelles sur le portail éditeur.
- Noter la date de fin de support de la version AOS retenue.

## 3. Procédure

1. Relever l'inventaire (numéros de série, IPMI, firmware) et valider la compatibilité.
2. Préparer les adresses et noms ; vérifier DNS direct/inverse et NTP.
3. Installer ou vérifier l'image AHV/AOS sur chaque nœud selon la procédure éditeur (Foundation ou méthode documentée).
4. Créer le cluster depuis une CVM, puis définir le nom, les VIP et les serveurs DNS/NTP.
5. Se connecter à Prism Element, accepter le contrat, enregistrer le cluster.
6. Créer un réseau VM (VLAN) et un conteneur de stockage avec les options de redondance retenues.
7. Charger une image ISO dans la bibliothèque d'images et créer une VM de test (vCPU, RAM, disque, NIC).
8. Installer les pilotes invités VirtIO si l'OS invité l'exige (Windows notamment).
9. Planifier une protection (snapshots/sauvegarde) et la tester par restauration vers une VM de test.

Contrôles en lecture depuis une CVM (commandes de diagnostic, à confirmer dans la documentation de la version) :
```bash
cluster status
ncli cluster info
ncc health_checks run_all
```

## 4. Vérifications

- `cluster status` : tous les services `UP` sur chaque CVM.
- Prism : santé du cluster verte, alertes traitées, tolérance de panne affichée conforme au RF.
- VM de test : démarrage, ping, migration à chaud entre nœuds, restauration depuis snapshot.

## 5. Rollback et risques

- Ne jamais arrêter plusieurs nœuds simultanément : le quorum métadonnées et la tolérance de panne peuvent être perdus.
- Mises à jour : réaliser par LCM/méthode éditeur, nœud par nœud, hors fenêtre de pointe, après sauvegarde et contrôle NCC. Pas de retour arrière automatique garanti : prévoir restauration depuis sauvegarde externe.
- Avant toute opération destructive (suppression de conteneur, ajout/retrait de nœud), obtenir un instantané et une sauvegarde hors cluster validés.
- Risque : cluster de test supprimé par erreur ; ne pas réutiliser d'adresses de production.

## 6. Documentation officielle

- <https://portal.nutanix.com/>
- <https://www.nutanix.dev/>
