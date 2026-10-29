# Fiche_Simple_-_VM_Debian_13_Bareos_Demarrer_Job_Pilote.md

- **Environnement** : Director, Storage et File Daemon Bareos 25 en lab; volume disque dédié
- **OS / Version** : Debian 13; Bareos Community 25
- **Catégorie** : sauvegarde réseau / job pilote

---

## Problème précis à résoudre

Démarrer les démons Bareos, valider leur configuration et exécuter un premier job manuel avec des données de test.

## 1. Hors-Production (Lab / Test / POC)

1. Démarrer les services :
   ```bash
   sudo systemctl enable --now bareos-director.service bareos-storage.service bareos-filedaemon.service
   sudo systemctl --no-pager status bareos-director.service bareos-storage.service bareos-filedaemon.service
   ```
   👉 Explication : les trois services doivent être `active (running)`.

2. Vérifier la syntaxe de chaque composant :
   ```bash
   sudo -u bareos /usr/sbin/bareos-dir -t
   sudo -u bareos /usr/sbin/bareos-sd -t
   sudo /usr/sbin/bareos-fd -t
   ```
   👉 Explication : aucun message d'erreur = configuration valide.

3. Lancer un job manuel dans la console :
   ```bash
   sudo bconsole
   ```
   Puis saisir : `run` (choisir le job pilote), `yes`, puis `messages`.
   👉 Explication : relever le JobId, puis contrôler l'état.

4. Contrôler le job, le volume et le catalogue :
   ```bash
   echo 'list jobs' | sudo bconsole
   echo 'list volumes' | sudo bconsole
   ```
   👉 Explication : le job doit être `T` (terminé OK) et le volume présent dans le pool disque dédié.

## 2. Production — Contrôles

Avant planification régulière, faire approuver fenêtres, filesets, volumes, rétention, alertes d'échec, capacité, clients et restauration.

## 3. Production — Sécurité

- Ne pas inclure des chemins contenant des secrets ou données hors périmètre.
- Limiter l'accès à `bconsole` et aux sockets de contrôle.
- Ne pas faire écouter les démons sur des interfaces publiques.
- Ne pas considérer un JobId terminé comme une preuve de restaurabilité.

## Validation et retour arrière

- **Validation** : syntaxe valide, job pilote terminé, volume alloué, catalogue et journaux cohérents.
- **Retour arrière** : arrêter le schedule pilote et conserver le volume/logs pour analyse; ne pas supprimer un volume qui contient des jobs utiles.

## Si le problème n'est pas résolu

- [Bareos — démarrage et configuration](https://docs.bareos.org/IntroductionAndTutorial/GettingStartedWithBareos.html)
- [Bareos — FileSets](https://docs.bareos.org/TasksAndConcepts/VolumeManagement.html)
- [Guide complet Bareos Debian 13](/02-fiches-completes/debian/13/installation-deploiement/59-deploiement-bareos-25-debian-13#4-demarrer-les-services-et-verifier-la-syntaxe)