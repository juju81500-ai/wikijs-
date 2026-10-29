# 📄 Fiche_Simple_-_VM_Debian_12_Verifier_Scheduler_Znuny.md

- **Environnement** : VM Debian 12 hébergeant Znuny 7.3.x
- **OS / Version** : Debian 12 Bookworm
- **Catégorie** : Supervision / diagnostic
- **Tags** : `debian12`, `znuny`, `scheduler`, `logs`, `itsm`

---

## 🎯 Problème précis à résoudre

Vérifier que le scheduler Znuny est lancé et que les tâches de fond ne restent pas bloquées.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Vérifier l'accès à la CLI :
   ```bash
   sudo -u znuny /opt/znuny/bin/znuny.Console.pl List | head -5
   ```
   👉 Explication : adapter `/opt/znuny` au chemin réel; confirme la CLI, pas le fonctionnement des tâches.

2. Vérifier les processus du scheduler :
   ```bash
   sudo -u znuny pgrep -af 'Cron|Daemon|znuny'
   ```
   👉 Explication : une seule instance du scheduler doit tourner.


## ⚡ 2. Production — Façon Simplifiée

1. Vérifier les événements récents :
   ```bash
   sudo journalctl -u apache2 --since "30 minutes ago" --no-pager
   sudo find /opt/znuny/var/log -type f -mmin -60 -print
   ```
   👉 Explication : repérer le journal applicatif modifié récemment; contrôler aussi l'heure de dernière exécution dans l'interface (**Admin > Processus et automatisation > Gestionnaire de tâches / Daemon**).

2. Lancer les outils CLI sous le bon propriétaire :
   ```bash
   sudo -u znuny /opt/znuny/bin/znuny.Daemon.pl status
   ```
   👉 Explication : n'utiliser jamais root; ne pas lancer un second scheduler avant d'avoir identifié le mécanisme actif.


## 🔒 3. Production — Façon Sécurisée

- Ne pas lancer un second scheduler avant d'avoir déterminé le mécanisme actif.
- Ne pas utiliser root pour les commandes Znuny et ne pas exposer les journaux en accès public.
- En cas de tâche bloquée, relever son nom, son heure, son extension et ses erreurs avant de la mettre en pause; modifier les statuts internes de tâche uniquement selon le runbook officiel.
- Si l'installation utilise `Cron.sh`, suivre sa procédure de démarrage/arrêt de la version Znuny correspondante.

## ✅ Validation et retour arrière

- **Précontrôles** : noter l'heure du problème, vérifier `znuny` et le chemin de l'application.
- **Validation** : confirmer que les tâches reprennent et que les journaux ne réaffichent pas l'erreur.
- **Retour arrière** : annuler le changement de scheduler ou de service appliqué; ne pas supprimer l'état ou les journaux pour masquer le symptôme.

## 🔗 Si le problème n'est pas résolu

- **Fiche de résolution complémentaire** : [[Debian12_Znuny_Scheduler_Tache_Bloquee]]
- [Znuny — Maintenance et journaux](https://doc.znuny.org/znuny/standardoperations/index.html)