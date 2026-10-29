# Fiche_Simple_-_VM_Debian_12_Bacula_Valider_Restauration.md

- **Environnement** : Bacula Community 15.0.3, Director/Storage, client File Daemon autorisé
- **OS / Version** : Debian 12 Bookworm avec paquets Backports
- **Catégorie** : Sauvegarde / restauration

---

## Problème précis à résoudre

Confirmer qu'un job Bacula terminé avec succès permet de restaurer un fichier vers un emplacement isolé.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler Director, Storage et client, puis relever le JobId du job pilote :
   ```bash
   sudo bconsole
   ```
   Dans `bconsole` : `status director`, `status storage`, `status client=NOM_CLIENT-fd`, puis `list jobs`.
   👉 Explication : le job pilote doit être terminé (`T`); noter son JobId.

2. Lancer l'assistant : `restore`, choisir « Select the most recent backup for a client » ou « Enter a list of JobIds », puis dans l'arbre `cd` vers le dossier et `mark` uniquement le fichier de test, `done`.
   👉 Explication : ne sélectionner que le fichier d'essai.

3. Avant de confirmer, vérifier JobId, client cible, Storage et `Where` : `mod`, option `Where`, valeur `/tmp/bacula-restore`.
   👉 Explication : un `Where` vide restaurerait sur le chemin d'origine et écraserait des données actives.

4. Confirmer (`yes`), puis comparer :
   ```bash
   sha256sum /tmp/bacula-restore/CHEMIN/FICHIER CHEMIN/FICHIER
   ls -l /tmp/bacula-restore/CHEMIN/FICHIER CHEMIN/FICHIER
   ```
   👉 Explication : remplacer `CHEMIN/FICHIER`; les empreintes doivent être identiques, ainsi que propriétaire et permissions.

5. Consigner le statut du job Restore et nettoyer l'essai :
   ```bash
   echo 'list jobs' | sudo bconsole | tail -5
   rm -rf /tmp/bacula-restore
   ```
   👉 Explication : le job Restore doit être `T`; ne supprimer que le dossier temporaire.

## 2. Production — Contrôles

Programmer des restaurations représentatives pour chaque type de client et niveau Full/Incremental/Differential. Vérifier séparément la restauration du catalogue, des volumes et du bootstrap; documenter les durées et l'écart aux RPO/RTO.

## 3. Production — Sécurité

- Ne pas restaurer directement sur les données actives avant validation du client et de l'emplacement.
- Ne pas afficher les secrets Director/Storage/File Daemon dans les logs ou la documentation.
- Vérifier que les volumes nécessaires sont présents, lisibles et protégés contre l'effacement depuis les clients.
- Confirmer que le trafic Bacula est limité aux réseaux autorisés et chiffré par TLS correctement validé.

## Validation et retour arrière

- **Validation** : job Restore terminé, empreinte identique, chemin et propriétés vérifiés, logs sans erreur.
- **Retour arrière** : conserver les données originales; nettoyer uniquement le dossier temporaire de restauration.

## Si le problème n'est pas résolu

- [Bacula 15.0.x — commande de restauration](https://www.bacula.org/15.0.x-manuals/en/main/Restore_Command.html)
- [Bacula Community 15.0.3 — annonce de version](https://www.bacula.org/bacula-community-15-0-3-released/)
- [Guide complet Bacula 15 sur Debian 12](/02-fiches-completes/debian/12/installation-deploiement/68-deploiement-bacula-15-debian-12-backports)