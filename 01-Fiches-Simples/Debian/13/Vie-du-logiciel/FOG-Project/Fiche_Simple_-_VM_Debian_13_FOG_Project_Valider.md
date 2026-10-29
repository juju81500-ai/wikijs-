# Fiche_Simple_-_VM_Debian_13_FOG_Project_Valider

- **Environnement** : VM Debian 13 dédiée FOG Project (clonage/déploiement d'images), réseau de laboratoire isolé
- **OS / Version** : Debian 13 Trixie; FOG Project (version et support Debian 13 à vérifier)
- **Catégorie** : automatisation / déploiement
- **Tags** : `debian13`, `fog-project`, `validation`, `recette`, `pxe`

---

## Problème précis à résoudre

Valider le fonctionnement de FOG sur un poste pilote avant extension.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'état des services :
   ```bash
   systemctl --no-pager --failed
   sudo journalctl -p warning -b --no-pager | tail -n 40
   ```
   👉 Explication : aucune unité en échec liée à FOG, web, base de données, TFTP ou NFS.

2. Dans l'interface : Hosts → inscrire un poste pilote (HOTE_PILOTE à remplacer).
   👉 Explication : inscrire un seul hôte de laboratoire.

3. Faire une capture d'une VM de test (Tasks → Capture) puis un déploiement sur une autre VM de test.
   👉 Explication : valide image, stockage et réseau ; ne pas déployer sur un poste contenant des données.

4. Vérifier le résultat (démarrage de l'OS, nom, réseau) et l'historique des tâches.
   👉 Explication : documenter durée et anomalies.

## 2. Production — Contrôles

Production : recette signée sur un lot pilote, supervision du service, matrice de support vérifiée, procédure de restauration testée.

## 3. Production — Sécurité

- Vérifier qu'aucune tâche planifiée ne cible un groupe étendu.
- Contrôler les journaux d'accès à l'interface.

## Validation et retour arrière

- **Validation** : capture et déploiement réussis sur VM de test.
- **Retour arrière** : annuler les tâches en file, supprimer l'hôte de test, restaurer l'instantané.

## Si le problème n'est pas résolu

- [Documentation officielle FOG Project](https://docs.fogproject.org/)
- [Dépôt officiel FOG Project](https://github.com/FOGProject/fogproject)
- [Fiche d'entrée FOG Project](../../../../Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Logiciel_-_FOG-Project.md)
