# Fiche_Simple_-_VM_Ubuntu_Ceph_Sauvegarde_Upgrade_Retrait.md

- **Environnement** : Cluster Ceph de laboratoire à trois nœuds (ceph01, ceph02, ceph03) géré par cephadm
- **OS / Version** : Ubuntu Server 22.04 LTS; Ceph Tentacle 20.2.4
- **Catégorie** : stockage / cluster Ceph

---

## Problème précis à résoudre

Protéger les données et opérer mise à niveau et retrait sans perte.

## 1. Hors-Production (Lab / Test / POC)

1. Prévoir une sauvegarde indépendante des données par le mécanisme du client, restaurable depuis un système distinct.
   👉 Explication : la réplication Ceph ne remplace pas une sauvegarde.

2. Sauvegarder séparément clés d'administration, inventaire et spécifications de service (ex. `/root/osd-lab.yaml`).
   👉 Explication : ces éléments permettent de reconstruire la gestion du cluster; les stocker chiffrés.

3. Avant mise à niveau, vérifier la santé :
   ```bash
   sudo ceph -s
   ```
   👉 Explication : le cluster doit être sain; lire release notes et procédure d'upgrade cephadm. Ne jamais lancer `apt full-upgrade` nœud par nœud.

4. Suivre un retrait d'OSD en cours :
   ```bash
   sudo ceph orch osd rm status
   ```
   👉 Explication : attendre la redistribution des PG et vérifier la capacité restante.

5. Ne pas employer `--force`, `--zap`, `ceph orch host rm --offline --force` ni purge en dépannage courant.
   👉 Explication : ces options peuvent provoquer une perte de données.

## 2. Production — Contrôles

Planifier la sauvegarde, la fenêtre de mise à niveau et la procédure de retrait avec test de restauration.

## 3. Production — Sécurité

- Protéger les sauvegardes de clés (chiffrement, accès restreint).

## Validation et retour arrière

- **Validation** : une restauration réussie depuis une sauvegarde indépendante et un cluster sain avant upgrade.
- **Retour arrière** : arrêter l'opération en cours si possible et revenir à la dernière configuration/sauvegarde validée; ne rien forcer.

## Si le problème n'est pas résolu

- [Ceph — upgrade cephadm](https://docs.ceph.com/en/tentacle/cephadm/upgrade/)
- [Ceph Tentacle — cephadm](https://docs.ceph.com/en/tentacle/cephadm/install/)
- [Guide complet](/02-fiches-completes/ubuntu/22-04/installation-deploiement/67-deploiement-ceph-tentacle-20-2-4-ubuntu-22-04#8-sauvegarde-mise-a-niveau-et-retrait)