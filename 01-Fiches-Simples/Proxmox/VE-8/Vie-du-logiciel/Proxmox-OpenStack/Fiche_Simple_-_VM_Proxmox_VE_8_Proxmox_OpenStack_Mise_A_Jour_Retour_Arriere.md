# Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM DevStack jetable sur Proxmox VE 8.x
- **OS / Version** : Ubuntu Server 24.04 LTS; DevStack selon branche officielle
- **Catégorie** : cloud privé / maintenance de lab
- **Tags** : `proxmox`, `openstack`, `devstack`, `mise-a-jour`, `retour-arriere`, `lab`

---

## Problème précis à résoudre

Renouveler un lab DevStack sans appliquer une procédure de mise à niveau de production non documentée.

## 1. Hors-Production (Lab / Test / POC)

1. Consulter Quick Start et notes de la branche DevStack visée; relever version Ubuntu et dépendances.
   👉 Explication : les prérequis changent; ne pas remplacer de branche sans tester.
2. Arrêter le lab et créer un snapshot dans Proxmox via **Datacenter > Node > VM > Snapshots > Take Snapshot**.
   👉 Explication : confirmer l’ID de VM; le snapshot n’est pas une sauvegarde hors hôte.
3. Pour un lab jetable, préférer créer une nouvelle VM propre et appliquer la procédure d’installation de la branche choisie plutôt qu’une mise à niveau en place non documentée.
   👉 Explication : DevStack est destiné au développement et ne fournit pas ici une procédure de migration prise en charge.
4. Vérifier l’interface et les services sur le réseau isolé; garder l’ancienne VM arrêtée tant que la nouvelle n’est pas validée.
   👉 Explication : cette comparaison permet de revenir au lab initial sans interruption.
5. En cas d’échec, restaurer le snapshot dans l’interface ou supprimer uniquement la nouvelle VM après avoir confirmé l’ID.
   👉 Explication : ne pas effacer l’original avant validation.

## 2. Production — Contrôles

- DevStack n’est pas une distribution de production ni une procédure d’upgrade OpenStack exploité.
- Une plateforme réelle nécessite les instructions de mise à niveau supportées par son déploiement.

## 3. Production — Sécurité

- Garder le lab sans données réelles et sur réseau isolé; ne pas publier `local.conf` ou secrets.
- Utiliser les dépôts et instructions officiels de la branche retenue.

## Validation et retour arrière

- **Validation** : nouveau lab démarré, services testés et scénarios réussis.
- **Retour arrière** : revenir au snapshot préalable ou conserver l’ancienne VM arrêtée; ne pas tenter de rétrogradation non documentée.

## Si le problème n'est pas résolu

- [DevStack — Quick Start](https://docs.openstack.org/devstack/latest/)
- [DevStack — guide mono-machine](https://docs.openstack.org/devstack/latest/guides/single-machine.html)
- [Proxmox VE — documentation](https://pve.proxmox.com/pve-docs/)
- [Fiche d’entrée du logiciel](../../../../Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_Proxmox-OpenStack.md)
