# Fiche_Simple_-_VM_Rocky_9_Podman_Quadlet_Verifier_Exposer.md

- **Environnement** : VM Rocky Linux 9 avec Podman rootless, systemd et Quadlet (pilote local)
- **OS / Version** : Rocky Linux 9; Podman des dépôts maintenus
- **Catégorie** : conteneurs / vérification

---

## Problème précis à résoudre

Contrôler l'état, la santé et l'exposition du service.

## 1. Hors-Production (Lab / Test / POC)

1. Lire l'état de l'unité :
   ```bash
   sudo -iu svcpodman systemctl --user --no-pager status monservice.service
   ```
   👉 Explication : doit être active.

2. Lister les conteneurs :
   ```bash
   sudo -iu svcpodman podman ps
   ```
   👉 Explication : confirme le mapping de port.

3. Lire les journaux :
   ```bash
   sudo -iu svcpodman journalctl --user -u monservice.service -b --no-pager
   ```
   👉 Explication : repère les erreurs de démarrage.

4. Rechercher les refus SELinux :
   ```bash
   sudo ausearch -m AVC -ts recent
   ```
   👉 Explication : corriger étiquetage et politique plutôt que désactiver SELinux.

## 2. Production — Contrôles

Vérifier santé applicative, mapping de port, droits sur volume et journaux.

## 3. Production — Sécurité

- Ne pas désactiver SELinux pour faire fonctionner le conteneur.

## Validation et retour arrière

- **Validation** : service actif, port répondant en local, aucun AVC.
- **Retour arrière** : arrêter l'unité utilisateur et retirer la règle de pare-feu éventuelle.

## Si le problème n'est pas résolu

- [Podman — Quadlet et unités systemd](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html)
- [Podman — référence CLI](https://docs.podman.io/en/latest/markdown/podman.1.html)
- [Guide complet Podman Quadlet Rocky Linux 9](/02-fiches-completes/rocky-linux/9/installation-deploiement/57-deploiement-podman-quadlet-rocky-linux-9#4-verifier-et-exposer-le-service)