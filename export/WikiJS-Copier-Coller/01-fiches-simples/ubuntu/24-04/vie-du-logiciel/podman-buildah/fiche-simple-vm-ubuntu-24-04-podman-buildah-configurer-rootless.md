# Fiche_Simple_-_VM_Ubuntu_24.04_Podman_Buildah_Configurer_Rootless

- **Environnement** : VM Ubuntu 24.04 LTS de laboratoire, utilisateur sudoer et compte de service dédié
- **OS / Version** : Ubuntu 24.04 LTS
- **Catégorie** : conteneurs

---

## Problème précis à résoudre

Configurer le rootless, les registres de confiance et un service Quadlet minimal.

## 1. Hors-Production (Lab / Test / POC)

1. Attribuer les plages subuid/subgid si absentes (UTILISATEUR à remplacer) :
   ```bash
   sudo usermod --add-subuids 100000-165535 --add-subgids 100000-165535 UTILISATEUR
   podman system migrate
   ```
   👉 Explication : méthode décrite par la documentation rootless de Podman ; vérifier que la plage ne chevauche pas un autre compte.

2. Déclarer les registres dans `~/.config/containers/registries.conf` (compte) ou `/etc/containers/registries.conf` (système) :
   ```bash
   mkdir -p ~/.config/containers
   cat > ~/.config/containers/registries.conf <<'EOP'
   unqualified-search-registries = ["REGISTRE"]
   EOP
   ```
   👉 Explication : REGISTRE est à remplacer par votre registre approuvé ; privilégier des noms d'images complets.

3. Permettre le démarrage du compte de service sans session (UTILISATEUR à remplacer) :
   ```bash
   sudo loginctl enable-linger UTILISATEUR
   ```
   👉 Explication : nécessaire pour qu'un service utilisateur systemd tourne au boot.

4. Quadlet : créer `~/.config/containers/systemd/APPLICATION.container` (APPLICATION, REGISTRE, IMAGE et VERSION_FIXE à remplacer) :
   ```ini
   [Container]
   Image=REGISTRE/IMAGE:VERSION_FIXE
   ReadOnly=true
   DropCapability=all
   NoNewPrivileges=true
   PublishPort=127.0.0.1:8080:8080

   [Service]
   Restart=on-failure

   [Install]
   WantedBy=default.target
   ```
   👉 Explication : Quadlet est présent à partir de Podman 4.4 ; vérifier la version installée. Détails dans la fiche Rocky 9 liée plus bas.

5. Recharger et démarrer l'unité :
   ```bash
   systemctl --user daemon-reload
   systemctl --user start APPLICATION.service
   systemctl --user status APPLICATION.service
   ```
   👉 Explication : Quadlet génère l'unité à partir du fichier `.container` ; ne pas utiliser `systemctl enable` sur l'unité générée.

## 2. Production — Contrôles

Versionner les fichiers Quadlet et la configuration des registres. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Limiter `PublishPort` à l'adresse nécessaire.
- Épingler l'image par version ou digest.

## Validation et retour arrière

- **Validation** : l'unité démarre et le conteneur tourne sous le compte de service.
- **Retour arrière** : `systemctl --user stop APPLICATION.service`, supprimer le fichier `.container` puis `daemon-reload`.

## Si le problème n'est pas résolu

- [Podman — unités Quadlet](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html)
- [Fiche Rocky Linux 9 — Quadlet (référence)](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/podman/fiche-simple-vm-rocky-9-podman-quadlet-declarer-service)
- [Fiche connexe — Prerequis Limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/podman-buildah/fiche-simple-vm-ubuntu-24-04-podman-buildah-prerequis-limites)