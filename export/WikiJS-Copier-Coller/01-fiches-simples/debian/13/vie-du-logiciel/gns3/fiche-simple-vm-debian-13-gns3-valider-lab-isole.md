# Fiche_Simple_-_VM_Debian_13_GNS3_Valider_Lab_Isole.md

- **Environnement** : GNS3 2.2.61 sur Debian 13, serveur local et topologie isolée
- **OS / Version** : Debian 13 Trixie amd64
- **Catégorie** : simulation réseau / laboratoire

---

## Problème précis à résoudre

Vérifier qu'un projet GNS3 s'ouvre et s'enregistre sur le serveur local sans pont vers le réseau physique ni image dont l'utilisation n'est pas autorisée.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer versions, QEMU et KVM :
   ```bash
   gns3 --version
   gns3server --version
   qemu-system-x86_64 --version | head -1
   ls -l /dev/kvm
   id -nG | tr ' ' '\n' | grep -x kvm
   ```
   👉 Explication : `/dev/kvm` doit exister et l'utilisateur appartenir au groupe `kvm`.

2. Créer un projet : **File > New blank project**, nom de test, serveur **Local**; ajouter uniquement des nœuds internes (switch Ethernet, VPCS).
   👉 Explication : topologie interne seulement.

3. Enregistrer puis rouvrir : **File > Save project**, **File > Close project**, **File > Open project**.
   👉 Explication : contrôler les liens et les éventuels fichiers d'appliance manquants.

4. Si une image libre autorisée est utilisée : clic droit sur le nœud > **Start**, puis **Stop**, et :
   ```bash
   ps aux | grep -c '[q]emu'
   ```
   👉 Explication : aucun processus QEMU ne doit rester après l'arrêt.

5. Inspecter le projet : **Topology Summary** (panneau de gauche) et :
   ```bash
   grep -E '"node_type": "(cloud|nat)"' ~/GNS3/projects/NOM_PROJET/*.gns3 || echo "aucun noeud Cloud/NAT"
   ```
   👉 Explication : remplacer `NOM_PROJET`; aucun pont physique ni NAT vers un tiers.

## 2. Production — Contrôles

Identifier l'administrateur du poste, les projets, ressources CPU/RAM/disque, versions et propriétaire/licence de chaque image avant un atelier partagé.

## 3. Production — Sécurité

- Serveur lié au poste local; compte nominatif et groupes de système limités au besoin.
- Topologie isolée, sans carte physique, réseau de production ou cible externe.
- Images éditeur seulement via une source autorisée; respecter leurs licences et ne pas distribuer les binaires.
- Ne pas placer de secrets ou de configurations réelles dans les projets de démonstration.
- Sauvegarder les projets et supprimer uniquement les ressources temporaires clairement identifiées.

## Validation et retour arrière

- **Validation** : version stable cohérente, serveur local disponible, projet rouvert, aucun uplink physique.
- **Retour arrière** : conserver la copie initiale du projet; arrêter le lab et retirer uniquement les noeuds ajoutés pour le test.

## Si le problème n'est pas résolu

- [GNS3 — documentation officielle](https://docs.gns3.com/docs/)
- [GNS3 — installation Linux Debian](https://docs.gns3.com/docs/getting-started/installation/linux)
- [Guide complet GNS3 2.2.61 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/77-deploiement-gns3-2-2-61-debian-13)