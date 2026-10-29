# Nettoyer l'espace disque d'un hôte Docker

- **Environnement** : Hôte Docker Engine Linux
- **Catégorie** : Maintenance / Stockage
- **Tags** : `docker`, `maintenance`, `stockage`, `prune`, `journaux`

## Problème

Récupérer de l'espace occupé par des ressources Docker inutilisées sans supprimer des données persistantes ni interrompre des services actifs.

> Ne pas lancer un nettoyage avec `--volumes` à l'aveugle. Un volume supprimé peut contenir des données qui ne sont pas sauvegardées. Les exemples ci-dessous n'automatisent pas une purge globale.

## 1. Diagnostic sans suppression

```bash
df -h
docker system df -v
docker ps -a --size
docker volume ls
docker image ls
```
   👉 Explication : mesure l'usage disque et liste conteneurs, volumes et images sans rien supprimer.

Identifier le répertoire ou le type de ressource qui consomme réellement l'espace. Vérifier les sauvegardes des bases et volumes avant toute suppression.

## 2. Essai en laboratoire

Afficher les ressources supprimables, sans `--force` :

```bash
docker container prune
docker image prune
```
   👉 Explication : supprime conteneurs arrêtés et images non utilisées; chaque commande demande confirmation, ne jamais ajouter `--volumes` sans sauvegarde.

Docker demande une confirmation. Les conteneurs arrêtés et les images dangling supprimés devront éventuellement être retéléchargés ou recréés.

## 3. Nettoyage de production ciblé

Après validation du périmètre et de la fenêtre de maintenance, supprimer uniquement les conteneurs arrêtés explicitement approuvés :

```bash
docker ps -a --filter status=exited
docker container prune --filter 'until=168h'
docker system df
```
   👉 Explication : en lab, limite le nettoyage aux conteneurs arrêtés depuis plus de 7 jours et mesure le gain.

La commande conserve une confirmation interactive. Pour récupérer davantage d'espace, examiner les images inutilisées puis exécuter `docker image prune --filter 'until=168h'` après validation. Ne pas supprimer les volumes dans cette procédure.

## 4. Journaux du moteur

Pour un démon utilisant `json-file`, sauvegarder puis valider `/etc/docker/daemon.json` avant application :

```json
{
  "log-driver": "local",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
```
   👉 Explication : contenu de `/etc/docker/daemon.json` : limite la taille des journaux des conteneurs.

Le pilote `local` applique une rotation intégrée. Le changement du pilote par défaut ne modifie pas les conteneurs déjà créés : recréer les services de façon contrôlée pour qu'ils l'utilisent. Vérifier la compatibilité des options avec la version installée et la configuration existante avant de remplacer le fichier.

```bash
sudo dockerd --validate --config-file=/etc/docker/daemon.json
```
   👉 Explication : valide le JSON avant de redémarrer Docker.

Si `--validate` n'est pas disponible dans la version installée, ne pas redémarrer le démon sur la base de ce contrôle ; valider avec la procédure propre à cette version. Planifier tout redémarrage Docker en production et confirmer le comportement de reprise des conteneurs.

## 5. Contrôles et retour arrière

```bash
docker system df -v
docker ps
docker volume ls
systemctl --no-pager status docker
```
   👉 Explication : vérifie que tout est resté fonctionnel après nettoyage.

Une ressource prune ne possède pas de restauration automatique. Recréer les conteneurs depuis leur définition versionnée et restaurer les données depuis une sauvegarde vérifiée. Ne jamais considérer un volume Docker comme une sauvegarde.