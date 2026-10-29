# Fiche_Simple_-_VM_Ubuntu_24.04_Podman_Buildah_Valider

- **Environnement** : VM Ubuntu 24.04 LTS de laboratoire, utilisateur sudoer et compte de service dédié
- **OS / Version** : Ubuntu 24.04 LTS
- **Catégorie** : conteneurs

---

## Problème précis à résoudre

Recette de Podman et Buildah : exécution rootless, build, réseau, service.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler versions et mode rootless :
   ```bash
   podman --version
   buildah --version
   podman info --format '{{.Host.Security.Rootless}}'
   ```
   👉 Explication : rootless attendu à `true` en compte non root.

2. Lancer un conteneur de test éphémère (REGISTRE, IMAGE et VERSION_FIXE à remplacer) :
   ```bash
   podman run --rm REGISTRE/IMAGE:VERSION_FIXE echo OK
   ```
   👉 Explication : valide le téléchargement, le runtime et le stockage.

3. Vérifier le service Quadlet et les journaux :
   ```bash
   systemctl --user --no-pager status APPLICATION.service
   journalctl --user -u APPLICATION.service -n 50 --no-pager
   ```
   👉 Explication : l'unité est active sans erreur.

4. Contrôler l'espace utilisé :
   ```bash
   podman system df
   ```
   👉 Explication : détecte une accumulation d'images ou de volumes.

## 2. Production — Contrôles

Consigner la recette dans le dossier d'exploitation. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Supprimer les conteneurs et images de test.

## Validation et retour arrière

- **Validation** : toutes les commandes répondent comme attendu.
- **Retour arrière** : reprendre la fiche concernée par l'échec.

## Si le problème n'est pas résolu

- [Podman — documentation officielle](https://docs.podman.io/en/latest/)
- [Podman — installation](https://podman.io/docs/installation)
- [Fiche connexe — Prerequis Limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/podman-buildah/fiche-simple-vm-ubuntu-24-04-podman-buildah-prerequis-limites)