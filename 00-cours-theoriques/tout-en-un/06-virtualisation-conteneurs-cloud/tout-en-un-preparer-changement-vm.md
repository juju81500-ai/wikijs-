# Fiche_Simple_-_Tout-en-un_Preparer_Changement_VM

- **Environnement** : plateforme de virtualisation de laboratoire ou de production approuvée
- **OS / Version** : hyperviseur et outils selon plateforme ; exemple [[Glossary:CLI]] Proxmox VE à adapter
- **Catégorie** : Tout-en-un / Virtualisation, conteneurs et cloud
- **Tags** : `transverse`, `tout-en-un`, `virtualisation`, `vm`, `changement`

---

## Problème précis à résoudre

Préparer une modification réversible d'une [[Glossary:VM]] en identifiant son état, ses dépendances et le point de retour, avant d'intervenir dans l'invité.

## 1. Hors-Production (Lab / Test / POC)

1. Examiner l'identité, l'état et la configuration de la VM sur un hyperviseur Proxmox VE autorisé :
   ```bash
   VMID=100
   qm status "$VMID"
   qm config "$VMID"
   ```
   👉 Explication : relève l'état et les paramètres de la VM ; remplacer `VMID` par une cible du laboratoire, jamais par un identifiant supposé.

2. Vérifier les snapshots existants :
   ```bash
   qm listsnapshot "$VMID"
   ```
   👉 Explication : montre les points de retour présents ; un snapshot n'est pas une sauvegarde indépendante et peut dépendre du stockage sous-jacent.

3. Créer un snapshot avant une modification dans un laboratoire non-critique :
   ```bash
   qm snapshot "$VMID" before-change --description "Point de retour avant changement approuvé"
   ```
   👉 Explication : crée un état de retour pour une VM arrêtée ou en cours selon les capacités du stockage ; valider les conséquences et la disponibilité de l'espace avant exécution.

4. Vérifier le retour sans toucher à la VM d'origine en clonant vers un ID libre, si la politique et le stockage l'autorisent :
   ```bash
   qm clone "$VMID" 101 --name validation-change --full 1
   ```
   👉 Explication : crée un clone complet distinct ; contrôler l'ID libre, l'identité réseau, les adresses et les démarrages automatiques avant de connecter le clone.

5. Confirmer l'état après le changement et documenter le résultat :
   ```bash
   qm status "$VMID"
   qm listsnapshot "$VMID"
   ```
   👉 Explication : confirme l'état courant et le point de retour ; la validation applicative doit être faite dans l'invité par le propriétaire du service.

## 2. Production — Contrôles

Vérifier la sauvegarde indépendante, l'espace datastore, les jobs, la haute disponibilité, les réplications, le réseau et la fenêtre. Un snapshot seul ne suffit pas pour garantir un PRA.

## 3. Production — Sécurité

Ne jamais démarrer simultanément un clone et l'original sur le même réseau avant d'avoir traité [[Glossary:IP]], nom machine, clés, agents et tâches planifiées. Les commandes Proxmox nécessitent des droits hyperviseur ; utiliser le moindre privilège.

## Validation et retour arrière

- **Validation** : changement vérifié par un test applicatif et point de retour conservé selon la rétention approuvée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde via l'hyperviseur après approbation ; tenir compte de la perte des écritures intervenues depuis le snapshot.

## Si le problème n'est pas résolu

- [Documentation Proxmox VE — gestion des VM](https://pve.proxmox.com/pve-docs/)
- Utiliser la procédure équivalente du fournisseur d'hyperviseur ; ne pas transposer les commandes `qm` à VMware ou Hyper-V.

## Historique de vérification

| Vérifié le | OS / version | Logiciel / version | Testeur | Verdict | Sources |
|---|---|---|---|---|---|
| 2026-10-31 | Proxmox VE — version à confirmer | `qm` | — | Non testé sur plateforme cible | Documentation Proxmox ci-dessus |
