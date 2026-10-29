# Fiche_Simple_-_VM_Ubuntu_24.04_Podman_Buildah_Sauvegarder_Restaurer

- **Environnement** : VM Ubuntu 24.04 LTS de laboratoire, utilisateur sudoer et compte de service dédié
- **OS / Version** : Ubuntu 24.04 LTS
- **Catégorie** : conteneurs

---

## Problème précis à résoudre

Sauvegarder et restaurer images, volumes et fichiers de configuration Podman.

## 1. Hors-Production (Lab / Test / POC)

1. Exporter une image au format OCI (IMAGE, VERSION_FIXE, REGISTRE à remplacer) :
   ```bash
   podman save --format oci-archive -o IMAGE-VERSION_FIXE.tar REGISTRE/IMAGE:VERSION_FIXE
   sha256sum IMAGE-VERSION_FIXE.tar
   ```
   👉 Explication : permet de recharger l'image hors ligne ; consigner l'empreinte.

2. Exporter un volume (VOLUME à remplacer) après arrêt du service concerné :
   ```bash
   podman volume export VOLUME -o VOLUME.tar
   ```
   👉 Explication : sauvegarde cohérente si le service est arrêté ; pour une base de données, utiliser plutôt son outil de dump.

3. Sauvegarder la configuration :
   ```bash
   tar czf podman-config.tgz -C ~ .config/containers
   ```
   👉 Explication : inclut registres, policy utilisateur et fichiers Quadlet ; vérifier l'absence de secret.

4. Restaurer :
   ```bash
   podman load -i IMAGE-VERSION_FIXE.tar
   podman volume create VOLUME
   podman volume import VOLUME VOLUME.tar
   tar xzf podman-config.tgz -C ~
   ```
   👉 Explication : recharge l'image, recrée et remplit le volume et restaure la configuration.

## 2. Production — Contrôles

Intégrer ces archives à la sauvegarde chiffrée de l'hôte. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Chiffrer les archives de volumes (données applicatives).
- Les secrets Podman ne sont pas inclus : les recréer depuis votre coffre.

## Validation et retour arrière

- **Validation** : archives et empreintes présentes ; la restauration en lab redémarre le service.
- **Retour arrière** : supprimer le volume restauré (`podman volume rm VOLUME`) et recommencer depuis une archive saine.

## Si le problème n'est pas résolu

- [Podman — documentation officielle](https://docs.podman.io/en/latest/)
- [Fiche connexe — Prerequis Limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/podman-buildah/fiche-simple-vm-ubuntu-24-04-podman-buildah-prerequis-limites)