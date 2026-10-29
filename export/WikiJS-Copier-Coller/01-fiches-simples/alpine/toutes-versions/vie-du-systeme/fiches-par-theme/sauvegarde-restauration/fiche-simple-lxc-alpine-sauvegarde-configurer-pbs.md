# Fiche_Simple_-_LXC_Alpine_Sauvegarde_Configurer_PBS.md

- **Environnement** : hôte Proxmox VE autorisé, datastore Proxmox Backup Server validé
- **OS / Version** : Proxmox VE et PBS selon versions maintenues du cluster
- **Catégorie** : sauvegarde LXC / configuration PBS

---

## Problème précis à résoudre

Relier PVE à PBS et planifier la sauvegarde du CT avec identité et privilèges minimaux.

## 1. Hors-Production (Lab / Test / POC)

1. Ajouter le datastore PBS : **Datacenter > Storage > Add > Proxmox Backup Server** (ID, serveur, datastore, utilisateur/token dédié, **Fingerprint**).
   👉 Explication : valider l'empreinte du certificat; le compte n'a que les droits minimaux.

2. Créer la tâche : **Datacenter > Backup > Add** (Storage = PBS, Mode = Snapshot, Selection = le CT, Schedule, Retention, Encryption, notifications).
   👉 Explication : vérifier planification, rétention et alertes.

3. Test manuel ponctuel :
   ```bash
   vzdump CTID --storage STOCKAGE_PBS --mode snapshot
   ```
   👉 Explication : remplacer `CTID` et le stockage; choisir une fenêtre d'arrêt si l'application ne tolère pas un snapshot à chaud.

## 2. Production — Contrôles

Faire approuver le compte/token, permissions, datastore, planification, mode, fenêtre, rétention, chiffrement et notifications.

## 3. Production — Sécurité

- Ne pas accepter une empreinte inconnue sans validation indépendante.
- Ne pas utiliser un compte administrateur PBS partagé si un token dédié est possible.
- Ne pas enregistrer les secrets de connexion dans le CT ou dans des documents accessibles.
- Ne pas supposer qu'un snapshot à chaud garantit la cohérence applicative.

## Validation et retour arrière

- **Validation** : tâche configurée, CT ciblé sans ambiguïté, test réussi et alertes opérationnelles.
- **Retour arrière** : désactiver uniquement la tâche créée et supprimer l'accès/token selon procédure après vérification des sauvegardes conservées.

## Si le problème n'est pas résolu

- [Proxmox Backup Server — documentation](https://pbs.proxmox.com/docs/)
- [Proxmox VE — vzdump](https://pve.proxmox.com/pve-docs/vzdump.1.html)
- [Guide complet sauvegarde/restauration LXC Alpine](/02-fiches-completes/alpine/toutes-versions/autres/18-alpine-lxc-sauvegarde-restauration-production#2-preparer-proxmox-backup-server)