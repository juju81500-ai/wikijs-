# Fiche_Simple_-_VM_Ubuntu_Ceph_Pool_RBD_Pilote.md

- **Environnement** : Cluster Ceph de laboratoire à trois nœuds (ceph01, ceph02, ceph03) géré par cephadm
- **OS / Version** : Ubuntu Server 22.04 LTS; Ceph Tentacle 20.2.4
- **Catégorie** : stockage / cluster Ceph

---

## Problème précis à résoudre

Valider le stockage avec un petit pool RBD de test.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier d'abord capacité et distribution des OSD :
   ```bash
   sudo ceph df
   sudo ceph osd tree
   ```
   👉 Explication : un pool répliqué à trois copies exige assez de domaines de panne pour les placer.

2. Créer et initialiser le pool :
   ```bash
   sudo ceph osd pool create lab-rbd
   sudo rbd pool init lab-rbd
   ```
   👉 Explication : prépare le pool `lab-rbd` pour RBD.

3. Créer une image de 1 Go et la lister :
   ```bash
   sudo rbd create lab-rbd/test-image --size 1G
   sudo rbd ls lab-rbd
   ```
   👉 Explication : vérifie que l'écriture fonctionne.

4. Supprimer l'image de test :
   ```bash
   sudo rbd rm lab-rbd/test-image
   ```
   👉 Explication : nettoie le test; seule cette image de 1 Go est supprimée.

## 2. Production — Contrôles

Définir règle CRUSH, nombre de copies, quota et droits clients selon le service; créer des clients dédiés.

## 3. Production — Sécurité

- Ne pas réutiliser `client.admin` pour des clients applicatifs.

## Validation et retour arrière

- **Validation** : l'image est créée, listée puis supprimée sans erreur et la santé reste stable.
- **Retour arrière** : supprimer le pool de test uniquement en lab et après confirmation qu'il est vide (nécessite d'activer `mon_allow_pool_delete`, à ne faire que volontairement).

## Si le problème n'est pas résolu

- [Ceph — RBD](https://docs.ceph.com/en/tentacle/rbd/)
- [Ceph Tentacle — cephadm](https://docs.ceph.com/en/tentacle/cephadm/install/)
- [Guide complet](/02-fiches-completes/ubuntu/22-04/installation-deploiement/67-deploiement-ceph-tentacle-20-2-4-ubuntu-22-04#6-creer-un-pool-rbd-pilote)