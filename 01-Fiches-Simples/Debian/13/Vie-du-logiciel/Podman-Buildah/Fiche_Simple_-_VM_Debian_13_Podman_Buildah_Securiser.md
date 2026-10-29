# Fiche_Simple_-_VM_Debian_13_Podman_Buildah_Securiser

- **Environnement** : VM Debian 13 de laboratoire, utilisateur sudoer et compte de service dédié
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : conteneurs
- **Tags** : `debian13`, `podman`, `buildah`, `conteneurs`, `rootless`, `oci`

---

## Problème précis à résoudre

Durcir l'exécution des conteneurs Podman : rootless, capacités, système de fichiers, confiance des images, pare-feu.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter sous le compte de service et limiter les privilèges (REGISTRE, IMAGE et VERSION_FIXE à remplacer) :
   ```bash
   podman run --rm --read-only --cap-drop=all --security-opt=no-new-privileges --pids-limit=200 --memory=256m REGISTRE/IMAGE:VERSION_FIXE
   ```
   👉 Explication : supprime les capacités, interdit l'élévation et borne les ressources.

2. Contrôler la politique de confiance des images : lire `/etc/containers/policy.json`.
   ```bash
   cat /etc/containers/policy.json
   ```
   👉 Explication : la politique par défaut peut accepter toute image ; la durcir (signatures GPG ou sigstore, registres listés) suivant `containers-policy.json(5)`.

3. Utiliser les secrets Podman plutôt que des variables d'environnement (NOM_SECRET à remplacer ; le mot de passe est saisi, jamais écrit en dur) :
   ```bash
   read -rs MDP && printf '%s' "$MDP" | podman secret create NOM_SECRET -
   unset MDP
   ```
   👉 Explication : le secret est stocké par Podman et monté dans le conteneur avec `--secret NOM_SECRET`.

4. Filtrer les ports publiés au niveau du pare-feu de l'hôte (nftables) et publier sur `127.0.0.1` quand c'est possible.
   👉 Explication : le pare-feu hôte et la publication de port doivent être cohérents ; tester l'exposition depuis un autre poste.

## 2. Production — Contrôles

Revoir périodiquement images, politique et exposition réseau. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Pas de `--privileged` ni de montage de la racine ou de sockets hôte.
- Utiliser des images épinglées par digest quand c'est possible.
- Pas de secret en clair dans les unités ni les images.

## Validation et retour arrière

- **Validation** : le conteneur démarre avec privilèges réduits et la politique de confiance est celle attendue.
- **Retour arrière** : retirer les options de durcissement fautives une à une ; supprimer le secret (`podman secret rm NOM_SECRET`).

## Si le problème n'est pas résolu

- [Podman — documentation officielle](https://docs.podman.io/en/latest/)
- [Podman — installation](https://podman.io/docs/installation)
- [Fiche connexe — Prerequis Limites](Fiche_Simple_-_VM_Debian_13_Podman_Buildah_Prerequis_Limites.md)
